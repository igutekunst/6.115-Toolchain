#modify this to be your seiral port
ifeq (${shell uname} , Darwin)
USERPORT := `ls /dev/tty.PL2303*`
else
USERPORT := `ls /dev/ttyUSB*`
endif
# modifty this to include the asm file you want to proram
SRC := test

PRE := tpypp.py
AS := rasm
PROG := prog8051

all: ${SRC}.obj


${SRC}.obj: ${SRC}.asm
	${PRE} ${SRC}.asm ${SRC}.asm.p
	${AS} ${SRC}.asm.p

clean:
	rm *.lst
	rm *.err
	rm *.obj
	rm *.asm.p

program: all
	${PROG}  ${SRC}.obj --serial-port ${USERPORT}

