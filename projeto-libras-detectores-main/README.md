# projeto-libras-sistemas

Detector de Libras

---

## Como rodar 

1. Abra o terminal e fique na **pasta do projeto** onde está o `requirements.txt`.
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Rode o sistema:
```bash
python main.py
```

> Se o seu `main.py` estiver dentro de outra pasta, use o caminho completo (ex.: `python projeto-libras-sistemas/scripts/main.py`).

---

## Relatório

### Introdução (por que Libras?)
Libras (Língua Brasileira de Sinais) é a forma natural de comunicação da comunidade surda no Brasil. Ainda assim, no dia a dia, é comum encontrar barreiras — na escola, no atendimento e na convivência social — que dificultam a comunicação.

Por isso, criar um sistema que **reconheça sinais de Libras** ajuda a aproximar pessoas surdas e ouvintes, deixando a comunicação mais acessível e inclusiva.

### Metodologia (IA com MediaPipe)
O projeto funciona como um **pipeline** (um processo em etapas). A ideia é que uma fase produza informação útil para a próxima:

1. **Coleta e organização dos dados**
   - Os exemplos de sinais geraram um dataset (`dataset.csv`).
   - Nele:
     - **X (entradas):** dados numéricos extraídos dos sinais (representação das mãos/corpo)
     - **y (saída):** a letra/classe correspondente ao sinal

2. **Extração de características com MediaPipe**
   - O MediaPipe detecta pontos do corpo (principalmente mãos).
   - Em vez de a IA “ler” a imagem inteira, ela aprende com **coordenadas**, que descrevem o movimento de forma mais consistente.

3. **Treinamento do modelo de classificação**
   - Com o dataset pronto, o modelo aprende a relação **X → y**.
   - Depois do treino, o modelo é salvo para ser usado no reconhecimento.

### Resultados
O resultado do projeto é visto de forma prática porque o pipeline só avança quando cada etapa cumpre seu papel:

- **Dados consistentes:** o sistema verifica se o `dataset.csv` existe e não está vazio.
- **Treinamento concluído:** a etapa de treino só termina quando o modelo é gerado com sucesso.
- **Modelo disponível:** o modelo fica salvo e pronto para reconhecimento.

No fim, a combinação de **MediaPipe (extração dos pontos)** com **aprendizado de máquina (classificação)** cria um processo organizado, verificável e que permite evoluir com segurança.


---

## Como rodar (bem simples)

1. Abra o terminal e fique na pasta do projeto onde está o `requirements.txt`.
2. Instale as dependências:
```bash
pip install -r requirements.txt
si3. Rode o projeto:
```bash
s```

> Se o seu `main.py` estiver dentro de outra pasta, rode com o caminho completo (ex.: `python projeto-libras-sistemas/scripts/main.py`).

---

## Relatório — Membro 4 (Estratégista)

### Introdução (por que Libras?)
Libras é a língua natural da comunidade surda no Brasil. E, na vida real, ainda existem muitos momentos em que a comunicação não acontece do jeito que deveria — seja na escola, em atendimentos, ou no dia a dia.

Por isso, desenvolver um sistema que **reconhece sinais de Libras** é mais do que um projeto técnico: é uma forma de apoiar a inclusão e tornar a comunicação mais acessível.

### Metodologia (IA com MediaPipe)
O projeto foi construído em um fluxo de etapas (pipeline). A lógica é simples: cada etapa prepara o que a próxima precisa.

1. **Coleta e organização dos dados**
   - Os exemplos de sinais viram um dataset (`dataset.csv`).
   - No dataset:
     - **X (entradas):** dados numéricos extraídos do sinal (a representação do que o usuário fez)
     - **y (saída):** a letra/classe que o sistema deve identificar

2. **Extração de características com MediaPipe**
   - O MediaPipe detecta pontos do corpo (principalmente mãos).
   - Em vez de “olhar” a imagem inteira, ele transforma o movimento em **coordenadas**, que são mais fáceis da IA aprender.

3. **Treinamento do modelo de classificação**
   - Com o dataset pronto, o modelo aprende o padrão que liga **X → y**.
   - Depois do treino, o modelo é salvo para ser usado no reconhecimento.

### Resultados
Os resultados aparecem de forma bem concreta porque o pipeline tem validações em cada etapa:

- **Dados consistentes:** o sistema verifica se o `dataset.csv` existe e não está vazio antes de treinar.
- **Treino concluído:** o fluxo só segue se o treinamento termina com sucesso.
- **Modelo disponível:** ao final, o modelo fica salvo para o reconhecimento funcionar depois.

No fim, a combinação de **MediaPipe (visão/extração de pontos)** com **aprendizado de máquina (classificação)** deixa o processo organizado, testável e pronto para evoluir.

