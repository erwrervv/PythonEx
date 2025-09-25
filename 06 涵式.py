# def 涵式名稱 ():
# 	a=input("輸入一個數字")
# 	print('定義涵式')
# 涵式名稱 () 

# print('呼叫')
# def functionA (a,b):
#     for i in range (a):
#         (print('*',end=''))
#     print()

#     # for i in range (a,b):
#     #     print('*',end='')
#     # print()
# functionA(20,1)
# functionA(20,30)

# def FtoC():
#     F = eval(input("請輸入一個要轉換的華氏溫度"))
#     C = (F-32)*5/9
#     print(f"攝氏度為：{C:.2f}")
#     if C < 10 : 
#         print("多穿衣服，溫度偏低")
#     if C >= 20 : 
#         print("注意防曬，溫度偏高")
# FtoC()


# def FtoC(F):
#     C = (F - 32) * 5 / 9
#     print(f"攝氏度為：{C:.2f}")
#     if C < 10:
#         print("多穿衣服，溫度偏低")
#     if C >= 20:
#         print("注意防曬，溫度偏高")
#     fd(C)
# def fc():
#     try:
#         F = float(input("請輸入一個要轉換的華氏溫度："))
#         FtoC(F)
#     except ValueError:
#         print("請輸入有效的數字")

# def fd(C):
#     print(f"攝氏溫度是{C}")
# fc()

# # 函氏可以傳送多個參數值，上限為256個。
# def tol(a,b):
#     if a > b: a,b = b,a 
#     total = 0
#     for i in range(a,b+1):
#         total += i
#     print(total)
# a = int(input("輸入起始值:"))
# b = int(input("輸入結束值:"))
# tol(a,b)

# def total_count(a):
#     if a == 999:
#         print("執行結束")
#         return True  # 傳回 True 告訴主程式結束
#     elif a < 0:
#         print("數值輸入錯誤")
#     else:
#         i = 1
#         total = 0
#         while i <= a:
#             total += i
#             i += 1
#         print(f"總和是 {total}")
#     return False  # 不結束程式

# def ex():
#     while True:
#         try:
#             a = int(input("輸入一個數字會從1加到它（輸入 999 結束）："))
#             if total_count(a):  # 如果 total_count 傳回 True，就結束
#                 break
#         except ValueError:
#             print("請輸入有效的整數")

# ex()

#歡迎畫面：字串

# def welcome(name):
#     print(f"歡迎您，{name}")
# n = input("輸入你的名字")
# welcome(n)


# def total():
#     tol = 0
#     for i in range(1,101):
#         tol += i
#     return tol      #把變數 tol 的內容傳回給呼叫端

# def main():
#     t = total() +1    #呼叫total()函式，用變數t接受函式回傳值
#     print('計算由1到100的總和：',total(),t)

# main()

# def tol(a,b,k,l):
#     if a > b: a,b = b,a 
#     total = 0
#     print("z:",k,",p:",l)
#     for i in range(a,b+1):
#         total += i
#     print("total:",total)
# x = int(input("輸入起始值:"))
# y = int(input("輸入結束值:"))
# z = int(input("輸入z值:"))
# p = int(input("輸入p值:"))
# tol(x,y,z,p)

# def total():
#     tol=0
#     i=1
#     while i < 101:
#         tol+=i
#         i+=1
#     return tol
# def calltotal():
#     t = total()+1
#     print("計算由1+到100的總和",total(),t)
# calltotal()

# def total():
#     tol=0
#     i=1
#     while i < 101:
#         tol+=i
#         i+=1
#     return tol
# def calltotal():
#     print("計算由1+到100的總和",total())
# calltotal()

