# bill = int(input("금액을 입력하세요(카드전용)"))
# menu = {"콜라":800, "마운틴 듀":700, "스프라이트":500, "Dr페퍼":400}
# change = 0
# change = bill
# while True:
#     num = 0
#     for key,value in menu.items():
#         num += 1
#         if value < change:
#             print(num, key, value)
#         else:
#             print(num, key,"잔액부족")
#     while True:
#         choice_menu = int(input("메뉴를 고르시오(번호)"))
#         if str(choice_menu).isdigit() is True:
#             choice_menu = int(choice_menu)
#             break
#         else:
#             p rint("숫자만 입력하시오")
#         if choice_menu > 4:
#             print("판매하지 않는 음료입니다.")
#         else:
#             break
#
#     if choice_menu == 1:
#         if change <= menu["콜라"]:
#             print("잔액부족, 구매불가")
#         else:
#             change = change - menu["콜라"]
#     elif choice_menu == 2:
#         if change <= menu["마운틴 듀"]:
#             print("잔액부족")
#         else:
#             change = change - menu["콜라"]
#     elif choice_menu == 3:
#         change = change - menu["콜라"]
#     elif choice_menu == 4:
#         change = change - menu["콜라"]
#     print("남은 금액은 ", change, "원")
#     if change < 400:
#         break
import time
import tkinter
import turtle

# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# t.speed(0)
# t.penup()
# t.setposition(-300,300)
# t.pendown()
# t.begin_fill()
# t.fillcolor("yellow")
#
# for j in range(6):
#     if j% 2 == 0:
#         for i in range(6):
#             if i % 2 == 1:
#                 t.begin_fill()
#                 t.fillcolor("yellow")
#                 for i in range(4):
#                     t.forward(100)
#                     t.right(90)
#                 t.end_fill()
#             else:
#                 for i in range(4):
#                     t.forward(100)
#                     t.right(90)
#             t.forwari ind(100)
#     else:
#         for i in range(6):
#             if i % 2 == 1:
#                 for  range(4):
#                     t.forward(100)
#                     t.right(90)
#             else:
#                 t.begin_fill()
#                 t.fillcolor("yellow")
#                 for i in range(4):
#                     t.forward(100)
#                     t.right(90)
#                 t.end_fill()
#             t.forward(100)
#
#     t.penup()
#     t.setposition(-300,t.ycor()-100)
#     t.pendown()
#
# s.mainloop()


# a = "12345678"
#
# for i in a:
#     if i == "3":
#         print("짝",end="")
#     else:
#         print(i,end="")

# a = "123456789"
# for i in a:
#     if i == "3:" or i == "6" or i == "9":
#         print("짝")
#     else:
#         print(i)


# for i in range(1,101):
#     if i == 3:
#         print("짝")
#     else:
#         print(i)
# num = int(input("숫자입력"))
# for i in range(1,(num*2)+1):
#     if i % num == 0:
#         print(i)
#     else:
#         print(i,end=" ")




# a = input("입력하시오")
# print("20"+a[0:2]+"년")
# print(a[2:4]+"월")
# print(a[4:6]+"일")

# w1,w2 = input(",로 구분하여 입력하시오").split()
# s = w1 + w2
# print(s)


# a,b,c = input(",로 구분하여 입력하시오").split(",")
# list = [a,b,c]
# for i in list:
#     if int(i)%2==0:
#         print("짝")
#     else:
#         print("홀")
# while True:
#     a = input("숫자입력")
#     if a == "q":
#         break
#     print(a)
# a = input("sec..")
# f_button = 0
# s_button = 0
# t_button = 0
#     f_button = int(a) // 60
#     if int(a) % 60 > 0:
#         s_button = (int(a)%60)//30
#         if (int(a)%60)//30
# if int(a)%60 > 0:
#     if a%60:
#         f_button = int(a)//60
#         if a

