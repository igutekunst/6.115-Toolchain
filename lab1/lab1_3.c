


//what i want it to do

while (1){
  getNextPattern();
    for(led = 0; led<8;led++){
      offTime = *(128 + led);
      if(offTime ==0){
        P1 |= ~(1<<led); // turn off current led
      }else{
        P1 &= (1<<led); // turn on current led
      }
    }
  for (i = 0; i < 16; i++) {
      offTime = *(128 + led);
    for(led = 0; led<8;led++){
      if(offTime == now){
        P1 |= ~(1<<led) // turn off current led
      }
    }
  }
}
