# Submissão Oficial — Regressão Logística

**Data:** 28/04/2026
**Atividade:** 03 — Avaliação de Classificadores
**Disciplina:** Machine Learning
**Equipe:** 2 computeiros e um matemágico

---

## Resumo

| Campo | Valor |
|---|---|
| **Modelo usado** | Logistic Regression |
| **Hiperparâmetros** | `C=3.0`, `solver='lbfgs'`, `max_iter=4000`, `random_state=42` |
| **Acurácia no servidor** | **64.31%** |
| **Status** | ✅ Sucesso |
| **URL do servidor** | `https://aydanomachado.com/mlclass/03_Validation.php` |
| **DEV_KEY** | `2 computeiros e um matemagico` |
| **Predições enviadas** | 1045 |
| **Resposta do servidor** | `{\"status\":\"success\",\"dev_key\":\"...\",\"accuracy\":0.6430622009569378,\"old_accuracy\":0}` |

---

## Pipeline Utilizado

O pipeline do script é idêntico ao usado nos notebooks de validação:

```
Pipeline([
  ('preprocessor', ColumnTransformer([
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False), ['sex']),
    ('num', StandardScaler(), [length, diameter, height, whole_weight, shucked_weight, viscera_weight, shell_weight])
  ])),
  ('classifier', LogisticRegression(C=3.0, solver='lbfgs', max_iter=4000, random_state=42))
])
```

**Features após pré-processamento (9 no total):**
- `sex_I`, `sex_M` (One-Hot Encoding, drop='first')
- `length`, `diameter`, `height`, `whole_weight`, `shucked_weight`, `viscera_weight`, `shell_weight` (StandardScaler)

---

## Comparação com Validação Local

| Fonte | Accuracy | Observação |
|---|---|---|
| CV local (10-fold) | 64.99% ± 1.98% | Mais otimista porque usa apenas 80% dos dados |
| Holdout local | 66.67% | Validação em 20% separado |
| **Servidor professor** | **64.31%** | Resultado oficial — a fonte mais confiável |

A diferença de ~0.5-2% entre holdout/local e servidor é normal. O servidor usa um conjunto de teste secreto que não vemos, então a acurácia real sempre varia um pouco.

---

## Por que Logistic Regression em vez de SVM (RBF)?

O SVM (RBF) teve melhor acurácia local (65.27% vs 64.99% em CV), mas a diferença era de apenas ~0.3%.权衡:

| Critério | Logistic Regression | SVM (RBF) |
|---|---|---|
| Performance | ✅ 64.99% CV | ✅ 65.27% CV (+0.28%) |
| Interpretabilidade | ✅ Coeficientes explicáveis | ❌ “caixa preta” |
| Complexidade | ✅ Simples, rápido | ⚠️ Mais complexo |
| Justificativa para professor | ✅ Fácil de explicar | ⚠️ Difícil de explicar |

**Decisão:** Logistic Regression. A margem de ~0.3% não justifica perder a capacidade de explicar os coeficientes ao professor durante a apresentação/defesa.

---

## Coeficientes do Modelo (para apresentação)

Os coeficientes mostram como cada feature empurra a classificação para cada classe:

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

**Interpretação rápida:**
- **Classe 1:** strongly puxada por `sex_I` (infantil) e `shucked_weight`
- **Classe 3:** strongly puxada por `whole_weight` e `shell_weight` (abalone adulta e pesada)
- **Classe 2:** fica no meio — balanceada entre as outras duas

---

## Distribuição das Predições

| Classe | Treino (%) | Predito (%) | Diferença |
|---|---|---|---|
| 1 | 34.4 | 31.9 | -2.6% |
| 2 | 32.0 | 33.1 | +1.1% |
| 3 | 33.6 | 35.0 | +1.5% |

A distribuição das predições é coerente com a do treino — não houve colapso em classe única, o que indicaria overfitting.

---

## Arquivos Entregues

| Arquivo | Local | Conteúdo |
|---|---|---|
| `abalone_logreg_submission.py` | `mlclass/03_Validation/` | Script de envio (treino + predição + POST) |
| `abalone_logreg_submission.csv` | `mlclass/03_Validation/` | CSV de backup das predições LR |
| `abalone_submission.csv` | `pipeline_output/` | CSV das predições SVM (RBF) — não enviado |
| `notebook_5_insights.md` | `Questao_2_ML/docs/` | Documentação oficial dos resultados |

---

## Próximo Envio Possível

⚠️ A atividade permite **1 envio a cada 12h**. Se quiser tentar melhorar a acurácia (por exemplo, enviando com SVM RBF ou ajustando hiperparâmetros), aguarde pelo menos 12h após este envio.

### Ideias para próxima tentativa (se decidir enviar novamente):
1. **SVM (RBF)** com grid search em `C` e `gamma` — pode ganhar ~0.5-1%
2. **Feature engineering** — criar ratios de peso, remover correlacionadas
3. **Ensemble** — Voting entre LR + SVM RBF + LDA