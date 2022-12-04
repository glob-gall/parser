

def reducer(to:str):
  stack = ['0', 'V', '6', '=', '15', 'T', '5', '*', '13', 'F', '19']
  aux = to.split()
  b = aux[0]
  c = aux[2:]
  c.reverse()
  while(len(c) != 0):
    last = stack.pop()
    if last == c[0]:
      c.pop(0)
    print(f"stack:{stack}")
    print(f"c:{c}")

def main():
  reducer("T -> T * F")

main()