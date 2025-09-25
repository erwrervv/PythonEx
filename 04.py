# # 1
# # i = 0
# # while i < 5:
# #     print(i)
# #     i+=1
# # print("程序結束")


# # # 2
# # i=0
# # total=0
# # #    x+=i，i+=1 的程序順序會影響迴圈次數，導致執行程序次數不同預期
# # while i<11:
# #     total+=i
# #     i+=1
# # print("total=",total,"|i=",i)

# # # 3 
# # i = 1
# # s = "+"
# # emt = " "
# # max_width = eval(input("輸入一個數字"))

# # while i <= max_width:
# #     spaces = emt * (max_width - i)
# #     symbols = s * (2 * i - 1)
# #     print(spaces + symbols)
# #     i += 1

# # #5
# # sum=0
# # for i in range(1,101,1):
# #     sum += i 
# # print(sum)
# # sum =0
# # i=0
# # while i<101:
# #     sum+=i
# #     i+=1
# # print(sum)


# # # 6
# # x=1
# # while x <10:
# #     y=1
# #     while y<10:
# #         print(f"{x}x{y}={x*y}", end="\t")
# #         y+=1
# #     x+=1
# # print("程式結束")

# # for x in range(0,10,1):
# #     print("x=",x )
# #     for y in range(0,10,1):
# #         print("y=",y,end="\t")
# #     print("這是y",)
# # print("這是x",)
# # print("程式結束")

# # # #9
# # for x in range(1,10):
# #     for y in range(1,10):
# #         print(f'{x}*{y} = {x*y:2}',end = ' ')
# #     print()
# # print("程序結束")
# #     # x*y 是要輸出的值（乘積）
# #     # :2 表示這個輸出的欄位寬度是 至少 2 個字元寬
# #     # 如果乘積小於 10（例如 2x3=6），會 自動補上空格，對齊輸出



# # 練習題
# # 1	使用迴圈敘述撰寫程式，讓使用者輸入兩個正整數 a、b (a<b) ，利用迴圈計算從a開始連加到b的總和。例如：輸入a=1、b=100 (1+2+3+…+100)，則輸出結果為5050
# # 1.1	輸入說明： 請輸入兩個正整數(a、b且a<b) 輸入範例
# # 請輸入第一個正整數66
# # 請輸入第二個正整數666
# # 1.2	輸出說明： 計算從 a 開始到 b的總和 輸出範例
# # 219966

# # # Q1
# # a=eval(input("輸入第一個數字"))
# # b=eval(input("輸入第二個數字"))

# # if a > b:
# #     a, b = b, a
# # total = 0
# # current = a
# # while current <= b:
# #     total += current
# #     current += 1
# # print("總和等於", total)
    

# # 2	使用迴圈敘述撰寫程式，讓使用者輸入兩個正整數 a、b (a<b) ，利用迴圈計算從a開始連加到b的偶數總和。例如：輸入a=1、b=100 (2+4+6+…+100)，則輸出結果為2550
# # 2.1	輸入說明： 請輸入兩個正整數(a、b且a<b) 輸入範例
# # 請輸入第一個正整數6
# # 請輸入第二個正整數88
# # 2.2	輸出說明： 計算從 a 開始到 b的偶數總和 輸出範例
# # 1974

# # #Q2
# # a=int(input("輸入第一個數字"))
# # b=int(input("輸入第二個數字"))
# # sum =0
# # current = a
# # if a>b:
# #     a,b=b,a
# # while current < b:
# #     sum+=current
# #     a+=2
# # print("sum= ",sum)
# # print("結束")
    




# # 3	使用迴圈敘述撰寫程式，讓使用者輸入一個正整數 (<30)然後以三角形方式依序輸出此數階乘結果
# # 3.1	輸入說明： 請輸入一個正整數(<30) 輸入範例
# # 12
# # 3.2	輸出說明： 以三角形方式依序輸出此數階乘結果 輸出範例
# #    1
# #    2   4
# #    3   6   9
# #    4   8  12  16
# #    5  10  15  20  25
# #    6  12  18  24  30  36
# #    7  14  21  28  35  42  49
# #    8  16  24  32  40  48  56  64
# #    9  18  27  36  45  54  63  72  81
# #   10  20  30  40  50  60  70  80  90 100
# #   11  22  33  44  55  66  77  88  99 110 121
# #   12  24  36  48  60  72  84  96 108 120 132 144

