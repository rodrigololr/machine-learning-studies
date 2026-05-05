


### 1. Defina o que é Aprendizagem de Máquina, quando existe a real necessidade de aplicá-la. Também cite e explique os 3 tipos de Aprendizagem de Máquina falados em sala.

Definição: É a área que busca desenvolver algoritmos capazes de aprender padrões a partir de dados e melhorar seu desempenho em tarefas específicas sem serem explicitamente programados para cada regra.

Necessidade: Aplicamos Machine Learning quando as regras são muito complexas para serem descritas manualmente ou quando os dados mudam constantemente

- Supervisionada: Na aprendizagem supervisionada o modelo aprende a partir de dados rotulados e sabe exatamente o que deve retornar, por exemplo, rotular email como spam

- Não supervisionada: O modelo busca encontrar padrões ou estruturas ocultas em dados sem rótulos. exemplos: Agrupamento (clustering) de clientes por comportamento.

- Por reforço: Em suma, tentiva e erro, pórem com ressalvas, onde quando o modelo erra ele é penalizado e quando acerta é recomensado. Por exemplo, um agente aprender um "padrão" de um jogo, sendo recompesado quando ganha e punido quando perde


### 2. Como se dá o processo de descoberta de conhecimento em banco de dados?

O processo é conhecido como KDD (Knowledge Discovery in Databases) e é composto por 5 etapas sequenciais que transformam dados brutos em conhecimento útil:

- Seleção: Identificação e extração dos dados relevantes para o problema a partir de diversas fontes (bancos de dados, planilhas, arquivos).

- Pré-processamento: Preparação dos dados selecionados para garantir sua qualidade. Envolve:
1. Limpeza: Remoção de ruídos, tratamento de inconsistências e eliminação de dados irrelevantes.
2. Enriquecimento: Tratamento de valores ausentes (imputação) e combinação com informações externas para tornar a base mais completa.

- Transformação: Procura-se reduzir a dimensionalidade ou transformar os dados em formatos mais adequados para a mineração. Exemplo: Criar um atributo "IMC" a partir dos campos de "Peso" e "Altura" (Engenharia de Atributos).

- Mineração de Dados (Data Mining): É o coração do processo, onde algoritmos de Aprendizagem de Máquina são aplicados para extrair padrões, associações ou modelos preditivos dos dados transformados.

- Interpretação e Avaliação: Análise dos resultados obtidos para verificar se o conhecimento descoberto é válido, inovador e útil para o negócio/cliente. Nesta fase, filtram-se os padrões redundantes e avalia-se o valor final gerado.

### 3. Explique de forma detalhada que metodologia você usaria para construir e avaliar classificadores.

Eu seguiria esses passos:

1. Pré-processamento e Normalização: Antes de iniciar o treinamento, aplicaria a normalização ou padronização dos dados (especialmente se usar algoritmos baseados em distância como o KNN). Isso garante que atributos com escalas diferentes não enviesem o modelo.

2. Divisão dos Dados (Holdout): Utilizaria o Método Holdout, dividindo a base em 80% para treino e 20% para teste. O modelo aprende com os 80% e sua performance final é medida nos 20% restantes (dados inéditos).

3. Validação Cruzada (K-Fold): Para tornar a avaliação mais confiável e garantir a capacidade de generalização do modelo, aplicaria a Validação Cruzada. A base seria dividida em $K$ partes; o modelo treinaria em K-1 partes e testaria na parte restante, repetindo o processo até que todas as partes fossem usadas para teste. O resultado final seria a média dos desempenhos.

4. Treinamento: Escolheria um algoritmo de classificação adequado ao problema (ex: KNN, Árvores de Decisão ou Regressão Logística) e ajustaria seus hiperparâmetros.

5. Avaliação por Matriz de Confusão: Utilizaria a Matriz de Confusão para analisar os erros e acertos. A partir dela, calcularia métricas como:

- Acurácia: Proporção total de acertos.
- Precisão e Recall (Revocação): Para entender o desempenho em cada classe específica e evitar problemas como o Overfitting (decorar os dados de treino).
- Escolha da Métrica: A escolha da métrica principal (ex: priorizar Recall em diagnósticos médicos) dependeria inteiramente da natureza do problema de negócio.


### 4. Por que existe a necessidade da redução de dimensionalidade? Como você trataria esse problema?

Necessidade: Ter atributos demais aumenta o custo computacional (tempo e memória), gera redundância (dados que dizem a mesma coisa) e insere ruído no modelo, o que pode levar a associações falsas e prejudicar o aprendizado. Reduzir a base torna o modelo mais simples, rápido e com maior capacidade de generalização.

Tratamento: Eu trataria o problema através de duas frentes principais:

1. Seleção de Atributos (Feature Selection): Identificar e remover manualmente colunas irrelevantes para o problema (ex: ID do caminhão em uma classificação de frutas) ou usar métodos estatísticos para manter apenas as variáveis com maior correlação com o alvo.

2. Extração de Atributos (Feature Extraction):
- Engenharia de Atributos: Criar novas variáveis que resumam a informação de outras (ex: transformar Peso e Altura em IMC).
- PCA (Principal Component Analysis): Aplicar esta técnica matemática para projetar os dados em um novo espaço de menor dimensão, combinando as variáveis originais em "componentes principais" que preservam o máximo de informação (variância) possível, eliminando a redundância.
