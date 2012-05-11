import mov
by_name		 = 	{}
by_name['ACALL']	 = 	{ "desc" : "Absolute Call"}
by_name['ADD']		 = 	{"desc" : "Add Accumulator (With Carry)"}
by_name['AJMP']	 = 	{ "desc" : "Absolute Jump"}
by_name['ANL']		 = 	{ "desc" : "Bitwise AND"}
by_name['CJNE']	 = 	{ "desc" : "Compare and Jump if Not Equal"}
by_name['CLR']		 = 	{ "desc" : "Clear Register"}
by_name['CPL']		 = 	{ "desc" : "Complement Register"}
by_name['DA']		 = 	{ "desc" : "Decimal Adjust"}
by_name['DEC']		 = 	{ "desc" : "Decrement Register"}
by_name['DIV']		 = 	{ "desc" : "Divide Accumulator by B"}
by_name['DJNZ']	 = 	{ "desc" : "Decrement Register and Jump if Not Zero"}
by_name['INC']		 = 	{ "desc" : "Increment Register"}
by_name['JB']		 = 	{ "desc" : "Jump if Bit Set"}
by_name['JBC']		 = 	{ "desc" : "Jump if Bit Set and Clear Bit"}
by_name['JC']		 = 	{ "desc" : "Jump if Carry Set"}
by_name['JMP']		 = 	{ "desc" : "Jump to Address"}
by_name['JNB']		 = 	{ "desc" : "Jump if Bit Not Set"}
by_name['JNC']		 = 	{ "desc" : "Jump if Carry Not Set"}
by_name['JNZ']		 = 	{ "desc" : "Jump if Accumulator Not Zero"}
by_name['JZ']		 = 	{ "desc" : "Jump if Accumulator Zero"}
by_name['LCALL']	 = 	{ "desc" : "Long Call"}
by_name['LJMP']	 = 	{ "desc" : "Long Jump"}
by_name['MOV']		 = 	mov
by_name['MOVC']	 = 	{ "desc" : "Move Code Memory"}
by_name['MOVX']	 = 	{ "desc" : "Move Extended Memory"}
by_name['MUL']		 = 	{ "desc" : "Multiply Accumulator by B"}
by_name['NOP']		 = 	{ "desc" : "No Operation"}
by_name['ORL']		 = 	{ "desc" : "Bitwise OR"}
by_name['POP']		 = 	{ "desc" : "Pop Value From Stack"}
by_name['PUSH']	 = 	{ "desc" : "Push Value Onto Stack"}
by_name['RET']		 = 	{ "desc" : "Return From Subroutine"}
by_name['RETI']	 = 	{ "desc" : "Return From Interrupt"}
by_name['RL']		 = 	{ "desc" : "Rotate Accumulator Left"}
by_name['RLC']		 = 	{ "desc" : "Rotate Accumulator Left Through Carry"}
by_name['RR']		 = 	{ "desc" : "Rotate Accumulator Right"}
by_name['RRC']		 = 	{ "desc" : "Rotate Accumulator Right Through Carry"}
by_name['SETB']	 = 	{ "desc" : "Set Bit"}
by_name['SJMP']	 = 	{ "desc" : "Short Jump"}
by_name['SUBB']	 = 	{ "desc" : "Subtract From Accumulator With Borrow"}
by_name['SWAP']	 = 	{ "desc" : "Swap Accumulator Nibbles"}
by_name['XCH']		 = 	{ "desc" : "Exchange Bytes"}
by_name['XCHD']	 = 	{ "desc" : "Exchange Digits"}
by_name['XRL']		 = 	{ "desc" : "Bitwise Exclusive OR"}
