import math
#from math import sin, cos, tan

derece = 0
while derece <= 90:
  #print(derece)
  derece += 1#derece=derece+1 -> 0=0+1 {temp}
  if derece%5 == 0:#{mod}
    #print(derece)
    #print(derece,"sin =", math.sin(derece))
    #print(derece,"cos =", math.cos(derece))
    #print(derece,"tan =", math.tan(derece))
    #print("sin\tcos\ttan")

    print(derece,"=","sin {0} cos {1} tan {2}\n".format(math.sin(derece),math.cos(derece),math.tan(derece)))    