import instruction

class SJMP(instruction.Instruction):
    opcode = 0x80
    bytes = 2
    description = 'SJMP jumps unconditionally to the address specified reladdr. Reladdr must be within -128 or +127 bytes of the instruction that follows the SJMP instruction.'
    
    def getHexa(self,args):
        pass