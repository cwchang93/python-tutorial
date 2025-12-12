"""
進階練習：更多 Python 基礎題目
涵蓋：字串方法、列表、元組、字典、集合、條件判斷、迴圈等基礎概念
"""

# ==================== 字串進階操作 ====================

# 題目 1：字串方法
# 使用字串方法完成下列操作
text = "  Python Programming  "
# 1) 移除前後空白
# cleaned = ?
# 2) 轉換為全大寫
# upper_text = ?
# 3) 轉換為全小寫
# lower_text = ?
# 4) 計算字串長度
# text_length = ?
# print(cleaned, upper_text, lower_text, text_length)

# 題目 2：字串切片
# 使用切片操作取得字串的不同部分
message = "Hello World"
# 1) 取得前 5 個字元
# first_five = ?
# 2) 取得後 5 個字元
# last_five = ?
# 3) 取得第 2 到第 7 個字元（索引 1 到 6）
# middle = ?
# 4) 反轉整個字串
# reversed_msg = ?
# print(first_five, last_five, middle, reversed_msg)

# 題目 3：字串搜尋與替換
sentence = "I love Python and Python loves me"
# 1) 檢查 "Python" 是否在句子中
# has_python = ?
# 2) 找出 "Python" 第一次出現的位置
# position = ?
# 3) 計算 "Python" 出現幾次
# count = ?
# 4) 將所有 "Python" 替換成 "JavaScript"
# new_sentence = ?
# print(has_python, position, count, new_sentence)

# ==================== 列表 (List) ====================

# 題目 4：列表基本操作
fruits = ["apple", "banana", "cherry"]
# 1) 在列表末尾加入 "orange"
# TODO: fruits.append(?)
# 2) 在索引 1 的位置插入 "mango"
# TODO: fruits.insert(?, ?)
# 3) 移除 "banana"
# TODO: fruits.remove(?)
# 4) 印出列表長度
# print(len(fruits))
# 5) 印出最終的列表
# print(fruits)

# 題目 5：列表切片與複製
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1) 取得前 3 個數字
# first_three = ?
# 2) 取得後 3 個數字
# last_three = ?
# 3) 取得所有偶數索引的數字（0, 2, 4...）
# even_indices = ?
# 4) 複製整個列表（使用切片）
# numbers_copy = ?
# print(first_three, last_three, even_indices, numbers_copy)

# 題目 6：列表排序
scores = [85, 92, 78, 95, 88]
# 1) 排序列表（由小到大）
# TODO: scores.sort()
# 2) 找出最高分
# max_score = ?
# 3) 找出最低分
# min_score = ?
# 4) 計算平均分（提示：使用 sum() 和 len()）
# average = ?
# print(scores, max_score, min_score, average)

# ==================== 元組 (Tuple) ====================

# 題目 7：元組基本操作
point = (3, 4)
# 1) 取得 x 座標（第一個元素）
# x = ?
# 2) 取得 y 座標（第二個元素）
# y = ?
# 3) 嘗試修改元組會發生什麼？（註解掉以免報錯）
# point[0] = 5  # 這行會報錯
# 4) 將元組轉換成列表
# point_list = ?
# print(x, y, point_list)

# 題目 8：元組解包
student = ("Alice", 20, "Computer Science")
# 使用解包取得姓名、年齡、科系
# name, age, major = ?
# print(name, age, major)

# ==================== 字典 (Dictionary) ====================

# 題目 9：字典基本操作
person = {
    "name": "Bob",
    "age": 25,
    "city": "Taipei"
}
# 1) 取得 name 的值
# person_name = ?
# 2) 新增一個鍵值對：job = "Engineer"
# TODO: person["job"] = ?
# 3) 修改 age 為 26
# TODO: person["age"] = ?
# 4) 刪除 city 這個鍵
# TODO: del person["city"]
# 5) 印出所有的鍵
# print(person.keys())
# 6) 印出所有的值
# print(person.values())
# 7) 印出最終的字典
# print(person)

