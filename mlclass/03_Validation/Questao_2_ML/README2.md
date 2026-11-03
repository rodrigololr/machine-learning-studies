# Abalone Classification — Relatório Completo do Projeto

**Atividade:** 03 — Avaliação de Classificadores  
**Dataset:** Abalone (classes 1, 2 e 3)  
**Modelo final:** Regressão Logística (C=3.0, solver=lbfgs)  
**Acurácia no servidor:** 64.31% 

---

## 1. O Problema

Classificar exemplares de Abalone (molusco marinho) em três categorias (tipo 1, 2 ou 3) com base em medidas físicas: sexo, comprimento, diâmetro, altura, e pesos (whole, shucked, viscera, shell).

- **Treino:** 3.132 registros rotulados
- **Teste (app):** 1.045 registros sem rótulo
- **Classes:** razoavelmente balanceadas (34%/32%/34%)
- **Métrica de avaliação:** Acurácia (enviada ao servidor do professor)

---

## 2. O Que Investigamos (Notebooks 01 e 02)

### 2.1 Qualidade dos Dados

- Base limpa: **sem valores nulos, sem duplicados**
- Variáveis `height` e `viscera_weight` tinham mínimo zero — investigamos e eram valores válidos
- Treino e aplicação vinham da **mesma população** (médias e desvios compatíveis)

### 2.2 Padrões Encontrados na EDA

**Distribuição das classes é coerente com tamanho:**
- Classe 1 → menores medidas (juvenis/infantis)
- Classe 2 → intermediária
- Classe 3 → maiores abalones adultas

**Correlação muito alta entre features numéricas:**
- `length` × `diameter` ≈ 0.99
- `whole_weight` × `shucked_weight` ≈ 0.97
- `whole_weight` × `shell_weight` ≈ 0.95

Isso confirmou redundância — todas as variáveis medem essencialmente o mesmo eixo biológico de "tamanho/massa".

**A variável `sex` é muito informativa:**
- `sex_I` (infantil) → fortemente associado à classe 1
- `sex_F` (fêmea) → mais associada à classe 3
- `sex_M` (macho) → distribuído entre classes 2 e 3

**LDA confirmou boa estrutura de separação:**
- Componente 1 explica 88.4% da variância discriminante
- Componente 2 explica 11.6%
- **Problema:** sobreposição entre classes 2 e 3

---

## 3. O Que Fizemos (Notebook 03)

### 3.1 Split Estratificado

Separamos 80% treino / 20% validação (holdout), mantendo proporções das classes. Resultado:

| Conjunto | Classe 1 | Classe 2 | Classe 3 |
|---|---|---|---|
| Treino | 34.4% | 32.0% | 33.6% |
| Validação | 34.5% | 32.1% | 33.5% |

### 3.2 Pipeline de Pré-processamento

Mantivemos **todas** as features. Nada removemos ainda (redundância não significa que deve remover — os modelos lidam bem com isso).

**Encoding de `sex`:**
```
OneHotEncoder(drop='first', handle_unknown='ignore')
```
Gera duas colunas: `sex_I` e `sex_M` (F é a referência).

**Escalonamento das numéricas:**
```
StandardScaler()
```
Apenas as numéricas são escalonadas; o One-Hot não.

**Resultado:** 9 features finais (`sex_I`, `sex_M` + 7 numéricas padronizadas)

### 3.3 Verificação de Vazamento

Confirmamos que o Scaler viu **somente o treino** (80%):
- Treino: média ≈ 0, desvio ≈ 1 
- Validação: distribuição própria (não vazou) 

---

## 4. Comparação de Modelos (Notebooks 04 e 04.1)

Testamos 8 modelos com **10-fold Stratified Cross-Validation** e validação holdout:

### Resultados Cross-Validation (10 folds)

| Modelo | Accuracy CV | Macro F1 CV |
|---|---|---|
| **SVM (RBF)** | **0.6527 ± 0.0258** | 0.6470 ± 0.0246 |
| Logistic Regression (C=3.0) | 0.6499 ± 0.0198 | 0.6455 ± 0.0194 |
| SVM (Linear) | 0.6463 ± 0.0209 | 0.6455 ± 0.0202 |
| Random Forest (100) | 0.6359 ± 0.0278 | 0.6324 ± 0.0257 |
| LDA | 0.6323 ± 0.0224 | 0.6338 ± 0.0211 |
| KNN (k=5) | 0.6144 ± 0.0224 | 0.6109 ± 0.0210 |
| Decision Tree | 0.5740 ± 0.0288 | 0.5702 ± 0.0280 |
| Dummy (most frequent) | 0.3441 ± 0.0014 | 0.1707 ± 0.0005 |

### Resultados Holdout (20% separado)

| Modelo | Accuracy | Macro F1 |
|---|---|---|
| SVM (RBF) | 0.6762 | 0.6727 |
| **Logistic Regression** | **0.6667** | **0.6622** |
| SVM (Linear) | 0.6571 | 0.6539 |

### 4.1 Busca de Hiperparâmetros — Logistic Regression

| C | Solver | Accuracy CV | Macro F1 CV |
|---|---|---|---|
| 0.1 | lbfgs | 0.6399 | 0.6340 |
| 1.0 | lbfgs | 0.6491 | 0.6444 |
| **3.0** | **lbfgs** | **0.6499** | **0.6455** |
| 10.0 | lbfgs | 0.6491 | 0.6446 |
| 1.0 | newton-cg | 0.6495 | 0.6448 |

