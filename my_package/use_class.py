#from classes import calculator as cal

#calc = cal.Calculator(4, 5)
#print("Multiplication of 4 & 5: ", calc.mul())

#from classes import calculator

#calc = calculator.Calculator(2, 4)
#print("Addition of 2 & 4: ", calc.add())

#import classes.calculator as cal
#calc = cal.Calculator(4, 1)
#print("Substraction of 1 by 4: ", calc.sub())

#import classes.calculator
#calc = classes.calculator.Calculator(6, 3)
#print("Division of 6 by 3: ", calc.div())

from  classes.calculator import Calculator as cal
 
calc = cal(10, 5)
print("Division of 10 by 5: ", calc.div())


