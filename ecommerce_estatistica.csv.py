import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# 1. Carregamento dos Dados
# Substitua pelo caminho correto do seu arquivo CSV, se necessário
df = pd.read_csv(r'C:\Users\Moises\Downloads\pychard\ecommerce_estatistica.csv')

# 2. Criação das Figuras com Plotly (para integração nativa no Dash)
fig_hist = px.histogram(
    df, x="Preço", nbins=30,
    title="Distribuição da Frequência de Preços dos Produtos",
    color_discrete_sequence=["skyblue"]
)
fig_hist.update_layout(xaxis_title="Preço (R$)", yaxis_title="Frequência de Produtos")

fig_scatter = px.scatter(
    df, x="Preço", y="N_Avaliações", opacity=0.7,
    title="Relação entre Preço do Produto e Número de Avaliações",
    color_discrete_sequence=["teal"]
)
fig_scatter.update_layout(xaxis_title="Preço (R$)", yaxis_title="Número de Avaliações")

# Mapa de Calor de Correlação numéricas
numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_df.corr()
fig_corr = px.imshow(
    corr_matrix, text_auto=True, color_continuous_scale="RdBu",
    title="Mapa de Calor de Correlação entre Variáveis Numéricas"
)

# Top 10 Marcas/Categorias
coluna_categoria = "Marca" if "Marca" in df.columns else df.columns[0]
top_categorias = df[coluna_categoria].value_counts().head(10).reset_index()
top_categorias.columns = ['Categoria', 'Quantidade']
fig_bar = px.bar(
    top_categorias, x='Categoria', y='Quantidade',
    title="Top 10 Marcas/Categorias com Mais Produtos Cadastrados",
    color='Quantidade', color_continuous_scale="Viridis"
)

# 3. Inicialização da Aplicação Dash
app = dash.Dash(__name__)
server = app.server  # Necessário caso queira fazer deploy futuramente

# 4. Layout do Dashboard
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px', 'backgroundColor': '#f9f9f9'},
                      children=[

                          # Cabeçalho
                          html.H1("Dashboard de Análise de E-commerce",
                                  style={'textAlign': 'center', 'color': '#333', 'marginBottom': '30px'}),
                          html.P("Painel interativo gerado a partir dos dados estatísticos de e-commerce.",
                                 style={'textAlign': 'center', 'color': '#666', 'fontSize': '16px',
                                        'marginBottom': '40px'}),

                          # Grid de Gráficos
                          html.Div(
                              style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center', 'gap': '20px'},
                              children=[

                                  html.Div(style={'width': '48%', 'minWidth': '400px', 'backgroundColor': 'white',
                                                  'padding': '15px', 'borderRadius': '8px',
                                                  'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
                                      dcc.Graph(figure=fig_hist)
                                  ]),

                                  html.Div(style={'width': '48%', 'minWidth': '400px', 'backgroundColor': 'white',
                                                  'padding': '15px', 'borderRadius': '8px',
                                                  'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
                                      dcc.Graph(figure=fig_scatter)
                                  ]),

                                  html.Div(style={'width': '48%', 'minWidth': '400px', 'backgroundColor': 'white',
                                                  'padding': '15px', 'borderRadius': '8px',
                                                  'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
                                      dcc.Graph(figure=fig_bar)
                                  ]),

                                  html.Div(style={'width': '48%', 'minWidth': '400px', 'backgroundColor': 'white',
                                                  'padding': '15px', 'borderRadius': '8px',
                                                  'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
                                      dcc.Graph(figure=fig_corr)
                                  ])

                              ])
                      ])

# 5. Execução do Servidor Local
if __name__ == '__main__':
    app.run(debug=True)