**Melhor configuração:** C=3.0, solver=lbfgs

---

## 5. Por Que Escolhemos Regressão Logística (Mesmo o SVM sendo Marginalmente Melhor)

A decisão foi por **interpretabilidade**, não por máxima performance pura.

### SVM (RBF) vs Logistic Regression — Comparação

| Critério | Logistic Regression  | SVM (RBF) |
|---|---|---|
| Accuracy CV | 64.99% | 65.27% (+0.28%) |
| Accuracy holdout | 66.67% | 67.62% (+0.95%) |
| **Interpretabilidade** | ** Coeficientes explicáveis** |  "caixa preta" |
| Simplicidade |  linear, 1 step |  não-linear, 2 hiperparams |
| Explicar ao professor |  fácil |  difícil |

Com Logistic Regression, conseguimos mostrar ao professor **como cada feature influencia cada classe** — impossível com SVM RBF.

### Coeficientes do Modelo (para apresentação)

| Feature | Classe 1 | Classe 2 | Classe 3 |
|---|---|---|---|
| `sex_I` (infantil) | **+0.644** | -0.149 | -0.496 |
| `sex_M` (macho) | +0.014 | -0.005 | -0.009 |
| `length` | +0.375 | +0.050 | -0.425 |
| `diameter` | -0.602 | +0.416 | +0.187 |
| `height` | -0.464 | +0.167 | +0.297 |
| `whole_weight` | -1.676 | -1.227 | **+2.903** |
| `shucked_weight` | **+2.042** | +0.508 | -2.550 |
| `viscera_weight` | +0.083 | +0.304 | -0.386 |
| `shell_weight` | -1.204 | +0.253 | +0.951 |

**Como ler:** valor positivo = puxa para essa classe, valor negativo =afasta dessa classe.

**Interpretação rápida:**
- **Classe 1:** puxada por `sex_I` (infantil) e `shucked_weight`
- **Classe 3:** puxada por `whole_weight` e `shell_weight` (abalone adulta e pesada)
- **Classe 2:** fica no meio — balanceada entre as outras duas

---

## 6. Pipeline Final

```
Pipeline([
  ('preprocessor', ColumnTransformer([
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), ['sex']),
    ('num', StandardScaler(), [length, diameter, height,
                                whole_weight, shucked_weight,
                                viscera_weight, shell_weight])
  ])),
  ('classifier', LogisticRegression(C=3.0, solver='lbfgs',
                                     max_iter=4000, random_state=42))
])
```

**Features de entrada:** 8 (7 numéricas + 1 categórica)  
**Features após pré-processamento:** 9

---

## 7. Resultado no Servidor do Professor

**URL:** `https://aydanomachado.com/mlclass/03_Validation.php`

```
{"status":"success","accuracy":0.6430622009569378}
```

| Métrica | Valor |
|---|---|
| **Acurácia no servidor** | **64.31%** |
| Status |  Sucesso |
| Data | 28/04/2026 |
| Predições | 1.045 |

### Distribuição das Predições vs Treino

| Classe | Treino | Predito | Diferença |
|---|---|---|---|
| 1 | 34.4% | 31.9% | -2.6% |
| 2 | 32.0% | 33.1% | +1.1% |
| 3 | 33.6% | 35.0% | +1.5% |

Distribuição coerente — nenhum colapso em classe única.

---

## 8. Dívidas Técnicas e Ideias para Melhorar

Se fizéssemos mais uma tentativa (lembrando: 1 envio a cada 12h):

1. **SVM (RBF)** com grid search em `C` e `gamma` — pode ganhar ~0.5-1%
2. **Feature engineering** — criar ratios de peso (ex.: shucked_weight/whole_weight)
3. **Remover features correlacionadas** — testar com apenas 4-5 features mais fortes
4. **Ensemble** — Voting entre LR + SVM RBF + LDA

---

## 9. Conclusão

O projeto seguiu o fluxo completo:
1. **EDA** → descobriu estrutura, correlação, separabilidade
2. **Pré-processamento** → split estratificado, encoding, escalonamento (sem vazamento)
3. **Modelagem** → comparou 8 modelos, elegida Logistic Regression por interpretabilidade
4. **Validação** → 10-fold CV + holdout + resultado oficial do servidor (64.31%)

A diferença de ~0.3% entre Logistic Regression e SVM RBF foi aceita em nome da explicabilidade —.choice que se paga na apresentação ao professor.

---

## Arquivos do Projeto

| Arquivo | Conteúdo |
|---|---|
| `01_estudo_dados.ipynb` | Análise inicial de estrutura e qualidade |
| `02_eda_detalhada.ipynb` | EDA completa com gráficos |
| `03_preprocessamento_transformacao.ipynb` | Split + pipeline + artefatos |
| `04_modelagem_validacao.ipynb` | Comparação de 8 modelos |
| `04_1_regressao_logistica_experimentos.ipynb` | Fine-tuning Logistic Regression |
| `05_modelo_final_e_predicao_app.ipynb` | Pipeline final + geração de submissão |
| `abalone_logreg_submission.py` | Script que enviou ao servidor |
| `abalone_logreg_submission.csv` | CSV de backup das predições |
| `docs/submissao_oficial_logreg.md` | Relatório oficial do envio |

---

*Gerado em 28/04/2026 — Atividade 03, Questão 2*