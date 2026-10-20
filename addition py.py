import random
numsize = int(input("1st list size: "))
numsize2 = int(input("2nd list size: "))

numbers = [] 
for i in range(numsize):
    num = random.randint(1,9)
    numbers.append(num)
print (numbers)
numbers2 = []
for i in range(numsize2):
    num = random.randint(1,9)
    numbers2.append(num)
print (numbers2)
resu = ''
length = len(numbers)
length2 = len(numbers2)
if length > length2:
    w = 1
if length2 > length:
    w = 2
if length == length2:
    w = 0
if w == 1:
    while length2 < length:
       numbers2 = [0] + numbers2
       length2 += 1
if w == 2:
    while length < length2:
       numbers = [0] + numbers
       length += 1

c = length - 1
add = 0
while c > -1:
    num = numbers[c] + numbers2[c] + add
    add = 0
    if num > 10:
         num -= 10
         add += 1
   
    resu = str(num) + resu
    c -= 1

print (resu)