"""
進階練習解答：exercises-2.py 的參考答案
建議先自行完成練習，遇到困難再參考此檔案
"""

# ==================== 字串進階操作 ====================

# 題目 1：字串方法
text = "  Python Programming  "
cleaned = text.strip()  # 移除前後空白
upper_text = text.upper()  # 轉換為全大寫
lower_text = text.lower()  # 轉換為全小寫
text_length = len(text)  # 計算字串長度
print("題目 1:")
print("Cleaned:", cleaned)
print("Upper:", upper_text)
print("Lower:", lower_text)
print("Length:", text_length)
print()

# 題目 2：字串切片
message = "Hello World"
first_five = message[:5]  # 取得前 5 個字元
last_five = message[-5:]  # 取得後 5 個字元
middle = message[1:7]  # 取得第 2 到第 7 個字元
reversed_msg = message[::-1]  # 反轉整個字串
print("題目 2:")
print("First 5:", first_five)
print("Last 5:", last_five)
print("Middle:", middle)
print("Reversed:", reversed_msg)
print()

# 題目 3：字串搜尋與替換
sentence = "I love Python and Python loves me"
has_python = "Python" in sentence  # 檢查是否包含
position = sentence.find("Python")  # 找出第一次出現的位置
count = sentence.count("Python")  # 計算出現次數
new_sentence = sentence.replace("Python", "JavaScript")  # 替換
print("題目 3:")
print("Has Python:", has_python)
print("Position:", position)
print("Count:", count)
print("New sentence:", new_sentence)
print()

# ==================== 列表 (List) ====================

# 題目 4：列表基本操作
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # 在末尾加入
fruits.insert(1, "mango")  # 在索引 1 插入
fruits.remove("banana")  # 移除特定元素
print("題目 4:")
print("Length:", len(fruits))
print("Fruits:", fruits)
print()

# 題目 5：列表切片與複製
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_three = numbers[:3]  # 前 3 個
last_three = numbers[-3:]  # 後 3 個
even_indices = numbers[::2]  # 偶數索引
numbers_copy = numbers[:]  # 複製列表
print("題目 5:")
print("First 3:", first_three)
print("Last 3:", last_three)
print("Even indices:", even_indices)
print("Copy:", numbers_copy)
print()

# 題目 6：列表排序
scores = [85, 92, 78, 95, 88]
scores.sort()  # 排序
max_score = max(scores)  # 最高分
min_score = min(scores)  # 最低分
average = sum(scores) / len(scores)  # 平均分
print("題目 6:")
print("Sorted scores:", scores)
print("Max:", max_score)
print("Min:", min_score)
print("Average:", average)
print()

# ==================== 元組 (Tuple) ====================

# 題目 7：元組基本操作
point = (3, 4)
x = point[0]  # 取得第一個元素
y = point[1]  # 取得第二個元素
# point[0] = 5  # 這行會報錯，因為元組不可變
point_list = list(point)  # 轉換成列表
print("題目 7:")
print("x:", x, "y:", y)
print("Point as list:", point_list)
print()

# 題目 8：元組解包
student = ("Alice", 20, "Computer Science")
name, age, major = student  # 解包
print("題目 8:")
print("Name:", name)
print("Age:", age)
print("Major:", major)
print()

# ==================== 字典 (Dictionary) ====================

# 題目 9：字典基本操作
person = {
    "name": "Bob",
    "age": 25,
    "city": "Taipei"
}
person_name = person["name"]  # 取得值
person["job"] = "Engineer"  # 新增鍵值對
person["age"] = 26  # 修改值
del person["city"]  # 刪除鍵
print("題目 9:")
print("Name:", person_name)
print("Keys:", person.keys())
print("Values:", person.values())
print("Person:", person)
print()

# 題目 10：字典方法
product = {
    "name": "Laptop",
    "price": 30000,
    "stock": 5
}
price = product.get("price", 0)  # 使用 get()
discount = product.get("discount", 10)  # 取得不存在的鍵
has_stock = "stock" in product  # 檢查鍵是否存在
print("題目 10:")
print("Price:", price)
print("Discount:", discount)
print("Has stock:", has_stock)
print()

# ==================== 集合 (Set) ====================

# 題目 11：集合基本操作
colors = {"red", "green", "blue"}
colors.add("yellow")  # 加入元素
colors.remove("green")  # 移除元素
colors.add("red")  # 加入重複元素（不會改變集合）
print("題目 11:")
print("Colors:", colors)
print()

# 題目 12：集合運算
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union = set_a | set_b  # 聯集（也可用 set_a.union(set_b)）
intersection = set_a & set_b  # 交集（也可用 set_a.intersection(set_b)）
difference = set_a - set_b  # 差集（也可用 set_a.difference(set_b)）
print("題目 12:")
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print()

# ==================== 條件判斷 ====================

# 題目 13：if-elif-else
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("題目 13:")
print("Score:", score, "Grade:", grade)
print()

# 題目 14：多重條件
age = 20
has_license = True
can_rent = age >= 18 and has_license  # 使用 and 運算子
print("題目 14:")
print("Age:", age, "Has license:", has_license)
print("Can rent car:", can_rent)
print()

# 題目 15：三元運算子
temperature = 28
weather = "Hot" if temperature >= 30 else "Warm"  # 三元運算子
print("題目 15:")
print("Temperature:", temperature, "Weather:", weather)
print()

# ==================== 迴圈 ====================

# 題目 16：for 迴圈基礎
print("題目 16-1: 印出 1 到 5")
for i in range(1, 6):
    print(i, end=" ")
print()

print("題目 16-2: 印出水果")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")
print()

print("題目 16-3: 印出 2 到 10 的偶數")
for i in range(2, 11, 2):
    print(i, end=" ")
print("\n")

# 題目 17：while 迴圈
print("題目 17-1: 從 10 倒數到 1")
count = 10
while count > 0:
    print(count, end=" ")
    count -= 1
print()

print("題目 17-2: 計算 1 到 100 的總和")
total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print("Sum:", total)
print()

# 題目 18：break 和 continue
print("題目 18-1: 找出第一個能被 7 整除的數字")
for i in range(1, 100):
    if i % 7 == 0:
        print("First number divisible by 7:", i)
        break

print("題目 18-2: 印出 1 到 10 中的奇數")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n")

# ==================== 綜合應用 ====================

# 題目 19：列表推導式
print("題目 19-1: 1 到 10 的平方數")
squares = [i ** 2 for i in range(1, 11)]
print("Squares:", squares)

print("題目 19-2: 篩選大於 50 的數字")
numbers = [23, 67, 45, 89, 12, 56, 34, 78]
large_numbers = [n for n in numbers if n > 50]
print("Large numbers:", large_numbers)
print()

# 題目 20：綜合練習
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

print("題目 20-1: 所有學生名字")
for student in students:
    print(student["name"], end=" ")
print()

print("題目 20-2: 平均分數")
total_score = 0
for student in students:
    total_score += student["score"]
average_score = total_score / len(students)
print("Average score:", average_score)

print("題目 20-3: 分數最高的學生")
top_student = max(students, key=lambda s: s["score"])
print("Top student:", top_student["name"], "Score:", top_student["score"])

print("題目 20-4: 及格的學生")
passed_students = [s["name"] for s in students if s["score"] >= 80]
print("Passed students:", passed_students)

print("\n=== 所有解答完成！===")
