# Roteiro de Apresentacao — Perfil de Olhos Barrett II

> **Publico-alvo:** Cliente (clinica oftalmologica)
> **Tom:** Consultoria profissional — Engenharia de Conhecimento / Data Mining
> **Duracao estimada:** 15-20 minutos

---

## Slide 1 — Capa

**O que dizer:**
> "Bom dia/tarde. Somos uma equipe de engenharia de conhecimento e data mining, e hoje vamos apresentar os resultados da analise que realizamos na base de dados biometrica de voces, o Barrett II Eyes. Nosso objetivo foi identificar se existem perfis distintos de olhos nessa base e, se existirem, caracterizar cada um deles de forma clara e acionavel."

---

## Slide 2 — O Desafio

**O que dizer:**
> "Voces nos trouxeram uma pergunta fundamental: existem perfis distintos de olhos na base de dados? Para responder, usamos uma abordagem de aprendizado nao-supervisionado — ou seja, clustering. Isso significa que nao partimos de rotulos ou classes predefinidas. Deixamos os dados falarem por si mesmos e revelarem os padroes naturais que existem na anatomia ocular. O entregavel final sera a caracterizacao completa de cada perfil que encontrarmos."

**Ponto-chave:** Enfatizar que nao havia hipoteses previas — os dados guiaram a descoberta.

---

## Slide 3 — As Variaveis que Usamos

**O que dizer:**
> "Trabalhamos exclusivamente com 5 medidas biometricas. Cada uma delas captura uma dimensao diferente da anatomia do olho:
> - **AL** e o comprimento axial — basicamente o 'tamanho' do olho, da cornea ate a retina.
> - **ACD** e a profundidade da camara anterior — o espaco entre a cornea e o cristalino.
> - **WTW** e a distancia branco a branco — o diametro horizontal da cornea.
> - **K1 e K2** sao as medidas de curvatura corneana nos dois meridianos principais.
>
> Um ponto importante: a base tambem tem uma coluna chamada 'Correto', com valores S ou N. Essa coluna **nao foi usada** para encontrar os grupos. Ela sera apresentada no final apenas como complemento, depois que os perfis ja estiverem definidos. Nao queremos confundir grupo com classe — os grupos sao padroes naturais, nao categorias pre-existentes."

---

## Slide 4 — Anatomia do Olho

**O que dizer:**
> "Para contextualizar, aqui esta uma referencia anatomica que mostra onde cada medida se localiza no olho. O AL vai da frente ate o fundo do olho. O ACD e o espaco logo atras da cornea. O WTW e a largura da cornea. E K1/K2 medem a curvatura da superficie corneana. Entender isso e fundamental para interpretar os perfis que vamos apresentar."

---

## Slide 5 — Exploracao Inicial: Distribuicoes

**O que dizer:**
> "Antes de aplicar qualquer algoritmo, fizemos uma exploracao completa dos dados. Nos histogramas, vemos que o AL tem a maior variabilidade — varia mais de 10mm entre o menor e o maior olho. O WTW e bem mais uniforme. E K1 e K2 tem distribuicoes muito similares, o que faz sentido pois medem a mesma coisa em meridianos diferentes."

---

## Slide 6 — Exploracao Inicial: Outliers

**O que dizer:**
> "Nos boxplots, identificamos outliers em todas as variaveis. O AL tem 44 outliers, o que representa quase 3% da base. Mas aqui fizemos uma escolha consciente: **mantivemos os outliers**. Por que? Porque em dados biometricos, outliers representam variabilidade anatomica real — olhos que sao genuinamente diferentes. Remover seria perder informacao valiosa sobre a diversidade da populacao."

---

## Slide 7 — Exploracao Inicial: Correlacoes

**O que dizer:**
> "A matriz de correlacao nos mostra relacoes importantes. K1 e K2 sao quase perfeitamente correlacionados — r de 0.975 — o que era esperado. AL e ACD tem correlacao moderada: olhos maiores tendem a ter camara anterior mais profunda. E o WTW e relativamente independente, o que significa que captura uma dimensao unica da anatomia. Todas as 5 variaveis trazem informacao complementar."

---

## Slide 8 — Pre-processamento

