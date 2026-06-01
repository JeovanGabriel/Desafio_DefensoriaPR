# Desafio_DefensoriaPR-API_REST

 Este projeto foi feito para um desafio proposto pela Defensoria Pública do Paraná, tendo como objetivos a criação e implementação de uma Api de base Rest.

 A linguagem usada foi a **Python** com o uso das bibliotecas **FastAPI** e **Requests** para o desenvolvimento de uma API simples que utilizasse a requisição GET para pegar dados de uma outra API disponibilizada.

 ### 1. Preparação

 O arquivo "main.py" é o qual eu irei apresentar, sendo o arquivo principal da API, o "alternative_main.py" é uma ideia de implementação alternativa que está descrito posteriormente neste Readme.
 As bibliotecas que utilizei e devem ser instaladas são: **FastAPI, Requests e Uvicorn** através de:

 ```bash
 pip install fastapi
 pip install requests
 pip install uvicorn
 ```

 E para se conectar a máquina local com a internet deve-se ativar o Uvicorn através do terminal:

 ```bash
 python -m uvicorn main:app 
 ```

 sendo ``main`` o arquivo main.py que criei e ``app`` a variável que guarda a API.

 Caso dê este erro:

 ```bash
 ERROR:    Error loading ASGI app. Could not import module "main".
 ```
 Provavelmente por ter instalado o arquivo zip do repositório, o seu compilador esteja na pasta raiz e não na mesma pasta em que o arquivo "main.py" está, por isso você deve utilizar o:

 ```bash
 cd Desafio_DefensoriaPR-main
 ```

 E aí sim ativar o Uvicorn.

 ### 2. Inserir os parâmetros

 Quando estiver testando a API dentro da sua máquina insira na URL a sua data atual junto da rota existente sempre colocando nesta formatação "DD-MM-AAAA", e após isso você receberá como resultado os preços dos tapetes em formato JSON, junto da data atual requisitada. Ex: ``http://127.0.0.1:8000/01-06-2026``

 ### 3. alternative_main
 Mesmo não sendo requisitado no desafio mais sendo algo que eu quis fazer apenas como alternativa foi o uso da biblioteca datetime própria do python que possibilita que apenas ao inserir "precos" na URL você possa receber automaticamente a tabela de preços da API requisitada e a sua data atual de agora, é só uma medida alternativa que decidi implementar por teste do que utilizar no desafio em si.
 Caso queira utilizar reinicie o código e coloque no seu terminal:

 ```bash
 python -m uvicorn alternative_main:alternative_app
 ```

 ### 4. Documentação
 Caso queira acessar a documentação das APIS basta ir na URL e no final de todas elas colocar "docs" que você vai e acha a documentação que é gerada automaticamente pela FastAPI. Ex: ``http://127.0.0.1:8000/docs``


 E por aqui eu termino o Readme, foi um desafio interessante já que eu nunca fiz algo desse tipo, e foi legal ter aprendido a como criar uma API e a como usar os seus comandos, e isso mostra que mesmo não sabendo de nada dessa área, tem muita coisa legal a aprender sobre.