#modify this to be your seiral port
ifeq (${shell uname} , Darwin)
USERPORT := `ls /dev/tty.PL2303*`
else
USERPORT := `ls /dev/ttyUSB*`
endif
# modifty this to include the asm file you want to proram
SRC := test

PRE := tpypp/tpypp.py
AS := rasm
PROG := prog8051

${SRC}.asm.processed : ${SRC}.asm
	${PRE} ${SRC}.asm

${SRC}.obj: ${SRC}.asm.processed
	${AS} ${SRC}.asm.processed
all: ${SRC}.obj

clean:
	rm *.lst
	rm *.err
	rm *.obj
	rm *.asm.processed

program: all
	${PROG}  ${SRC}.obj --serial-port ${USERPORT}

