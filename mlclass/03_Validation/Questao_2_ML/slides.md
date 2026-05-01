---
marp: true
theme: gaia
paginate: true
---

<style>
:root {
  --bg: #f7f5f1;
  --bg-2: #eef2f7;
  --text: #243447;
  --accent: #1d4ed8;
  --accent-soft: rgba(29, 78, 216, 0.08);
}

section {
  background:
    radial-gradient(circle at top right, rgba(29, 78, 216, 0.06), transparent 28%),
    radial-gradient(circle at bottom left, rgba(29, 78, 216, 0.04), transparent 30%),
    linear-gradient(180deg, var(--bg) 0%, var(--bg-2) 100%);
  color: var(--text);
  font-size: 26px;
}

section.lead {
  background:
    linear-gradient(135deg, rgba(29, 78, 216, 0.08), rgba(29, 78, 216, 0.02)),
    linear-gradient(180deg, var(--bg) 0%, var(--bg-2) 100%);
  border-top: 10px solid var(--accent);
}

section.visual {
  background:
    radial-gradient(circle at top left, rgba(29, 78, 216, 0.05), transparent 30%),
    linear-gradient(180deg, var(--bg) 0%, var(--bg-2) 100%);
}

h1, h2, h3 {
  color: var(--accent);
  letter-spacing: -0.02em;
}

h1 {
  font-size: 2.0em;
}

h2 {
  border-bottom: 2px solid rgba(29, 78, 216, 0.20);
  padding-bottom: 0.18em;
  margin-bottom: 0.45em;
}

p, li {
  color: var(--text);
  line-height: 1.35;
}

strong, .accent {
  color: var(--accent);
}

img {
  display: block;
  margin: 0.25rem auto 0.65rem auto;
  border-radius: 18px;
  border: 1px solid rgba(36, 52, 71, 0.08);
  box-shadow: 0 18px 45px rgba(36, 52, 71, 0.12);
  max-width: 100%;
}

blockquote {
  margin: 0.5rem 0 0.8rem 0;
  padding: 0.65rem 0.9rem;
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  border-radius: 0 12px 12px 0;
}

.small {
  font-size: 0.82em;
}

</style>

<!-- _class: lead -->
<!-- _paginate: false -->

# Abalone Classification

**Atividade 03 — Avaliacao de Classificadores**

Equipe: 2 computeiros e um matematico  
Modelo final: Regressao Logistica (C=3.0)  
Resultado oficial: **64.31%** de acuracia no servidor

---

## O Problema

- Classificar Abalone em **3 tipos** (1, 2 e 3)
- **8 features**: sexo, comprimento, diametro, altura, pesos
- **3.132** registros de treino e **1.045** de aplicacao
- Classes balanceadas: **34% / 32% / 34%**
- Objetivo: boa validacao local e envio ao servidor oficial

---

## EDA — O Que Descobrimos

<!-- _class: visual -->
![height:350](./docs/correlation_heatmap.png)

- Features **muito correlacionadas** (length x diameter = 0.99)
- `sex` muito informativa: infantil = classe 1, femea = classe 3
- LDA: componente 1 explica **88.4%** da variancia discriminante
- **Classe 2** e a mais dificil (sobreposicao com classe 3)

---

## Pre-processamento

- **Split estratificado**: 80% treino / 20% validacao
- `sex` = OneHotEncoder (drop='first') = **sex_I, sex_M**
- Numericas = **StandardScaler**
- Sem vazamento: scaler ajustado **so no treino**
- Resultado: **9 features** (2 dummy + 7 padronizadas)

---

## Comparacao de Modelos

<!-- _class: visual -->
![height:350](./docs/model_comparison.png)

- **SVM (RBF)** liderou a validacao cruzada
- **Logistic Regression** ficou muito perto
- Modelos lineares foram fortes desde o inicio
- Dummy confirmou que existe sinal real na base

---

## Por Que Logistic Regression?

- **Trade-off:** performance vs interpretabilidade
- Diferenca para SVM (RBF): apenas **0.28%** em CV
- Logistic Regression entrega coeficientes explicaveis
- C=3.0 foi o melhor ajuste testado para o modelo
- SVM (RBF) ficou como benchmark de desempenho

---

## O Modelo Explica as Classes

<!-- _class: visual -->
![height:320](./docs/logreg_coefficients.png)

- **Classe 1**: `sex_I` e `shucked_weight`
- **Classe 3**: `whole_weight` e `shell_weight`
- **Classe 2**: intermediaria, com maior sobreposicao
- Coeficientes ajudaram na defesa do modelo com o professor

---

## Resultado no Servidor

<!-- _class: visual -->
![height:350](./docs/confusion_matrix_logreg.png)

- Acuracia oficial: **64.31%**
- Predicoes enviadas: **1.045**
- Distribuicao coerente com o treino
- Pipeline completo validado: EDA = preprocessamento = modelagem = submissao

---

## Conclusao

- Regressao Logistica foi a escolha certa para a defesa
- SVM (RBF) foi o melhor benchmark, mas com pouca vantagem
- Classe 2 continua sendo o gargalo do problema
- O pipeline ficou limpo, estratificado e sem vazamento

**O modelo mais simples foi o suficiente.**

---

*28/04/2026 — Atividade 03 — Machine Learning*
