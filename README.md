# Simplex
Implementação do método simplex para a solução de PPLs

## Executando aplicação
Para executar a aplicação basta buildar a imagem e executar o container do Docker:

    sudo docker run -it  $(sudo docker build -q .)

Após isto execute o arquivo main.py:

    python3 main.py < Exemplo1\(Barras\).txt
