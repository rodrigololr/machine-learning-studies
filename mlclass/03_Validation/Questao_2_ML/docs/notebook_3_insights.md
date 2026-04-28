# Notebook 3 — Pré-processamento e Transformação

## Objetivo
Validar o pipeline básico de preparação dos dados sem vazamento e deixar os artefatos prontos para modelagem.

## Resumo dos resultados

- **Split estratificado correto**: 80/20 preservando as proporções
- **Encoding de `sex`**: gerou 2 colunas (`sex_I`, `sex_M`)
- **Escalonamento**: médias ~0 e desvios ~1 no treino
- **Validação**: valores fora do padrão esperado, como deve ser
- **Artefatos salvos**: pipeline e arrays `.npy`

## Insights principais

### 1) O split ficou muito bom
As proporções no treino e na validação ficaram praticamente iguais às da base total. Isso é o comportamento esperado para `stratify=y`.

### 2) O pipeline está sem vazamento
O `StandardScaler` foi ajustado apenas no treino. Isso aparece no treino com média ~0 e desvio ~1, enquanto a validação mantém distribuição própria.

### 3) O One-Hot de `sex` ficou correto
Como a variável tem 3 categorias e usamos `drop='first'`, o pipeline gera duas colunas binárias. Isso evita multicolinearidade desnecessária.

### 4) O baseline é coerente com a EDA
A EDA mostrou correlação forte entre features, mas não é motivo para remover nada antes de testar. Manter todas as variáveis como baseline é uma boa decisão.

### 5) O sinal principal ainda parece estar no conjunto completo
As variáveis padronizadas aparecem com valores altos e consistentes, reforçando que o modelo provavelmente vai precisar explorar a estrutura conjunta das features.

## Ajustes feitos no código

- Corrigido o caminho do dataset para usar `DATA_DIR + 'abalone_dataset.csv'`
- Mantido o baseline conservador: `OneHotEncoder + StandardScaler`
- Preparado para comparar depois com modelos mais sofisticados

## Conclusão
O pré-processamento está pronto. Não há sinais de vazamento nem necessidade urgente de mexer no pipeline antes do notebook 4. O próximo passo certo é testar modelos e ver se a colinearidade atrapalha ou não na prática.
