mov P1, #00h ;Clear the LED Bank
setb P1.8
loop:
  sjmp loop
