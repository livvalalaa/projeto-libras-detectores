import pandas as pd
import joblib
from sklearn.model_selection import train_test_split 
from sklearn.ensembl import RandomForestClassifier

df = pd.read_csv('dados/dataset.csv')

X = df.drop('label', axis=1) 
y = df['label']

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2,
random_state=42)

modelo = RandomForestClassifier(n_estimators=100)

modelo.fit(X_treino, y_treino)

joblib.dump(modelo, 'modelos/modelo_libras.pkl')
print("Treinamento concluído!")
