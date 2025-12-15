"""
Lesson 02：輸出 print 基礎
- 為什麼需要輸出：讓程式執行結果能被看見
- print 的基本用法（中英數字皆可）
- 同一個 print 輸出多個內容
- 調整分隔符號 sep 與結尾符號 end

執行本檔即可看到對應的範例輸出。
"""


def section(title: str) -> None:
    """小段落標題，讓輸出區隔更清楚。"""
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)


section("為什麼要學輸出：呈現程式執行的結果")
result = 1 + 1
print("1 + 1 的結果是", result)

section("print 的基本用法：可以輸出中英數混和")
print("Hello world!")
print("是在哈囉")
print("python 好棒棒")
print("ಠ_ಠ")
print("9487")   # 字串 9487
print(9487)     # 數字 9487，輸出看起來一樣但型態不同

section("同一個 print 輸出多個內容，逗號分隔 -> 會自動補空格")
print("是在", "哈囉")
print("是在", "Hello")
print(94, 87)
print(7, "pupu")
print("不想考指考", "(ಥ_ಥ)")

section("調整分隔符號 sep：預設是空格")
print("台灣", "發大財", sep="")      # 空字串：內容緊貼
print("台灣", "發大財", sep="\n")    # 換行符號：強制換行
print("台灣", "發大財", sep="$")     # 自訂符號：用 $ 分隔

section("調整結尾符號 end：預設自動換行")
print("python")
print("南波萬")
print("python", end="")    # end="" -> 不換行，下一段接著輸出
print("南波萬")
print("python", end="~~")  # 自訂結尾符號
print("南波萬", end="~~")
print()  # 手動補一個換行，避免下一個提示接在同一行

section("input 基本用法：取得使用者輸入（會回傳字串）")
# 提醒：真正執行 input() 會等待使用者輸入，這裡先用示意值展示效果
print("input('提示文字') -> 會等待輸入，按 Enter 後回傳字串")
demo_name = "小明"  # 假設使用者輸入「小明」
print("嗨，", demo_name, "，歡迎來到 Python！")

section("將 input 的字串轉成數字再運算")
print("大多數運算需要數字，請用 int() 或 float() 轉型")
demo_age_str = "18"           # 假設 input 回傳的字串
demo_age = int(demo_age_str)  # 轉成 int
print("字串", demo_age_str, "轉成整數後 +1 =", demo_age + 1)

section("實際使用 input 的範例（想體驗請取消註解）")
# name = input("請輸入姓名：")
# print("Hello,", name)
# age = int(input("請輸入年齡："))
# print("明年你就", age + 1, "歲啦！")