# ## Q3

# #while寫法
# try:
#     num = int(input("請輸入一個小於 30 的正整數: "))

#     if num >= 30 or num <= 0:
#         print("你輸入的數字不在有效範圍內（1~29），請重新輸入。")
#     else:
#         i = 1  # 控制行數
#         while i <= num:
#             j = 1  # 控制列數
#             while j <= i:
#                 print(f"{i * j:4}", end="")  # 格式化輸出，對齊
#                 j += 1
#             print()  # 每一列輸出完要換行
#             i += 1

# except ValueError:
#     print("輸入型別錯誤，請輸入正整數。")
    
# #for寫法
# try:
#     num = int(input("請輸入一個小於 30 的正整數: "))
    
#     if num >= 30 or num <= 0:
#         print("你輸入的數字不在有效範圍內（1~29），請重新輸入。")
#     else:
#         for i in range(1, num + 1):  # 控制行數
#             for j in range(1, i + 1):  # 控制每行的列數
#                 print(f"{i * j:4}", end="")  # 4格對齊
#             print()  # 換行

# except ValueError:
#     print("輸入型別錯誤，請輸入正整數。")
# # 4	使用迴圈敘述撰寫程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間(含)所有5的倍數和。
# # 4.1	輸入說明： 請輸入一個正整數 輸入範例
# # 500
# # 4.2	輸出說明： 所有5的倍數和 輸出範例
# # 25250

# ##Q4
# # a = int(input("輸入一個正整數："))
# # current = 1
# # total = 0

# # while current <= a:
# #     if current % 5 == 0:
# #         total += current
# #     current += 1

# # print("總和 =", total)

# # 5	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數，將此數反轉順序輸出 (利用 % 與 // 處理)
# # 5.1	輸入說明： 請輸入一個正整數 輸入範例
# # 31283
# # 5.2	輸出說明： 將數值反順序輸出 輸出範例
# # 38213


# ## Q5
# # a=int(input("輸入一個正整數"))
# # next=0
# # while a>0:
# #     next=a%10
# #     a=a//10
# #     print(next,end="")

# # 6	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數n，利用迴圈計算n!的值。
# # 6.1	輸入說明： 請輸入一個正整數 輸入範例
# # 15
# # 6.2	輸出說明： 計算n！值 輸出範例
# # 1307674368000

# ##Q6
# # a=int(input("輸入一個數"))
# # current = a
# # sum = 0
# # while current>0:
    
# #     sum+=current
# #     current-=1
# # print(f"{a}! = {sum}")

# # 7	(1) 請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數n (n < 10)，顯示 n*n乘法表。
# # (2)每項運算式格式化排列整齊，每個運算子與運算元輸出的欄寬為2，而每項乘積輸出的欄寬為4，皆靠左對齊不跳行。
# # 7.1	輸入說明： 請輸入一個正整數n (n<10)
# # 3
# # 7.2	輸出說明： 輸出格式化n * n乘法表
# # 1* 1 = 1    2* 1 = 2    3* 1 = 3
# # 1* 2 = 2    2* 2 = 4    3* 2 = 6
# # 1* 3 = 3    2* 3 = 6    3* 3 = 9
# # 7.3	若輸入大於或等於10，顯示”輸入錯誤！數字不能大於或等於10”

# ##Q7
# max=int(input("請輸入一個數值"))
# n=1
# while n <max:
#     i=1
#     while i <10:
#         print(f"{i:2}x {n:2} = {i*n:2}",end="   ")
#         i+=1
#     print()
#     n +=1

# # 8	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數，代表後面要測試的次數。 每次測試都是輸入一個正整數，將所有位數加起來輸出結果
# # 1.1	輸入說明： 請輸入一個正整數，代表要測試數字的”次數”。
# #    每次輸入一個兩位數以上資料。
# # 1.2	輸出說明： 看所有位數加總和