**O que dizer:**
> "Para que os algoritmos de clustering funcionem bem, precisamos que todas as variaveis estejam na mesma escala. Um milimetro de AL nao pode pesar mais que uma dioptria de K1. Aplicamos o StandardScaler, que transforma cada variavel para ter media zero e desvio padrao um. Testamos tambem o MinMaxScaler, mas o Standard se mostrou mais adequado. E importante: o scaler foi ajustado apenas nos dados de treino — sem vazamento de informacao."

---

## Slide 9 — Metodologia: 3 Abordagens

**O que dizer:**
> "Nao confiamos em um unico algoritmo. Testamos tres abordagens diferentes de clustering:
> - **K-Means:** o mais classico, minimiza a variancia dentro de cada grupo.
> - **DBSCAN:** baseado em densidade, identifica regioes compactas e detecta outliers.
> - **Hierarchical com Ward:** constroi uma arvore de similaridade entre todos os pontos.
>
> Testar tres metodos nos da confianca de que os perfis encontrados sao reais e nao artefato de um algoritmo especifico."

---

## Slide 10 — Elbow Method

**O que dizer:**
> "A primeira pergunta foi: quantos perfis existem? O metodo do cotovelo nos da uma pista. O grafico mostra a inertia em funcao do numero de clusters. O 'cotovelo' — onde a curva comeca a achatar — aparece entre K=2 e K=4. Apos K=4, o ganho marginal e minimo. Isso sugere que 2 grupos ja capturam a estrutura principal dos dados."

---

## Slide 11 — Silhouette Analysis

**O que dizer:**
> "Para confirmar, usamos a analise de silhueta, que mede quao bem cada ponto se encaixa no seu grupo. O score varia de -1 a 1, e quanto maior, melhor. O resultado foi claro: **K=2 tem o maior silhouette score**, de 0.2867. A partir de K=3, o score cai. Isso confirma que 2 e o numero otimo de perfis."

---

## Slide 12 — Resultado Principal: K-Means K=2

**O que dizer:**
> "Com K=2 definido, aplicamos o K-Means. O resultado: dois grupos bem balanceados — 742 olhos em um grupo e 786 no outro. Usamos PCA e t-SNE para visualizar em 2 dimensoes, e ambos confirmam: ha uma separacao bimodal clara. Sao dois grupos naturais nos dados."

---

## Slide 13 — Radar Chart

**O que dizer:**
> "O radar chart mostra o perfil de cada grupo de forma visual. Os valores sao padronizados — mostram quantos desvios padrao cada grupo esta acima ou abaixo da media. Notem como os perfis sao quase espelhados: onde o Grupo 0 esta abaixo da media, o Grupo 1 esta acima, e vice-versa. Isso indica uma separacao muito clara entre os dois perfis."

---

## Slide 14 — DBSCAN

**O que dizer:**
> "O DBSCAN nos deu um resultado diferente: encontrou apenas 1 cluster dominante, com 98.5% dos dados. Isso acontece porque o DBSCAN identifica regioes de alta densidade, e os dados formam uma regiao continua sem separacoes claras por densidade. Isso nao invalida os resultados do K-Means — apenas mostra que a estrutura dos dados e melhor capturada por particionamento do que por densidade."

---

## Slide 15 — Hierarchical

**O que dizer:**
> "O clustering hierarquico com Ward linkage tambem encontrou 2 grupos. O dendrograma mostra claramente a divisao principal na distancia de aproximadamente 50. Isso e uma confirmacao independente: tres metodos diferentes, e dois deles concordam que existem 2 perfis naturais."

---

## Slide 16 — Validacao Comparativa

**O que dizer:**
> "Para decidir qual metodo e o melhor, usamos tres metricas de validacao:
> - **Silhouette:** mede coesao interna — quanto maior, melhor.
> - **Calinski-Harabasz:** mede separacao entre grupos — quanto maior, melhor.
> - **Davies-Bouldin:** mede sobreposicao — quanto menor, melhor.
>
> O K-Means com K=2 venceu em todas as metricas relevantes. Ele tem a melhor separacao entre grupos e a menor sobreposicao. Esse e o metodo que recomendamos."

---

## Slide 17 — Perfil 1: Grupo 0 (Olhos Compactos)

