from random import *
firstPart = ["Journey to the  ", "Return of ", "Adventures in ", "Battle for the ", "The Trials of ", "Night of the  ", "Haunting of ", "Chaos in the  ", "Lord of the  ", "Touch of "]
secondPart = ["Putrid ", "Amazing ", "Bright ", "Scary ","Powerful ", "Inspiring ", "Strong ", "Quick ", "Fat ", "Heavy "]                                                                               
thirdPart = ["Center of the Earth ", "The Wild West ", "Wonderland ", "Gates of Hell ", "Kings ", "The Tenth Dimension ", "Godzilla's Mouth ", "The Gallows ", "Mines ", "Cornfields "]    
i = 0
while i <= 10:
  x = firstPart[randrange(10)]
  y = secondPart[randrange(10)]
  z = thirdPart[randrange(10)]
  title = x + "" + y + "" + z
  print(title)
  i = i + 1