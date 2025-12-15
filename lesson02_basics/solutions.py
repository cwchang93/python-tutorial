"""
參考解答：對照 exercises.py。
可以直接執行本檔案，觀察輸出與型態。
"""

# 題目 1：變數與賦值
x = 10
x = 20          # 右邊的值覆蓋左邊原有的 10
y = x           # y 得到 20
print("題目 1 y =", y)  # 20

# 題目 2：變數命名規則
candidate_names = ["2nd_place", "my-name", "class", "user_id", "Score", "score"]
# 合法的：user_id, Score, score（class 是保留字；數字開頭與含 - 都不行）
legal_names = ["user_id", "Score", "score"]
print("題目 2 合法名稱 =", legal_names)
# 建立 snake_case 變數
user_age = 18
print("user_age =", user_age)

# 題目 3：資料型態與 type()
a = 10          # int
b = "10"        # str
c = 5.0         # float
d = True        # bool
e = "True"      # str
print(type(a), type(b), type(c), type(d), type(e))

# 題目 4：型態轉換 (Casting)
result1 = int("50") + 10      # 60, int
result2 = str(10) + "20"      # "1020", str
print(result1, type(result1))
print(result2, type(result2))

# 題目 5：字串操作
name = "Amy"
age = 18
superman = "Super" + "Man"
sentence = f"{name} 已經 {age} 歲"
print(superman)               # SuperMan
print(sentence)               # 例如 "Amy 已經 18 歲"
# 錯誤示範：print("Age: " + 18) -> TypeError
print("Age:", age)            # 或 print("Age: " + str(age))

# 題目 6：數學與邏輯運算
div_result = 4 / 2            # 2.0 (float)
floor_result = 7 // 2         # 3
mod_result = 7 % 2            # 1
pow_result = 2 ** 3           # 8
print(div_result, type(div_result))
print(floor_result, mod_result, pow_result)
print(10 == 10)               # True
print(10 > 20)                # False
x = 5
x += 1
print("x after += 1 ->", x)   # 6

# 題目 7：運算優先順序
expr1 = 5 + 2 * 3     # 11
expr2 = (5 + 2) * 3   # 21
print(expr1)
print(expr2)

# 題目 8：縮排 (Indentation) 修正版
age = 16
if age >= 18:
    print("可以考駕照")
else:
    print("還不能考駕照")
