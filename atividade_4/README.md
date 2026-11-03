# Clustering Espacial do Mapa Epitelial Corneano (OCT RTVue)

Projeto de **Aprendizado Não-Supervisionado (Unsupervised Machine Learning)**voltado à análise morfológica e descoberta de perfis de espessura do epitélio da córnea humana utilizando dados de tomografia de coerência óptica de domínio espectral (**SD-OCT RTVue**).

---

## Contexto Clínico & Relevância Médica

O epitélio corneano é uma camada celular dinâmica que atua como compensador óptico: ele tende a afinar sobre irregularidades ou elevações do estroma corneano e a espessar sobre depressões ("efeito donut"). 

Na oftalmologia diagnóstica, a **paquimetria epitelial setorial**por OCT é uma das ferramentas mais sensíveis para:
1. **Detecção precoce de ceratocone e ectasias corneanas**, antes mesmo de alterações detectáveis na topografia/curvatura anterior.
2. Identificação de padrões de afinamento focal (tipicamente no setor inferior ou inferotemporal).
3. Triagem pré-operatória de segurança para cirurgia refrativa a laser (LASIK/PRK).

O objetivo deste projeto é aplicar algoritmos de agrupamento não-supervisionado para mapear perfis fenotípicos naturais de distribuição epitelial na população estudada.

---

## Mapeamento Espacial dos Setores Anatômicos

Os dados capturados pelo tomógrafo RTVue dividem a córnea em 8 setores paracentrais/periféricos e 1 zona central:

```
                  Superior (S)
        Superior-Nasal (SN)   Superior-Temporal (ST)
    Nasal (N)          Central (C)          Temporal (T)
        Inferior-Nasal (IN)   Inferior-Temporal (IT)
                  Inferior (I)
```

| Sigla | Setor Corneano | Relevância no Diagnóstico Clínico |
|:---:|---|---|
| **C**| Central | Espessura basal de referência (geralmente ~50-54 $\mu$m em olhos saudáveis) |
| **S**| Superior | Setor fisiologicamente mais espesso devido à proteção palpebral superior |
| **ST**| Superior Temporal | Quadrante súpero-lateral |
| **T**| Temporal | Meridiano horizontal temporal |
| **IT**| Inferior Temporal | **Setor crítico:**localização mais comum do ápice do cone em ceratocones precoces |
| **I**| Inferior | **Setor crítico:**assimetrias I - S (Inferior menos Superior) são preditores de ectasia |
| **IN**| Inferior Nasal | Quadrante ínfero-medial |
| **N**| Nasal | Meridiano horizontal nasal |
| **SN**| Superior Nasal | Quadrante súpero-medial |

Além dos 9 atributos espaciais de espessura ($\mu$m), a base registra:
- `pID`: Identificador anônimo do paciente (permite pareamento entre olhos).
- `Age`: Idade do paciente (covariável demográfica).
- `Gender`: Sexo biológico.
- `Eye`: Lateralidade ocular (`OD` = *Oculus Dexter* / Olho Direito; `OS` = *Oculus Sinister* / Olho Esquerdo).

---

## Fluxo de Trabalho & Engenharia de Dados

1. **Ingestão & Auditoria (`notebooks/01_data_loading.ipynb`):**
   - Carga do conjunto bruto `RTVue_20221110_MLClass.csv`.
   - Limpeza de caracteres não numéricos e padronização de tipos primitivos.
   - Detecção de inconsistências de digitação e verificação de integridade referencial por paciente (`pID`).
   - Exportação da base higienizada e auditada para `df_clean.csv`.

2. **Engenharia de Atributos Anatômicos (Feature Engineering):**
   - Criação de índices derivados de assimetria espacial:
     - Diferença vertical: $\Delta_{vert} = \text{I} - \text{S}$
     - Diferença inferotemporal: $\Delta_{IT-SN} = \text{IT} - \text{SN}$
     - Desvio padrão epitelial espacial: heterogeneidade da camada epitelial.

3. **Clusterização & Análise de Padrões:**
   - Padronização de escala com `StandardScaler` e `RobustScaler`.
   - Aplicação de K-Means, Clustering Hierárquico (Ward) e DBSCAN para segmentação de fenótipos epiteliais típicos vs atípicos/ectásicos.
   - Projeção t-SNE e PCA para visualização da separação geométrica dos padrões.

---

## Estrutura de Arquivos

```
atividade_4/
 enunciado.txt                           # Diretrizes do problema clínico e descrição dos setores
 RTVue_20221110_MLClass.csv             # Conjunto de dados brutos de OCT epitelial
 df_clean.csv                            # Base tratada e validada pós-ingestão
 notebooks/
     01_data_loading.ipynb               # Pipeline de carga, auditoria e limpeza dos dados
```

---

## Como Executar

```bash
jupyter notebook notebooks/01_data_loading.ipynb
```