# ##Q8
# # a=int(input("輸入一個數"))
# # i=1
# # total=0
# # while i<=a:
# #     b = int(input(f"輸第{i}個數"))
# #     if b <= 10:
# #         print(f"請輸入兩位數以上的數字！")
# #         continue  # 不算這次，重來
# #     else:
# #         total = 0
# #         temp = b  # 用 temp 來保存數字，避免破壞原始 b

# #         while temp > 0:
# #             total += temp % 10
# #             temp = temp // 10

# #         print(f"{b} 的各位數字總和為：{total}")
# #     i+=1
# #     print(f"sum= {total}")
# # print("結束")


# # 輸出結果：
# # 請輸入測試次數 2
# # 請輸入正整數 32145
# #   32145 數字拆開後相加為 15
# # 請輸入正整數 654789
# #   654789 數字拆開後相加為 39

# # 9	使用者輸入一筆存款金額、年利率及經過的月份，並顯示每個月存款總額。輸出到小數點第二位數。
# # 例：存款10000 年利率5.75%
# # 滿一個月，存款為：10000+10000*5.75/1200=10047.92
# # 滿二個月，存款為：10047.92+10047.92*5.75/1200=10096.06
# # 滿三個月，存款為：10096.06+10096.06*5.75/1200=10144.44 餘下類推
# # 輸出結果：
# # 請輸入本金50000
# # 請輸入利率3
# # 請輸入月份5
# # Month    Amount 
# #   1      50125.00
# #   2      50250.31
# #   3      50375.94
# #   4      50501.88
# #   5      50628.13

# ##Q9
# F=float(input("輸入第一筆存款"))
# L=float(input("輸入利率"))
# M=int(input("輸入經過幾個月"))

# Amount =F
# monthly_rate = L / 12 / 100 
# i=1
# print("Month    Amount ")
# while i <= M:
#     Amount += Amount *monthly_rate
#     print(f"{i:<9}{Amount :.2f}")
#     i+=1
#     # print(f"你第{i}個月的存款是{Amount :.2f}")
    
#自己的
# code = "opiur"    
# a= str(input("請輸入密碼"))
# tryTime=3
# count=1
# if a ==code:
#     print(f"第{count}次輸入正確")
#     print("輸入正確")
#     # 中斷程序
#     print("退出程序")
#     count+=1
# else:
#     while tryTime >1:
#         if tryTime !=0:
#             if a ==code:
#                 print(f"第{count}次輸入正確")
#                 print("退出程序")
#                 break
#             else:
#                 print("輸入錯誤")
#                 tryTime-=1
#                 print(f"還有輸入次數：{tryTime}")
#                 a= str(input("請輸入密碼"))
#                 count+=1
        
#         else:print("退出程序")

# except ValueError:
#     print("輸入型別錯誤")
#     a= str(input("請輸入密碼"))

# ##產生的
# code = "opiur"
# tryTime = 3  # 最多可輸入次數
# count = 0     #計數器

# while tryTime > 0:
#     a = input("請輸入密碼: ")

#     if a == code:
#         count += 1
#         print(f"第 {count} 次輸入正確")
#         print("開啟程序")
#         break
#     else:
#         tryTime -= 1
#         if tryTime > 0:
#             print("輸入錯誤")
#             print(f"還有輸入次數：{tryTime}")
#         else:
#             print("密碼錯誤次數過多，退出程序")

生日 = 220
全票 = 320
優惠 = 270
生日張數 = 0
全票張數 = 0
優惠張數 = 0

try:
    while True:
        i = int(input("輸入決定模式 0.結帳 1.生日 2.全票 3.優惠: "))

        if i == 1:
            生日張數 = int(input("輸入有幾張(數字): "))
        elif i == 2:
            全票張數 = int(input("輸入有幾張(數字): "))
        elif i == 3:
            優惠張數 = int(input("輸入有幾張(數字): "))
        elif i == 0:
            總金額 = 生日 * 生日張數 + 全票 * 全票張數 + 優惠 * 優惠張數
            print(f"生日: {生日 * 生日張數} 全票: {全票 * 全票張數} 優惠: {優惠 * 優惠張數} 總和: {總金額}")
            break
        else:
            print("輸入錯誤，請重新輸入模式（0～3）")

except ValueError:
    print("輸入型別錯誤，請輸入整數")