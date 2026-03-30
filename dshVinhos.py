import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Dashboard - Wine Quality (UCI)",
    page_icon="🍷",
    layout="wide"
)

RED_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
WHITE_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"


@st.cache_data
def load_data():
    red = pd.read_csv(RED_URL, sep=";")
    red["type"] = "red"

    white = pd.read_csv(WHITE_URL, sep=";")
    white["type"] = "white"

    df = pd.concat([red, white], ignore_index=True)
    return df


df = load_data()

st.title("🍷 Dashboard Interativo - Wine Quality (UCI)")
st.markdown(
    """
    Este dashboard apresenta uma análise exploratória do dataset **Wine Quality**
    do UCI Machine Learning Repository, com filtros interativos e múltiplas visualizações.
    """
)

numeric_cols = [col for col in df.columns if df[col].dtype != "object" and col != "quality"]
all_numeric_for_corr = [col for col in df.columns if df[col].dtype != "object"]

# =========================
# SIDEBAR
# =========================
st.sidebar.header("Filtros")

wine_types = st.sidebar.multiselect(
    "Tipo de vinho",
    options=sorted(df["type"].unique()),
    default=sorted(df["type"].unique())
)

quality_min = int(df["quality"].min())
quality_max = int(df["quality"].max())
quality_range = st.sidebar.slider(
    "Faixa de qualidade",
    min_value=quality_min,
    max_value=quality_max,
    value=(quality_min, quality_max)
)

alcohol_range = st.sidebar.slider(
    "Faixa de álcool",
    min_value=float(df["alcohol"].min()),
    max_value=float(df["alcohol"].max()),
    value=(float(df["alcohol"].min()), float(df["alcohol"].max()))
)

x_var = st.sidebar.selectbox("Variável do eixo X", numeric_cols, index=numeric_cols.index("alcohol"))
y_var = st.sidebar.selectbox("Variável do eixo Y", numeric_cols, index=numeric_cols.index("volatile acidity"))
color_var = st.sidebar.selectbox(
    "Colorir pontos por",
    ["type", "quality"] + numeric_cols,
    index=1
)

filtered = df[
    (df["type"].isin(wine_types)) &
    (df["quality"].between(quality_range[0], quality_range[1])) &
    (df["alcohol"].between(alcohol_range[0], alcohol_range[1]))
].copy()

# =========================
# KPIs
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Quantidade de registros", f"{len(filtered):,}".replace(",", "."))
col2.metric("Qualidade média", f"{filtered['quality'].mean():.2f}" if len(filtered) > 0 else "0.00")
col3.metric("Álcool médio", f"{filtered['alcohol'].mean():.2f}" if len(filtered) > 0 else "0.00")
col4.metric("pH médio", f"{filtered['pH'].mean():.2f}" if len(filtered) > 0 else "0.00")

st.divider()

if filtered.empty:
    st.warning("Nenhum dado encontrado com os filtros selecionados.")
    st.stop()

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "Distribuição",
    "Relação entre Variáveis",
    "Correlação",
    "Resumo Analítico"
])

# -------------------------
# TAB 1 - HISTOGRAMA + BOXPLOT
# -------------------------
with tab1:
    c1, c2 = st.columns(2)

    with c1:
        fig_hist = px.histogram(
            filtered,
            x="quality",
            color="type",
            barmode="group",
            nbins=10,
            title="Distribuição da Qualidade dos Vinhos"
        )
        fig_hist.update_layout(xaxis_title="Qualidade", yaxis_title="Frequência")
        st.plotly_chart(fig_hist, use_container_width=True)

    with c2:
        fig_box = px.box(
            filtered,
            x="type",
            y="alcohol",
            color="type",
            title="Distribuição do Teor Alcoólico por Tipo de Vinho",
            points="outliers"
        )
        fig_box.update_layout(xaxis_title="Tipo", yaxis_title="Álcool")
        st.plotly_chart(fig_box, use_container_width=True)

# -------------------------
# TAB 2 - DISPERSÃO
# -------------------------
with tab2:
    fig_scatter = px.scatter(
        filtered,
        x=x_var,
        y=y_var,
        color=color_var,
        hover_data=["quality", "type"],
        title=f"Dispersão: {x_var} vs {y_var}",
        opacity=0.7
    )
    fig_scatter.update_layout(xaxis_title=x_var, yaxis_title=y_var)
    st.plotly_chart(fig_scatter, use_container_width=True)

# -------------------------
# TAB 3 - MAPA DE CALOR
# -------------------------
with tab3:
    corr = filtered[all_numeric_for_corr].corr(numeric_only=True)

    fig_heatmap = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="Mapa de Calor das Correlações"
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

# -------------------------
# TAB 4 - INSIGHTS AUTOMÁTICOS
# -------------------------
with tab4:
    st.subheader("Resumo dos dados filtrados")

    summary = filtered.describe().T[["mean", "std", "min", "max"]]
    st.dataframe(summary, use_container_width=True)

    st.subheader("Principais observações")
    quality_mean = filtered["quality"].mean()
    alcohol_quality_corr = filtered["alcohol"].corr(filtered["quality"])
    volatile_quality_corr = filtered["volatile acidity"].corr(filtered["quality"])

    st.markdown(
        f"""
        - A **qualidade média** no recorte atual é **{quality_mean:.2f}**.
        - A correlação entre **álcool** e **qualidade** é **{alcohol_quality_corr:.2f}**.
        - A correlação entre **acidez volátil** e **qualidade** é **{volatile_quality_corr:.2f}**.
        - Use os filtros da barra lateral para verificar como essas relações mudam entre vinhos tintos e brancos.
        """
    )

st.divider()
st.caption("Projeto acadêmico de Visualização de Dados usando Streamlit + Plotly + UCI Wine Quality.")