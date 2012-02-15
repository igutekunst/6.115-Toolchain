import sys
import operands, instructions, pseudo_instructions
from insert_once_dict import DuplicateKeyError, InsertOnceDict
from program import Program
from sets import Set

class Assembler(object):

  def __init__(self, input_filename, parent = None):
    self.f = open(input_filename,'r')
    self.filename = input_filename
    if parent is None:
      self.address = 0
      self.program = Program()
      self.line_number = 1
      self.labels = InsertOnceDict()
      self.segment_size = 0
    else:
      self.address = parent.current_address
      self.parent_include_line_number = parent.line_number
      self.line_number = 1
      self.program = parent.program
      self.segment_size = parent.segment_size
      self.labels = parent.labels
  def assemble(self):
    
    self.program.cseg(0)
    for line in self.f:
      # Could be a normal op, a label, or a pseudo-op
      
      tokens = line.replace(',', ' ').split()
      if tokens[-1].endswith(':'):
        label_name = tokens[-1][:-1]
        new_label = operands.Label(label_name,
                               self.address,
                               self.filename,
                               self.line_number)

        self.labels[label_name] = new_label
      else:
        op_name = tokens[0].upper()
        if op_name in instructions.by_name:
          op_module = instructions.by_name[op_name]
          op_factory = op_module.get_op
          args = [] 
          for arg in tokens[1:]:
            data = operands.construct_operand(arg)
            args.append(data)
          args = tuple(args)
          instruction = op_factory(args)
          self.program.append(instruction) 
          self.address += len(instruction)
        elif op_name in pseudo_instructions.by_name:
          pass
          # pseudo_instruction
    for instruction in self.program:
      print instruction 
    print self.labels
    


target_segment_size = 10

filename = "test.asm"

assembler = Assembler(filename)

assembler.assemble()



