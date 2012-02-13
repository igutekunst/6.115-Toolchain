import instruction
import operands

class Mov(instruction.Instruction):
  def __init__(self,args):
    """docstring for __init__"""
    pass

  def __str__(self):
    return "<MOV >"


class MovIndirectR0FromLiteral(Mov):
  def __init__(self):
    """docstring for __init__"""
    pass

class MovIndirectR1FromLiteral(Mov):
  def __ini__(self):
    """docstring for __ini__"""
    pass

class MovIndirectR0FromA(Mov):
  """docstring for MovIndirectR0FromA"""
  def __init__(self, args):
    pass

class MovIndirectR1FromA(Mov):
  """docstring for MovIndirectR0FromA"""
  def __init__(self, args):
    pass

class MovDirectFromLiteral(Mov):
  opcode = 0x75
  def __init__(self, args):
    self.direct = args[0]
    self.literal = args[1]
    
  def getHex(self):
    return [self.opcode, self.direct.value, self.literal.value] 

  def __str__(self):
    return "<mov direct: 0x%x, literal: 0x%x>" % (self.direct.value,self.literal.value)

by_signature = {}
o = operands 
by_signature[  (o.DirectAddress, o.NumberLiteral)] = MovDirectFromLiteral


    
    
def get_op(args):
  signature = tuple([x.__class__ for x in args] )
  return by_signature[signature](args)