# n = int(input())
# n = input("입력")
# c =
# while True:
#     s+=c
#     c+=1
#     of s>=n:
#     break
# print(s)
# a = [85.6,79.5,83.1,80.0,78.2,75.0]
# b,c = input("입력")
# print(int(b)+int(c))
# a = -1
# b = 100
# print(a,"\n", b)
# a = 55
# b = 10
# c = 2008
# d = 1999
# print(a,"-",b,"=",int(a)-int(b))
# print(c,"-",d,"=",int(c)-int(d))
# a = 49
# b = 0.2683
# print(a, "x" ,b,"=",a*b)
# a = input("입력")
# print("school?",a)
#a = input("입력")
# b = input("입력")
# print("Number 1?", a)
# print("Number 2?", b)
# a = input("가로 입력")
# b = input("세로 입력")
# print("Garo",":",a)
# print("Sero",":",b)
# print("hello.","I","love")
# print("studying","computer")
# print("very","much.")
# print("10","+","20","=","30")
# a = 80.5
# b = 22.34
# print(a,b,a+b)
# def convert_int(a):
#     print(a.replace('.',""))
# convert_int(("1.234.567"))


# a = ([3,4,5,6,7,8])
# r_a= []
# def pickup_even(a):
#     for i in a:
#         if i % 2  == 0:
#             r_a.append(i)
# pickup_even(a)
# print(r_a)
# a = "abcd"
# def make_list(a):
#     return print(a)
# print(make_list(a))
# print_score([1,2,3])
# def print_scoreㅁ

# import turtle
# import time
# s = turtle.Screen()
# t = turtle.Turtle()
# t1 = turtle.Turtle()
#
# t1.shape("turtle")
# t1.shapesize(4)
# t1.penup()
# t1.speed()
#
# t.penup()
# t.setposition(-150,150)
# t.pendown()
# t.hideturtle()
# write = turtle.Turtle()
# for i in range(4):
#     t.forward(300)
#     t.right(90)
# write.penup()
# write.setposition(-75,75)
# write.pendown()
# for i in range(1,11):
#     write.write(1,font=("굴림체",120,"bold"), align="center")
#     time.sleep(1)
#     wrtie.clear()
# t2 = turtle.Turtle()
# t2.shape("turtle")
# t2.shapesize(4)
# t2.penup()
# t2.speed(0)
# t2.color("red")
# t2.setposition(0,-100)
#
# s.tracer(0)
# while True:
#     t1.forward(1)
#     t2.forward(1)
#     s.update()
# import turtle
# import time
# s = turtle.Screen()
# t = turtle.Turtle()
# circle = turtle.Turtle()
# circle.penup()
# circle.setposition(0,-200)
# circle.pendown()
# circle.circle(200)
# circle.hideturtle()
# circle.penup()
# circle.setposition(0,0)
# circle.setheading(90)
# grid = 90
# number = 0
# for i in range(5):
#     circle.forward(180)
#     circle.pendown()
#     circle.forward(20)
#     circle.penup()
#     circle.forward(10)
#     circle.awrite()
#     circle.setposition(0,0)
#     circle.setheading(grid)
#     grid -= 90
#
# t.hideturtle()
# s.tracer(0)
# dig = 90
# while True:
#     t.setheading(dig)
#     t.forward(170)
#     t.clear()
#     t.backward(170)
#     dig -= 1
#     s.update()
#     time.sleep(1)
#
#
# s.mainloop()


# a = input("입력")
# for i in range(int(a)):
#     for j in range(i+1):
#         print('*',end="")
#     print('')


# for i in range(6):
#     if i >= 4:
#         print(i*"*")
#     elif i == 3:
#         print(3*"*")
#         print(3*"*")
#     else:
#         print((6-i)*"*")

# sum = 0
# while True:
#     a = input("입력")
#     if int(a) == 0:
#         print(sum)
#         break
#     if int(a) % 2 != 0:
#         sum += int(a)


# a = "을(를) 선택"
# b = input("입력")
# if int(b) == 1:
#     print("입력"+a)
# if int(b) == 2:
#     print("출력"+a)
# if int(b) == 3:
#     print("삭제"+a)
# if int(b) == 4:
#     print("끝내기"+a)


