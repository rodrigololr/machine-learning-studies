# Guia de Estudo: Tópicos Essenciais da AB2 (Baseado nos Slides)

Este guia resume os conceitos mais importantes dos slides do professor, destacando o que pode ser cobrado na prova (incluindo alternativas ao Apriori como o Partition, medidas de interesse como o Lift, e detalhes de clustering).

---

## 📑 Índice dos Módulos
1. [Agrupamento (Clustering)](#1-agrupamento-clustering)
2. [Introdução às Regras de Associação](#2-introdução-às-regras-de-associação)
3. [Medidas de Interesse (Lift, Dependência e Exceções)](#3-medidas-de-interesse-lift-dependência-e-exceções)
4. [Algoritmos de Extração: Apriori vs. Partition](#4-algoritmos-de-extração-apriori-vs-partition)

---

## 1. Agrupamento (Clustering)

Agrupamento é a identificação de um conjunto finito de categorias (clusters) que contêm objetos similares, onde os grupos **não são previamente definidos**.

### Representações de Entrada
*   **Matriz de Dados (Atributos):** Contém os valores de $p$ atributos para cada um dos $n$ objetos. (Dimensão: $n \times p$).
*   **Matriz de Dissimilaridade (Distâncias):** Contém as distâncias $d(i, j)$ calculadas entre cada par de objetos. (Simétrica, diagonal zero, valores $\ge 0$).

### Características Desejáveis de um Algoritmo de Clustering (Potencial questão teórica)
1.  **Escalabilidade:** Capacidade de rodar eficientemente com grandes volumes de dados.
2.  **Aceitar diferentes tipos de dados:** Capacidade de lidar com atributos categóricos, numéricos, binários, etc.
3.  **Identificar clusters de formatos arbitrários:** Não se limitar a formas esféricas.
4.  **Poucos parâmetros de entrada:** Exigir pouca configuração manual do usuário.
5.  **Tratamento de ruídos:** Habilidade de ignorar ou identificar outliers sem estragar os grupos.

---

## 2. Introdução às Regras de Associação

Representam padrões de relacionamento do tipo $X \Rightarrow Y$ (se compra $X$, compra $Y$), onde $X$ (antecedente) e $Y$ (consequente) são conjuntos de itens disjuntos ($X \cap Y = \emptyset$).

### Índices de Validação Básicos
*   **Suporte (Relevância):** Qual a fração de transações que contêm todos os itens de $X \cup Y$ juntos?
    $$\text{Suporte}(X \Rightarrow Y) = \frac{T_{X \cup Y}}{T}$$
*   **Confiança (Validade):** Das transações que contêm $X$, qual a porcentagem que também contém $Y$?
    $$\text{Confiança}(X \Rightarrow Y) = \frac{T_{X \cup Y}}{T_X}$$

### Tipos de Regras que o Professor pode cobrar:
*   **Transacionais convencionais:** Apenas presença/ausência de itens em transações (ex: $\{P\tilde{a}o\} \Rightarrow \{Leite\}$).
*   **Quantitativas:** Envolvem atributos numéricos e relacionais (ex: $\text{Idade}(X, \text{"20..30"}) \wedge \text{Sexo}(X, \text{"M"}) \Rightarrow \text{Salário}(X, \text{">5K"})$).
*   **Híbridas:** Misturam dados relacionais/categóricos com itens comprados (ex: $\text{Cidade} = \text{"Recife"} \wedge \text{compra inclui "leite"} \Rightarrow \text{compra inclui "pão"}$).
*   **Meta-Regras:** Restrições definidas pelo usuário para filtrar o formato das regras que ele quer minerar (ex: $P1(X, Y) \wedge P2(X, Z) \Rightarrow \text{compra}(X, \text{"software"})$).

---

## 3. Medidas de Interesse (Lift, Dependência e Exceções)

### O Problema do Modelo Suporte/Confiança
Apenas exigir Suporte e Confiança mínimos gera um **volume excessivo de regras**, muitas vezes **redundantes, ilusórias ou contraditórias**.

### Dependência entre Itens
Para saber se $A$ e $B$ são realmente associados, comparamos a Confiança da regra com o Suporte individual do consequente $B$:
1.  **Independência:** A compra de $A$ não afeta a de $B$.
    $$\text{Confiança}(A \Rightarrow B) = \text{Suporte}(B)$$
2.  **Dependência Negativa:** A compra de $A$ **diminui** a chance de comprar $B$ (ex: marcas concorrentes).
    $$\text{Confiança}(A \Rightarrow B) < \text{Suporte}(B)$$
3.  **Dependência Positiva:** A compra de $A$ **aumenta** a chance de comprar $B$.
    $$\text{Confiança}(A \Rightarrow B) > \text{Suporte}(B)$$

### Lift (Aumento)
Mede o quanto mais frequente $B$ se torna quando $A$ ocorre.
$$\text{Lift}(A \Rightarrow B) = \frac{\text{Confiança}(A \Rightarrow B)}{\text{Suporte}(B)}$$
*   $\text{Lift} = 1$: Itens independentes.
*   $\text{Lift} > 1$: Associação positiva (regra útil).
*   $\text{Lift} < 1$: Associação negativa.

### Mineração de Exceções (Positivas e Negativas)
Consiste em descobrir se uma regra geral se torna significativamente **mais forte** ou **mais fraca** em um subconjunto específico dos dados.
*   **Exceção Negativa ($-s$ ou $-c$):** A regra enfraquece em um grupo (ex: regra geral é verdadeira, exceto para mulheres do Norte).
*   **Exceção Positiva ($+s$ ou $+c$):** Uma regra que geralmente é fraca torna-se muito forte em um grupo específico (ex: pessoas com Doutorado têm renda $>50K$ com confiança muito maior que a média).

---

## 4. Algoritmos de Extração: Apriori vs. Partition

### O que é Escalabilidade? (Definição exata dos slides)
> "Um algoritmo é dito escalável se, dada uma quantidade fixa de memória principal, seu tempo de execução cresce linearmente com o número de registros da base de dados."

### As Duas Fases da Mineração de Regras:
1.  **Fase 1:** Encontrar todos os conjuntos frequentes $Z$ (onde $Sup(Z) \ge SupMin$). **É a fase computacionalmente cara.**
2.  **Fase 2:** Gerar as regras $X \Rightarrow Y$ a partir dos conjuntos frequentes que satisfaçam a confiança mínima.

---

### Algoritmo 1: Apriori
Baseia-se em reduzir o espaço de busca através da propriedade: **"Todo subconjunto de um conjunto frequente é frequente"** (e o seu contra-positivo para poda).

*   **Processo:**
    1. Calcula o suporte de conjuntos de tamanho 1, elimina os infrequentes.
    2. Gera candidatos de tamanho 2 a partir dos sobreviventes de tamanho 1.
    3. Repete gerando candidatos de tamanho $k$ a partir dos frequentes de tamanho $k-1$.
*   **Geração de Candidatos ($C_k$):**
    *   **Junção:** Une conjuntos frequentes de tamanho $k-1$ que compartilham os primeiros $k-2$ itens ordenados.
    *   **Poda:** Remove o candidato de $C_k$ se ele contiver qualquer subconjunto de tamanho $k-1$ que não seja frequente.
*   **Estrutura de dados usada:** Árvore Hash (Hash Tree) para contagem rápida de suporte.
*   **Desvantagem principal:** Lê a base de dados inteira em **cada uma** das $k$ iterações.

---

### Algoritmo 2: Partition
Criado para resolver o problema de excesso de leituras no disco do Apriori.

*   **Propriedade Fundamental:**
    > "Se um conjunto é frequente em relação a toda a base de dados (frequência global), então ele é frequente em relação a pelo menos uma partição da base de dados (frequência local)."
*   **Como funciona (Apenas 2 leituras na base):**
    *   **Fase I (1ª leitura total):** Divide a base de dados em $n$ partições (que caibam na memória principal). Para cada partição, roda o Apriori localmente para encontrar todos os frequentes locais. A união de todos os frequentes locais forma o conjunto de **candidatos globais**.
    *   **Fase II (2ª leitura total):** Percorre toda a base de dados apenas mais uma vez para contar o suporte real de todos os candidatos globais e filtra quem atingiu o $SupMin$ globalmente.
*   **Vantagem:** Lê a base de dados **apenas duas vezes**.
*   **Desvantagem:** Se as partições gerarem muitos candidatos locais que no final não são frequentes globais, o desempenho na Fase II pode ser muito prejudicado.
