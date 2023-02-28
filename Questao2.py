def verificarFibonacci(numero):
  primeiroNumero = 0
  segundoNumero = 1

  while primeiroNumero < numero:
    primeiroNumero, segundoNumero = segundoNumero, (primeiroNumero + segundoNumero)

  if(primeiroNumero == numero):
    print("O numero ",numero," pertence a sequência de Fibonacci!")
  else:
    print("O numero ",numero," não pertence a sequência de Fibonacci!")


numeroVerificacao = int(input("Digite o numero para verificar se pertence a sequencia de Fibonacci: "))
verificarFibonacci(numeroVerificacao)