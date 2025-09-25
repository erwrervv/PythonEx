#亂數產生器
# import random                 #載入random模組
# random.seed()       #初始化隨機數，若()內設定數字，無論隨機幾次都會產生固定結果
# r = random.random()  #隨機產生0-1(不含1)的浮點數
# print(r)
# r = random.uniform(1, 50)     #隨機產生1-50的浮點數
# print(r)
# r = random.randint(1,50)      #隨機產生1-50的整數
# print(r)
# r = random.randrange(1,50,2)  #隨機產生1-49的整數(奇數)
# print(r)
# r = random.choice([5,8,7,4,66,33,99,45])
# print(r)         #從串列中隨機產生1個數字
# r = random.choices([5,8,7,4,66,33,99,45],k=4)
# print(r)         #從串列中隨機產生指定個數數字(會重複)
# r = random.sample([5,8,7,4,66,33,99,45],k=4)
# print(r)         #從串列中隨機產生指定個數數字(不重複)

# import random as RNumber
# for i in range(1,11):
#     rnd = RNumber.randint(1,50)
#     print(f"{rnd}",end=" ")

# import random as rnd
# i=0
# while i<10:
#     RNumber = rnd.randint(1,50)
#     i+=1
#     print(f"{RNumber:2}",end=" ")

#from random import randint 
#只載入 randint 可以減少記憶體使用

# import random
# even =0 #計數器
# odd =0
# i=0
# while i < 11:
#     randNum = random.randint(1,100)
#     print(f"{randNum}",end=" ")
#     if randNum %2 ==0:
#         even +=1
#     else:
#         odd +=1
#     i+=1
# print()
# print(f"even={even} | odd:{odd}")

# import random
# time3 =0
# time5 =0
# time7 =0
# i=0
# others =0
# while i<11:
#     isDivisible = False 
#     randomNumber =  random.randint(1,100)
#     if randomNumber%3==0:
#         time3+=1
#         isDivisible = True
#         print(f"{randomNumber:6}",end="｜")
#     if randomNumber%5==0:
#         time5+=1
#         isDivisible = True
#         print(f"{randomNumber:6}",end="｜")
#     if randomNumber%7==0:
#         time7+=1
#         isDivisible = True
#         print(f"{randomNumber:6}",end="｜")
#     if isDivisible != True:
#         print(f"{randomNumber:3}(x)", end="｜")
#         others+=1
#     i+=1
# print()
# print(f"3的倍數{time3},5的倍數{time5},7的倍數{time7},都不是{others}")


# #修正後版本（每次印一個不重複的數字，共 10 組）：
# import random

# time3 = 0
# time5 = 0
# time7 = 0
# others = 0
# i = 0

# while i < 10:
#     randomNumber = random.randint(1, 100)
#     label = []  # 用來記錄倍數類別

#     if randomNumber % 3 == 0:
#         time3 += 1
#         label.append("3")
#     if randomNumber % 5 == 0:
#         time5 += 1
#         label.append("5")
#     if randomNumber % 7 == 0:
#         time7 += 1
#         label.append("7")

#     if not label:
#         label_str = "(x)"
#         others += 1
#     else:
#         label_str = f"({'/'.join(label)})"

#     print(f"{randomNumber:3} {label_str}", end="｜")
#     i += 1

# print()
# print(f"3的倍數: {time3}, 5的倍數: {time5}, 7的倍數: {time7}, 都不是: {others}")

# #一次產生 10 個不重複的 1~100 整數
# import random

# unique_numbers = random.sample(range(1, 101), 10)
# print(unique_numbers)

# #修正版（使用 random.sample()，保證不重複的隨機數）
# import random

# time3 = 0
# time5 = 0
# time7 = 0
# others = 0
# unique_numbers = random.sample(range(1, 101), 10)

# for randomNumber in unique_numbers:
#     label = []

#     if randomNumber % 3 == 0:
#         time3 += 1
#         label.append("3")
#     if randomNumber % 5 == 0:
#         time5 += 1
#         label.append("5")
#     if randomNumber % 7 == 0:
#         time7 += 1
#         label.append("7")

