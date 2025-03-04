# 클래스를 활용한 메서드 공용 사용

class Calculator:   # 대부분 관례로 클래스는 대문자로 시작함.(객체라는 뜻)
    def __init__(self):   # 생성자(객체가 생성될때 초기값을 결정)
        self.result = 0     # result 변수에 0초기값을 넣음

    def add(self, num):   # add(메서드) 생성, num을 받아 계산 후 리턴
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result

cal1 = Calculator()     # 객체를 생성해서 cal1 변수에 연결
cal2 = Calculator()

user1 = cal1.add(5)
print(user1)
user1 = cal1.add(6)
print(user1)
user1 = cal1.sub(7)
print(user1)
user1 = cal1.mul(8)
print(user1)
user1 = cal1.div(10)
print(user1)

print("="*10)

user2 = cal2.add(10)
print(user2)
user2 = cal2.add(20)
print(user2)
user2 = cal2.sub(5)
print(user2)
user2 = cal2.mul(4)
print(user2)
user2 = cal2.div(2)
print(user2)

class FourCal :

    def __init__(self, first, second):
        self.first = first
        self.second = second

    # first, second와 같은 초깃값을 설정해야 할 필요가 있을 때는
    # setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다
    # 생성자를 구현하는 것이 안전한 방법이다. (객체가 생성될 때 자동으로 호출되는 메서드)

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
b = FourCal(3,8)
#a.setdata(4,2)
print(a.first, a.second)

#a.setdata(4,2)
#b.setdata(3,8)
print(a.first, b.first)

print(a.add(),b.add())
print(a.sub(),b.sub())
print(a.mul(),b.mul())
print(a.div(),b.div())

print("="*10)

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):  # 메서드 오버라이딩
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return "0으로 나눌 수 없음!"
        else:
            return self.first / self.second

a = MoreFourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())

a = MoreFourCal(4, 0)

print(a.div())

print("="*10)

class Family:
     lastname = "김"

print(Family.lastname)
a = Family()
b = Family()
print(a.lastname, b.lastname)
Family.lastname = "박"
print(a.lastname, b.lastname)
# 클래스변수는 객체변수와 달리 클래스로 만든 모든 객체에 공유된다는 특징이 있다.
a.lastname = "최"
print(a.lastname, b.lastname)