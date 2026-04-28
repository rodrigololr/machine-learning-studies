# Notebook 4 — Modelagem e Validação

## Objetivo
Comparar classificadores, validar localmente e escolher o melhor modelo para seguir com a submissão.

## Resumo dos resultados observados

### Cross-validation (10 folds)

- **Dummy (most frequent):** 0.3441 accuracy / 0.1707 macro F1
- **Logistic Regression:** 0.6491 / 0.6444
- **LDA:** 0.6323 / 0.6338
- **KNN (k=5):** 0.6144 / 0.6109
- **SVM (Linear):** 0.6463 / 0.6455
- **SVM (RBF):** 0.6527 / 0.6470
- **Decision Tree:** 0.5740 / 0.5702
- **Random Forest (100):** 0.6359 / 0.6324

### Holdout

- **SVM (RBF):** 0.6762 accuracy / 0.6727 macro F1
- **Logistic Regression:** 0.6667 / 0.6622
- **SVM (Linear):** 0.6571 / 0.6539

## Conclusões principais

### 1) O baseline confirmou sinal real na base
O Dummy ficou próximo da proporção da classe mais frequente. Isso confirma que os modelos reais estão extraindo sinal verdadeiro, não apenas sorte.

### 2) Modelos lineares já funcionam muito bem
Logistic Regression, SVM Linear e LDA ficaram próximos do topo. Isso combina com a EDA: as variáveis numéricas carregam separação forte e quase monotônica.

### 3) SVM (RBF) foi o melhor modelo geral
Ele teve o melhor resultado em CV e também no holdout. O ganho sobre Logistic Regression é pequeno, mas consistente.

### 4) Classe 2 continua sendo a mais difícil
Na matriz de confusão, a classe 2 teve pior precision/recall que as outras. Isso confirma a sobreposição visual observada na EDA.

### 5) Árvores não ganharam dos modelos de margem
Decision Tree e Random Forest ficaram atrás dos melhores modelos lineares/não lineares suaves. O problema parece mais bem resolvido por fronteiras contínuas.

## Decisão atual

**Modelo escolhido:** SVM (RBF)

## Impacto no notebook 5

O notebook final deve usar SVM (RBF) como modelo padrão e fallback. Random Forest deve permanecer apenas como opção secundária de comparação histórica, não como escolha operacional.

## Nota técnica importante

A validação atual foi feita sobre os dados já transformados no notebook 3. Isso funciona como baseline, mas é levemente otimista porque o pré-processamento não está dentro da `Pipeline` durante a cross-validation.

**Recomendação:** a validação ideal deve ser refeita com o pré-processamento embutido na pipeline, para eliminar qualquer vazamento sutil.

## Próximos passos

- Rodar o notebook 5 com o melhor modelo salvo
- Gerar a submissão final
- Se houver tempo, refazer a validação do notebook 4 com pipeline completa

## Conclusão
O conjunto de dados parece bem resolvido com SVM (RBF). A diferença para Logistic Regression é pequena, então a escolha final pode ser mantida por performance ligeiramente superior. A principal dívida técnica agora é só refinar a validação para ficar 100% pipeline-based.
