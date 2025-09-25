###常用 count() 與 index() pop() 與 remove() sort() & sort(reverse = True)& reverse()
## 串列(1維2維) list [6,8,1] 元組 tuple("","","") 集合 set{} 字典 dic{a:b,c:d,e:f} 字串 str:""
# ids = "A123456789"
# id = list(ids)  #將字串轉換為串列
# print(id) #['A', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# list1 = []  #建立一個空串列
# list2 = [1,2,3,4,5] 
# list3 = ['apple','orange','banana'] #建立串列並賦予字串資料
# list4 = [1,2,34,56,'word'] #建立串列賦予不同型別資料
# list5 = list(('apple','banana','cherry')) #使用list指令將元組創建為串列
# list6 = [x for x in range(10)] # 創建0-9連續數字的串列
# list7 = [0]*10  #創建 10個 0的串列
# words = ["白板筆","立可白","清潔劑","漂白水"]

# list2.insert(2,(int(input('輸入整數：'))))
# print(list2)
# i=int(input('輸入整數：'))
# list2.insert(3,(i))
# print(list2)
# list2.append(int(input('輸入整數：'))) #在list2最末端加入一筆資料
# list2.insert(2,(int(input('輸入整數：'))))

# 串列可以當作是儲存資料的容器，這有利於資料的存取。串列在其他程式語言如C、C++、Java則稱為陣列(array)。Python的串列可以存放不同型態的資料，與上述其他語言的陣列型態不相同，其餘使用方式與性質則相同。
# 串列在運用上，可同時以一個名稱，乘載多個變數內容，能簡化變數使用，能簡化變數運用。
# 串列語法
# 串列名稱  = [串列值1,串列值2,串列值3... ]
# i.	如變數一般，先設定串列名稱，等號後面加上中括號，當中放入需要的內容，與變數不同，內容可以有多筆，以逗號區隔開來。
# ii.	中括號 [ ] 內容可以是空的，表示後面程式會在置入新的內容
# 串列存放模式
# 編號 0	編號1	編號2	編號3	編號4
# 元素(資料)	元素	元素	元素	元素
# 長度共有5格，索引碼(編號)為0~4
# 1	串列建立
# 建立串列的時候，透過[ ] 存放內容。

# import os
# os.system('cls')
# list1 = []  #建立一個空串列
# list2 = [1,2,3,4,5] #建立串列並賦予數值資料
# list3 = ['apple','orange','banana'] #建立串列並賦予字串資料
# list4 = [1,2,34,56,'word'] #建立串列賦予不同型別資料
# list5 = list(('apple','banana','cherry')) #使用list指令將元組創建為串列
# list6 = [x for x in range(10)] # 創建0-9連續數字的串列
# list7 = [0]*10  #創建 10個 0的串列
# words = ["白板筆","立可白","清潔劑","漂白水"]

# print(list1)
# print(list2)        #印出list2的所有內容
# print(list3)
# print(list4)
# print(list5)
# print(list6)
# print(list7)
# print(words)

# 2	串列運作
# 2.1	[ ] [start : end ] 檢索值
# 串列存放透過索引值檢索資料，在檢索資料的時候，[ ]中的數字代表檢索值，用來尋找特定位置的內容
# print(list2[3])     #印出索引值(index) 3 的串列項目
# print(list2[1:3])   #印出索引值 1~(3-1) 的串列項目
# print(list2[0:5])   #印出索引值 0~4 的串列項目
# print(list2[:4])    #印出索引值 3之前 的串列項目
# print(list2[3:])    #印出索引值 3之後 的串列項目
# print(list2[-1])    #印出索引值 由後往前算第一位的串列項目
# print(list2[:-1])   #印出索引值 由後往前算所有的項目(注意不含-1)

# 2.2	len()：計算串列長度
# 透過len(串列名稱 ) 可以查出串列中一共有多少個值
# x = len(list1)
# print(x)
# print(len(list1))   #取得串列"list1"的長度
# print(len(list2))
# print(len(list3))
# print(len(list4))
# print(len(list7))

# ids = "A123456789"
# id = list(ids)  #將字串轉換為串列
# print(id) #['A', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# print(id[0])
# print(id[1])
# print(id[-2])
# print(id[2:9])
# print(len(id))

# for i in range (0,len(id)):
#     print(id[i],end='')


# 2.3	sum 、 max 以及 min 函式
# sum()函式可以加總串列中的所有數值和，利用max() 和min()，可以找出最大與最小的資料
# import os
# os.system('cls')
# listsum = [i for i in range(12)]
# print(listsum)
# su=sum(listsum)
# print(su)
# maxsu=max(listsum)
# print(maxsu)
# minsu=min(listsum)
# print(minsu)

# list2 = [i for i in range(11)]
# print(list2)
# a = sum(list2) #sum 將串列內的int全總合出一個值
# print(a)
# b = max(list2)
# c = min(list2)
# print(f"list內元素和為：{a}\n最大值為：{b}\n最小值為：{c}")

# 輸出
# list內元素和為：15
# 最大值為：5
# 最小值為1

# 2.4	append() 與 insert()
# 使用 append(value)的方法，將內容增加到串列尾端，利用
# insert (index,value)將內容插入串列的索引值位置。

