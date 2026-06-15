# projeto-libras-sistemas
Detector de Libras

### README.md — como rodar (do jeito mais fácil)

1. Abra o terminal e fique na **pasta do projeto** onde estão os arquivos do projeto (especialmente o `requirements.txt`).
2. Instale tudo o que o projeto precisa:
```bash
pip install -r requirements.txt
```
3. Agora é só rodar:
```bash
python main.py
```

> Se der algum erro dizendo que não existe `main.py`, não se assuste: neste repositório ele pode estar dentro de outra pasta. Nesse caso, rode o `main.py` com o caminho completo (ex.: `python projeto-libras-sistemas/scripts/main.py`).


---

### Relatório

#### Introdução (por que Libras?)
Libras (Língua Brasileira de Sinais) é a forma natural de comunicação da comunidade surda no Brasil. E, na rotina, ainda tem muita barreira no meio do caminho: em situações simples, como educação, atendimento e convivência social, nem sempre é fácil se fazer entender.

Por isso, criar um sistema que **reconhece sinais de Libras** faz diferença de verdade: ajuda a aproximar pessoas surdas e ouvintes e deixa a comunicação mais acessível.


#### Metodologia (IA com MediaPipe)
O projeto foi pensado como um fluxo em etapas (pipeline). Cada parte faz seu papel e entrega a informação pronta para a próxima etapa.

1. **Coleta e preparação dos dados**
   - Os exemplos de sinais foram organizados em um dataset (`dataset.csv`).
   - No dataset, temos:
     - **entradas (X):** dados numéricos extraídos do sinal (representação das mãos/corpo)
     - **saída (y):** a letra/classe que o sistema deve identificar

2. **Extração de características com MediaPipe**
   - O MediaPipe detecta pontos do corpo (principalmente das mãos) e traduz isso para números.
   - Em vez de a IA tentar “entender” a imagem inteira, ela trabalha com **coordenadas**, o que deixa os padrões do movimento mais fáceis de aprender.

3. **Treinamento do modelo de classificação**
   - Com os dados prontos, o modelo aprende a relacionar os padrões numéricos (X) com a classe correta (y).
   - Depois do treino, o modelo é salvo para ser usado futuramente no reconhecimento.

#### Resultados
Os resultados do projeto foram acompanhados de forma prática, porque o pipeline só avança quando cada etapa cumpre o seu objetivo:

- **Consistência dos dados:** o dataset precisa existir e ter conteúdo (senão o treino não faz sentido).
- **Treinamento concluído:** a etapa de treino só termina quando o modelo foi gerado sem erros.
- **Modelo salvo:** o sistema passa a ter um “cérebro” (o arquivo do modelo), pronto para ser usado em reconhecimento.

Em resumo: essa estratégia junta visão computacional (MediaPipe) com aprendizado de máquina, criando um processo que dá pra acompanhar, testar e melhorar com segurança.
