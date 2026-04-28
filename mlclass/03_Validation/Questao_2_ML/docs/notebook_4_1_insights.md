# Notebook 4.1 — Experimentos com regressão logística

## Objetivo
Aproximar a escolha final do trabalho para um modelo mais interpretável, sem perder muito desempenho.

## Resumo dos resultados

### Busca de hiperparâmetros

- **C = 0.1, solver lbfgs:** 0.6399 accuracy / 0.6340 macro F1
- **C = 1.0, solver lbfgs:** 0.6491 / 0.6444
- **C = 3.0, solver lbfgs:** 0.6499 / 0.6455
- **C = 10.0, solver lbfgs:** 0.6491 / 0.6446
- **C = 1.0, solver newton-cg:** 0.6495 / 0.6448

### Comparação com modelos interpretáveis

- **Logistic Regression:** 0.6499 / 0.6455
- **SVM Linear:** 0.6463 / 0.6455
- **LDA:** 0.6323 / 0.6338

### Holdout

- **Logistic Regression:** 0.6667 accuracy / 0.6622 macro F1
- **LDA:** 0.6571 / 0.6547
- **SVM Linear:** 0.6571 / 0.6539

## Conclusões principais

### 1) A regressão logística é competitiva
O modelo ficou muito perto dos melhores resultados já vistos, e superou LDA e SVM Linear no conjunto atual.

### 2) O melhor valor ficou em `C = 3.0`
Esse valor deu a melhor combinação de accuracy e macro F1 na validação cruzada. A diferença para `C = 1.0` e `C = 10.0` é pequena, então o modelo é estável nessa faixa.

### 3) O modelo generaliza bem no holdout
O holdout ficou em 66.67% de accuracy, o que confirma que a regressão logística não está apenas decorando o treino.

### 4) A classe 2 continua sendo o gargalo
O relatório de classificação mostra que a classe 2 segue com o pior equilíbrio entre precision e recall. As classes 1 e 3 são mais fáceis de capturar.

### 5) Os coeficientes contam uma história coerente

- `sex_I` puxa fortemente para a classe 1;
- variáveis de peso e tamanho sustentam a separação geral;
- `whole_weight` e `shell_weight` ajudam a diferenciar a classe 3;
- a classe 2 fica entre as outras duas.

## Leitura técnica

Como as variáveis numéricas são muito correlacionadas, os coeficientes não devem ser lidos como causa direta. Mesmo assim, eles ajudam a explicar o comportamento do modelo de forma bem melhor que SVM RBF.

## Conclusão prática

Se o objetivo principal for **explicabilidade**, regressão logística é uma escolha excelente para apresentação.

Se o objetivo principal for **apenas performance máxima**, SVM RBF ainda fica ligeiramente à frente.

## Recomendação

Para defesa com professor, eu recomendaria:

1. **Regressão logística como modelo principal de apresentação**
2. **SVM RBF como benchmark de desempenho**
3. **LDA e SVM Linear como comparações interpretáveis**

## Conclusão final
Os experimentos mostram que a regressão logística faz sentido para esse dataset e é forte o suficiente para ser o modelo principal do trabalho, especialmente se você quiser explicar tudo com clareza.
