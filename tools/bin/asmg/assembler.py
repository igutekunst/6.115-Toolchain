import operands, instructions
f = open("test.asm",'r')

for line in f:
  tokens = line.replace(',', ' ').split()
  op = tokens[0]  
  args = tokens[1:]
  for arg in args:
    data = operands.construct_operand(arg)
    print data