# list1 = []  #建立一個空串列
# print(list1)
# list2 = [1,2,3,4,5] 
# print(list2)        #印出list2的所有內容
# list3 = ['apple','orange','banana'] #建立串列並賦予字串資料
# print(list3)
# list4 = [1,2,34,56,'word'] #建立串列賦予不同型別資料
# print(list4)
# list5 = list(('apple','banana','cherry')) #使用list指令將元組創建為串列
# print(list5)
# list6 = [x for x in range(10)] # 創建0-9連續數字的串列
# print(list6)
# list7 = [0]*10  #創建 10個 0的串列
# print(list7)
# words = ["白板筆","立可白","清潔劑","漂白水"]
# print(words)

# list2.insert(2,(int(input('輸入整數：'))))
# print(list2)
# i=int(input('輸入整數：'))
# list2.insert(3,(i))
# print(list2)
# print(list1)
# list1.append("Tim"+"Tina")     #在list1最末端加入一筆資料 "Tim"
# print(list1)
# list1.append("Tina")     #在list1最末端加入一筆資料 "Tina"
# print(list1)
# list1.insert(1,"Sky")   #在list1索引值1的位置插入一筆資料 "Sky"
# print(list1)
# print(list3)
# list3.insert(5,'kiwi')  #給的索引值大於串列長度時會放在最後一筆
# print(list3)
# 執行結果
# []
# ['Tim']
# ['Tim', 'Tina']
# ['Tim', 'Sky', 'Tina']
# ['apple', 'orange', 'banana']
# ['apple', 'orange', 'banana', 'kiwi']

# print(list2)
# list2.append(int(input('輸入整數：')))
# print(list2)
# i = int(input('輸入整數：'))
# list2.append(i)
# print(list2)
# print(list4)

# i = int(input('輸入插入位址：'))  #輸入索引值(數字)
# c = input('輸入插入內容：')       #輸入內容(字串)
# list4.insert(i,c)
# print(list4)


# 執行結果
# 輸入整數：66
# [11, 12, 13, 14, 15, 66]
# 輸入整數：88
# [11, 12, 13, 14, 15, 66, 88]
# [1, 2, 34, 56, 'word']
# 輸入插入位址：2
# 輸入插入內容：try
# [1, 2, 'try', 34, 56, 'word']

# 練習：
# 1.1.1	使用上面範例list1，試著用迴圈存入1~10，印出最後結果
# 1.1.2	使用上面範例list2，輸入兩個值，第一個值是串列索引，第二個值是內容，插入指定索引位置

# 多筆輸入與手動輸入
# print(list1)

# for i in range (1,11):    #自動產生1-10數字內容
#     list1.append(i)
# print(list1)

# list1 = [i for i in range(1,11)]
# print(list1)

# list1 = [int(input("輸入串列內容：")) for i in range(5)] #手動輸入5個數字內容
# print(list1)
# list10 = [1,2,3]
# for i in range(5):    #手動輸入5個數字內容
#     list10.append(int(input("請輸入數字")))
# print(list10)

# 執行結果
# []
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 輸入串列內容：666
# 輸入串列內容：777
# 輸入串列內容：888
# 輸入串列內容：999
# 輸入串列內容：000
# [666, 777, 888, 999, 0]
# 請輸入數字123
# 請輸入數字456
# 請輸入數字789
# 請輸入數字987
# 請輸入數字654
# [666, 777, 888, 999, 0, 123, 456, 789, 987, 654]
#  

# 2.5	pop() 與remove()
# pop()可用來刪除串列最後一個數，pop(index)可用來刪除index指定的索引位置資料，利用remove(value)刪除串列中，內容為value所指定的資料。


# list4 = [1,2,34,56,'word']
# s= [i for i in range(1,10,2)]
# print("s：",s)
# p=int(input(""))
# list4.pop(p)
# print("list4：",list4)
# list4 = [1, 2, 34, 56, 'word']
# print("目前的 list4：", list4)
# try:
#     index = int(input(f"請輸入要刪除的索引值（0 ~ {len(list4)-1}）："))
#     removed = list4.pop(index)
#     print(f"已刪除：{removed}")
#     print("刪除後的 list4：", list4)
# except ValueError:
#     print("❌ 錯誤：請輸入整數索引！")
# except IndexError:
#     print("❌ 錯誤：索引超出範圍！")
    
    
# print(list4)
# list4.pop()     #刪除最後一筆資料
# print(list4)
# list4.pop(1)    #將索引值 1 內儲存資料刪除
# print(list4)
# list4.append(34)
# print(list4)
# list4.remove(34) #刪除第一筆符合的內容
# print(list4)
# 執行結果
# [1, 2, 34, 56, 'word']
# [1, 2, 34, 56]
# [1, 34, 56]
# [1, 34, 56, 34]
# [1, 56, 34]


