#modify this to be your seiral port
ifeq (${shell uname} , Darwin)
USERPORT := `ls /dev/tty.usbserial`
else
USERPORT := `ls /dev/ttyUSB*`
endif
# modifty this to include the asm file you want to proram
SRC := test

PREPROCESSOR := tpypp.py
AS := rasm
PROG := prog8051



${SRC}.obj: ${SRC}.asm
	${PREPROCESSOR} ${SRC}.asm ${SRC}.p.asm
	${AS} ${SRC}.p.asm

clean:
	rm -f *.lst
	rm -f *.err
	rm -f *.obj
	rm -f *.hex
	rm -f *.asm.p

all: ${SRC}.obj

program: all
	${PROG}  ${SRC}.p.obj --serial-port ${USERPORT}

