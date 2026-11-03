# Módulos de Aprendizagem de Máquina Aplicada — IC/UFAL

Repositório estruturado contendo projetos práticos, benchmarks e implementações dos principais paradigmas de **Machine Learning, Otimização e Inteligência Artificial**, desenvolvido no Instituto de Computação da Universidade Federal de Alagoas (IC/UFAL).

---

## Visão Geral dos Módulos

| Módulo | Paradigma / Área | Dataset / Aplicação | Algoritmos & Métodos Chave |
|---|---|---|---|
| [**01_Preprocessing**](./01_Preprocessing/) | Aprendizado Supervisionado & Data Prep | *Pima Indians Diabetes* | Imputação (MICE, KNNImputer, Média), Scalers (PowerTransformer, Robust), Tratamento de Zeros Fisiológicos |
| [**02_Optimization**](./02_Optimization/) | Metaheurísticas de Otimização Global | Otimização 3D de Padrão de Antenas Espaciais | Subida da Encosta (*Hill Climbing*), Têmpera Simulada (*Simulated Annealing*), Algoritmos Genéticos (*GA*) |
| [**03_Validation**](./03_Validation/) | Model Selection & MLOps Multiclasse | *Abalone Multiclass Classification* | Validação Cruzada Estratificada 5-fold, Pipelines Scikit-Learn, SVM (RBF/Linear), Regressão Logística, Random Forest |
| [**04_ReinforcementLearning**](./04_ReinforcementLearning/) | Aprendizado por Reforço (RL) & Simulação | PyGame Learning Environment (*PLE*) | Formulação de MDP, Ambientes de Simulação (Catcher, Maze, Flappy Bird, Doom), Agentes Reativos e Q-Learning |
| [**05_IOL_H1**](./05_IOL_H1/) | Avaliação de Generalização Clínica | Predição de Sucesso em Cirurgia de Catarata / LIO | Validação estatística rigorosa com submissão cega para prevenção de overfitting em dados biomédicos |

---

## Destaques Técnicos

1. **Prevenção de Vazamento de Dados (Data Leakage):**
   Todos os pré-processadores, estimadores de imputação e scalers são treinados estritamente na partição de treino e apenas transformados nos folds de validação/teste via `Pipeline` e `ColumnTransformer`.
2. **Benchmark Rigoroso:**
   Modelos não são escolhidos com base em treino ingênuo; utilizam-se métricas estratificadas (`StratifiedKFold`), matrizes de confusão completas e métricas robustas como Macro F1-Score e Curvas ROC/PR.
3. **Serialização e Entrega (MLOps):**
   Geração de artefatos prontos para deploy (`.pkl`) contendo todo o ciclo de transformação e inferência desacoplado de dependências do ambiente de treinamento.

---

## Créditos e Licença

- **Instituição:**Instituto de Computação — Universidade Federal de Alagoas (IC/UFAL)
- **Docente:**Prof. Dr. Aydano Machado
- **Licença de Código:**MIT License (consulte o arquivo [LICENSE](./LICENSE))