# ##直述句
# x = int(input("請輸入起始數字 x："))
# y = int(input("請輸入結束數字 y："))
# sum = 0
# i = x
# while i <= y:
#     sum += i
#     i += 1
# print(f"加總從 {x} 到 {y} 的總和為：{sum}")
# ##分成涵式
# def total(a,b):
#     sum = 0
#     i=1
#     while i<= b:
#         sum+=i
#         i+=1
#     return sum
# def calltotal():
#     x=int(input("請輸入x"))
#     y=int(input("請輸入y"))
#     s=total(x,y)
#     print(f"加總從{x}到{y}的總和:",total(x,y),s)
# calltotal()

# def totalAB(a,b):
#     total=0
#     average = 0 
#     i=a
#     while i <= b:
#         total +=i
#         i+=1
#     average = total/(b+1-a)
#     return total,average
# def calltotalAB():
    
#     x = int(input("輸入起始值"))
#     y = int(input("輸入結束值"))
#     t,a = totalAB(x,y)
#     print(f"總合為：{t}｜平均值為：{a}｜{totalAB(x,y)}")

# calltotalAB()


# def totalAndAverage(a=1,b=100): #預設 a=1, b=100
#     tol = 0
#     avarage = 0.0 #浮點數
#     for i in range(a, b+1):
#         tol += i
#     avarage = tol/(b+1-a)
#     return tol,avarage

# def main():
#     s,a = totalAndAverage()  #呼叫函式不加值
#     print (f'總和為：{s}，平均值為：{a:.2f}')
#     s,a = totalAndAverage(5)    #給一個值時，會傳送到函式的第一個參數
#     print (f'總和為：{s}，平均值為：{a:.2f}')
#     s,a = totalAndAverage(5,80) #傳送兩個值，同時更改兩個參數內容
#     print (f'總和為：{s}，平均值為：{a:.2f}')

# main()

##讓使用者輸入

# def totalAndAverage(a=1,b=100):
#     tol = 0
#     avarage = 0.0 #浮點數
#     for i in range(a, b+1):
#         tol += i
#     avarage = tol/(b+1-a)
#     return tol,avarage

# def main():
#     x,y = "",""
#     x = input("請輸入起始值：")
#     y = input("請輸入結束值：")
#     if x== ""and y=="":
#         s,a = totalAndAverage()
#     elif x=="":
#         print("起始值必須輸入資料，使用預設值計算")
#         s,a = totalAndAverage(1,int(y)) #第1個參數值沒有輸入時，必須使用程式加入參數值
#     elif y=="":
#         s,a = totalAndAverage(int(x)) #僅輸入1個參數時，系統會當作第1個參數傳入
#     else:
#         x = int (x)
#         y = int (y)
#         s,a = totalAndAverage(x,y)
     
#     print (f'總和為：{s}，平均值為：{a:.2f}')

# main()


# 練習題
# 	建立一個函式compute()，讓使用者輸入學號、姓名、科系，透過呼叫顯示這些訊息。
## Q1
# def compute():
#     學號=int(input("輸入你的學號"))
#     姓名=input("輸入你的姓名")
#     科系=input("輸入科系")
#     print(f"你的學號：{學號},你的姓名:{姓名},你的科系：{科系}")
# compute()

# 	建立一個函式compute(x,y)。讓使用者輸入2個數字做為參數，透過呼叫函式，回傳(return x*y)的乘積。

##Q2

# def compute(x, y):
#     return x * y

# # 讓使用者輸入兩個數字，以逗號分隔
# x, y = eval(input("請輸入兩個數字（用逗號分隔，例如 3,5）："))

# # 呼叫函式
# product = compute(x, y)

# # 印出結果
# print(f"{x} 和 {y} 的乘積是：",compute(x, y),product)

# 	讓使用者輸入2個整數，呼叫函式compute(x,y) 並傳送2個參數給函數，讓函數回傳從x到y連續加總的結果。

##Q3
# def compute(x,y):
#     total=0
#     i=x
#     while i<=y:
#         total+=i
#         i+=1
#     return total
# x,y=eval(input("輸入兩個數字以逗號分開"))
# total = compute(x,y)    
# print(f"{x}到{y}的加總是{total}")
    

