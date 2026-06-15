# projeto-libras-sistemas

## Detector de Libras com Inteligência Artificial

Sistema para reconhecimento de sinais da Língua Brasileira de Sinais (Libras) utilizando MediaPipe e técnicas de aprendizado de máquina.

---

## Como executar

1. Abra o terminal na pasta do projeto (onde está localizado o arquivo `requirements.txt`).

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o sistema:

```bash
python main.py
```

Caso o arquivo `main.py` esteja em outro diretório, utilize o caminho completo. Exemplo:

```bash
python projeto-libras-sistemas/scripts/main.py
```

---

## Relatório

### Introdução

A Libras (Língua Brasileira de Sinais) é a língua oficial da comunidade surda brasileira e desempenha papel fundamental na inclusão social e educacional. Apesar dos avanços na acessibilidade, ainda existem barreiras de comunicação entre pessoas surdas e ouvintes em diversos ambientes.
Dessa forma, o desenvolvimento de sistemas capazes de reconhecer sinais de Libras pode contribuir para uma comunicação mais acessível, promovendo inclusão e reduzindo dificuldades de interação no cotidiano.

### Metodologia

O projeto foi desenvolvido seguindo um pipeline composto por etapas sequenciais:

#### 1. Coleta e organização dos dados

Os exemplos de sinais foram utilizados para gerar um conjunto de dados armazenado no arquivo `dataset.csv`.

* **X (entradas):** características numéricas extraídas dos sinais.
* **y (saídas):** letra ou classe correspondente ao sinal realizado.

#### 2. Extração de características com MediaPipe

O MediaPipe é utilizado para detectar pontos de referência das mãos e do corpo.

Em vez de processar diretamente a imagem completa, o sistema utiliza as coordenadas desses pontos, permitindo uma representação mais consistente dos movimentos e posições dos sinais.

#### 3. Treinamento do modelo

Após a construção do dataset, o modelo de aprendizado de máquina é treinado para aprender a relação entre as entradas (X) e as respectivas classes (y).

Ao final do treinamento, o modelo é salvo para utilização na etapa de reconhecimento.

### Resultados

Os resultados são observados por meio do funcionamento correto de cada etapa do pipeline:

* Verificação da existência e consistência do arquivo `dataset.csv`.
* Treinamento bem-sucedido do modelo de classificação.
* Geração e armazenamento do modelo treinado.
* Disponibilização do modelo para reconhecimento de sinais em tempo real.

A integração entre o MediaPipe e técnicas de aprendizado de máquina permite a construção de um sistema organizado, escalável e adequado para futuras melhorias e expansões.
