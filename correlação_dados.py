import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv(r'C:\Users\Moises\Downloads\pychard\clientes-v3-preparado.csv')

# Uso do Pandas
print('Estatistica do dataframe: \n', df.describe())

print('Estatistica de um campo: \n', df[['salario', 'anos_experiencia']].describe())

print('Correlação: \n', df[['salario', 'idade']].corr())
print('Correlação com Normalização: \n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())
print('Correlação com Padronização: \n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

print('Correlação: \n', df[['salario', 'idade', 'idadeMinMaxScaler', 'idadeStandardScaler', 'idadeRobustScaler']].corr())

df_filtro_idade = df[df['idade'] < 65]

print('Correlação de clientes menores de 65 anos: \n', df_filtro_idade[['salario', 'idade']].corr())

# Variável espúria - aumenta com o tempo
df['variavel_espuria'] = np.arange(len(df))

print('Variavel_espuria', df['variavel_espuria'].values)

pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod']].corr(method='pearson')
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod']].corr(method='spearman')

print('\nCorrelação de Pearson: \n', pearson_corr)
print('\nCorrelação de Spearman:\n', spearman_corr)