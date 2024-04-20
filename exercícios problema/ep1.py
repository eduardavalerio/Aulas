"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Eduarda Valério de Jesus 
  NUSP : 12516672
  Turma: Turma 15 - IAG 2024
  Profa.: Leliane
  Monitora: Viviane

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

# Solicitação dos dados de entrada do GPS
gps = int(input(" digite (ou copie e cole) os dados do seu gps linha por linha e termine com a linha 000:"))

# Inicializações
bpm = 0 # batimento cardíaco
maior_bpm = 0 # maior batimento cardíaco registrado do corredor 
idade = 0 # idade de aptidão física 
metro_maior = 10 # maior posição
metro_menor = 99 # menor posição
cont = 0 #contagem 
dist = 0 # distância percorrida pelo corredor 
vm = 0 # velocidade média do corredor 
soma = 0 # soma dos divisores do maior bpm 
n = 1 # possíveis divisores para o maior bpm

while gps != 000:
    bpm = gps % 1000 # o resto da divisão é igual aos 3 últimos números que indica o batimento cardíaco do corredor 
    if bpm > maior_bpm: # definir bpm como maior batimento cardíaco registrado 
        maior_bpm = bpm 
        idade = 220 - bpm # idade de aptidão é a diferença entre limite superior de batimento cardíaco (220) e bpm
    metro = gps // 1000 # descascando o número para ter o valor que marca a posição 
    gps = int(input())
    if metro >= metro_maior: #determinar a maior e menor posição para obter a distância percorrida 
        metro_maior = metro
    if metro < metro_menor:
        metro_menor = metro
    cont = cont + 1
    dist = metro_maior - metro_menor # distância percorrida 
temp = cont - 1 # intervalor em segundos 
vm = dist // temp # distância por tempo resulta na velocidade 
print("##### seguem as suas estatisticas #####")
if idade < 10: 
   print("sua idade de aptidao fisica nao pode ser calculada")
else:  
   print("sua idade de aptidao fisica eh:", idade)
if vm >= 4: # classificação para cada pelotão dependendo da velocidade obtida
    print("seu pelotao eh o QUENIA")
elif vm >= 2 and vm < 4:
    print("seu pelotao eh o AZUL")
else:
    print("seu pelotao eh o BRANCO")
while n < maior_bpm: # determinar se terá ou não desconto dependendo se o maior bpm for um número abundante 
    if maior_bpm % n == 0:
        soma = soma + n
    n = n + 1
if soma > maior_bpm:
    print("parabens! voce terah desconto na inscricao da prova! \o/\o/\o/")
else:
    print()