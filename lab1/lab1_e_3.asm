org 00h               ; Reset vector
  ljmp main          ; Jump to user entry point


org 100h              ; main entry point at 100h
mov R3, #41h          ; loads the auto-wrap counter with 65
main:       
  lcall init          ; initialize the serial port
  loop:               ; infiinte loop
    lcall getchr      ; get a character fomr the serial port
    mov P1, A

    mov R0, #7Fh
    cjne A, 0, nobs
    push acc          ; save the accumulator for a second
    mov A, R3
    add A, #2h
    mov R3, A
    pop acc           ; restore the accumulator
    lcall backspace
    nobs:

    mov R0, #0Dh
    cjne, A, 0, nocrlf
    lcall crlf
    mov R3, #41h      ; resets the auto-wrap
    nocrlf:

    lcall putchr      ; echo that character right back

    djnz 3, loop
    mov R3, #41h      ; loads the character counter to 65
    lcall crlf
    sjmp loop


init:
; assume 11.0592 Mhz Clock
; user TIMER1 to create a 9600 baud connection
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

backspace:
  push acc
  lcall escape
  mov A, #31h ; '1'
  lcall putchr
  mov A, #44h ; 'D'
  lcall putchr

  lcall escape
  mov A, #4Bh
  lcall putchr
  pop acc
  ret
  

escape:
  mov A, #1bh
  lcall putchr
  mov A, #5Bh ; [
  lcall putchr
  ret


crlf:
  push acc
  mov A, #0Dh
  lcall putchr
  mov A, #0Ah
  lcall putchr
  pop acc
  ret
