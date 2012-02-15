from instruction import Instruction
class Segment(object):
  def __init__(self, start_address):
    self.start_address = start_address
    self.instructions = []
    self.length = 0

  def add_instruction(self, instruction):
    self.instructions.append(instruction)
    self.length += len(instruction)

class Program(object):
  segments_by_start_address = {}
  instructions = []
  def __init__(self, memory_size = 4096):
    self.current_segment_start_address = 0

  def cseg(self, address):
    """
    Starts a new code segment. Code segments cannot overlap
    """
    if address in self.segments_by_start_address:
      raise Exception(" Attempt create a code segment when one already exists")
    else:
      new_segment = Segment(addresss) 
      self.segments_by_start_address[address] = new_segment
      self.current_segment = new_segment
      self.current_address = address

  def add_instruction(self, instruction):
    if not isinstance(instruction, Instruction):
      raise Exception("Attempt to add non instruction to program")
    """
    Appends a new instruction to the current code segment
    """
    addresses_affected = [l + self.current_address for l in xrange(len(instruction))]
    for address in adresses_affected:
      if address in self.segments_by_start_address:
        raise Exception("Segment is overflowing")

    self.current_segement.add_instruction(instruction)
    self.instructions.append(instruction)
    

  def __iter__(self):
    return iter(self.instructions)



