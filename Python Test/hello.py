a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
import math
delta = (b**2) - (4*a*c)
if a == 0:
    print("Vì là phương trình bậc nhất nên sẽ có nghiệm x =",-c/b)
elif delta < 0:
    print("Phương trình có hai nghiệm phức như sau:")
    print("Nghiệm thứ nhất x1 =",-b+(math.sqrt(abs(delta)))/2*a)
    print("Nghiệm thứ nhất x2 =",-b-(math.sqrt(abs(delta)))/2*a)

elif delta == 0 :
    print("Phương trình có 1 nghiệm duy nhất là x =",-b/2*a)
else:
    print("Phương trình có 2 nghiệm phân biệt như sau:")
    print("Nghiệm thứ nhất x1 =",(-b+math.sqrt(delta))/2*a)
    print("Nghiệm thứ hai x2 =",(-b-math.sqrt(delta))/2*a)