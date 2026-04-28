# Notebook 1 — Estudo dos Dados

## Objetivo
Entender a estrutura da base, checar qualidade dos dados e levantar hipóteses iniciais para a etapa de pré-processamento e modelagem.

## Resumo dos resultados

- **Treino:** 3132 linhas, 9 colunas
- **Aplicação:** 1045 linhas, 8 colunas
- **Valores nulos:** nenhum
- **Duplicados:** nenhum
- **Classes do target:** 1, 2 e 3
- **Sex:** M, I e F

## Insights principais

### 1) Base bem limpa
Não foram encontrados valores nulos nem linhas duplicadas em treino ou aplicação. Isso reduz a necessidade de limpeza pesada e permite foco no pré-processamento e validação.

### 2) Classes razoavelmente balanceadas
A variável alvo está bem distribuída entre as três classes:

- Classe 1: 34.42%
- Classe 2: 32.02%
- Classe 3: 33.56%

Isso é positivo porque evita viés forte para uma classe dominante e facilita validação estratificada.

### 3) Variável categórica `sex` também está equilibrada
Distribuição próxima entre as categorias:

- M: 36.30%
- I: 33.27%
- F: 30.43%

Isso sugere que `sex` pode ser útil como feature.

### 4) Treino e aplicação parecem compatíveis
As médias e desvios das variáveis numéricas são próximos entre treino e aplicação. Isso indica que a base `abalone_app.csv` parece vir da mesma população do treino.

### 5) Atenção em variáveis com zero no mínimo
As variáveis abaixo tiveram mínimo igual a zero:

- `height`
- `viscera_weight`

Isso não é necessariamente erro, mas merece atenção na EDA detalhada para entender se são valores válidos ou casos extremos.

## Decisões para o Notebook 2

- Explorar assimetria das variáveis numéricas
- Verificar outliers com mais cuidado
- Avaliar correlação entre features
- Analisar a relação entre `sex` e `type`
- Verificar separabilidade das classes visualmente

## Conclusão
O dataset parece adequado para seguir para exploração detalhada e modelagem. A base está limpa, com classes equilibradas e sem sinais fortes de inconsistência entre treino e aplicação.
