from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Carregamento dos dados
df = pd.read_csv(r'C:\Users\Moises\Downloads\pychard\clientes-v3-preparado.csv')
lista_nivel_educacao = df['nivel_educacao'].unique()
options = [{'label': nivel, 'value': nivel} for nivel in lista_nivel_educacao]


def cria_graficos(selecao_nivel_educacao):
    # Tratamento caso nada esteja selecionado para evitar erros
    if not selecao_nivel_educacao:
        filtro_df = df.head(0)  # DataFrame vazio
    else:
        filtro_df = df[df['nivel_educacao'].isin(selecao_nivel_educacao)]

    # Gráfico de Barra (removido o px.colors incompleto para usar o padrão)
    fig1 = px.bar(filtro_df, x="estado_civil", y="salario", color="nivel_educacao", barmode="group")
    fig1.update_layout(
        title='Salário por Estado Civil e Nível de Educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='rgba(222, 255, 253, 1)',  # Fundo interno
        paper_bgcolor='rgba(186, 245, 241, 1)'  # Fundo externo
    )

    # Gráfico de Dispersão 3D
    fig2 = px.scatter_3d(filtro_df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')
    fig2.update_layout(
        title='Salário vs Idade e Anos de Experiência',
        scene=dict(
            xaxis_title='Idade',
            yaxis_title='Salário',
            zaxis_title='Anos de Experiência'
        )
    )
    return fig1, fig2


def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Dashboard Interativo"),
        html.Div('''
        Interatividade entre os dados.
        '''),
        html.Br(),
        html.H2("Gráfico de Salário por Estado Civil"),
        dcc.Checklist(
            id='id_selecao_nivel_educacaor',
            options=options,
            value=[lista_nivel_educacao[0]],  # Definir valor padrão
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d')
    ])

    return app


# Criação da instância do aplicativo
app = cria_app()


# Callback para conectar o Checklist aos Gráficos
@app.callback(
    [Output('id_grafico_barra', 'figure'),
     Output('id_grafico_3d', 'figure')],
    [Input('id_selecao_nivel_educacaor', 'value')]
)
def update_graphs(selecao_nivel_educacao):
    return cria_graficos(selecao_nivel_educacao)


if __name__ == '__main__':
    app.run(debug=True)