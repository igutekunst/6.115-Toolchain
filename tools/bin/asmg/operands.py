def number_from_string(string):

		if string.startswith("0x"):
		    return int(string[2:],16)
		elif string.startswith("0b"):
		    return int(string[2:],2)
		elif string.startswith("'"):
		    return ord(string[1])
		elif string[0] in "abcdefABCDEF0123456789":
		    if string.endswith('h'):
		        if len(string) < 4:
		            return int(string[:-1],16)
		    elif string.endswith('d'):
		        return int(string[:-1],10)
		    elif string.endswith('b'):
		        return int(string[:-1],2)
		    else:
		        return int(string,10)
class Operand():
    def __init__(self):
		pass
    def getOperand():
        raise NotImplemented

class InvalidOperand(Operand):
    def __init__(self):
  		pass
    

class Label(Operand):
  def __init__(self, name, address, filename, line_number):
    self.name = name
    self.filename = filename
    self.line_number = line_number
    self.address = address

  def from_string(string, address, filename, line_number):
    #TODO Validate input string here
    return Label(string, address, filename, line_number)

  def __hash__(self):
    return hash(self.name)

  def __str__(self):
    return "<Label: %s>" % self.name
  def __repr__(self):
    return str(self)
class Literal(Operand):
    def __init__(self, opstr):
    		pass

class NumberLiteral(Literal):
    def __init__(self, opstr):
      self.opstr = opstr
      self.value = number_from_string(opstr)
    def __str__(self):
	    return "<NumberLiteral: %d ascii: '%c' >" % (self.value,chr(self.value))
				    
    def getOperand(self):
	    return self
class Address(Operand):
    def __init__(self, opstr):
    		pass
class DirectAddress(Address):
   def __init__(self, opstr):
     self.value = number_from_string(opstr)

		
class IndirectAddress(Address):
   def __init__(self, opstr):
		pass
		
class BitAddress(Address):
   def __init__(self, opstr):
		pass
		
class ReservedConstant(Operand):
    """
    Pseudo-Operand, that will generate either a BitAddress, or a DirectAddress
    """
    def __init__(self):
   		pass
   		
def construct_operand(opstr):
    """
    Parses an operand string onto a subclass of Operand.
    If it does not match 
    """
    if opstr.startswith("#"):
        return NumberLiteral(opstr[1:])
    elif opstr.startswith("0x"):
        return DirectAddress(opstr )
    return Operand()