# 2.6	count() 與 index()
# count(value)用來計算某個資料(value)在串列中出現的次數，index(value) 立即回傳value這個內容所在位置。
# print(list3)
# list3.append('apple')
# print(list3)
# c = list3.count('apple')
# print(c) #計算apple在串列中出現幾次
# list3.insert(0,'kiwi')
# print(list3)
# print(list3.index('apple')) #搜尋apple第一次出現的位址(索引值)
# print(f"banana在串列中{list3.index('banana')}的位置")
# print(list5)
# list3.extend(list5)     #將list5串列資料加入到list3 >> list3 += list5
# print(list3)
# print(f"apple共出現{list3.count('apple')}次，banana第一次出現在{list3.index('banana')}")
#  #輸出
# # ['apple', 'orange', 'banana']
# # ['apple', 'orange', 'banana', 'apple']
# # 2
# # ['kiwi', 'apple', 'orange', 'banana', 'apple']
# # 1
# # banana在串列中3的位置
# # ['apple', 'banana', 'cherry']
# # ['kiwi', 'apple', 'orange', 'banana', 'apple', 'apple', 'banana', 'cherry']
# # apple共出現3次，banana第一次出現在3

# # 2.7	sort()與reversr()
# # 利用sort()串列由小至大加以排序。而reverse()則用來將串列內容反轉排列。
# list1 = [1,4,8,3,7,2]
# list1 = ["a1","fb4","cf8","cd3","gb7","vfs2"] #也可以對首字母排序 ascllcode
# print(list1)
# list1.sort()    #排序
# list1.sort(reverse = True)    #反向排序
# print(list1)
# list1.reverse() #反轉內容
# print(list1)
# # 輸出
# # [1, 4, 8, 3]
# # [1, 3, 4, 8]
# # [8, 4, 3, 1]
# #  


# # 2.8	in 與not in
# # in與 not in 用來判斷特定資料是否存在於串列中，其使用語法
# # 資料 in 串列  或 資料 not in 串列  ，傳回值為True 或False
# list1 = [1,4,8,3]
# a = 5 in list1
# b = 4 in list1

# if a == True:
#     print("串列中有5")
# else:
#     print("找不到5這個數")
# if b == True:
#     print("串列中有4")
# else:
#     print("找不到4這個數")
# print()

# a = 5 not in list1
# b = 4 not in list1
# print(a)
# if a == True:
#     print("串列中沒有5")
# else:
#     print("5存在")
# if b == True:
#     print("串列中沒有4")
# else:
#     print("4存在")
# # 輸出
# # 找不到5這個數
# # 串列中有4

# # 串列中沒有5
# # 4存在


# # 2.9	+ 與 *
# # 串列功能中，使用 + 號能將兩個串列連結在一起，使用 * 號 可以複製串列內容。
# print (list2,list3)
# lst = list2 + list3
# print(lst)
# # 輸出
# [1, 2, 3, 4, 5] ['apple', 'orange', 'banana']
# [1, 2, 3, 4, 5, 'apple', 'orange', 'banana']

# print(list2)
# lst = list2 * 2
# print(lst)
# # 或
# print(list2)
# lst = 2 * list2
# print(lst)
# # 輸出相同
# # [1, 2, 3, 4, 5]
# # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# #  


# # 2.10	使用for 迴圈列印
# # 使用for迴圈配合串列，可解決大量資料反覆列印的問題，前面已經用過迴圈進行串列輸入，在輸出部分也容易利用
# for i in range(len(list3)):
#     print(f"list[{i}] = {list3[i]}")
# # # 輸出
# # list[0] = apple
# # list[1] = orange
# # list[2] = banana

# # python 提供串列專用的for迴圈方式
# # for i in 串列名稱:
# # 這種模式i在迴圈進行時，會依序置入串列內容
# for i in list3:
#     print(i,end = ' ')
# # 輸出
# # apple orange banana
# # 這種方式會造成原來索引值i原來用作數值顯示功能，如上面範例list[i] 這時就無法使用，解決辦法再加一個變數
# x = 0
# for i in list2:
#     print(f"list3[{x}] = {i}")
#     x +=1
# # 輸出
# # list[0]=1
# # list[1]=2
# # list[2]=3
# # list[3]=4
# # list[4]=5

# # 串列(容器)運作函式
# # 函式	意義
# # len()	計算串列長度
# # sum()	加總串列每一個元素
# # max()	回傳串列最大值
# # min()	回傳串列最小值



# # 串列運作方法
# # 方法	意義
# # append(value)	附加value於串列尾端
# # insert(index, value)	在索引index處加入value
# # pop()	刪除串列最後一個元素
# # pop(index)	刪除串列索引index所在的元素
# # remove(value)	刪除串列中的value，若有多個相同value，只刪除第一個
# # count(value)	串列中出現value的個數
# # index(value)	value所在串列第一個出現的索引值
# # sort()	將串列元素由小至大排序
# # sort(reverse = True)	將串列元素由大至小排序
# # reverse()	將串列元素反轉



# # 串列運作相關運算子
# # 運算子	意義
# # in	檢視某一元素是否在串列中
# # not in	檢視某一元素是否不在串列中
# # [index]	印出串列index位置中某一元素
# # [start:end]	印出串列中從start 到end-1的元素
# # *	複製多次串列元素
# # +	連結兩個串列元素

# #  



# 1.2	練習
# 1.2.1	使用隨機方式產生樂透號碼 6個數字(1~49)，並存放入串列中，印出結果。
##Q1
import os
os.system("cls")

