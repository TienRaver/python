# List goc
number = [1,2,3,4,5,6,7,8,9]

# Tao list moi bang binh phuong x^2 list cu
# Cach 1: dung append
new_number1 = []
import math
for i in number:
    new_number1.append(int(math.pow(i,2)))
print(new_number1)

# Cach 2: dung list comprehension
import math
new_number2 = [int(math.pow(i,2)) for i in number if i%2==0]




print(new_number2)
