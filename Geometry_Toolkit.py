import math

class ShapeCalculator:
    def area(self, a, b=None):
        if b is None:
            return math.pi*a*a
        else:
            return a*b
        
SC = ShapeCalculator()
result = SC.area(70)
print(f"Area with One Parameter [Circle]: {result: .2f}")

ans = SC.area(70, 70)
print(f"Area with Two Parameter [Rectangle]: {ans: .2f}")