# import random
# LOP = random.sample(range(1, 50), k=6)
# print(LOP)
## Q2
# 1.2.2	上述樂透程式，加上串列檢查，當檢查出元素有重複時，替換該元素
# import random
# TOTALLOP = []
# while len(TOTALLOP)<6:
#     LOP = random.randint(1,49)
#     if LOP not in TOTALLOP:
#         TOTALLOP.append(LOP)
# print("產生的樂透號碼：",TOTALLOP)

# # 1.2.3	人工輸入12個正整數，存入串列，排序後輸出結果
## Q3
# num=[]
# while len(num) < 6:
#     newnum = int(input("輸入正整數：")) 
#     if newnum > 0:
#         num.append(newnum)
#     else:
#         print("⚠️ 請輸入正整數！")
# sorted_num = sorted(num)
# print("升冪排序結果：", sorted_num)
# sorted_desc = sorted(num, reverse=True)
# print("降冪排序結果：",sorted_desc) 

# 升冪排序後輸出（不影響原串列）
# sorted_num = sorted(num)
# print("升冪排序結果：", sorted_num)

# sorted() 是建立新串列，不會改變原串列
# .sort() 是就地排序，直接改變原本的串列
# 若你想保留原始順序，建議用 sorted()

# 降冪排序後輸出（直接修改原串列）
# num.sort(reverse=True)
# print("降冪排序結果：", num)

# ⚠️ 說明你原本程式碼的幾個小錯誤：
# 問題行	問題說明
# reversed = num.sort(...)	list.sort() 會直接修改原串列，但 不會回傳值，所以 reversed 是 None
# 沒檢查是否為「正整數」	若輸入負數或 0，應該排除



# 1.2.4	隨機輸出五張撲克牌，不論花色，點數存放到串列中，計算點數。
# ##Q4
# import random
# ran = random.choices(range(0,13),k=5)
# # print(ran)
# print(sum(ran))

# # 1.2.5	使用者輸入十個數字存放串列中，接著由大到小順序顯示最大的三個數字。
# ##Q5
# TotalNUM=[]
# while  len(TotalNUM)<6:
#     try:
#         NUM = int(input(f"請輸入第 {len(TotalNUM) + 1} 個數字："))
#         if NUM in TotalNUM:
#             print("⚠️ 重複輸入，請輸入不同的數字")
#             continue
#         else:
#             TotalNUM.append(NUM)
#     except ValueError:
#         print("輸入型別錯誤")
# sortedTotalNUM_desc = sorted(TotalNUM, reverse=True)
# print("由大到小排序：",sortedTotalNUM_desc)
# print("前三大數字：",sortedTotalNUM_desc[:3])

# # 1.2.6	使用者輸入十個數字，做為樣本數，輸出眾數(出現最多次數的數字
##Q6
# TotalNUM=[]
# maxcount=0
# maxnumber=0
# while len(TotalNUM)<10:
#     try:
#         newnumber= int(input(f"輸入第{len(TotalNUM)+1}數字："))
#         print(f"你輸入了：{newnumber}")
#         TotalNUM.append(newnumber)
        
#         if maxcount <TotalNUM.count(newnumber):
#             maxcount= TotalNUM.count(newnumber)
#             maxnumber=newnumber
#     except ValueError:
#         print("輸入型別錯誤，請輸入數字")
# print("最多重複數字是：",maxnumber)
# print("最多重複次數是：",maxcount)


# 1.2.7	使用迴圈反覆輸入成績，存放到串列，直到-9999結束，輸出最大值、最小值，加總與平均

##Q7
# minnumber=None
# maxnumber=None
# avenumber=None
# # 2. ❌ minnumber 初始值為 0，可能導致「最小值」無法正確記錄
# # 假如使用者輸入的成績全都高於 0（比如 60～100），minnumber > newnumber 就永遠不成立，造成最小值不會更新
# # 解法：一開始先把 minnumber 設為 101（或用 None 初始後動態判定）
# numberlist=[]
# while True:
#     try:
#         newnumber=int(input("輸入成績,輸入-9999停止程序"))
#         if newnumber==(-9999):
#             if not numberlist:
#                 print("⚠️ 沒有輸入任何成績！")
#             else:
#                 total = sum(numberlist)
#                 average = total / len(numberlist)
#                 print("\n📊 輸入結束，統計結果如下：")
#                 print("成績總和：", total)
#                 print("成績平均：", round(average, 2))
#                 print("最高分數：", max(numberlist))
#                 print("最低分數：", min(numberlist))
#             break
#         if newnumber>100 or newnumber<0:
#             print("請輸入在0到100之間的合理成績")
#             continue

#         numberlist.append(newnumber)
#         print(f"✅ 成績 {newnumber} 已儲存，目前已輸入：{numberlist}")

#     except ValueError:
#         print("❌ 請輸入有效的整數")
        



# 1.2.8	設定一個串列，建立5個部門員工姓名，透過迴圈輸入員工成績，接下來依照成績排序輸出評核等級
# 成績	等級
# 90~100	A
# 80~89	B
# 70~79	C
# 60~69	D
# 60(不含)以下	E

# ##Q8
# # 建立員工名單
# emper = ["元1", "朱2", "堂3", "送4", "誦5"]
# score_data = []

