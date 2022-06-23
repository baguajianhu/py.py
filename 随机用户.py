import random
number = 23
running = True
counts = 0
while running and counts < 3:
     guess = int(input("猜我输入了哪个数字？这个数的范围在1到100之间:"))
     if guess == number:
         print("恭喜你，猜对了")
         running = False
     elif guess > number:
         print("猜的太大了")

     elif guess < number:
         print("猜的太小了")
     counts +=1

else:
    print("游戏结束")

