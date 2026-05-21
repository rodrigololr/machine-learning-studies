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
  --success: #059669;
  --warning: #d97706;
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

section.dark {
  background:
    linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
  color: #f0f4f8;
}

section.dark h1, section.dark h2, section.dark h3 {
  color: #93c5fd;
}

section.dark p, section.dark li {
  color: #e2e8f0;
}

section.dark strong {
  color: #bfdbfe;
}

section.dark img {
  border: 1px solid rgba(147, 197, 253, 0.2);
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

.success {
  color: var(--success);
  font-weight: bold;
}

.warning {
  color: var(--warning);
  font-weight: bold;
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

table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.5rem 0;
  font-size: 0.85em;
}

th, td {
  border: 1px solid #cbd5e1;
  padding: 0.5rem 0.75rem;
  text-align: center;
}

th {
  background-color: var(--accent);
  color: white;
  font-weight: 600;
}

tr:nth-child(even) {
  background-color: rgba(29, 78, 216, 0.04);
}

.best {
  background-color: #d1fae5 !important;
  font-weight: bold;
}

.columns {
  display: flex;
  gap: 1.5rem;
}

.columns > div {
  flex: 1;
}

.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.metric-card {
  background: white;
  border-radius: 12px;
  padding: 0.75rem 1rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  text-align: center;
}

.metric-value {
  font-size: 1.8em;
  font-weight: bold;
  color: var(--accent);
}

.metric-label {
  font-size: 0.75em;
  color: #64748b;
  margin-top: 0.25rem;
}
</style>

<!-- _class: lead -->
<!-- _paginate: false -->

# Perfil de Olhos Barrett II

## Segmentacao Biometrica via Clustering

**Consultoria em Engenharia de Conhecimento e Data Mining**

Equipe: 2 computeiros e um matematico

---

## O Desafio

Voces nos contrataram para responder uma pergunta:

> **"Existem perfis distintos de olhos na nossa base de dados?"**

- **Base:** Barrett II Eyes — 1.528 registros de medidas oculares
- **Abordagem:** Aprendizado **nao-supervisionado** — sem rotulos, sem classes
- **Objetivo:** Descobrir **grupos naturais** baseados apenas na anatomia do olho
- **Entregavel:** Caracterizacao completa de cada perfil encontrado

> "Nao partimos de hipoteses — deixamos os dados revelarem os padroes."

---

## As Variaveis que Usamos

Somente **5 medidas biometricas** — nada mais:

| Variavel | O que e | Unidade | Faixa Observada |
|----------|---------|---------|-----------------|
| **AL** | Comprimento axial do olho | mm | 20.15 – 30.96 |
| **ACD** | Profundidade de camara anterior | mm | 1.13 – 5.23 |
| **WTW** | Distancia branco a branco | mm | 9.90 – 13.30 |
| **K1** | Curvatura no meridiano menos curvo | D | 30.93 – 49.41 |
| **K2** | Curvatura no meridiano mais curvo | D | 33.95 – 52.41 |

> **Importante:** A coluna "Correto" (S/N) **nao foi usada** para encontrar os grupos. Ela sera apresentada apenas como complemento, apos os perfis ja definidos.

---

## Anatomia do Olho — Referencia Visual

![height:350](https://www.draandreia.com.br/wp-content/uploads/2017/09/biom4.png)

- **AL (Axial Length):** do cornea ate a retina — define o "tamanho" do olho
- **ACD (Anterior Chamber Depth):** espaco entre cornea e cristalino
- **WTW (White-to-White):** diametro horizontal da cornea
- **K1/K2 (Keratometria):** curvatura da superficie corneana

*Fonte: Dra. Andreia — Referencia oftalmologica*

---

<!-- _class: visual -->

## Exploracao Inicial — Distribuicoes

![height:280](./imgs/hist_all.png)

- **AL:** maior variabilidade (range de 10.81mm), distribuicao assimetrica
- **WTW:** mais uniforme, menor variacao (std=0.43mm)
- **K1 e K2:** distribuicoes similares — mesma familia de medida

---

<!-- _class: visual -->

## Exploracao Inicial — Outliers

![height:300](./imgs/boxplot_all.png)

| Variavel | Outliers | % |
|----------|----------|---|
| AL | 44 | 2.9% |
| ACD | 26 | 1.7% |
| WTW | 7 | 0.5% |
| K1 | 26 | 1.7% |
| K2 | 21 | 1.4% |

Outliers representam **variabilidade anatomica real** — mantidos na analise.

---

<!-- _class: visual -->

## Exploracao Inicial — Correlacoes

![height:350](./imgs/correlation.png)

- **K1 x K2:** r = 0.975 — fortissima correlacao, esperado
- **AL x ACD:** correlacao moderada — olhos maiores tendem a ter camara mais profunda
- **WTW:** relativamente independente — captura dimensao unica

---

## Pre-processamento

Para algoritmos de distancia, padronizamos as escalas:

| Metodo | Resultado |
|--------|-----------|
| **StandardScaler** | Media=0, Std=1 |
| **MinMaxScaler** | Range=[0,1] |

- **Escolha:** StandardScaler — mais adequado para clustering
- **Sem vazamento:** scaler ajustado apenas nos dados de treino
- **Outliers mantidos:** representam variabilidade real do olho

![height:180](./imgs/preprocessing_comparison.png)

---

## Metodologia — 3 Abordagens de Clustering

| Algoritmo | Filosofia |
|-----------|-----------|
| **K-Means** | Minimiza variancia dentro de cada grupo |
| **DBSCAN** | Detecta regioes de alta densidade |
| **Hierarchical (Ward)** | Constroi arvore de similaridade |

**Por que testar 3?**
- Garantir que os perfis encontrados sao **reais**, nao artefato de um metodo
- Cada algoritmo revela aspectos diferentes da estrutura dos dados

---

<!-- _class: visual -->

## Quantos Perfis Existem? — Elbow Method

![height:320](./imgs/elbow_plot.png)

- O "cotovelo" aparece entre **K=2 e K=4**
- Apos K=4, o ganho marginal e minimo
- **K=2** oferece melhor equilibrio: simplicidade + separacao

---

<!-- _class: visual -->

## Quantos Perfis Existem? — Silhouette Analysis

![height:320](./imgs/silhouette_plot.png)

| K | Silhouette Score |
|---|------------------|
| **2** | **0.2867** |
| 3 | 0.2233 |
| 4 | 0.2223 |
| 5 | 0.2080 |

**K=2 e o otimo** — maior coesao interna e melhor separacao entre grupos.

---

<!-- _class: visual -->

## Resultado Principal — K-Means com K=2

![height:350](./imgs/kmeans_pca_tsne.png)

- **Grupo 0:** 742 olhos (48.6%)
- **Grupo 1:** 786 olhos (51.4%)
- PCA e t-SNE confirmam: **2 grupos naturais e bem separados**

---

<!-- _class: visual -->

## Os Dois Perfis — Radar Chart

![height:320](./imgs/radar_kmeans.png)

| Grupo | AL | ACD | WTW | K1 | K2 |
|-------|------|------|------|-------|-------|
| **0** | -0.615 | -0.380 | -0.577 | +0.664 | +0.683 |
| **1** | +0.580 | +0.358 | +0.544 | -0.627 | -0.645 |

*Valores padronizados (desvios da media)*

---

## DBSCAN — O Que Revelou?

![height:280](./imgs/kdistance_plot.png)

- **Resultado:** 1 cluster dominante (98.5% dos dados)
- **23 pontos** como ruido (1.5%)
- DBSCAN nao encontrou subgrupos — dados formam regiao de densidade continua
- **Conclusao:** K-Means e mais adequado para esta base

---

<!-- _class: visual -->

## Hierarchical — Confirmacao Independente

![height:350](./imgs/dendrogram.png)

- **Ward linkage:** minimiza variancia intra-grupo
- **2 grupos:** 998 (65.3%) e 530 (34.7%)
- Dendrograma confirma: **estrutura bimodal** nos dados
- Divisao principal na distancia ~50

---

## Validacao — Qual Metodo e Melhor?

| Metodo | Silhouette ↑ | Calinski-Harabasz ↑ | Davies-Bouldin ↓ |
|--------|--------------|---------------------|------------------|
| **K-Means (K=2)** | **0.2867** | **760.43** | **1.2582** |
| DBSCAN | 0.5441 | 13.06 | 4.5533 |
| Hierarchical | 0.2438 | 569.32 | 1.3868 |

**K-Means (K=2) vence em todas as metricas relevantes:**
- <span class="success">Melhor separacao entre grupos</span> (Calinski-Harabasz)
- <span class="success">Menor sobreposicao</span> (Davies-Bouldin)

---

<!-- _class: dark -->

## Perfil 1 — Grupo 0: Olhos Compactos

### Caracteristicas

- **AL menor:** olho mais curto (-0.615 std)
- **ACD menor:** camara anterior mais rasa (-0.380 std)
- **WTW menor:** cornea de diametro menor (-0.577 std)
- **K1/K2 maiores:** cornea mais curva (+0.66 / +0.68 std)

> **Interpretacao clinica:** Olhos menores com cornea mais curva — anatomia que pode estar associada a tendencia de hipermetropia. Requer atencao especial em calculos de Lente Intraocular (LIO).

---

<!-- _class: dark -->

## Perfil 2 — Grupo 1: Olhos Alongados

### Caracteristicas

- **AL maior:** olho mais longo (+0.580 std)
- **ACD maior:** camara anterior mais profunda (+0.358 std)
- **WTW maior:** cornea de diametro maior (+0.544 std)
- **K1/K2 menores:** cornea mais plana (-0.63 / -0.65 std)

> **Interpretacao clinica:** Olhos maiores com cornea mais plana — anatomia que pode estar associada a tendencia de miopia. Protocolos de medicao e calculo de LIO podem ser ajustados para este perfil.

---

## Complemento: Distribuicao da Coluna "Correto"

> **Atencao:** Esta analise e **apenas complementar**. Os grupos foram definidos **somente** pelas 5 variaveis biometricas. A coluna "Correto" **nao e uma classe** — nao foi usada para identificar padroes.

| | Grupo 0 | Grupo 1 | Total |
|---|-----------|-----------|-------|
| **N (Nao)** | 228 | 218 | 446 |
| **S (Sim)** | 514 | 568 | 1.082 |
| **Total** | 742 | 786 | 1.528 |

**Teste Qui-Quadrado:** Chi2 = 1.51, **p-value = 0.2188**

> Nao ha associacao significativa entre grupo e corretude (p > 0.05).  
> Os grupos capturam **variabilidade anatomica**, nao qualidade de medida.

---

## Conclusoes

### O que descobrimos

1. **Existem 2 perfis de olhos** distintos na base Barrett II
2. **K-Means (K=2)** e o metodo mais robusto para esta segmentacao
3. A diferenca principal e **dimensoes axiais vs. curvatura corneana**

### O que isso significa para voces

- **Grupo 0 (Compactos):** olhos menores, cornea mais curva — atencao em calculos de LIO
- **Grupo 1 (Alongados):** olhos maiores, cornea mais plana — protocolos ajustaveis
- Segmentacao permite **personalizar protocolos** clinicos por perfil

### Proximos passos sugeridos

- Validar com amostra externa de pacientes
- Investigar correlacao com desfechos cirurgicos reais
- Expandir analise para subgrupos por idade e sexo

---

*20/05/2026 — Consultoria em Engenharia de Conhecimento e Data Mining*