# sum = 0
# while True:
#         a = input("입력")
# import random
# com_num = random.randint(1,50)
# count = 0
# while True:
#         user_num = int(input("숫자입력"))
#         count += 1
#         print(user_num)
#         if com_num > user_num:
#                 print("up")
#         elif com_num < user_num:
#                 print("down")
#         else:
#                 print("시도횟수",count,"정답")
#                 break
#         if up_or_down == "up":

# from random import *  # 랜덤 모듈 import
#
# words = ["zelda", "maplestory", "darksoul","minecraft"]  # 리스트에 영어 단어 후보를 나열
# word = choice(words)  # 랜덤으로 단어 중 1개를 선택
# print("answer : " + word)  # 참고용으로 정답 출력 (실제 게임에서는 지우기)
# letters = ""  # 플레이어가 지금까지 입력한 알파벳들 저장
#
# # 정답을 맞힐 때까지 무한 반복
# while True:
#         succeed = True  # 성공 여부 확인 변수
#         print()
#         for w in word:  # 제시 단어를 알파벳별로 한 글자씩 비교
#                 if w in letters:  # 현재 알파벳이 플레이어가 입력한 값들 중에 있으면
#                         print(w, end=" ")  # 그 알파벳을 표시
#                 else:  # 입력한 값들 중에 없으면
#                         print("_", end=" ")  # 밑줄을 표시
#                         succeed = False  # 밑줄이 있다는 것은 아직 다 풀지 못했음을 의미 !
#         print()
#
#         if succeed:  # 만약 성공했다면 게임 종료
#                 print("Success")
#                 break
#
#         letter = input("Input letter > ")  # 플레이어로부터 한 글자씩 입력
#         if letter not in letters:  # 입력값 중에 포함되어 있지 않다면
#                 letters += letter  # 새로 입력받은 글자를 입력값에 추가
#
#         if letter in word:  # 입력한 글자가 제시 단어에 포함되었다면
#                 print("Correct")
#         else:  # 포함되어있지 않다면
#                 print("Wrong")
# import random
# a = random.randint(0,9)
# b = random.randint(0,9)
# c = random.randint(0,9)
# d = random.randint(0,9)
# e = str(a)+str(b)+str(c)+str(d)
# for j in range(4):
#         count = 0
#         for i in range(10):
#                 count += 1
#                 if i == int(e[j]):
#                         print(i)
#                         break
# print(count,"번")
# import random
# count = 0
# for i in range(10):
#         a = random.randint(0,1000)
#         if a % 2 == 0:
#                 count += 1
# print(int((count/10)*100),"%")
# import random
# count = 0
# a = input("입력")
# b = input("입력")
# r = random.randint(int(a),int(b)+1)
# if r % 2 == 0:
#         count += 1
# print(int((count/10)*100),"%")
# a = input("입력")
# a = a.split(" ")
# for i in range(len(a) -1,-1,-1):
#         print(a[i],end = " ")
# a = ("i am a boy boy")
# a = a.split(" ")
# count = 0
# for i in range(len(a)):
#         if a[i] == "boy":
#                 count += 1
# print("boy의 갯수는", count)
# import turtle
# import random
# t = turtle.Turtle()
# s = turtle.Screen()
#
# numbers = []
# for i in range(1,37):
#         numbers.append(i)
# random.shuffle(numbers)
# number = 0
# x = -200
# y = 200
# t.penup()
# for j in range(6):
#         for i in range(6):
#                 t.setposition(x,y)
#                 t.write(numbers[number], font=("Arial", 30, "normal"))
#                 x += 50
#         x = -200
#         y -= 50
# s.mainloop()
# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# while True:
#         s.tracer(0)
#         for i in range(4):
#                 t.forward(100)
#                 t.right(90)
#         s.tracer(1)
#         t.forward(50)
#         t.clear()
#         s.update()
# s.mainloop()
# for i in range(6):
#     for j in range(i+1):
#         print('*',end="")
#     print('')
# star = 6
# star = star+1
# for i in range(1, star):
#     print((' '*(star-i))+'*'*i)
# star = 6
# star = star+1
# for i in range(1,star):
#     print((' '*(star-i))+'*'*i)

# for i in range(6,-1,-1):
#     print(" "*i+"*"*(6-i))

