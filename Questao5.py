#invertendo caracteres com conceito de pilha de python
class Pilha:
  def __init__(self):
    self.head = []

  def append(self,valor):
    self.head.append(valor)

  def remove(self):
    return self.head.pop()

pilha = Pilha()
textInverted = ''
text = input("Digite a palavra que deseja inverter: ") #exemplo: uepb
for i in range(len(text)): #lendo a palavra
  pilha.append(text[i]) #pilha vai receber cada palavra

for i in range(len(text)):
  textInverted = textInverted + (pilha.remove())

print(textInverted)