# for name in emper:
#     while True:
#         try:
#             score=int(input(f"請{name}輸入0~100的成績："))
#             if 0<= score<=100:
#                 score_data.append((name,score))
#                 break
#             else:
#                 print("成績必須在0~100之間")
#         except ValueError:
#             print("❌ 請輸入有效的整數")
# sorted_scores = sorted(score_data, key=lambda x: x[1], reverse=True)
# print(sorted_scores)
# def get_level(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "E"
# # # # 輸出結果
# print("\n📊 員工評核結果（依成績高低排序）：")
# print(f"{'姓名':<5} {'成績':<5} {'等級':<5}")
# print("-" * 20)
# for name, score in sorted_scores:
#     level = get_level(score)
#     print(f"{name:<6} {score:<6} {level}")

# # 讓每位員工輸入成績
# for name in emper:
#     while True:
#         try:
#             score = int(input(f"請 {name} 輸入 0~100 的成績："))
#             if 0 <= score <= 100:
#                 score_data.append((name, score))  # 存成 (姓名, 成績)
#                 break
#             else:
#                 print("⚠️ 成績必須在 0 到 100 之間")
#         except ValueError:
#             print("❌ 請輸入有效的整數")

# 根據成績排序（由高到低）
# sorted_scores = sorted(score_data, key=lambda x: x[1], reverse=True)

# # 評核等級函數
# def get_level(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "E"

# # 輸出結果
# print("\n📊 員工評核結果（依成績高低排序）：")
# print(f"{'姓名':<5} {'成績':<5} {'等級':<3}")
# print("-" * 20)
# for name, score in sorted_scores:
#     level = get_level(score)
#     print(f"{name:<5} {score:<5} {level}")



######
# lst3=[[12454],[23456],[3333],[478956]]
# A=[i for i in range(6)]
# A=[[] for i in range(6)]
# A=[5]*40
# A[0]=[1234,555,456,6664]
# A=[[j for j in range(1,7)] for i in range(6)]
# row=int(input("輸入有幾列"))
# column=int(input("輸入有幾行"))
# A= [[1 for j in range(column)] for i in range(row)]
# print(A)


# ####
# import random
# lst2 = []
# #輸入列數、行數
# row = int(input('Enter the number of row: '))  #列
# column = int(input('Enter the number of column: ')) #行

# for i in range(0,row):  #依照輸入值產生列數  
#     lst2.append([])
#     for j in range(0,column):   #依照輸入值產生每列元素
#         lst2[i].append(random.randint(1,50))
# print(lst2,'\n')

# ##讀取lst2其中的元素
# lst2 = [[1,2,3],[4,5,6,99,55],[7,8,9],[4,5,6]] 
# for row in lst2:
#     for i in row:
#         print('%4d'%i,end ='')
#     print(i)
# print(row)

# # 3	列印二維串列所有元素
# # 1.
# for i in range(len(lst2)):          #列數
#     for j in range(len(lst2[0])):   #每列長度(元素數量)
#         print('lst2[%d][%d] = %2d'%(i,j,lst2[i][j])) #依序列印元素內容
#     print()
# # 2.
# for i in range(len(lst2)):
#     for j in range(len(lst2[i])):
#         print('%4d'%(lst2[i][j]),end ='')
#     print()

# # 3.Pythonic 寫法 (for-each 迴圈)
# lst2 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in lst2:               # 直接取出每一列
#     for val in row:            # 直接取出該列的每個元素
#         print(f"{val:4d}", end="")  # 格式化輸出
#     print()                    # 換行
    
    # for j in range(len(lst2[0])):
    # lst2[0] 👉 代表 第 0 列 (也就是第一列，因為 Python 的索引從 0 開始)。

    # len(lst2[0]) 👉 代表 第 0 列的長度，也就是這一列有多少個元素。

    # range(len(lst2[0])) 👉 就會依序產生 0 到 (元素數量-1) 的索引，用來當作「行索引」。
# # 📌 三種方式比較
# # 寫法1：有索引 → lst2[i][j]，方便 debug。
# # 寫法2：矩陣格式，使用索引。
# # 寫法3：最簡潔，直接迭代，不需要索引。


# 4	計算行、列和
# 二維串列計算行、列和，仍然使用雙層複迴圈，要計算每一列的和，就是列在外圈，行(元素數量)在內圈。
# lst2 = [[1,2,3],[4,5,6,99,55],[7,8,9],[4,5,6]] 

# # for i in range(len(lst2)):
# #     tol = 0
# #     for j in range(len(lst2[i])):
# #         tol += lst2 [i][j]
# #     print ('sum for row % d is '%i,tol)

# for i in range(len(lst2)):
#     tol= 0
#     for j in range(len(lst2[i])):
#         tol+=lst2[i][j]
#     print ('第 % d 列的欄位值總和 '%i,tol)
# 輸出結果
# Enter the number of row: 4
# Enter the number of column: 3
# [[4, 9, 40], [49, 7, 33], [49, 44, 44], [7, 44, 22]]
# sum for row  0 is  53
# sum for row  1 is  89
# sum for row  2 is  137
# sum for row  3 is  73

# # 反過來說，要求每一行的和，將行置於外圈，將列數置於內圈進行計算。

