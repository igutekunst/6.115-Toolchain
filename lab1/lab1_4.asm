mov P1, #0ffh ; Clear LED bank

  mov 10h, #0fh
  mov 11h, #0eh
  mov 12h, #07h
  mov 13h, #01h
  mov 14h, #07h
  mov 15h, #0eh
  mov 16h, #0fh
  mov 17h, #00h 

mov R6, #010h
loop:

  mov 1, #08h   ; Highest LED
  clr c
  mov A, #1h
  mov 2, A
  init:
    lcall loadLed ; load the led value into R0
    mov A, R0

    jz off
    mov A, 2
    orl P1, A
    off:
    
    
    mov A, R2
    rlc A
    mov R2, A
    djnz R1, init

  ; 1: led #
  ; 2: led mask
  ; 3: brightness value
  mov R3, #0fh
  for_each_brightness:
    
    mov R7, #08h   ; Highest LED
    clr c
    mov A, #1h    ; Led Mask for led 0
    mov R2, A      ; store in R2 for safe keeping

    for_each_led:
      mov 1, 7
      lcall loadLed   ; assumes LED# stored in R1
                      ; will learn about stacking later
      mov A, R0       ; get return value
      cjne A, 3, led_still_on
      mov A, 2        ;load the led mask
      xrl A, #0ffh    ; negate
      anl P1, A

      led_still_on:



      mov A, R2  ; Load LED mask
      clr c
      rlc A      ; left shift
      mov R2, A  ; store in R2
      djnz R7, for_each_led
      lcall delay

    djnz R3, for_each_brightness
    mov P1, #00h
    mov R7, #010h
    lcall long_delay

  djnz R6, loop
  lcall next
  mov R6, #10h
  sjmp loop 




next:
  mov A, 10h
  mov 10h, 11h
  mov 11h, 12h
  mov 12h, 13h
  mov 13h, 14h
  mov 14h, 15h
  mov 15h, 16h
  mov 16h, 17h
  mov 17h, A
  ret
delay:
  push 6
  mov 6, #05h
  dtop:
  nop
    djnz R6,dtop

  pop 6
  ret
;Loads the value of the led into R0
loadLed:    ; loads the led brighness value from the table stored from 0x10 to 0x17 into R0
    mov A, #18h
    subb A, R1

    push 1
    mov R1, A
    mov A, @R1
    pop 1
    mov R0, A
    ret
long_delay:
  lcall delay
  djnz 7, long_delay
  ret
