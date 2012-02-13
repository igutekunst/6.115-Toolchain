import operands, instructions
target_segment_size = 10


f = open("test.asm",'r')
line_number = 1
address = 0
segment_size = 0
program_instructions = []
labels = {}
for line in f:
  tokens = line.replace(',', ' ').split()
  if tokens[0].endswith(':'):
    label = tokens[0][:-1]
    if label in labels:
      raise Exception("Duplicate label %s one %d" % (label, line_number))
    else:
      labels[label] = address
  else:
    op_name = tokens[0].upper()
    op_factory = instructions.by_name[op_name]
    args = [] 
    for arg in tokens[1:]:
      data = operands.construct_operand(arg)
      args.append(data)
    args = tuple(args)
    instruction = op_factory(args)
    address += len(instruction.getHex())
    program_instructions.append(instruction)
print 
print labels
  

