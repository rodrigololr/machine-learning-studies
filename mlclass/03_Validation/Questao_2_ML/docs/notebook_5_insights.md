# Notebook 5 — Modelo Final e Predição em App

## Objetivo
Treinar o modelo final com toda a base rotulada, validar de forma pipeline-based, e gerar a submissão final para o dataset de aplicação.

## Resumo dos resultados

- **Modelo final enviado:** Logistic Regression (C=3.0, solver='lbfgs')
  > Decisão por interpretabilidade — a diferença de performance vs SVM (RBF) era pequena (~0.4%), então escolhemos o modelo mais explicável para apresentação e defesa com o professor.
- **Accuracy CV:** 0.6499 ± 0.0198
- **Macro F1 CV:** 0.6455 ± 0.0194
- **Accuracy holdout:** 0.6667
- **Accuracy no servidor:** 0.6431  (primeiro envio realizado em 28/04/2026)
- **Predições geradas:** 1045 linhas
- **Arquivo de submissão:** `abalone_logreg_submission.csv` (enviado ao servidor)
- **Script usado:** `abalone_logreg_submission.py` (em `mlclass/03_Validation/`)
- **CSV backup:** `pipeline_output/abalone_submission.csv` (SVM — não enviado)

## Conclusões principais

### 1) O pipeline final fechou sem erros
O notebook executou do início ao fim sem falhas. Isso confirma que o fluxo completo está pronto para uso.

### 2) A validação final confirmou o SVM (RBF)
O desempenho final ficou consistente com o notebook 4, e a execução sobre a base completa com pipeline reforça a escolha do modelo.

### 3) O desempenho final é estável
O desvio padrão ficou em torno de 0.016 para accuracy e macro F1. Isso indica um modelo relativamente estável entre folds.

### 4) A predição Logistic Regression no dataset de aplicação é coerente
Distribuição das classes preditas (enviadas ao servidor):

- Classe 1: 333 (31.9%) — treino 34.4% → diff -2.6%
- Classe 2: 346 (33.1%) — treino 32.0% → diff +1.1%
- Classe 3: 366 (35.0%) — treino 33.6% → diff +1.5%

Equilíbrio coerente com a distribuição de treino — sem colapso em classe única.

### 5) Resultado oficial do servidor: 64.31%
O servidor do professor retornou:
```
{status:success, accuracy:0.6430622009569378, old_accuracy:0}
```
Acurácia de **64.31%** — dentro da faixa esperada (CV local: 64.99%, holdout: 66.67%). A diferença de ~0.5-2% entre holdout e servidor é normal, pois o servidor usa um conjunto de teste que não vemos.

## Leitura técnica

O resultado de 64.31% no servidor confirma que a Logistic Regression generaliza bem. A escolha por esse modelo em vez do SVM (RBF) foi baseada na **interpretabilidade**: os coeficientes permitem explicar ao professor como cada feature influencia a classificação de cada classe — algo impossível com SVM RBF.

A diferença de acurácia entre SVM (RBF) e Logistic Regression no servidor é esperada ser pequena (~1-2%), pois ambos os modelos estão no mesmo patamar de complexidade para esse dataset.

## Dívida técnica restante

- **Ajuste fino de hiperparâmetros:** foi testado apenas C=0.1, 1.0, 3.0, 10.0. Valores intermediários ou grid search mais amplo podem melhorar marginalmente.
- **Feature engineering:** não foi testada remoção de features correlacionadas ou criação de novas features (ratios, polinomiais).
- **Ensemble:** não foi testado Voting ou Stacking com os melhores modelos.

## Conclusão
 **Enviado com sucesso em 28/04/2026.** O modelo Logistic Regression (C=3.0) foi treinado com toda a base, enviou 1045 predições ao servidor, e obteve **64.31% de acurácia** no servidor do professor. O fluxo completo — da EDA à submissão — está documentado nos notebooks 01 a 05, 04_1, e nos arquivos de insights em `/docs/`.
