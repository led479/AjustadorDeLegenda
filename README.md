# Ajustador De Legenda
Um simples script de python que adianta ou atrasa as legendas de um arquivo .srt

## Requisitos para executar

* Ter o python instalado

## Instruções de uso
* O programa pode ser rodado pelo comando: 
`py ajustador_de_legenda.py`

* O arquivo .srt deve estar na mesma pasta do script

## Exemplo de uso do script
Ao baixar o filme do Homem de Ferro e suas legendas percebi que elas estavam 1.3 segundos atrasadas

Nome do filme: `homem-de-ferro.mp4`

Nome da legenda: `homem-de-ferro.srt`

Deverá ser passado ao script o nome da legenda como: `homem-de-ferro`

E o tempo de ajustamento como: `1.3`

E o script criará um arquivo novo chamado `homem-de-ferro_atualizado.srt`, que terá todas as legendas atrasadas em 1.3 segundos
