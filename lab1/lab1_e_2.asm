org 00h               ; Reset vector
  ljmp main          ; Jump to user entry point


org 100h              ; main entry point at 100h
main:       
  lcall init          ; initialize the serial port
  loop:               ; infiinte loop
    lcall getchr      ; get a character fomr the serial port
    lcall putchr      ; echo that character right back
    sjmp loop           


init:
; assume 11.0592 Mhz Clock
; user TIMER1 to create a 9600 baude connection
  mov tmod, #20h
  mov tcon, #40h
  mov th1,  #0FDh
  mov scon, #50h
  ret

getchr:
; This routine receives characters from the UART
; jnb is bitwise jmp if bit not set
  jnb RI, getchr  ; wait until the rx interrupt flag is set
  mov A, sbuf     ; move the character into the accumulator
  anl A, #7fh      ; clear 8th bit (since this should be ASCII)
  clr RI          ; clear the intterupt flag
  ret


putchr:
  clr scon.1          ; Clear the transmit done flag
  mov sbuf, a
  txloop:
    jnb TI, txloop    ; Wait until the character is actually sent
    ret


