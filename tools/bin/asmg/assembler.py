import operands, instructions, pseudo_instructions
from program import Program
from sets import Set

class Assembler(object):

  segment_size = 0
  program_instructions = []
  labels = Set()
  address_by_label = []
  def __init__(self, input_filename, parent = None):
    try:
      self.f = open(input_filename,'r')
      self.filename = input_file
    except Exception as e:
      print str()
      sys.exit(1)
    if parent is None:
      self.current_address = 0
      self.line_number = 1
    else:
      self.program = Program()
      self.current_address = parent.current_address
      self.parent_include_line_number= parent.line_number
      self.line_number = 1
      self.labels = parent.labels

  def assemble(self):
    for line in self.f:
      # Could be a normal op, a label, or a pseudo-op
      
      if line.endswith(':'):
        label_name = tokens[0][:-1]
        if label_name in self.address_by_label:
          raise Exception("Duplicate label")
        label = operands.Label.from_string(label_name, address, filename, line_number)
      else:
        tokens = line.replace(',', ' ').split()
        op_name = tokens[0].upper()

        if op_name in instructions.by_name:
          pass
          #normal op
        elif op_name in pseudo_instructions.by_name:
          pass
          # pseudo_instruction

      pass
    for instruction in self.program:
      pass
      
    
     

target_segment_size = 10

filename = "test.asm"
f = open(filename,'r')
line_number = 1
address = 0
segment_size = 0
program_instructions = []
address_by_label = {}



for line in f:
  tokens = line.replace(',', ' ').split()
  if tokens[0].endswith(':'):
    label_name = tokens[0][:-1]
    label = operands.Label(label_name, address, filename, line_number)
    if label in address_by_label:
      raise Exception("Duplicate label %s on line %d" % (label, line_number))
    else:
      address_by_label[label] = address
  else:
    op_name = tokens[0].upper()
    op_module = instructions.by_name[op_name]
    op_factory = op_module.get_op
    args = [] 
    for arg in tokens[1:]:
      data = operands.construct_operand(arg)
      args.append(data)
    args = tuple(args)
    instruction = op_factory(args)
    address += len(instruction)
    program_instructions.append(instruction)
print program_instructions
print address_by_label
  

