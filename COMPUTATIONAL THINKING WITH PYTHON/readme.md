# COMPUTATIONAL THINKING WITH PYTHON

Base de conhecimento e como colocar no ar para testar a base do projeto. [Necessario para o testar os projetos de Web].

## Requisitos

- [Banco de dados](https://github.com/SgT012003/ESPR1-GS2/tree/main/BANCO%20DE%20DADOS)
- Comando de instalação para as bibliotecas usadas [`pip install Flask requests pyserial mysql-connector-python`]. [python 12.3.x]

## Separação do projeto

O projeto foi separado em dois serviços.

O Client Side e o Server Side e cada um tem seu proprio proposito.
Os quais será aprofundados em suas respectivas seções.


### Client Side.

Esse serviço foi feito para rodar nos modulos de computadores que estam diretamente conectadas aos arduinos.

#### Funções

- Ler a entrada Serial.
- Processar os dados.
- Enviar para o Banco de Dados.
- Em caso de falha no envio, armazenar os dados e enviar na proxima oportunidade.

### Server Side.

Esse serviço foi desenvolvido para agir como uma API, podendo ser requisitada atravez da Web utilizando uma biblioteca chamada de `Flask`.

![image](https://github.com/SgT012003/ESPR1-GS2/assets/82065998/85ee12e4-e466-4ea1-8b6a-194e8a4d0e1c)

Dando variabilidade de chamadas e filtrando os resultados com base nos argumentos usandos na web.

Por exemplo, o limite padrao de maximo de objetos disponibilizados na API é de 25, para passar para os proximos 25 se usa a url: `https://127.0.0.1:5000/?page=1`
Podendo tambem filtrar pelo nome do aparelho utilizando a url `https://127.0.0.1:5000/?name=dispositivo`
Ou Ambos utilizando `https://127.0.0.1:5000/?page=1&name=dispositivo`
