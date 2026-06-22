import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Criar a pasta
os.makedirs('modelos', exist_ok=True)

# Carrega os dados (como abrir uma planilha)
df = pd.read_csv('dados/dataset.csv')

# Garantir a segurança
if 'label' not in df.columns:
  raise ValueError("Coluna 'label' não encontrada no dataset!")

# Separar: X são as coordenadas (o que a IA vê), y é a letra (o que ela deve adivinhar)
X = df.drop('label', axis=1) 
y = df['label']

# Divisão: 80% para estudo, 20% para a prova
X_treino, X_teste, y_treino, y_teste = train_test_split(
  X, y, test_size=0.2, random_state=42, stratify=y
)

# Cria o "aluno" (modelo)
modelo = RandomForestClassifier(n_estimators=100)

# O treinamento em si (a parte em que ele estuda os dados)
modelo.fit(X_treino, y_treino)

# A "prova": avalia o modelo nos dados que ele nunca viu durante o treino
y_pred = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, y_pred)
print(f"Acurácia no conjunto de teste: {acuracia:.2%}")
print("\nRelatório detalhado por letra:")
print(classification_report(y_teste, y_pred))

# Salva o arquivo .pkl (como se estivesse salvando o cérebro do aluno para usar depois)
joblib.dump(modelo, 'modelos/modelo_libras.pkl')
print("Treinamento concluído!")
