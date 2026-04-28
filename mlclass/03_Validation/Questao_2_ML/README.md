# Questão 2 - ML - Atividade 03: Avaliação de Classificadores

## Objetivo
Construir e validar um modelo preditivo (classificador) para identificar o tipo do exemplar de Abalone (classes I, II e III), garantindo o poder de generalização do modelo.

## Dataset
- **Treino/Validação:** `abalone_dataset.csv` (3132 registros, com rótulo `type`)
- **Teste/Aplicação:** `abalone_app.csv` (1045 registros, sem rótulo)

## Atributos
| Atributo | Descrição |
|---|---|
| `sex` | Sexo: M (macho), F (fêmea), I (infantil) |
| `length` | Maior medida em mm da concha |
| `diameter` | Diâmetro em mm perpendicular a `length` |
| `height` | Altura em mm com a carne dentro da concha |
| `whole_weight` | Peso em gramas de toda a abalone |
| `shucked_weight` | Peso em gramas da carne |
| `viscera_weight` | Peso em gramas das vísceras após escorrer |
| `shell_weight` | Peso em gramas da concha após estar seca |
| `type` | **Variável alvo** - classes 1, 2 ou 3 |

## Arquitetura de Notebooks

### 01 - Estudo dos Dados
**Objetivo:** Entender a estrutura, schema e primeiras características do dataset.

- Leitura dos CSVs
- Shape e tipos de dados
- Valores nulos e duplicados
- Estatísticas descritivas
- Comparação train vs app

### 02 - Análise Exploratória Detalhada (EDA)
**Objetivo:** Explorar padrões, distribuições e relações entre variáveis.

- Histogramas das variáveis numéricas
- Boxplots por classe
- Análise de outliers
- Correlação entre variáveis
- Relação sex vs type
- Análise de separabilidade

### 03 - Pré-processamento e Transformação
**Objetivo:** Preparar os dados para modelagem sem vazamento.

- Definição da variável alvo
- Split estratificado local (holdout)
- Encoding de `sex`
- Padronização/normalização
- Pipeline e ColumnTransformer
- Teste de transformações

### 04 - Modelagem e Validação
**Objetivo:** Comparar modelos, validar e escolher o melhor.

- Modelos: Dummy, LogisticRegression, KNN, SVM, DecisionTree, RandomForest
- Validação: StratifiedKFold + Holdout
- Métricas: Accuracy, Macro F1, Matriz de confusão
- Tabela comparativa

### 05 - Modelo Final e Predição em App
**Objetivo:** Treinar modelo final e gerar arquivo de submissão.

- Treino com toda a base rotulada
- Predição em `abalone_app.csv`
- Geração do arquivo de submissão
- Verificação do formato

## Regras Importantes

1. **Nunca usar `abalone_app.csv` para treinar** — apenas para predição final
2. **Sempre usar split estratificado** para manter a proporção das classes
3. **Transformações dentro de Pipeline** para evitar vazamento de dados
4. **Comparar pelo menos 3 modelos** antes de escolher o final
5. **Validar localmente antes de enviar** — 1 envio a cada 12h

## Critérios de Escolha do Modelo Final

1. Maior **accuracy**
2. Melhor **macro F1**
3. Menor complexidade
4. Maior estabilidade na validação

## Stack Tecnológico

- Python 3
- pandas
- matplotlib / seaborn
- scikit-learn

## Pasta de Origem dos Dados
`../mlclass/03_Validation/`

---

## Resultado Oficial da Submissão

**Data do envio:** 28/04/2026
**Modelo:** Logistic Regression (C=3.0, solver='lbfgs', max_iter=4000, random_state=42)

### Comparação de Modelos (10-fold Stratified CV)

| Modelo | Accuracy CV | Macro F1 CV | Holdout |
|---|---|---|---|
| SVM (RBF) | 0.6527 ± 0.0258 | 0.6470 ± 0.0246 | 0.6762 |
| **Logistic Regression (C=3.0)** | **0.6499 ± 0.0198** | **0.6455 ± 0.0194** | **0.6667** |
| SVM (Linear) | 0.6463 ± 0.0209 | 0.6455 ± 0.0202 | 0.6571 |
| Random Forest (100) | 0.6359 ± 0.0278 | 0.6324 ± 0.0257 | — |
| LDA | 0.6323 ± 0.0224 | 0.6338 ± 0.0211 | — |
| KNN (k=5) | 0.6144 ± 0.0224 | 0.6109 ± 0.0210 | — |
| Decision Tree | 0.5740 ± 0.0288 | 0.5702 ± 0.0280 | — |
| Dummy (most frequent) | 0.3441 ± 0.0014 | 0.1707 ± 0.0005 | — |

### Resultado no Servidor do Professor

| Campo | Valor |
|---|---|
| **Acurácia oficial** | **64.31%** |
| Status | ✅ Sucesso |
| Servidor | `https://aydanomachado.com/mlclass/03_Validation.php` |
| DEV_KEY | `2 computeiros e um matemagico` |
| Predições enviadas | 1045 |

### Distribuição das Classes Preditas

| Classe | Treino | Predito | Diferença |
|---|---|---|---|
| 1 | 34.4% | 31.9% | -2.6% |
| 2 | 32.0% | 33.1% | +1.1% |
| 3 | 33.6% | 35.0% | +1.5% |

### Decisão Final

> Escolhemos **Logistic Regression (C=3.0)** como modelo principal por **interpretabilidade**. A diferença de performance vs SVM (RBF) era de apenas ~0.4% em CV, então a capacidade de explicar os coeficientes ao professor outweigh the marginal gain do SVM. O SVM (RBF) foi mantido como benchmark de desempenho.

### Artefatos da Submissão

| Arquivo | Descrição |
|---|---|
| `abalone_logreg_submission.py` | Script Python que treina o modelo e envia ao servidor |
| `abalone_logreg_submission.csv` | CSV de backup das predições Logistic Regression |
| `pipeline_output/abalone_submission.csv` | CSV das predições SVM (RBF) — não enviado |
| `pipeline_output/model_comparison.csv` | Tabela comparativa de todos os modelos |
| `pipeline_output/final_pipeline.pkl` | Pipeline sklearn completo (SVM) |