# 題目 10：字典方法
product = {
    "name": "Laptop",
    "price": 30000,
    "stock": 5
}
# 1) 使用 get() 方法取得 price（如果不存在回傳 0）
# price = ?
# 2) 使用 get() 取得不存在的鍵 "discount"（預設值 10）
# discount = ?
# 3) 檢查 "stock" 是否在字典中
# has_stock = ?
# print(price, discount, has_stock)

# ==================== 集合 (Set) ====================

# 題目 11：集合基本操作
colors = {"red", "green", "blue"}
# 1) 加入 "yellow"
# TODO: colors.add(?)
# 2) 移除 "green"
# TODO: colors.remove(?)
# 3) 嘗試加入重複的 "red"，觀察結果
# TODO: colors.add("red")
# 4) 印出集合
# print(colors)

# 題目 12：集合運算
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
# 1) 聯集（所有不重複的元素）
# union = ?
# 2) 交集（共同的元素）
# intersection = ?
# 3) 差集（在 set_a 但不在 set_b）
# difference = ?
# print(union, intersection, difference)

# ==================== 條件判斷 ====================

# 題目 13：if-elif-else
score = 75
# 根據分數給予評級：
# >= 90: A
# >= 80: B
# >= 70: C
# >= 60: D
# < 60: F
# grade = ?
# TODO: 使用 if-elif-else 完成
# print("Grade:", grade)

# 題目 14：多重條件
age = 20
has_license = True
# 判斷是否可以租車（年齡 >= 18 且有駕照）
# can_rent = ?
# TODO: 使用 and 運算子
# print("Can rent car:", can_rent)

# 題目 15：三元運算子
temperature = 28
# 如果溫度 >= 30 則為 "Hot"，否則為 "Warm"
# weather = ?  # 使用 value_if_true if condition else value_if_false
# print("Weather:", weather)

# ==================== 迴圈 ====================

# 題目 16：for 迴圈基礎
# 1) 印出 1 到 5 的所有數字
# TODO: for i in range(?):
#     print(i)

# 2) 印出列表中的每個水果
fruits = ["apple", "banana", "cherry"]
# TODO: for fruit in ?:
#     print(fruit)

# 3) 印出 2 到 10 的偶數
# TODO: for i in range(?, ?, ?):
#     print(i)

# 題目 17：while 迴圈
# 1) 從 10 倒數到 1
# count = 10
# TODO: while ?:
#     print(count)
#     count -= 1

# 2) 計算 1 到 100 的總和
# total = 0
# n = 1
# TODO: while ?:
#     total += n
#     n += 1
# print("Sum:", total)

# 題目 18：break 和 continue
# 1) 找出第一個能被 7 整除的數字（從 1 開始）
# TODO: for i in range(1, 100):
#     if ?:
#         print("First number divisible by 7:", i)
#         break

# 2) 印出 1 到 10 中的奇數（使用 continue 跳過偶數）
# TODO: for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# ==================== 綜合應用 ====================

# 題目 19：列表推導式 (List Comprehension)
# 1) 建立包含 1 到 10 的平方數的列表
# squares = ?  # [1, 4, 9, 16, ...]
# print(squares)

# 2) 從列表中篩選出大於 50 的數字
numbers = [23, 67, 45, 89, 12, 56, 34, 78]
# large_numbers = ?  # 使用列表推導式
# print(large_numbers)

# 題目 20：綜合練習
# 建立一個學生成績系統
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]
# 1) 印出所有學生的名字
# TODO: for student in students:
#     print(student["name"])

# 2) 計算平均分數
# total_score = 0
# TODO: 使用迴圈計算
# average_score = ?
# print("Average score:", average_score)

# 3) 找出分數最高的學生
# top_student = ?
# TODO: 使用迴圈或 max() 函式
# print("Top student:", top_student)

# 4) 找出及格的學生（分數 >= 80）
# passed_students = []
# TODO: 使用迴圈或列表推導式
# print("Passed students:", passed_students)

print("\n=== 所有練習完成！===")
print("完成後可以對照 solutions-2.py 檢查答案")