# import turtl        te
# import time
# import random
# t = turtle.Turtle()
# s = turtle.Screen()
#
# word_list = ["5 x 8","4 x 7","5 x 7","7 x 9","11 x 11"]
# go = s.textinput("입력","진행하려면 progress 클릭")
# random.randint()
# t.hideturtle()
# count = 0
# start = time.time()
# for i in range(5):
#     t.write(word_list[i], font=("A큐브", 50, "bold"))
#     time.sleep(3)
#     t.clear()
#     answer = s.textinput("입력", "단어를 입력하시오")
#     if answer == word_list[i]:
# .write("정답",font = ("a큐브",30,"bold"))
#         count += 1
#     else:
#         t.write("노답",font = ("a큐브",30,"bold"))
#     time.sleep(2)
#     t.clear()
# end = time.time()
# total = end - start
#
# t.write(str(count)+"개"+"걸린시간은"+str(total), font=("a큐브", 30, "bold"))
#
# s.mainloop()
# a = [100,200,300,400,500]
# a.remove(400)
# a.remove(500)
# print(a)
# a = [200,100,300]
# a.insert(2,10000)
# print(a)
# a = [100,200,300]
# print(type(1))
# a = ('AAABBBcccddd')
# print(a.lower('AAABBB')a.upper('cccddd'))
# a = 10
# b = 2
# for i in range(1,5,2):
    #     a += 1
# print(a+b)]
# for i in range(5,-1,-1):
#     print(" " * 5 + "*" * 1)
# count = 0
# for i in range(1,101):
#     if i%3 == 0:
#         count += 1
#     elif i%5 == 0:
# a = input("입력하시오")
# print(a[len(a)-1: : -1])
# a = int(input("입력하시오"))
# for i in range(1,)
#     b= 0
# if a%
# a_list = []
# for i in range(10):
#     a_list.append(int(input("입력")))
# print(min.a_list,max.a_list)
# for i in range(1,101):
#     print(i,end=" ")
# for i in range(2002,2051,4):
# print(i)
# for i in range(3,31,3):
#     print(i)
# for i in range(100,-1,-1):
#     print(i)
# for i in range(1,10):
#     print(str(0)+'.'+str(i)) hor
# a = 3
# for i in range(3,28,3):
#     for j in range(1,10):
#         print(str(a)+'x'+str(j),'=',str(i))
# list_a = [1,3,5,7,9]
# list_b = [3,9,15,21,27]
# a = 3
# print(str(a)+'x'+list_a,'=',list_b)
# from keras.models import load_model  # TensorFlow is required for Keras to work
# import cv2  # Install opencv-python
# import numpy as np
#
# # Disable scientific notation for clarity
# np.set_printoptions(suppress=True)
#
# # Load the model
# model = load_model("keras_Model.h5", compile=False)
#
# # Load the labels
# class_names = open("labels.txt", "r").readlines()
#
# # CAMERA can be 0 or 1 based on default camera of your computer
# camera = cv2.VideoCapture(0)
#
# while True:
#     # Grab the webcamera's image.
#     ret, image = camera.read()
#
#     # Resize the raw image into (224-height,224-width) pixels
#     image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
#
#     # Show the image in a window
#     cv2.imshow("Webcam Image", image)
#
#     # Make the image a numpy array and reshape it to the models input shape.
#     image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
#
#     # Normalize the image array
#     image = (image / 127.5) - 1
#
#     # Predicts the model
#     prediction = model.predict(image)
#     index = np.argmax(prediction)
#     class_name = class_names[index]
#     confidence_score = prediction[0][index]
#
#     # Print prediction and confidence score
#     print("Class:", class_name[2:], end="")
#     print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
#
#     # Listen to the keyboard for presses.
#     keyboard_input = cv2.waitKey(1)
#
#     # 27 is the ASCII for the esc key on your keyboard.
#     if keyboard_input == 27:
#         break


#Tlqkf ehfdkrkdigksek roTlqkfd RHr ehfdkrksek
# camera.release()
# cv2.destroyAllWindows()
# import sys
# print(sys.version)