# 	讓使用者輸入2個整數，呼叫函式compute(x,y) 並傳送2個參數給函數，讓函數回傳x^y的值。
## Q4
# def compute(x,y):
#     total=x**y
#     return total
# x,y=eval(input("輸入兩個數字以逗號分開"))
# total = compute(x,y)
# print(f"第一個數字{x}的第二個數字{y}次方是",total)

# 	建立一個函式compute(a,x,y) 使用者輸入3個參數：a (字元)、x(個數)、y(列數)，印出 y列 x個的a字元。

# ##Q5
# def compute(a, x, y):
#     i = 1
#     while i <= y:
#         j = 1
#         while j <= x:
#             print(a, end="")
#             j += 1
#         print()
#         i += 1
# a, x, y = input("請輸入三個值：字元a、個數x、列數y（以逗號分隔，例如 * , 5 , 3）：\n").split(",")

# # 去除空白並轉型
# a = a.strip()
# x = int(x.strip())
# y = int(y.strip())

# compute(a, x, y)
    


# 	撰寫圓面積、長方形面積、三角形面積函式，透過輸入圓形半徑、長方形長、寬，三角形底和高，計算並輸出三個圖形面積與三個面積和。
# ##Q6

# import math

# def area(圓形半徑, 長方形長, 長方形寬, 三角形底, 三角形高):
#     圓形面積 = (圓形半徑 ** 2) * math.pi
#     長方形面積 = 長方形長 * 長方形寬
#     三角形面積 = 三角形底 * 三角形高 * 0.5
#     面積總和 = 圓形面積 + 長方形面積 + 三角形面積
#     return 圓形面積, 長方形面積, 三角形面積, 面積總和

# # 使用者輸入並轉換為 float
# 輸入資料 = input("請輸入：圓形半徑, 長方形長, 長方形寬, 三角形底, 三角形高（以半形逗號分隔）：\n")
# 圓形半徑, 長方形長, 長方形寬, 三角形底, 三角形高 = map(float, 輸入資料.split(","))

# 圓形面積, 長方形面積, 三角形面積, 面積總和 = area(圓形半徑, 長方形長, 長方形寬, 三角形底, 三角形高)

# print(f"圓形面積：{圓形面積:.2f}")
# print(f"長方形面積：{長方形面積:.2f}")
# print(f"三角形面積：{三角形面積:.2f}")
# print(f"面積總和：{面積總和:.2f}")

# lambda 是 Python 中用來建立 匿名函式（即沒有名字的函式） 的關鍵字。
# 它常用於需要臨時小函式、只用一次的場景，例如與 map()、filter()、sorted() 等搭配使用。


# 	輸入2個正整數x,y，傳入最大公因數函式內，函式回傳最大公因數計算結果。
## Q7
# def compute(x, y):
#     result = 1
#     for i in range(2, min(x, y) + 1):
#         if x % i == 0 and y % i == 0:
#             result = i
#     return result

# def Callcompute():
#     try:
#         x, y = map(int, input("輸入兩個正整數，以逗號隔開：").split(","))
        
#         if x <= 0 or y <= 0:
#             print("❌ 請輸入正整數！")
#             return
        
#         gcd = compute(x, y)
#         print(f"{x} 和 {y} 的最大公因數為：{gcd}")
    
#     except ValueError:
#         print("❌ 輸入格式錯誤，請輸入兩個整數，用逗號隔開。")

# Callcompute()

## # 輾轉相除法
# def compute(x, y):
#     # 輾轉相除法
#     while y != 0:
#         x, y = y, x % y
#     return x

# def Callcompute():
#     try:
#         x, y = map(int, input("輸入兩個正整數，以逗號隔開：").split(","))
        
#         if x <= 0 or y <= 0:
#             print("❌ 請輸入正整數！")
#             return
        