# for i in range(len(lst2)):
#     tol = 0
#     for j in range(len(lst2[i])):
#         tol += lst2 [j][i]
#     print ('total for column % d is '%i,tol)
# # 輸出結果
# # Enter the number of row: 2
# # Enter the number of column: 3
# # [[12, 44, 10], [4, 18, 7]]

# # sum for column  0 is  16
# # sum for column  1 is  62
# # sum for column  2 is  17

# # 上次課程中有提到 sum(list)這個函數，可以加總串列 (列) 每一個元素，所以計算一個列的和，還可以用以下方法

# for row in range(len(lst2)):
#     tol = 0
#     tol += sum(lst2[row])
#     print('sum for row %d is %d'%(row,tol))
    
# # 輸出結果
# # [[5, 40, 49, 5], [14, 46, 43, 29], [41, 39, 36, 45]]

# # sum for row 0 is 99
# # sum for row 1 is 132
# # sum for row 2 is 161

# #######撲克牌######################撲克牌
# 撲克（a deck of cards）共有四種花色(four suits)
# 比大小時依序為：
# spade 黑桃 / heart 紅心 / diamond 方塊 / club 梅花

# 一種花色有 13 張數字，2-10 為正常數字唸法，1 點為 A。
# 其他非數字的花牌（face cards）有：
# Jack J（騎士，11 點）/ Queen Q（皇后，12點）/ King K（國王，13 點）
# (1)	試寫出抽一張牌比大小

# color1="spade" 
# color2="heart"
# color3="diamond"
# color4="club"
# def randomCardColorNumber():
#     import random
#     randomcolor= random.randint(1,4)
#     randomnumber= random.randint(1,13)
#     return randomnumber,randomcolor
    
# import random
# # 花色
# colors = ['♠','♥','♦','♣']

# # 抽牌
# def draw_card():
#     color = random.choice(colors)        # 隨機花色
#     number = random.randint(1, 13)       # 隨機點數 (1~13)
#     return color, number

# # 轉換數字為撲克牌符號
# def card_to_str(color, number):
#     if number == 1:
#         rank = "A"
#     elif number == 11:
#         rank = "J"
#     elif number == 12:
#         rank = "Q"
#     elif number == 13:
#         rank = "K"
#     else:
#         rank = str(number)
#     return f"{color} {rank}"

# #1.電腦和你抽一張比大小
# def play_style1():
#     com_color, com_number = draw_card()
#     player_color, player_number = draw_card()

#     print("電腦抽到:", card_to_str(com_color, com_number))
#     print("玩家抽到:", card_to_str(player_color, player_number))

#     if com_number > player_number:
#         print("電腦贏了！")
#     elif com_number < player_number:
#         print("玩家贏了！")
#     else:
#         print("平手！")
# play_style1()
# #2.上面範例 A 為點數 1為最小，請將A改為最大牌。
# def card_value(number):
#     # 將 A (1) 當作最大牌
#     return 14 if number == 1 else number  # 2~13 保持原數字
# import random

# # 抽牌
# def draw_card():
#     number = random.randint(1,13)
#     return number

# # 比大小
# com_number = draw_card()
# player_number = draw_card()

# # 將 A 設為最大牌
# com_val = card_value(com_number)
# player_val = card_value(player_number)

# # 顯示牌
# def card_to_str(number):
#     if number == 1:
#         return "A"
#     elif number == 11:
#         return "J"
#     elif number == 12:
#         return "Q"
#     elif number == 13:
#         return "K"
#     else:
#         return str(number)

# print("電腦抽到:", card_to_str(com_number))
# print("玩家抽到:", card_to_str(player_number))

# if com_val > player_val:
#     print("電腦贏了！")
# elif com_val < player_val:
#     print("玩家贏了！")
# else:
#     print("平手！")

#3. 只用一副牌
# import random

# # 定義花色
# colors = ["spade", "heart", "diamond", "club"]

# # 建立一副牌 (每張牌唯一)
# deck = [(color, number) for color in colors for number in range(1, 14)]

# # 將 A 設為最大牌
# def card_value(number):
#     return 14 if number == 1 else number

# # 將數字轉成撲克牌符號
# def card_to_str(color, number):
#     if number == 1:
#         rank = "A"
#     elif number == 11:
#         rank = "J"
#     elif number == 12:
#         rank = "Q"
#     elif number == 13:
#         rank = "K"
#     else:
#         rank = str(number)
#     return f"{color} {rank}"

# # 從牌堆抽一張牌，並移除，確保唯一
# def draw_card(deck):
#     card = random.choice(deck)
#     deck.remove(card)
#     return card

# # 比大小遊戲
# def play_style1(deck):
#     if len(deck) < 2:
#         print("牌不足兩張，遊戲結束！")
#         return

#     com_color, com_number = draw_card(deck)
#     player_color, player_number = draw_card(deck)

#     print("電腦抽到:", card_to_str(com_color, com_number))
#     print("玩家抽到:", card_to_str(player_color, player_number))

#     # 將 A 設為最大牌
#     com_val = card_value(com_number)
#     player_val = card_value(player_number)

#     if com_val > player_val:
#         print("電腦贏了！")
#     elif com_val < player_val:
#         print("玩家贏了！")
#     else:
#         print("平手！")