#     if not label:
#         label_str = "(x)"
#         others += 1
#     else:
#         label_str = f"({'/'.join(label)})"

#     print(f"{randomNumber:3} {label_str}", end="｜")

# print()
# print(f"3的倍數: {time3}, 5的倍數: {time5}, 7的倍數: {time7}, 都不是: {others}")

# import random
# time35 =0; time37=0; time57=0; time3=0; time5=0; time7=0; other=0; count=0
# i=0

# while i<10:

#     uniqueNumbers = random.sample(range(1, 101), 10)
#     num= uniqueNumbers[i]
#     print(f"{num:4}",end="｜")
#     count+=1
#     if count %10==0:
#         print()#每次產生十個數字到下一行，美觀用
#     if num%3==0 and num%5==0:
#         time35+=1
#     elif num%3==0 and num%7==0:
#         time37+=1
#     elif num%5==0 and num%7==0:
#         time57+=1    
#     elif num%3==0:
#         time3+=1
#     elif num%5==0:
#         time5+=1
#     elif num%7==0:
#         time7+=1
#     else:
#         other+=1
#     print(f"3的倍數{time3}｜5的倍數{time5}｜7的倍數{time7}｜3、5的倍數{time35}｜5、7的倍數{time57}｜37的倍數{time37}｜都不是{other}")
#     i+=1


# 定數迴圈與不定數迴圈
# 當我們對迴圈設定固定執行次數時，稱之為定數迴圈。不定數迴圈，
# 表示事先沒有設定迴圈次數，在執行中讓使用者以其他方式中止迴圈執行。
# 定數迴圈例：產生60個亂數(範圍1 - 49)，每6個一列，排成6 * 10的矩形格式

# import random
# count = 1
# while count <= 10:
#     for i in range(1,7):
#         randNum = random.randint(1,49)
#         print(f"{randNum:3}",end = ' ')
#     print()
#     count += 1
# print('Over')

#####
# import random
# count = 1
# while count <= 10:
#     i=1
#     while i < 8:
#         randNum = random.randint(1,49)
#         print(f"{randNum:3}",end = ' ')
#         i+=1
#     print()
#     count += 1
# print('Over') 
#這程式屬於多重迴圈，外迴圈用while來控制亂數產生的次數，
# 以count便數來控制。在內迴圈控制每次產生幾個亂數，
# 兩個迴圈配合就可以產生10 * 6 共計60個亂數。
# import random
# while True:
#     for i in range(1,7):
#         randNum = random.randint(1,50)
#         print("%3d"%(randNum),end=" ")
#     print()
#     a= print("請輸入1-7數值;0停止")
#     if a == "0":
#         break
# print('Over') 

##
# import random
# n1 = random.randint(1,50)
# n2 = random.randint(1,50)
# ans = n1+n2
# print(f"第一個數字{n1} + 第二個數字{n2}=？")

# your_ans = int(input("輸入總和的答案"))

# while True:
#     if your_ans != ans:
#         print(f"答錯了，{n1} + {n2} 不等於 {your_ans}")
#         print(f"第一個數字{n1} + 第二個數字{n2}=？")
#         your_ans = int(input("輸入總和的答案"))
#     else: 
#         your_ans == ans
#         print(f"答對了")
#         print(f"結束程序")
#         break

# import random
# n1 = random.randint(1,50)
# n2 = random.randint(1,50)
# op=random.choice(["/"])
# print(f"{n1} {op} {n2}為 ",end="")
# if op == "+":
#     ans=n1 + n2
# elif op == "-":
#     ans=n1 - n2
# elif op == "*":
#     ans=n1 * n2
# elif op == "/":
#     if n1 !=0:
#         ans=round(n1 / n2,2) #四捨五入後取2位置
#     else :print("第二個數字為0所以無解")
        
# your_ans = float(input("輸入答案如果有小數點取後二位"))
# while True:
#     if your_ans != ans:
#         print(f"答錯了，{n1} {op} {n2} 不等於 {your_ans}")
#         print(f"{n1} {op} {n2}=？")
#         your_ans = float(input("輸入答案如果有小數點取後二位"))    
#     else: 
#         your_ans == ans
#         print(f"答對了")
#         print(f"結束程序")
#         break

