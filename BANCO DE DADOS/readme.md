# Banco de dados

Base de conhecimento e como colocar no ar para testar a base do projeto. [Necessario para o testar os projetos de Web e Python].

## Requisitos

- Instalação do [XAMPP](https://www.apachefriends.org/download.html) - [8.2.12]
- Instalação de qualquer ferramenta acesso de Banco de Dados. [Utilizamos [HeidiSQL](https://www.heidisql.com/download.php?download=installer) - [12.7]]

## Processo de Instalação

Após a instalação do XAMPP é só abrir o painel de controle do mesmo e procurar por uma opção nomeada de `MySQL` e apertar no botão `start` ao lado dela.
![image](https://github.com/SgT012003/ESPR1-GS2/assets/82065998/5410e9bb-bc24-4f1e-a741-fccf376133d3)

O proximo passo já é no HeidiSQL ou software respectivo.
Quando dentro do software é só criar uma conexão declarando que a base é MariaDB ou MySQL
Por padrão o XAMPP cria o serviço com as seguintes configurações:
```json
"configs" : {
    "user": "root",
    "password": "",
    "host": "127.0.0.1",
    "port": 3306
}
```

Por conseguinte é só rodar a Querry de criação do aquivo já disponibilizado no repositorio. [acesso](https://github.com/SgT012003/ESPR1-GS2/blob/main/BANCO%20DE%20DADOS/CreateQuerry.sql)

E então terá um estrutura de Banco Identica a esta a qual será utilizada pelo client e server do projeto.
![image](https://github.com/SgT012003/ESPR1-GS2/assets/82065998/41f448fb-49fa-4ace-bcf5-16d543f2f277)

Respeciva estrutura da `Table` de dados.
![image](https://github.com/SgT012003/ESPR1-GS2/assets/82065998/c775f61c-bc72-4b06-973e-2147ad9614ed)

Respeciva estrutura da `Table` de dispositivos.
![image](https://github.com/SgT012003/ESPR1-GS2/assets/82065998/ff33ef42-9f2d-4ff5-a606-b6c92f349cee)

