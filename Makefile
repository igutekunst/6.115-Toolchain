#modify this to be your seiral port
ifeq (${shell uname} , Darwin)
USERPORT := `ls /dev/tty.PL2303*`
else
USERPORT := `ls /dev/ttyUSB*`
endif
# modifty this to include the asm file you want to proram
SRC := lab1_0

AS := rasm
PROG := prog8051

${SRC}.obj: ${SRC}.asm
	${AS} ${SRC}.asm
all: ${SRC}.obj

clean:
	rm ${SRC}.lst
	rm ${SRC}.err
	rm ${SRC}.obj

program: all
	${PROG}  ${SRC}.obj --serial-port ${USERPORT}