#         gcd = compute(x, y)
#         print(f"{x} 和 {y} 的最大公因數為：{gcd}")
    
#     except ValueError:
#         print("輸入格式錯誤，請輸入兩個整數，用逗號隔開。")

# Callcompute()


# 	某市區停車場車位不足，為鼓勵車輛提早移出，進行如下規範：
# (a). 2小時以內(含2小時)，每小時以30元計算
# (b). 2小時以上到4小時(含4小時)，每小時以50元計算
# (c). 4小時以上到6小時(含6小時)，每小時以80元計算
# (d). 6小時以上，每小時以100元計算
# 請撰寫程式輸入停車時數，傳入函數參數內，函數傳回停車費計算結果。


# ##Q8
# def compute(x,y):
#     time = int(input("輸入停車時數"))
#     total=0
#     if time<0:
#         print("請輸入0以上的數字")
#         return
#     elif time<=2:
#         total=time*30
#     elif 2<time<=4:
#         total=time*50
#     elif 4<time<=6:
#         total=time*80
#     else :
#         total=time*100
    
#     return total
# def Callcompute():
#     x,y=0,0
#     total=compute(x,y)
#     print("總費用是：",total)
# Callcompute()

# def compute():
#     try:
#         time = int(input("請輸入停車時數（0以上整數）："))
#         if time < 0:
#             print("❌ 請輸入 0 或以上的整數")
#             return
#     except ValueError:
#         print("❌ 輸入錯誤，請輸入整數")
#         return

#     # 根據停車時數計費
#     if time <= 2:
#         total = time * 30
#     elif time <= 4:
#         total = time * 50
#     elif time <= 6:
#         total = time * 80
#     else:
#         total = time * 100

#     return total

# def Callcompute():
#     total = compute()
#     if total is not None:
#         print("✅ 總費用是：", total)

# Callcompute()


# 	使用函數撰寫骰子比大小程式，先由電腦模擬投擲三個骰子和，再由使用者輸入一個值(自訂)模擬投擲動作，透過亂數產生三個骰子和，並和電腦輸出結果比大小，印出"你贏了"或"你輸了"。
## Q9
# import random
# def roll_compute():
#     dice=[random.randint(1,6) for i in range(3)]
#     total=sum(dice)
#     # print(dice)
#     return dice, total
# def Callcompute():
#     while True:
#         computer_dice, computer_total=roll_compute()
#         print("🎮 電腦正在擲骰...")
#         print(f"電腦的骰子點數：{computer_dice}，總和：{computer_total}\n")
#         user_dice, user_total = roll_compute()
        
#         a=input("你模擬擲投子按0停止")
#         if a=="0":
#             print("程序停止")
#             break
#         print(f"你的骰子點數：{user_dice}，總和：{user_total}\n")
#             # 比大小
#         if user_total > computer_total:
#             print("🎉 你贏了！")
#         elif user_total < computer_total:
#             print("😞 你輸了...")
#         else:
#             print("🤝 平手！")

# Callcompute()
        


# import random

# def roll_dice():
#     # 擲三顆骰子並回傳總和與個別點數
#     dice = [random.randint(1, 6) for _ in range(3)]
#     total = sum(dice)
#     return total, dice

# def play_game():
#     print("🎮 電腦正在擲骰...")
#     computer_total, computer_dice = roll_dice()
#     print(f"電腦的骰子點數：{computer_dice}，總和：{computer_total}\n")

#     input("請按 Enter 鍵模擬你擲骰子的動作...")
#     user_total, user_dice = roll_dice()
#     print(f"你的骰子點數：{user_dice}，總和：{user_total}\n")

#     # 比大小
#     if user_total > computer_total:
#         print("🎉 你贏了！")
#     elif user_total < computer_total:
#         print("😞 你輸了...")
#     else:
#         print("🤝 平手！")

# # 執行遊戲
# play_game()