# # 執行範例
# deck_copy = deck.copy()  # 複製一副牌，避免修改原本 deck
# play_style1(deck_copy)


# 練習題
# # 1.	輸入兩個正整數，當作串列的 列數 與 行數 ，每個位置存放內容為那個位置本身的 "行數索引值" 減去 "列數索引值" 的結果。

# row_count= int(input("輸入列數"))
# col_count = int(input("輸入行數"))
# lst = [[j - i for j in range(col_count)] for i in range(row_count)]
# for i in range(row_count):
#     for j in range(col_count):
#         print(f"{lst[i][j]:4d}", end="")  # 格式化排版
#     print()  # 換行


# 2.	輸入三位學生各五筆平時測驗成績，接著計算並輸出每位總分與平均
# def score():
#     num_students = int(input("輸入有幾個學生"))
#     num_scores = 5
#     for i in range(1,num_students+1):
            
#         listscore = []
        
#         print(f"請輸入第{i}位學生的成績")        
#         for j in range(1,num_scores+1):
#             score_input = int(input(f"輸入第{j}次成績"))
#             listscore.append(score_input)
#         print(f"第{i}位學生的成績")
        
#         totalscore= sum(listscore)
#         avescore=totalscore/num_scores
#         print(f"第{i}位學生的總分{totalscore}，平均{avescore}") 
#         print()          
# score()
# def score():
#     num_students = 3
#     num_scores = 5

#     for i in range(1, num_students + 1):
#         listscore = []  # 存放每位學生成績
#         print(f"請輸入第{i}位同學的成績：")
#         for j in range(1, num_scores + 1):
#             score_input = int(input(f"  第{j}筆成績: "))
#             listscore.append(score_input)

#         totalscore = sum(listscore)
#         avgscore = totalscore / num_scores
#         print(f"第{i}位同學總分: {totalscore}, 平均: {avgscore:.2f}")
#         print()  # 換行

# score()

# 3.	建立一個3 * 3的串列矩陣，內容為鍵盤輸入的整數(不能重複)，接著輸出矩陣最大與最小值的索引。

### Q3. 建立一個3 * 3的串列矩陣，內容為鍵盤輸入的整數(不能重複)，
#    接著輸出矩陣最大與最小值的索引。

# matrix = []  # 建立空矩陣
# used = set() # 用來檢查是否重複
# print("請依序輸入 3x3 矩陣的整數 (不能重複)：")
# for i in range(3):
#     row = []
#     for j in range(3):
#         while True:
#             num = int(input(f"請輸入第 {i} 列 第 {j} 行的整數: "))
#             if num in used:
#                 print("⚠️ 這個數字已經輸入過，請重新輸入！")
#             else:
#                 used.add(num)
#                 row.append(num)
#                 break
#     matrix.append(row)
# # 印出矩陣
# print("\n你輸入的 3x3 矩陣：")
# for row in matrix:
#     print(row)
# # 找最大值與最小值
# max_val = matrix[0][0]
# min_val = matrix[0][0]
# max_pos = (0, 0)
# min_pos = (0, 0)
# for i in range(3):
#     for j in range(3):
#         if matrix[i][j] > max_val:
#             max_val = matrix[i][j]
#             max_pos = (i, j)
#         if matrix[i][j] < min_val:
#             min_val = matrix[i][j]
#             min_pos = (i, j)
# # 輸出結果
# print(f"\n最大值: {max_val}，位置: {max_pos}")
# print(f"最小值: {min_val}，位置: {min_pos}")

# 4.	讓使用者建立2個 2* 2的串列矩陣內容，內容為鍵盤輸入的整數，接著輸出這兩個矩陣內容及相加結果。

# def input_matrix(n,m,name="矩陣"):
#     matrix = []
#     print(f"\n請輸入 {name} 的內容：")
#     for i in range(n):
#         row=[]
#         for j in range (m):
#             num=int(input(f"輸入整數：第{i}列第{j}列"))
#             row.append(num)
#         matrix.append(row)
#         print("\n目前矩陣內容：")
#         for r in matrix:
#             print(r)
#     return matrix
# matrix1=input_matrix(2,2,"矩陣1")
# matrix2=input_matrix(2,2,"矩陣2")
# # 計算相加結果
# total = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]
# # 印出結果
# print("\n矩陣1：")
# for row in matrix1:
#     print(row)

# print("\n矩陣2：")
# for row in matrix2:
#     print(row)

# print("\n相加結果：")
# for row in total:
#     print(row)
    
    
# # 5.	使用者建立四週各三天溫度，接著計算並輸出這四週的平均溫度，及最高最低溫。
# ##Q5
# def input_tep(n,m,name="溫度"):
#     matrix = []
#     print(f"\n請輸入 {name} 的溫度：")
#     for i in range(n):
#         row=[]
#         for j in range(m):
#             num=int(input(f"輸入第{i+1}周,第{j+1}天的溫度"))
#             row.append(num)
#         matrix.append(row)
#         print(matrix)
#     return matrix
# def each_week_tep(n,m,name):
#     溫度=input_tep(n,m,name)
#     print("\n完整輸入後的溫度：")
#     for i in range(len(溫度)):          # i 是周索引
#         for j in range(len(溫度[i])):   # j 是天索引