# ### #########
# 練習題
# 1	使用迴圈敘述撰寫程式，讓使用者輸入兩個正整數 a、b (a<b) ，利用迴圈計算從a開始連加到b的總和。例如：輸入a=1、b=100 (1+2+3+…+100)，則輸出結果為5050
# 1.1	輸入說明： 請輸入兩個正整數(a、b且a<b) 輸入範例
# 請輸入第一個正整數66
# 請輸入第二個正整數666
# 1.2	輸出說明： 計算從 a 開始到 b的總和 輸出範例
# 219966

# #Q1
# a= int(input("輸入第一個數字"))
# b= int(input("輸入第二個數字，如果比第一個數字小會當作起始值"))
# if a>b:
#     a,b = b,a
# total =0    
# while a<= b:
#     total +=a
#     # print(total)
#     a+=1
# print(f"{a}加到{b}總和等於", end ="{total}")

# 2	使用迴圈敘述撰寫程式，讓使用者輸入兩個正整數 a、b (a<b) ，利用迴圈計算從a開始連加到b的偶數總和。例如：輸入a=1、b=100 (2+4+6+…+100)，則輸出結果為2550
# 2.1	輸入說明： 請輸入兩個正整數(a、b且a<b) 輸入範例
# 請輸入第一個正整數6
# 請輸入第二個正整數88
# 2.2	輸出說明： 計算從 a 開始到 b的偶數總和 輸出範例
# 1974

# ##Q2
# a= int(input("輸入第一個正數字"))
# b= int(input("輸入第二個正數字，如果比第一個數字小會當作起始值"))
# while True:
#     start = min(a, b)
#     end = max(a, b)
#     current = start
#     if start>0 and end>0:
#         total =0    
#         while current<= end:
#             if current%2==0:
#                 total +=current
#                 # print(total)
#                 current+=1
#             else:current+=1
#         print(f"從 {start} 加到 {end} 的偶數總和為：{total}")
#         print(f"{start}加到{end}總和等於", end =f"{total}")
#         break
#     else:
#         print("輸入值要是正整數")
#         b= int(input("輸入第二個正數字，如果比第一個數字小會當作起始值"))
#         a= int(input("輸入第一個正數字"))

# 3	使用迴圈敘述撰寫程式，讓使用者輸入一個正整數 (<30)然後以三角形方式依序輸出此數階乘結果
# 3.1	輸入說明： 請輸入一個正整數(<30) 輸入範例
# 12
# 3.2	輸出說明： 以三角形方式依序輸出此數階乘結果 輸出範例
#    1
#    2   4
#    3   6   9
#    4   8  12  16
#    5  10  15  20  25
#    6  12  18  24  30  36
#    7  14  21  28  35  42  49
#    8  16  24  32  40  48  56  64
#    9  18  27  36  45  54  63  72  81
#   10  20  30  40  50  60  70  80  90 100
#   11  22  33  44  55  66  77  88  99 110 121
#   12  24  36  48  60  72  84  96 108 120 132 144

# ##Q3

# while True:
#     a = int(input("請輸入一個正整數（小於30）："))
#     if 0 < a < 30:
#         for i in range(1, a + 1):           # 控制列數
#             for j in range(1, i + 1):       # 控制每列的數量
#                 print(f"{i * j:4}", end="")  # 輸出對齊的乘積（寬度 4）
#             print()  # 換行
#         break
#     else:
#         print("輸入錯誤，請輸入一個大於 0 且小於 30 的正整數")

# 4	使用迴圈敘述撰寫程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間(含)所有5的倍數和。
# 4.1	輸入說明： 請輸入一個正整數 輸入範例
# 500
# 4.2	輸出說明： 所有5的倍數和 輸出範例
# 25250

# ##Q4
# a = int(input("請輸入一個正整數計算從1到正整數之間(含)所有5的倍數和"))
# start = a
# total = 0
# current =1
# while current<=start:
#     if current%5==0:
#         total+=current
#     current+=1
# print(f"1到{start}的總合為{total}")

