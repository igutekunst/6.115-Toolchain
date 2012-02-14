org 00h               ; Reset vector
  ljmp main          ; Jump to user entry point

org 100h
main:       
  lcall init          ; initialize the serial port
  loop:               ; infiinte loop
    mov R4, #06h
    getNumbers:
      lcall getNum    ; get a valid number
      push acc        ; push it onto the stack
      mov A, 4
      mov 2, #4
      cjne, A, 2, noCRLF
      lcall crlf
      noCRLF:
      djnz 4, getNumbers
    ; this next part pops the numbers from the stack, and multiplies each digit by it's
    ; power to get two arguments for the addition and subtraction
    pop 1           ; store ones place of arg 2 in R1
    pop acc         ; move tens place into acc
    mov B, #0Ah     ; Move 10 in to B
    mul AB          ; Multiply tens place by 10
    add A, 1        ; add to the ones places
    mov 1, A        ; store the partial sum in R1
    pop acc         ; Pop the hundreds place into acc
    mov B, #64h     ; Store 100 in B
    mul AB          ; Multiply 100's place by 100
    add A, 1        ; complete the sum for argument 2
    mov 2, A        ; store 2nd argument in R3
    
    pop 1           ; store ones place of arg 1 In R1
    pop acc         ; pop the tens place into the accumulator
    mov B, #0Ah     ; move 10 into B
    mul AB          ; multiply ten's place by 10
    add A, 1        ; add to ones place
    mov 1, A        ; move partial sum into R1
    pop acc         ; pop the hundred's place into the acumulator
    mov B, #64h     ; move 100 into B
    mul AB          ; multiply hundred's place by 100
    add A, 1        ; complete the sum for argument 1
    mov R1, A       ; Move argument 1 in R1
    
    lcall getOperand;Determine whether to add or subtract by calling getOperand  
    jz subtract     ; if getOperand returns zero, we should subtract
                    ; It's addition..
    mov A, R2       ; Move argument 2 into accumulator
    add A, R1       ; add with argument 1
    lcall crlf      ; send crlf
    mov P1, A       ; display on led bar
    lcall printNum  ; print the number on the UART
    lcall crlf      ; send crlf
    sjmp loop       ; jump to begninning again

    subtract:       ; we should enter this for to perform a subtraction
    mov   A, R1     ; Mov R1 into accumulator (so this will return R1 -R2)
    subb  A, R2     ; subtract R2 from R2 
    mov P1, A       ; display result on led bar
    lcall crlf      ; send CRLF
    lcall printNum  ; print the number of the UART
    lcall crlf      ; send another CRLF 
    sjmp loop       ; return to top    

getOperand:
; Return 0 if a '-' was received over the uart, and 1 if a '+'
; blocks and eats characters until a '+' or '-' is received
; result in accumulator
  push 1              ;save R1

  lcall getchr
  mov 1, #2Bh         ; move ascii '+' into R1
  cjne A, 1, notPlus
  mov A, #01h         ; It's a plus. Prepare to return 1
  pop 1               ; restore R1
  ret
  notPlus:
  mov 1, #2Dh         ; move ascii '-' into R1
  cjne A, 1, getOperand  ; if neither + or -, try again
  mov A, #0h          ; it's a minus. Prepare to return 0 
  pop 1               ; restore R1
  ret
getNum:
; Returns a number from 0-9 in the accumulator
; by sitting on the serial port until a valid character is returne
; depends on isNum subroutine to determine what valid chracters are
; modifes LED bank on P1
; leaves registers alone (on return)
  push 0                ;save R0
    getLoop:
      lcall getchr      ; get a character fomr the serial port
      mov P1, A
      mov R0, A         ; save the accumulator
      lcall isNum       ; see if received character is a number
      jz  getLoop       ; if it's not, try again
      mov A, R0         ; restore the accumulator
      anl A, #0Fh       ; mask out higher bits to get numeric value
      push acc          ; push the numeric value onto the stack
      mov A, R0         
      lcall putchr      ; echo that character right back
      pop acc           ; pop the numeric value back into the acc for return
      pop 0             ; restore R0
      ret
; Gets three numbers, and pushes them onto the stack
; in the order they were received

printNum:
; prints a number between 0 and 255 over the UART
; argument is accumulator
  push 0
  push 1
  push 2
  mov R0, A
  hundreds:
    mov B, #64H
    div AB
    mov R1, A       ; R1 contains number of hundreds
    mov R0, B       ; R0 contains the remainder
    mov A, R1
    orl A, #30h   ;converts to ascii
    lcall putchr
  tens:
    mov A, R0        ; A contains remainder
    mov B, #0Ah
    div AB          ; divide by ten
    mov R1, A       ; R1 contains number of tens
    mov R0, B
    mov A, R1       ; Move the # tens into the accumulator
    orl A, #30h   ;converts to ascii
    lcall putchr
  ones:
    mov A, R0
    orl A, #30h   ;converts to ascii
    lcall putchr
  noOnes:
  pop 2
  pop 1
  pop 0
  ret
isNum:    
; this subroutine will set the accumulator to nonzero
; (ascii 0-9)
; if the value in the accumulator is a valid ascii number
; it lets a few numbers through, so i'm not going to worry about it
  push 0                ; save R0 for safe keeping
  push 1                ; save R1
  mov R1, A             ; move potential ascii number into R1
  anl A, #0F0h          ; mask out lower nibble
  mov R0, #30h          ; ascii for '0'
  cjne A, 0, notNumber  ; if it's not a match, it's not number 

  mov A, #01h           ; return 1 for a number
  pop 1
  pop 0
  ret
  notNumber:
    mov A, #0h          ; return 0 for non number
    pop 1
    pop 0
    ret


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