#             某天溫度 = 溫度[i][j]
#             print(f"第 {i+1} 周, 第 {j+1} 天 = {某天溫度} 度")
#         print(f"第{i+1}周溫度")
#     return 溫度
# 四周三天 = each_week_tep(2, 2, "四周三天")

# 6.	主程式 main( ) 宣告一個名為 lst、大小為5的整數串列，傳給函式 output(aList)。
# output(aList)函式讓使用者輸入串列內容，傳回主程式輸出。
# 主程式將串列傳給自定義的 min(aList)和max(aList)函式，各自計算最大值和最小值並傳回主程式輸出。
# ##Q6
# def output(size):
#     aList = []
#     for i in range(size):
#         num = int(input(f"輸入第 {i+1} 個整數: "))
#         aList.append(num)
#     return aList
# def min(aList):
#     min_val =aList[0]
#     for num in aList:
#         if num<min_val:
#             min_val=num
#     return min_val
# def max(aList):
#     max_val =aList[0]
#     for num in aList:
#         if num>max_val:
#             max_val=num
#     return max_val
# def main( ):
#     lst = output(5)  # 大小為 5 的整數串列
#     print("輸入的串列:", lst)

#     min_val = min(lst)
#     max_val = max(lst)

#     print(f"最小值：{min_val} ｜ 最大值：{max_val}")

# main()
# ##Q6
# def output(size):
#     aList = []
#     for i in range(size):
#         num = int(input(f"輸入第 {i+1} 個整數: "))
#         aList.append(num)
#     return aList
# # 自訂找最小值
# def my_min(aList):
#     min_val =aList[0]
#     for num in aList:
#         if num<min_val:
#             min_val=num
#     return min_val
# #自訂找最大值
# def my_max(aList):
#     max_val=aList[0]
#     for num in aList:
#         if num > max_val:
#             max_val=num
#     return max_val
# def main():
#     lst = output(5)  # 大小為 5 的整數串列
#     print("輸入的串列:", lst)

#     min_val = my_min(lst)
#     max_val = my_max(lst)

#     print(f"最小值：{min_val} ｜ 最大值：{max_val}")

# main()

# # # 7.	主程式 main()中，讓使用者輸入不重複的10個數字到串列，將串列傳遞給 compute()函式，函式接收一個串列lst 和一個變數 a (預設值為3)，並傳回lst中a個最大數字，將結果回傳主程式 main()輸出。
#Q7
# def compute(lst,a=3):
    
#     sorted_lst = sorted(lst, reverse=True)
#     return sorted_lst[:a]
# def main():
#     numbers = []  # 存使用者輸入的數字
#     print("請輸入不重複的10個數字：")

#     while len(numbers) < 10:
#         num=int(input(f"請輸入第{len(numbers)+1}個數字："))
#         if num in numbers:
#             print("輸入沒輸入過的10個數字")
#         else:
#             numbers.append(num)
#     max_numbers = compute(numbers)  # 預設 a=3
#     print(f"輸入的串列為：{numbers}")
#     print(f"最大3個數字為：{max_numbers}")
# main()

#Q7
# def compute(lst, a=3):
#     """
#     接收一個串列 lst 與變數 a (預設3)
#     回傳 lst 中 a 個最大數字 (由大到小)
#     """
#     # 先排序（由大到小）
#     sorted_lst = sorted(lst, reverse=True)
#     # 取前 a 個
#     return sorted_lst[:a]
# def main():
#     numbers = []  # 存使用者輸入的數字
#     print("請輸入不重複的10個數字：")

#     while len(numbers) < 10:
#         try:
#             num = int(input(f"請輸入第 {len(numbers)+1} 個數字："))
#             if num in numbers:
#                 print("這個數字已經輸入過了，請輸入其他數字！")
#             else:
#                 numbers.append(num)
#         except ValueError:
#             print("請輸入整數！")

#     # 呼叫 compute() 取出最大的3個數字
#     max_numbers = compute(numbers)  # 預設 a=3
#     print(f"輸入的串列為：{numbers}")
#     print(f"最大3個數字為：{max_numbers}")


# # 執行主程式
# if __name__ == "__main__":
#     main()

    
# 8.	使用lotto ()產生6個樂透號碼，並以main()函式呼叫5次lotto()函式產生五組號碼，並由小到大排序出來。


# import random

# def lotto():
#     """產生 6 個由小到大排序的樂透號碼"""
#     return sorted(random.sample(range(1, 50), k=6))

# def main(times):
#     """呼叫 lotto() times 次，回傳所有組號碼的 list"""
#     matrix = []
#     for _ in range(times):
#         matrix.append(lotto())
#     return matrix

# def print_lotto(all_numbers):
#     print("樂透號碼 (每組6個，由小到大排序) ")
#     print("---------------------------")
#     for idx, nums in enumerate(all_numbers, start=1):
#         print(f"第 {idx} 組：", end="")
#         for n_idx, num in enumerate(nums, start=1):
#             if n_idx != len(nums):
#                 print(f"第{n_idx:2}個號碼：{num:2}, ", end="")
#             else:
#                 print(f"第{n_idx:2}個號碼：{num:2}")  # 最後一個換行

# # 使用範例
# all_numbers = main(5)
# print_lotto(all_numbers)