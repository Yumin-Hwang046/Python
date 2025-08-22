#Class exercise

#5-5 사용자로부터 첫 번째 숫자, 연산자(+, -, *, /), 두 번째 숫자를 순차적으로 입력받아 연산을 수행하는 프로그램을 작성하세요.
#  단, 사용자로부터 입력받는 부분, 연산하는 부분 모두 클래스의 함수로 구현하고,
#  main 함수에서는 이 클래스를 객체로 생성하고 연산을 수행하는 함수를 호출하세요.

#Sol

class calculator:
    n1 = 0.0
    operator = ""
    n2 = 0.0

    def __init__(self):
        self.n1 = float(input("Put your first number here: "))
        self.operator = input("Put the operator you want here: ")
        self.n2 = float(input("Put your first number here: "))
    
    def execute_calculation(self):
        if self.operator == '+':
            return self.n1+self.n2
        elif self.operator == '-':
            return self.n1-self.n2
        elif self.operator == '*':
            return self.n1*self.n2
        elif self.operator == '/':
            return self.n1/self.n2
        else:
            return "this calculator does not support the specified operator."

if __name__ == '__main__':
    Calculation = calculator()
    print(Calculation.execute_calculation())

#Sol_Book

class userCalculation:
    name = "연산하는 클래스"

    def __init__(self):
        print("연산 클래스 생성자 호출")

    def execPlus(self, num1, num2):
        return num1 + num2
    
    def execMinus(self, num1, num2):
        return num1 - num2
    
    def execMultiply(self, num1, num2):
        return num1 * num2
    
    def execDivide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("can't divide by 0")
            return 0
        
    def executeCalculation(self):
        num1 = float(input())
        operator = input()
        num2 = float(input())

        if operator == '+':
            result = self.execPlus(num1, num2)
        elif operator == '-':
            result = self.execMinus(num1, num2)
        elif operator == '*':
            result = self.execMultiply(num1, num2)
        elif operator == '/':
            result = self.execDivide(num1, num2)
        else:
            print("Error")
            result = 0

        print(result)
        return num1, operator, num2
    
    def __del__(self):
        print("연산 클래스 소멸자 호출")
    
if __name__=='__main__':
    cal = userCalculation()
    num1, operator, num2 = cal.executeCalculation()

#5-6 물품의 단가 및 가격의 합계를 입출력할 수 있는 클래스를 작성해보세요. 물품은 우유와 콜라가 있으며 해당 물품의 가격은 객체 생성 시 할당합니다.
#  사용자는 우유의 개수와 콜라의 개수를 입력하면 해당 물품의 가격 총합을 출력할 수 있습니다.

#Sol

class PosMachine:
    milk = 0.0
    coke = 0.0

    def __init__(self, milk, coke):
        self.milk = float(milk)
        self.coke = float(coke)

    def total_price(self):
        milk_num = int(input("how many bottle of milk do you want?: "))
        coke_num = int(input("how many bottle of coke do you want?: "))

        return self.milk * milk_num + self.coke * coke_num
    
if __name__=="__main__":
    milk = 1000
    coke = 1500
    ShoppingCart = PosMachine(milk, coke)
    print(ShoppingCart.total_price())

#Sol_Book

class productPrice:
    milkPrice = 0
    cokePrice = 0

    def __init__(self, milkPrice, cokePrice):
        self.milkPrice = milkPrice
        self.cokePrice = cokePrice
    
    def setMilkPrice(self, milkPrice):
        self.milkPrice = milkPrice
    
    def getMilkPrice(self):
        return self.milkPrice
    
    def setCokePrice(cokePrice):
        self.cokePrice = cokePrice

    def getCokePrice(self):
        return self.cokePrice
    
    def getTotalPrice(self, numOfMilk, numOfCoke):
        return (self.milkPrice * numOfMilk) + (self.cokePrice * numOfCoke)

if __name__=='__main__':
    pp = productPrice(2100, 1500)
    print(pp.getTotalPrice(3, 2))

#5-7 과목 점수를 입출력하고 평균 점수를 계산할 수 있는 메서드를 포함한 클래스를 작성해보세요.
#  과목은 국어, 영어, 수학이 있으며 해당 객체 생성시 기본값을 할당합니다.
#  사용자는 세 과목의 평균 점수를 해당 클래스 메서드를 통해 연산 후 출력합니다.

class ScorePrinter:
    Korean = 0.0
    English = 0.0
    Math = 0.0

    def __init__(self, Korean, English, Math):
        self.Korean = float(Korean)
        self.English = float(English)
        self.Math = float(Math)
    
    def get_KoreanScore(self):
        return self.Korean
    
    def get_EnglishScore(self):
        return self.English
    
    def get_MathSCore(self):
        return self.Math
    
    def print_average(self):
        return (self.Korean + self.English + self.Math)/3
    
if __name__=='__main__':
    MyScore = ScorePrinter(78, 99, 86)
    print(MyScore.get_KoreanScore())
    print(MyScore.print_average())
