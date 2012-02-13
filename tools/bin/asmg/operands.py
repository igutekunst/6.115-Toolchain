class Operand():
    def __init__(self):
		pass
    def getOperand():
        raise NotImplemented

class InvalidOperand(Operand):
    def __init__(self):
  		pass
    

class Label(Operand):
   def __init__(self, opstr):
		pass
class Literal(Operand):
    def __init__(self, opstr):
    		pass

class NumberLiteral(Literal):
    def __init__(self, opstr):
		self.opstr = opstr
		if opstr.startswith("0x"):
		    self.value = int(opstr[2:],16)
		elif opstr.startswith("0b"):
		    self.value = int(opstr[2:],2)
		elif opstr.startswith("'"):
		    self.value = ord(opstr[1])
		elif opstr[0] in "abcdefABCDEF0123456789":
		    if opstr.endswith('h'):
		        if len(opstr) < 4:
		            self.value = int(opstr[:-1],16)
		    elif opstr.endswith('d'):
		        self.value = int(opstr[:-1],10)
		    elif opstr.endswith('b'):
		        self.value = int(opstr[:-1],2)
		    else:
		        self.value = int(opstr[:-1],10)
    def __str__(self):
	    return "<NumberLiteral: %d ascii: '%c' >" % (self.value,chr(self.value))
				    
    def getOperand(self):
	    return self
class Address(Operand):
    def __init__(self, opstr):
    		pass
class DirectAddress(Address):
   def __init__(self, opstr):
		pass
		
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
        return Address(opstr )
    return Operand()