# 5	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數，將此數反轉順序輸出 (利用 % 與 // 處理)
# 5.1	輸入說明： 請輸入一個正整數 輸入範例
# 31283
# 5.2	輸出說明： 將數值反順序輸出 輸出範例
# 38213

# a= int(input("輸入一個正整數後會反轉印出"))
# start = a
# current =1
# while start!=0:
#     new = start%10
#     start = start//10
#     print(f"{new}",end="")


#############
# # 練習題
# # 	撰寫一個程式，由使用者輸入10個數字，然後找出最小值並且輸出
# ####
# times=0
# new_min_number = 99999999
# while True:
#     while times !=10:
#         min_number = int(input("輸入一個數字總共輸入十個字"))
#         if  min_number < new_min_number:
#             new_min_number = min_number
#             times+=1
#             print(f"最小值目前是{new_min_number},第幾次：{times}")
#         else: 
#             times+=1
#             print(f"最小值目前是{new_min_number},第幾次：{times}")
#     break
        

    

####
# # 	撰寫一個程式，由使用者輸入數字，輸入的動作直到輸入值為9999結束，然後找出其最小值並且輸出。
# # ####
# min_number = None  # 初始設為 None，表示尚未輸入任何數

# while True:
#     num = int(input("請輸入一個數字（輸入 9999 結束）："))
    
#     if num == 9999:
#         break  # 結束輸入
    
#     if min_number is None or num < min_number:
#         min_number = num  # 更新最小值

# if min_number is not None:
#     print(f"最小值是：{min_number}")
# else:
#     print("你沒有輸入任何有效的數字。")
####

# 	撰寫一個程式：
# 	由使用者輸入兩個正整數a、b (a<b)
# 	輸出從a到b(包含a 、b)之間4或9的倍數(一列輸出10個數字，欄寬為4、靠左對齊)。
# 	輸出4或9的倍數共有幾個數。
# 	輸出4或9的倍數加總和。
#######
# a = int(input("請輸入第一個正整數 a（a < b）："))
# b = int(input("請輸入第二個正整數 b："))

# # 確保 a < b
# if a>b:
#     a,b=b,a
# else:
#     count = 0     # 符合條件的數量
#     total = 0     # 總和
#     line_count = 0  # 每列10個用的計數器

#     for i in range(a, b + 1):
#         if i % 4 == 0 or i % 9 == 0:
#             print(f"{i:<4}", end="")  # 欄寬4，靠左對齊
#             count += 1
#             total += i
#             line_count += 1
#             if line_count == 10:
#                 print()
#                 line_count = 0

#     # 如果最後一行未滿10個，手動換行
#     if line_count != 0:
#         print()

#     print(f"\n符合條件的數字共有：{count} 個")
#     print(f"這些數字的總和為：{total}")
####
# 	撰寫一個程式：
# 	輸入一個正整數。
# 	將這個正整數以反轉的順序輸出。
# 	若輸入值為0，就輸出0

# a= int(input("輸入一個正整數後會反轉印出"))
# start = a
# current =1
# if start==0:
#     print("0")
# else:
#     while start!=0:
#         new = start%10
#         start = start//10
#         print(f"{new}",end="")

# # 	撰寫一個程式：
# # 	輸入代表成績的正整數。
# # 	根據分數與等級對照表，印出對應的等級。
# # 	輸入9999結束迴圈

# while True:
#     a= int(input("請輸入你的成績，輸入9999為停止輸入"))
#     if 101>a>=90:
#         print(f"你的成績{a}是A")
#     elif 90>a>=80:
#         print(f"你的成績{a}是B")
#     elif 80>a>=70:
#         print(f"你的成績{a}是C")
#     elif 70>a>=60:
#         print(f"你的成績{a}是D")
#     elif 60>a>=0:
#         print(f"你的成績{a}是E")
#     elif a==9999:
#         print("程序結束")
#         break
#     else:
#         print(f"你的成績輸入不在100到0之間")
        
        
    
# 分數	等級
# 90 ~ 100	A
# 80 ~ 89	B
# 70 ~ 79	C
# 60 ~ 69	D
# 0 ~ 59	E



