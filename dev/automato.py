# 1. Shift (carrega): terminal do início da entrada para o topo da pilha

# 2. Reduce (reduz): cadeia α do topo da pilha é reduzida para  A, se existir BNF A → α.

#  A pilha está vazia no início do processo e conterá o símbolo inicial ao final se bem sucedida.

class Automata:
  transition: str = ''
  currentStates: set = {'q0'}
  nextStates: set = set()
  curentToken: str = ''
  stack: str = ''

  def goto(self,to):
      self.nextStates.add(to)

  def shifter(self,to):
      self.nextStates.add(to)

  def reducer(self,to):
      self.nextStates.add(to)
    
  def execActiveNodes(self):
    if 'numberState' in self.currentStates:
        self.numberState()

  def run(self,code:str):
        self.currentStates= {'tokenState', 'numberState', 'wordState'}
        self.transition =''

        for c in code:
            self.transition = c
            # print(self.currentStates)
            # print(self.transition)
            self.execActiveNodes()
            
            self.transition=''
            self.currentStates = self.nextStates.copy()
            self.nextStates.clear()
        self.execActiveNodes()

  def state0(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      self.shifter(7)
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      self.shifter(5)
    elif self.transition == 'num':
      self.shifter(8)
    elif self.transition == '$':
      pass

  def state1(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.goto('accept')

  def state2(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      self.shifter(9)
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      self.shifter(10)
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer('S -> E')

  def state3(self):
    if self.transition == '=':
      self.shifter(11)
    elif self.transition == '+':
      self.reducer('F -> V')
    elif self.transition == '*':
      self.reducer('F -> V')
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer('F -> V')
    elif self.transition == '-':
      self.reducer('F -> V')
    elif self.transition == '/':
      self.reducer('F -> V')
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer('F -> V')

  def state4(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      self.reducer('E -> T')
    elif self.transition == '*':
      self.shifter(12)
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer('E -> T')
    elif self.transition == '-':
      self.reducer('E -> T')
    elif self.transition == '/':
      self.shifter(13)
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer('E -> T')

  def state5(self):
    if self.transition == '=':
      self.reducer('V -> id')
    elif self.transition == '+':
      self.reducer('V -> id')
    elif self.transition == '*':
      self.reducer('V -> id')
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer('V -> id')
    elif self.transition == '-':
      self.reducer('V -> id')
    elif self.transition == '/':
      self.reducer('V -> id')
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer('V -> id')

  def state6(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      self.reducer('T -> F')
    elif self.transition == '*':
      self.reducer('T -> F')
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer('T -> F')
    elif self.transition == '-':
      self.reducer('T -> F')
    elif self.transition == '/':
      self.reducer('T -> F')
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer('T -> F')

  def state7(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state8(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state9(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state10(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state11(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state12(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state13(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state14(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state15(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state16(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state17(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state18(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state19(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state20(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state21(self):
    if self.transition == '=':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass


terminais = ["num", "id", "+", "-", "*", "/", "=", "(", ")"]

def main():
  automata = Automata()
  txt_file1 = open("./teste/entrada1.txt","r")
  data1 = txt_file1.read()
  print("entrada1.txt")

  automata.run(data1)


main()