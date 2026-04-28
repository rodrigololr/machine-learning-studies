# Regressão logística por dentro

## O que é
Regressão logística é um modelo de **classificação**.
Ela estima a probabilidade de uma amostra pertencer a cada classe.

Apesar do nome, ela não prevê valores contínuos.

## Ideia central
O modelo combina as variáveis de entrada em uma soma ponderada:

```text
z = b0 + b1*x1 + b2*x2 + ... + bn*xn
```

Depois ele aplica a função sigmoide:

```text
p = 1 / (1 + e^(-z))
```

Isso transforma qualquer número em uma probabilidade entre 0 e 1.

## Como ela decide a classe

- Se `p >= 0.5`, o modelo tende a prever a classe positiva.
- Se `p < 0.5`, ele tende a prever a classe negativa.

Para mais de duas classes, como no seu caso, o modelo usa uma extensão multiclasse.

## Como funciona em 3 classes
No seu dataset, o alvo tem as classes 1, 2 e 3.

O `scikit-learn` usa uma abordagem multiclasse automática. Dependendo do solver,
ele pode trabalhar com:

- **multinomial**: aprende todas as classes ao mesmo tempo;
- **one-vs-rest**: treina um classificador por classe.

Com o solver padrão `lbfgs`, a regressão logística multiclasse funciona bem para
esse tipo de problema.

## O que os coeficientes significam
Depois do treino, cada variável recebe um peso.

- coeficiente positivo: aumenta a chance da classe;
- coeficiente negativo: diminui a chance da classe;
- coeficiente com valor absoluto maior: maior influência.

Como suas variáveis numéricas estão padronizadas, esses pesos ficam mais fáceis de comparar.

## Por que ela faz sentido neste dataset
Ela combina bem com este problema porque:

- as classes têm relação quase ordenada com tamanho e peso;
- as features são numéricas e bem comportadas;
- o dataset está balanceado;
- a EDA mostrou separação razoável entre classes.

## Pontos de atenção

- as variáveis numéricas têm correlação alta entre si;
- isso pode deixar os coeficientes menos estáveis;
- por isso, a interpretação deve ser feita com cuidado.

## Quando ela é uma boa escolha
Use regressão logística quando você quer:

- um modelo explicável;
- probabilidades por classe;
- boa performance com fronteira aproximadamente linear;
- uma base sólida para apresentação acadêmica.

## Quando ela pode perder
Ela pode ficar atrás de modelos como SVM RBF quando:

- a fronteira entre classes é bem curva;
- existem interações complexas;
- a separação não é quase linear.

No seu dataset, a diferença para os melhores modelos é pequena, então a regressão logística continua sendo uma escolha muito forte.

## Como explicar ao professor
Você pode dizer:

> “A regressão logística transforma a soma ponderada das variáveis em probabilidade,
> e aprende pesos que indicam o efeito de cada atributo sobre cada classe. No
> dataset de abalone, ela faz sentido porque as variáveis são numéricas, bem
> organizadas, e mostram separação clara por tamanho e peso.”

## Resumo curto
Regressão logística é boa para este problema porque é simples, interpretável, e
já captura bem o padrão dominante do dataset.
