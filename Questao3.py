#Importação do json
import json

#carregando o json
with open("dados.json") as meu_json:
    dadosJson = json.load(meu_json)

#função para importar o json para um array
def importValueJson(array):
    for i in dadosJson:
        array.append((i['valor']))
#função para limpar os dias sem faturamento
def cleanDaysWithoutBilling(array):
    arrayAux = []
    for i in array:
        if i != 0:
            arrayAux.append(i)
    array = arrayAux
    del arrayAux
#função para pegar o maior e menor valor de faturamento
def highestAndLowestBillingAmount(array):
    highestValue = 0
    for i in range(len(array)):
        if array[i] > highestValue:
            highestValue = array[i]
    
    lowerValue = highestValue
    for i in range(len(array)):
        if array[i] < lowerValue:
            lowerValue = array[i]

    print("O maior valor de faturamento é: ",highestValue)
    print("O menor valor de faturamento é: ",lowerValue)
#função que calcula os dias que o faturamento diário ultrapassou a média mensal
def dailyTopMonthly(array):
    sum = 0
    average = 0
    days = 0
    cleanDaysWithoutBilling(array)

    for i in range(len(array)):
        sum += array[i]
    average = sum/len(array)

    for i in range(len(array)):
        if array[i] > average:
            days = days + 1
    print("Teve um Total de ",days," dias que o valor diário ultrapassou a média mensal.")

#atribuindo as funções ao array vázio
array = []
importValueJson(array)
print(array)
highestAndLowestBillingAmount(array)
dailyTopMonthly(array)
