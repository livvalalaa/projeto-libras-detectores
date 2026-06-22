import pandas as pd
import joblib
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier

# Carrega os dados (como abrir uma planilha
df = pd.read_csv('dados/dataset.csv')

# Separar: X são as coordenadas (o que a IA vê), y é a letra (o que ela deve adivinhar)
X = df.drop('label', axis=1) 
y = df['label']

# Divisão: 80% para estudo, 20% para a prova
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2,
random_state=42)

# Cria o "aluno" (modelo)
modelo = RandomForestClassifier(n_estimators=100)

# O treinamento em si (a parte em que ele estuda os dados)
modelo.fit(X_treino, y_treino)

# Salva o arquivo .pkl (como se estivesse salvando o cérebro do aluno para usar depois)
joblib.dump(modelo, 'modelos/modelo_libras.pkl')
print("Treinamento concluído!")