**O que dizer:**
> "Agora vamos ao que interessa: os perfis. O **Grupo 0** sao olhos que chamamos de 'compactos'. Eles tem:
> - Comprimento axial menor — o olho e mais curto.
> - Camara anterior mais rasa — menos espaco entre cornea e cristalino.
> - Diametro corneano menor.
> - E, crucialmente, **cornea mais curva** — K1 e K2 acima da media.
>
> Do ponto de vista clinico, essa anatomia pode estar associada a tendencia de hipermetropia. E um perfil que requer atencao especial em calculos de Lente Intraocular, pois a curvatura corneana mais acentuada influencia diretamente o poder da lente."

---

## Slide 18 — Perfil 2: Grupo 1 (Olhos Alongados)

**O que dizer:**
> "O **Grupo 1** sao olhos 'alongados'. O perfil e praticamente o inverso:
> - Comprimento axial maior — olho mais longo.
> - Camara anterior mais profunda.
> - Diametro corneano maior.
> - E **cornea mais plana** — K1 e K2 abaixo da media.
>
> Clinicamente, essa anatomia pode estar associada a tendencia de miopia. Para este perfil, os protocolos de medicao e calculo de LIO podem ser ajustados de forma especifica."

---

## Slide 19 — Complemento: Coluna "Correto"

**O que dizer:**
> "Agora, como complemento, vamos olhar a distribuicao da coluna 'Correto' entre os dois grupos. **Reforco:** isso nao foi usado para definir os grupos. Os grupos foram definidos exclusivamente pelas 5 variaveis biometricas.
>
> A tabela mostra que a distribuicao de 'S' e 'N' e muito similar entre os dois grupos. O teste qui-quadrado confirma: p-value de 0.22, muito acima de 0.05. Ou seja, **nao ha associacao significativa** entre o perfil biometrico e a corretude da medida.
>
> Isso e importante porque mostra que os grupos capturam **variabilidade anatomica real**, nao qualidade de medida ou erro. Sao perfis genuinos de olhos."

---

## Slide 20 — Conclusoes

**O que dizer:**
> "Para encerrar, tres conclusoes principais:
>
> **Primeiro:** Existem 2 perfis de olhos distintos na base Barrett II. Isso nao era obvio — os dados revelaram.
>
> **Segundo:** O K-Means com K=2 e o metodo mais robusto para esta segmentacao, validado por tres metricas independentes.
>
> **Terceiro:** A diferenca principal entre os perfis e dimensoes axiais versus curvatura corneana — um grupo tem olhos menores com cornea mais curva, o outro tem olhos maiores com cornea mais plana.
>
> **Para voces, isso significa que:**
> - O Grupo 0 requer atencao especial em calculos de LIO pela curvatura corneana.
> - O Grupo 1 permite protocolos ajustados para olhos alongados.
> - A segmentacao permite personalizar protocolos clinicos por perfil.
>
> **Como proximos passos, sugerimos:**
> - Validar com uma amostra externa de pacientes.
> - Investigar correlacao com desfechos cirurgicos reais.
> - Expandir a analise para subgrupos por idade e sexo.
>
> Obrigado. Estamos a disposicao para perguntas."

---

## Dicas de Apresentacao

### Postura
- Falar como consultor, nao como estudante
- Usar linguagem acessivel — evitar jargao tecnico desnecessario
- Quando mencionar metricas (silhouette, etc.), explicar o que significam em termos simples

### Tempo
- Slides 1-4: 3 min (contexto e dados)
- Slides 5-8: 3 min (exploracao e preprocessamento)
- Slides 9-16: 5 min (metodologia e resultados)
- Slides 17-18: 4 min (perfis — o mais importante!)
- Slide 19: 2 min (complemento)
- Slide 20: 3 min (conclusoes)

### Pontos de Atencao
- **NUNCA** dizer que "Correto" e uma classe ou rotulo
- **SEMPRE** enfatizar que os grupos foram encontrados apenas com AL, ACD, WTW, K1, K2
- Usar termos "perfil" e "grupo", nunca "classe" ou "categoria"
- Se perguntarem sobre a coluna "Correto", explicar que e apenas uma variavel adicional que nao participou do clustering
