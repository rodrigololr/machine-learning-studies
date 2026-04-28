# Notebook 2 — Análise Exploratória Detalhada

## Objetivo
Explorar distribuição, correlação, outliers e separabilidade das classes para orientar o pré-processamento e a escolha do modelo.

## Resumo dos resultados

- **Assimetria:** moderada na maioria das variáveis; `height` quase simétrica
- **Outliers:** presentes, mas em quantidade baixa/moderada
- **Correlação:** muito alta entre várias features numéricas
- **`sex` vs `type`:** relação forte e útil
- **Separabilidade:** boa estrutura linear global, com sobreposição entre classes 2 e 3

## Insights principais

### 1) As distribuições são unimodais e consistentes
Os histogramas mostram que as variáveis numéricas têm uma forma bem definida, sem multimodalidade forte. Isso sugere que as classes não vêm de populações totalmente distintas, mas de um mesmo contínuo de tamanho/peso.

### 2) Há assimetria, mas não extrema
Skewness observada:

- `length`: -0.64
- `diameter`: -0.61
- `height`: 0.02
- `whole_weight`: 0.56
- `shucked_weight`: 0.76
- `viscera_weight`: 0.63
- `shell_weight`: 0.66

Conclusão: as variáveis estão razoavelmente comportadas. Não há necessidade imediata de transformação agressiva, mas testar uma transformação suave pode ser útil se o modelo precisar.

### 3) As classes se separam por escala
Os boxplots mostram um padrão claro:

- **Classe 1**: menores medidas e pesos
- **Classe 2**: intermediária
- **Classe 3**: maiores valores

Isso indica que o problema tem forte componente ordenado/monotônico.

### 4) Outliers existem, mas não parecem ser o problema principal
Contagem de outliers (IQR):

- `length`: 47
- `diameter`: 36
- `height`: 14
- `whole_weight`: 26
- `shucked_weight`: 36
- `viscera_weight`: 21
- `shell_weight`: 34

Esses valores representam uma fração pequena da base. Minha leitura: não remover automaticamente; primeiro testar sensibilidade do modelo.

### 5) A correlação entre features é muito alta
Os pares mais críticos:

- `length` × `diameter` ≈ 0.99
- `whole_weight` × `shucked_weight` ≈ 0.97
- `whole_weight` × `viscera_weight` ≈ 0.93
- `whole_weight` × `shell_weight` ≈ 0.95
- `shucked_weight` × `viscera_weight` ≈ 0.97

Isso mostra redundância forte. Os atributos medem praticamente o mesmo eixo biológico de tamanho/massa.

### 6) A variável alvo tem correlação moderada com todas as medidas
Correlação com `type`:

- `shell_weight`: 0.630
- `height`: 0.608
- `diameter`: 0.598
- `length`: 0.582
- `whole_weight`: 0.581
- `viscera_weight`: 0.564
- `shucked_weight`: 0.491

Conclusão: nenhuma variável sozinha resolve o problema, mas o conjunto tem sinal bom.

### 7) `sex` é muito informativa
Distribuição por classe:

- **F**: mais associada à classe 3
- **I**: fortemente associada à classe 1
- **M**: mais espalhada entre classes 2 e 3

Isso justifica manter `sex` no modelo com encoding categórico simples.

### 8) Pairplot e LDA confirmam a estrutura
O pairplot mostra relação quase diagonal entre as variáveis mais fortes, e o LDA explica boa parte da separação com o primeiro eixo.

Variância discriminante do LDA:

- Componente 1: 0.884
- Componente 2: 0.116

Leitura: existe uma estrutura global bem clara de separação, mas ainda com sobreposição relevante entre as classes 2 e 3.

## Decisões para o Notebook 3

- Manter `sex` com One-Hot Encoding
- Começar com `StandardScaler` como baseline
- Não remover outliers automaticamente
- Considerar, se necessário, um teste adicional com transformação suave (ex.: Yeo-Johnson)
- Considerar um experimento de seleção/redução de features por causa da multicolinearidade

## Conclusão
O dataset tem sinal forte e boa separabilidade, especialmente por magnitude das medidas. A principal preocupação é a redundância entre variáveis numéricas, não a limpeza dos dados. O pipeline atual é um bom baseline, mas vale testar no notebook 3/4 se uma transformação adicional ou uma redução de features melhora a validação.
