# 1. Shift (carrega): terminal do início da entrada para o topo da pilha

# 2. Reduce (reduz): cadeia α do topo da pilha é reduzida para  A, se existir BNF A → α.

#  A pilha está vazia no início do processo e conterá o símbolo inicial ao final se bem sucedida.

class Automata:
  transition: chr = ''
  stack  = []
  currentStates: set = {}
  nextStates: set = set()
  fita: list[str]
  posicaoFita: int = 0
  lastAct: str = ''

  def __init__(self, fita:str):
      self.fita = fita.split()
      self.fita.append('$')
      # self.fita =list( map(lambda x: x.replace(" ", ""), tmp))

  def goto(self,to):
    self.lastAct = "goto"
    if to == 'accept':
      self.nextStates.add(to)
    else:
      self.nextStates.add(f"state{to}")
      self.stack.append(str(to))

  def shifter(self,to:int):
    self.lastAct = "shift"
    self.nextStates.add(f"state{to}")
    self.posicaoFita+=1
    self.stack.append(self.transition)
    self.stack.append(str(to))

  def reducer(self,to: str):
    self.lastAct = "reduce"
    aux = to.split()
    b = aux[0]
    c = aux[2:]
    c.reverse()
    while(len(c) != 0):
      last = self.stack.pop()
      if last == c[0]:
        c.pop(0)
      # print(f"stack:{self.stack}")
      # print(f"c:{c}")

    self.nextStates.add(f"state{self.stack[-1]}")
    self.stack.append(b)


  def state0(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        self.goto(2)
      elif self.stack[-1] == 'F':
        self.goto(3)
      elif self.stack[-1] == 'S':
        self.goto(4)
      elif self.stack[-1] == 'T':
        self.goto(5)
      elif self.stack[-1] == 'V':
        self.goto(6)
    elif self.transition == '(':
      self.shifter(1)
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      self.shifter(7)
    elif self.transition == 'num':
      self.shifter(8)
    elif self.transition == '$':
      pass
  
  def state1(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        self.goto(9)
      elif self.stack[-1] == 'F':
        self.goto(3)
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        self.goto(5)
      elif self.stack[-1] == 'V':
        self.goto(10)
    elif self.transition == '(':
      self.shifter(1)
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      self.shifter(7)
    elif self.transition == 'num':
      self.shifter(8)
    elif self.transition == '$':
      pass

  def state2(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      self.shifter(11)
    elif self.transition == '-':
      self.shifter(12)
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("S -> E")

  def state3(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("T -> F")
    elif self.transition == '*':
      self.reducer("T -> F")
    elif self.transition == '+':
      self.reducer("T -> F")
    elif self.transition == '-':
      self.reducer("T -> F")
    elif self.transition == '/':
      self.reducer("T -> F")
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("T -> F")

  def state4(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.goto('accept')

  def state5(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("E -> T")
    elif self.transition == '*':
      self.shifter(13)
    elif self.transition == '+':
      self.reducer("E -> T")
    elif self.transition == '-':
      self.reducer("E -> T")
    elif self.transition == '/':
      self.shifter(14)
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("E -> T")

  def state6(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("F -> V")
    elif self.transition == '*':
      self.reducer("F -> V")
    elif self.transition == '+':
      self.reducer("F -> V")
    elif self.transition == '-':
      self.reducer("F -> V")
    elif self.transition == '/':
      self.reducer("F -> V")
    elif self.transition == '=':
      self.shifter(15)
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("F -> V")

  def state7(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("V -> id")
    elif self.transition == '*':
      self.reducer("V -> id")
    elif self.transition == '+':
      self.reducer("V -> id")
    elif self.transition == '-':
      self.reducer("V -> id")
    elif self.transition == '/':
      self.reducer("V -> id")
    elif self.transition == '=':
      self.reducer("V -> id")
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("V -> id")

  def state8(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("F -> num")
    elif self.transition == '*':
      self.reducer("F -> num")
    elif self.transition == '+':
      self.reducer("F -> num")
    elif self.transition == '-':
      self.reducer("F -> num")
    elif self.transition == '/':
      self.reducer("F -> num")
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("F -> num")

  def state9(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.shifter(16)
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      self.shifter(11)
    elif self.transition == '-':
      self.shifter(12)
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      pass

  def state10(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("F -> V")
    elif self.transition == '*':
      self.reducer("F -> V")
    elif self.transition == '+':
      self.reducer("F -> V")
    elif self.transition == '-':
      self.reducer("F -> V")
    elif self.transition == '/':
      self.reducer("F -> V")
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("F -> V")

  def state11(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        self.goto(3)
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        self.goto(17)
      elif self.stack[-1] == 'V':
        self.goto(10)
    elif self.transition == '(':
      self.shifter(1)
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      self.shifter(7)
    elif self.transition == 'num':
      self.shifter(8)
    elif self.transition == '$':
      pass

  def state12(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        self.goto(3)
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        self.goto(18)
      elif self.stack[-1] == 'V':
        self.goto(10)
    elif self.transition == '(':
      self.shifter(1)
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      self.shifter(7)
    elif self.transition == 'num':
      self.shifter(8)
    elif self.transition == '$':
      pass

  def state13(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        self.goto(19)
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        self.goto(10)
    elif self.transition == '(':
      self.shifter(1)
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      self.shifter(7)
    elif self.transition == 'num':
      self.shifter(8)
    elif self.transition == '$':
      pass

  def state14(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        self.goto(20)
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        self.goto(10)
    elif self.transition == '(':
      self.shifter(1)
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      self.shifter(7)
    elif self.transition == 'num':
      self.shifter(8)
    elif self.transition == '$':
      pass

  def state15(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        self.goto(21)
      elif self.stack[-1] == 'F':
        self.goto(3)
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        self.goto(5)
      elif self.stack[-1] == 'V':
        self.goto(10)
    elif self.transition == '(':
      self.shifter(1)
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      pass
    elif self.transition == '-':
      pass
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      self.shifter(7)
    elif self.transition == 'num':
      self.shifter(8)
    elif self.transition == '$':
      pass

  def state16(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("F -> ( E )")
    elif self.transition == '*':
      self.reducer("F -> ( E )")
    elif self.transition == '+':
      self.reducer("F -> ( E )")
    elif self.transition == '-':
      self.reducer("F -> ( E )")
    elif self.transition == '/':
      self.reducer("F -> ( E )")
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("F -> ( E )")

  def state17(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("E -> E + T")
    elif self.transition == '*':
      self.shifter(13)
    elif self.transition == '+':
      self.reducer("E -> E + T")
    elif self.transition == '-':
      self.reducer("E -> E + T")
    elif self.transition == '/':
      self.shifter(14)
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("E -> E + T")

  def state18(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("E -> E - T")
    elif self.transition == '*':
      self.shifter(13)
    elif self.transition == '+':
      self.reducer("E -> E - T")
    elif self.transition == '-':
      self.reducer("E -> E - T")
    elif self.transition == '/':
      self.shifter(14)
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("E -> E - T")

  def state19(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("T -> T * F")
    elif self.transition == '*':
      self.reducer("T -> T * F")
    elif self.transition == '+':
      self.reducer("T -> T * F")
    elif self.transition == '-':
      self.reducer("T -> T * F")
    elif self.transition == '/':
      self.reducer("T -> T * F")
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("T -> T * F")

  def state20(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      self.reducer("T -> T / F")
    elif self.transition == '*':
      self.reducer("T -> T / F")
    elif self.transition == '+':
      self.reducer("T -> T / F")
    elif self.transition == '-':
      self.reducer("T -> T / F")
    elif self.transition == '/':
      self.reducer("T -> T / F")
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("T -> T / F")

  def state21(self):
    if self.lastAct == "reduce":
      if self.stack[-1] == 'E':
        pass
      elif self.stack[-1] == 'F':
        pass
      elif self.stack[-1] == 'S':
        pass
      elif self.stack[-1] == 'T':
        pass
      elif self.stack[-1] == 'V':
        pass
    elif self.transition == '(':
      pass
    elif self.transition == ')':
      pass
    elif self.transition == '*':
      pass
    elif self.transition == '+':
      self.shifter(11)
    elif self.transition == '-':
      self.shifter(12)
    elif self.transition == '/':
      pass
    elif self.transition == '=':
      pass
    elif self.transition == 'id':
      pass
    elif self.transition == 'num':
      pass
    elif self.transition == '$':
      self.reducer("S -> V = E")

  def execActiveNodes(self):
    if 'state0' in self.currentStates:
        self.state0()
    if 'state1' in self.currentStates:
        self.state1()
    if 'state2' in self.currentStates:
        self.state2()
    if 'state3' in self.currentStates:
        self.state3()
    if 'state4' in self.currentStates:
        self.state4()
    if 'state5' in self.currentStates:
        self.state5()
    if 'state6' in self.currentStates:
        self.state6()
    if 'state7' in self.currentStates:
        self.state7()
    if 'state8' in self.currentStates:
        self.state8()
    if 'state9' in self.currentStates:
        self.state9()
    if 'state10' in self.currentStates:
        self.state10()
    if 'state11' in self.currentStates:
        self.state11()
    if 'state12' in self.currentStates:
        self.state12()
    if 'state13' in self.currentStates:
        self.state13()
    if 'state14' in self.currentStates:
        self.state14()
    if 'state15' in self.currentStates:
        self.state15()
    if 'state16' in self.currentStates:
        self.state16()
    if 'state17' in self.currentStates:
        self.state17()
    if 'state18' in self.currentStates:
        self.state18()
    if 'state19' in self.currentStates:
        self.state19()
    if 'state20' in self.currentStates:
        self.state20()
    if 'state21' in self.currentStates:
        self.state21()

  def run(self):
    self.currentStates = {'state0'}
    self.transition = ''
    self.stack = ['0']
    self.posicaoFita = 0
    print(f"fita: {self.fita}")

    print("stack                   entrada               lastAct                     estado")
    while self.posicaoFita < len(self.fita):
      self.transition = self.fita[self.posicaoFita]
      self.execActiveNodes()
      print("----------------------------------------------------------------------------------------------------")
      print(f"{self.stack}        {self.fita[self.posicaoFita:]}      {self.lastAct}      {self.currentStates}",'')
      if len(self.nextStates) == 0:
        break
      self.currentStates = self.nextStates.copy()
      self.nextStates.clear()

    if 'accept' in self.currentStates:
      print("OK")
    else:
      print("NÃO OK")


def main():
  txt_file1 = open("./teste/entrada1.txt","r")
  data1 = txt_file1.read()
  print("entrada1.txt")

  # automata = Automata(data1)
  # automata = Automata("id = ( id ) + num")
  automata = Automata("id = id + (")
  automata.run()


main()