# 	撰寫一個程式：
# 	以迴圈方式，提供使用者反覆輸入身高與體重，直到輸入9999結束。
# 	計算出BMI值，並列印出相對應的意義。
# 	輸出到小數點後第二位。
# BMI公式： BMI = 體重(公斤) / 〖身高〗^2(〖公尺〗^2)
# while True:
#     a = float(input("請輸入你的體重 (公斤)，若輸入 9999 則結束："))
#     if a == 9999:
#         print("程序結束")
#         break
#     b = float(input("請輸入你的身高 (公分)："))
#     if b <= 0 or a <= 0:
#         print("❗ 體重和身高必須是正數，請重新輸入")
#         continue

#     b = b * 0.01  # 轉換成公尺
#     BMI = a / (b ** 2)

#     print(f"你的 BMI 是 {BMI:.2f}")

#     if BMI > 30:
#         print("➡️ 肥胖")
#     elif BMI >= 25:
#         print("➡️ 過重")
#     elif BMI >= 18.5:
#         print("➡️ 適中")
#     else:
#         print("➡️ 過輕")

# BMI	說明
# < 18.5	過輕
# 18.5 - 24.9	正常
# 25.0 - 29.9	過重
# > 30	肥胖

# 	撰寫一個程式：
# 	以迴圈方式，提供使用者反覆輸入西元年分，直到輸入9999結束。
# 	判斷輸入年份是否為閏年。判斷規則為，每4年一閏，100年不閏，但400年也一閏
# while True:
#     a= int(input("輸入一個年份，輸入9999結束"))
#     if a ==9999:
#         print("程序結束")
#         break
#     else:
#         if (a%4==0 and a%100!=100) or a%400 == 0:
#             print(f"{a}是閏年")
#         else:print(f"{a}不是閏年")

# # 	撰寫一個程式：
# # 	輸入兩個西元年分，顯示兩個西元年分之間所有閏年。
# # 	每一列輸出10筆資料，並且對齊

# a=int(input("輸入第一個年份"))
# b=int(input("輸入第二個年份"))

# start = min(a,b)
# end = max(a,b)
# count=0
# while start<=end:            
#     if (start%4==0 and start%100!=0) or (start%400 == 0):
#         print(f"{start:>6}是閏年", end=" ")
#         count+=1
#         if count==10:
#             print()
#             count=0
#     start+=1
# if count !=0:
#     print()

# a = int(input("輸入第一個年份："))
# b = int(input("輸入第二個年份："))

# start = min(a, b)
# end = max(a, b)
# count = 0

# while start <= end:
#     if (start % 4 == 0 and start % 100 != 0) or (start % 400 == 0):
#         print(f"{start:<6}", end="")
#         count += 1
#         if count == 10:
#             print()
#             count = 0
#     start += 1  
# if count != 0:
#     print()

# # 	輸入3個正整數 a、b、c然後求出最大公因數

# a = int(input("請輸入第一個數字求最大公因數"))
# b = int(input("請輸入第二個數字求最大公因數"))
# c = int(input("請輸入第三個數字求最大公因數"))

# gcd = min(a, b, c)  # 最大公因數不可能超過最小的那個數

# while gcd > 0:
#     if a % gcd == 0 and b % gcd == 0 and c % gcd == 0:
#         print(f"最大公因數為：{gcd}")
#         break
#     gcd -= 1

# 	完美數：一個數如果恰好等於它的因數(不含數字本身)之和，這個數就稱為[完美數]。請使用 for 迴圈設計一程式，輸入一個值，找出這個值以內的所有完美數，執行結果如範例。
# 執行結果
# # 請輸入一個數： 1000
# # 1 ~ 1000 完美數有: 6  28  496  
# a = int(input("請輸入一個最大範圍找到所有完美數："))

# #######
# a = int(input("請輸入一個最大範圍找到所有完美數："))
# print(f"1~{a}的完美數有: ",end="")
# for i in range(2,a+1):
#     divisor_sum =0
#     for j in range (1,i):
#         if i % j ==0:
#             divisor_sum+= j
#     if divisor_sum == i :
#         print(f"{i}",end="  ")

