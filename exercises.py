"""
小試身手：依提示完成程式並執行，確認輸出/型態與預期一致。
建議逐題完成，理解概念再看 solutions.py。
"""

# 題目 1：變數與賦值
# 步驟：x 先給 10，之後更新為 20，將 x 指派給 y，再印出 y。
x = 10
# TODO: 依提示完成下方兩行
x = 10
x = 20
y = x
# y = ?
print("題目 1 y =", y)

# 題目 2：變數命名規則
# 下列哪些名稱合法？請把合法的放進 legal_names。
candidate_names = ["2nd_place", "my-name", "class", "user_id", "Score", "score"]
legal_names = []  # TODO: 填入合法名稱字串（不需真的建立變數）
# TODO: 建立一個符合 snake_case 的變數，表示使用者年齡，例如 user_age
# user_age = ?
# print("user_age =", user_age)

# 題目 3：資料型態與 type()
# 請建立下列變數並印出它們的型態：10, "10", 5.0, True, "True"
# 提示：使用 type() 函式
# a = 10
# b = "10"
# c = 5.0
# d = True
# e = "True"
# print(type(a))

# 題目 4：型態轉換 (Casting)
# 1) 計算 int("50") + 10，印出結果與型態
# 2) 計算 str(10) + "20"，觀察結果是 "1020" 還是 30
# hint_result1 = ?
# hint_result2 = ?
# print(hint_result1, type(hint_result1))
# print(hint_result2, type(hint_result2))

# 題目 5：字串操作
# 1) 將 "Super" 與 "Man" 串接
# 2) 使用 f-string 將 name 與 age 放入句子中
name = "Amy"
age = 18
# superman = ?
# sentence = ?
# print(superman)
# print(sentence)
# 3) 嘗試執行 print("Age: " + 18) 會發生什麼？請修正成正確寫法（不報錯）

# 題目 6：數學與邏輯運算
# 1) 計算 4 / 2、7 // 2、7 % 2、2 ** 3，印出結果與型態
# 2) 比較運算：10 == 10、10 > 20
# div_result = ?
# floor_result = ?
# mod_result = ?
# pow_result = ?
# print(div_result, type(div_result))
# print(floor_result, mod_result, pow_result)
# print(10 == 10)
# print(10 > 20)
# 3) 指定運算子：令 x = 5，使用 x += 1，印出 x

# 題目 7：運算優先順序
# 1) 計算 5 + 2 * 3，觀察結果應為 11
# 2) 計算 (5 + 2) * 3，觀察結果
# expr1 = ?
# expr2 = ?
# print(expr1)
# print(expr2)

# 題目 8：縮排 (Indentation)
# 下方程式會發生 IndentationError，請重新排版讓它能正常執行。
# 提示：if 內的敘述需要縮排。
code = """
age = 16
if age >= 18:
print("可以考駕照")
else:
print("還不能考駕照")
"""
# TODO: 將上面的程式修正後貼在下方，並執行確認不報錯
