import cv2
import mediapipe as mp
import csv
import os

# Inicialização do MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

os.makedirs("dados", exist_ok=True)

caminho_csv = "dados/dataset.csv"

# Criação do cabeçalho se o arquivo for novo
if not os.path.exists(caminho_csv):
    with open(caminho_csv, "w", newline="") as f:
        writer = csv.writer(f)
        header = [f"x{i}" for i in range(21)] + [f"y{i}" for i in range(21)] + ["label"]
        writer.writerow(header)

cap = cv2.VideoCapture(0)

print("INSTRUÇÕES:")
print("1. Posicione a mão na câmera.")
print("2. Faça o sinal da vogal (A, E, I, O, ou U).")
print("3. Pressione a recla correspondente no teclado para salvar.")
print("4. Pressione 'q' para sair.")

contador = 0

while True:
    sucesso, img = cap.read()
    if not sucesso:
        break

    # Inverter a imagem horizontalmente
    img = cv2.flip(img, 1)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resultado = hands.process(img_rgb)

    tecla = cv2.waitKey(1) & 0xFF
    letra = None

    if tecla in [ord("a"), ord("e"), ord ("i"), ord("o"), ord("u")]:
        letra = chr(tecla).upper()

    if resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Capturação da tecla
            if len(resultado.multi_hand_landmarks) == 1:
                dados = []
                
                # Extração dos pontos (21 x e 21 y)
                for lm in hand_landmarks.landmark:
                    dados.append(lm.x)
                for lm in hand_landmarks.landmark:
                    dados.append(lm.y)
                dados.append(letra)

                # Salvamento
                with open(caminho_csv, "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(dados)

                contador += 1
                print(f"Salvo: {letra} ({contador})")

    cv2.imshow("Coleta de Dados - Vogais", img)
    if tecla == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