# ## 樂透
# #1,49 選六個隨機號，你輸入六次數字後對照
# import random
# while True:
#     number_your = []
#     for i in range(1, 7):
#         num = int(input(f"輸入第{i}個數字（1~49）：(9999是停止)"))
#         if num == 9999:
#             print("🎉 感謝使用，遊戲結束！")
#             exit()  # 直接結束整個程式        
#         while num < 1 or num > 49 or num in number_your:
#             num = int(input("請重新輸入不重複、1~49 的數字："))
#         number_your.append(num)

#     # 隨機產生樂透號碼（不重複）
#     lotto = random.sample(range(1, 50), k=6)

#     # 顯示雙方號碼
#     print("\n🎯 你的號碼：", sorted(number_your))
#     print("💰 樂透號碼：", sorted(lotto))

#     # 對中幾個
#     match = [num for num in number_your if num in lotto]
#     print(f"\n✅ 你對中了 {len(match)} 個號碼：{sorted(match)}" if match else "\n❌ 沒有中獎，再接再厲！")

# ## 猜拳
# import random
# num1="拳頭"
# num2="剪刀"
# num3="布"
# while True:
#     a= int(input("輸入數字：1(拳頭)、2(剪刀)、3(布)"))
#     ccb = random.choice([1,2,3])
#     if ccb == 1:
#         if a== 1:      
#             print("電腦出拳頭，你出拳頭平手")
#         elif a== 2:
#             print("電腦出拳頭，你出剪刀輸了")
#         elif a== 3:
#             print("電腦出拳頭，你出布贏了")
#         else:print("你必須輸入1~3的數字")
#     elif ccb == 2:  
#         if a== 1:      
#             print("電腦出剪刀，你出拳頭贏了")
#         elif a== 2:
#             print("電腦出剪刀，你出剪刀平手")
#         elif a== 3:
#             print("電腦出剪刀，你出布輸了")
#         else:print("你必須輸入1~3的數字")   
#     elif ccb == 3:  
#         if a== 1:      
#             print("電腦出布，你出拳頭輸了")
#         elif a== 2:
#             print("電腦出布，你出剪刀贏了")
#         elif a== 3:
#             print("電腦出布，你出布平手")
#         else:print("你必須輸入1~3的數字")

# import random

# choices = {1: "拳頭", 2: "剪刀", 3: "布"}
# # print(choices[2])
# while True:
#     try:
#         a = int(input("請輸入數字：1(拳頭)、2(剪刀)、3(布)，輸入 0 結束遊戲： "))
#         if a == 0:
#             print("遊戲結束，感謝遊玩！👋")
#             break
#         if a not in [1, 2, 3]:
#             print("⚠️ 請輸入有效的數字（1~3）")
#             continue

#         computer = random.choice([1, 2, 3])
#         print(f"你出：{choices[a]}，電腦出：{choices[computer]}")

#         if a == computer:
#             print("🤝 平手！")
#         elif (a == 1 and computer == 2) or (a == 2 and computer == 3) or (a == 3 and computer == 1):
#             print("🎉 你贏了！")
#         else:
#             print("😢 你輸了！")
#     except ValueError:
#         print("⚠️ 請輸入數字！")

import random

while True:
    try:
        a = int(input("輸入比0大並低於50的數字\n或輸入0以下的整數結束遊戲："))
        if a<=0:             
            print("遊戲結束，謝謝遊玩！")
            break
        elif a> 50:
            print("輸入錯誤")
            continue
        # 讓使用者輸入 b，直到輸入正確
        while True:
            b = int(input("輸入1選擇比大小押注，收益2倍點數\n輸入2選擇猜點數，猜中得到10倍點數："))
            if b in [1, 2]:
                break
            else:
                print("請輸入有效的選項（1 或 2）")

        ran_number = random.randint(1, 50)

        print(f"押注：{a}，隨機號碼：{ran_number}")

        if b == 1:
            if a > ran_number:
                pizz = a * 2
                print(f"恭喜！你贏了！獎金：{pizz}")
            else:
                print("很遺憾，沒中獎")
        elif b == 2:
            if a == ran_number:
                pizz = a * 10
                print(f"恭喜！你猜中了！獎金：{pizz}")
            else:
                print("很遺憾，沒猜中")

    except ValueError:
        print("請輸入有效的整數！")