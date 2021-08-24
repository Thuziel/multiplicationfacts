#imports
import random

#vars
numbers = "123456789"

totalAsk = input("How many questions do you want to answer: ")
total = int(totalAsk)
correct = 0

#logic
for i in range(0, total):
    num1 = random.randint(0, len(numbers)-1)
    num11 = int(numbers[num1])

    num2 = random.randint(0, len(numbers)-1)
    num22 = int(numbers[num2])

    q = str(num11) + "*" + str(num22) + "="
    a = input(q)

    if num11*num22 == int(a):
        print("correct")
        correct += 1
    else:
        print("wrong")

percent = str(correct)+"/"+str(total)
print(percent)

