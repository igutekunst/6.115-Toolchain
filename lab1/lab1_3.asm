mov P1, #00h ; Clear led bank
mov P1, #55h ; Turn on Highest led
loop:
  sjmp loop ; loop forever
