#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Atividade 03 - Avaliação de Classificadores - Abalone
# Regressao Logistica (C=3.0, solver=lbfgs)
# Envia predicoes para o servidor do professor

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import requests
import os

print('=' * 60)
print('ABALONE - REGRESSAO LOGISTICA - ENVIO AO SERVIDOR')
print('=' * 60)

# Config
DATA_DIR = '/home/antonio/Documentos/Machine Learning/mlclass/03_Validation'
DEV_KEY = '2 computeiros e um matemagico'
URL = 'https://aydanomachado.com/mlclass/03_Validation.php'

# 1. Ler base de treino
print('\n[1] Lendo base de treino...')
df_train = pd.read_csv(os.path.join(DATA_DIR, 'abalone_dataset.csv'))
print(f'    Treino: {df_train.shape}')

# 2. Ler base de aplicacao (sem label)
print('\n[2] Lendo base de aplicacao...')
df_app = pd.read_csv(os.path.join(DATA_DIR, 'abalone_app.csv'))
print(f'    Aplicacao: {df_app.shape}')

# 3. Definir colunas
cat_cols = ['sex']
num_cols = ['length', 'diameter', 'height',
            'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight']
feature_cols = num_cols + cat_cols

# 4. Preparar X e y
X_train = df_train[feature_cols]
y_train = df_train['type']
X_app = df_app[feature_cols]

print(f'\n[3] Distribuicao do treino:')
print(y_train.value_counts().sort_index())

# 5. Pipeline de pre-processamento (identico aos notebooks)
def make_one_hot():
    try:
        return OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False)
    except TypeError:
        return OneHotEncoder(drop='first', handle_unknown='ignore', sparse=False)

preprocessor = ColumnTransformer([
    ('cat', make_one_hot(), cat_cols),
    ('num', StandardScaler(), num_cols),
])

# 6. Montar pipeline com Logistic Regression (C=3.0 — melhor do notebook 04.1)
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(
        C=3.0,
        solver='lbfgs',
        max_iter=4000,
        random_state=42
    )),
])

# 7. Treinar
print('\n[4] Treinando Logistic Regression (C=3.0, solver=lbfgs)...')
pipeline.fit(X_train, y_train)
print('    Modelo treinado!')

# 8. Predizer
print('\n[5] Gerando predicoes no dataset de aplicacao...')
y_pred = pipeline.predict(X_app)
print(f'    Total de predicoes: {len(y_pred)}')

# 9. Distribuicao das classes preditas
print('\n[6] Distribuicao das classes preditas:')
pred_counts = pd.Series(y_pred).value_counts().sort_index()
for cls, cnt in pred_counts.items():
    print(f'    Classe {cls}: {cnt} ({cnt/len(y_pred)*100:.1f}%)')

# 10. Mostrar comparacao com a distribuicao do treino
train_counts = y_train.value_counts().sort_index()
print('\n[7] Comparacao com distribuicao do treino:')
for cls in sorted(y_train.unique()):
    train_pct = train_counts[cls] / len(y_train) * 100
    pred_pct = pred_counts[cls] / len(y_pred) * 100
    diff = pred_pct - train_pct
    print(f'    Classe {cls}: treino={train_pct:.1f}% | predito={pred_pct:.1f}% | diff={diff:+.1f}%')

# 11. Salvar CSV de backup
csv_path = os.path.join(DATA_DIR, 'abalone_logreg_submission.csv')
submission = pd.DataFrame({'type': y_pred})
submission.to_csv(csv_path, index=False)
print(f'\n[8] CSV de backup salvo em: {csv_path}')

# 12. Enviar ao servidor
print('\n[9] Enviando ao servidor...')
data_payload = {
    'dev_key': DEV_KEY,
    'predictions': pd.Series(y_pred).to_json(orient='values')
}

try:
    r = requests.post(url=URL, data=data_payload, timeout=30)
    print(f'\n    Status code: {r.status_code}')
    print(f'    Resposta do servidor:\n')
    print(r.text)
    print('\n[10] SUCESSO — submissao enviada!')
except Exception as e:
    print(f'\n    ERRO ao enviar: {e}')
    print('    O CSV de backup foi salvo. Voce pode tentar novamente manualmente.')

print('\n' + '=' * 60)
print('RESUMO')
print(f'  Modelo: Logistic Regression (C=3.0, solver=lbfgs)')
print(f'  Predicoes: {len(y_pred)}')
print(f'  CSV salvo: {csv_path}')
print('=' * 60)