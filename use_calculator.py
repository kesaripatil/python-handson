#import module_calculator as Calculator

#calc = Calculator.Calculator(2,3)
#print("Addition of 2 & 3: ", calc.add())

#import module_calculator

#calc = module_calculator.Calculator(5, 3)
#print("Substraction of 5 & 3: ", calc.sub())

from module_calculator import Calculator
calc = Calculator(10, 5)
print("Division of 10 by 5: ", calc.div())
