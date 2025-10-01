- Data preparation: Antes de tudo, é importante saber o estado do seu Dataframe.
  - Pandas Functions:
    .head() & .tail() -> retorna respectivamente os 5 primeiros e as 5 ultimas linhas do meu DataFrame
    .info() & .shape() -> info() retorna um resumo conciso do Df e o shape() uma tupla no formato (número_de_linhas, número_de_colunas).
    .isnull().sum() -> Retorna a qtde total de valores nulos (NaN) dentro de cada coluna individualmente.

- Análise estatística: Dispersão e tendência central das variáveis(How the data looks like).
  .describe() -> retorna media, desvio padrão, minimo, maximo, quartis
  .value_counts() -> retorna uma Series que contém a contagem de ocorrências de cada valor único em uma coluna
  .unique() -> retorna uma lista com os valores unicos da Series
  .nunuque() -> retorna a qtde de valores unicos da Series
- Análise multivariada e agrupamentos: Colunas interagindo entre si
  .groupby()[] -> agrupa e agrega
    ex: df.groupby('departamento')['salario'].mean()
      # Media salarial por departamento.
