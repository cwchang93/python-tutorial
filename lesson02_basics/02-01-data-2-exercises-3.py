"""
02-01：Python 資料結構基礎（List / Tuple / Dict / Set）

學習目標：
- 認識四大常用資料結構：List、Tuple、Dict、Set 的基本操作與差異
- 能讀懂並使用索引、增刪改查、避免常見錯誤（IndexError / KeyError / TypeError）
- 透過情境題選擇合適的資料結構並做簡單計算

使用方式：
- 直接執行本檔：`python 02-01-data-2-exercises-3.py`
- 依提示輸入題號（例如 "1-2"）可單獨跑某題；直接按 Enter 會依序跑全部題目。
- 每題皆有簡易示範輸出；若尚未完成 TODO，會顯示範例輸出供對照。

建議學習方法：
- 先自己完成 TODO，再執行查看輸出是否符合預期。
- 不要一開始看解答區；真的卡關再參考底部的「解答區」。
"""

# ==========
# Q0-1 變數與 list 的型態
# 題目描述：建立 name（字串）與 names（list），並用 type() 印出兩者型態。
# TODO：建立變數並印出型態
# 提示：type(name), type(names)
# 預期輸出（示例）：
# <class 'str'>
# <class 'list'>
# ==========
def q0_1():
    # TODO: 建立 name 與 names，並印出型態
    # name = ?
    # names = ?
    # print(type(name))
    # print(type(names))
    raise NotImplementedError("請完成 Q0-1")


# ==========
# Q0-2 真實世界資料結構選擇
# 題目描述：根據描述選擇合適的資料結構（用字串印出答案）。
# TODO：分別印出對應的資料結構
# 提示：單一地點座標 -> Tuple；購物車商品列表 -> List；會員資料（含欄位） -> Dict；不重複標籤 -> Set
# 預期輸出（示例）：
# 單一地點座標：Tuple
# 購物車商品列表：List
# 會員資料：Dict
# 不重複標籤：Set
# ==========
def q0_2():
    # TODO: 印出每個描述最合適的資料結構
    # print("單一地點座標：", ?)
    # print("購物車商品列表：", ?)
    # print("會員資料：", ?)
    # print("不重複標籤：", ?)
    raise NotImplementedError("請完成 Q0-2")


# ==========
# Q1-1 List 長度與平均
# 題目描述：給定 scores，印出元素個數與平均值。
# TODO：計算 len 與平均
# 提示：len(scores)、sum(scores) / len(scores)
# 預期輸出（示例）：
# 長度：5
# 平均：82.0
# ==========
def q1_1():
    scores = [80, 75, 90, 85, 80]
    # TODO: 計算並印出長度與平均
    # length = ?
    # average = ?
    # print("長度：", length)
    # print("平均：", average)
    raise NotImplementedError("請完成 Q1-1")


# ==========
# Q1-2 List 索引練習
# 題目描述：印出 items 的第一個與最後一個元素。
# TODO：使用 items[0] 與 items[-1]
# 提示：負索引 -1 代表最後一個
# 預期輸出（示例）：
# 第一個：apple
# 最後一個：orange
# ==========
def q1_2():
    items = ["apple", "banana", "orange"]
    # TODO: 印出第一個與最後一個
    # print("第一個：", ?)
    # print("最後一個：", ?)
    raise NotImplementedError("請完成 Q1-2")


# ==========
# Q1-3 List 修改元素
# 題目描述：將 foods 中的 "Pizza" 改成 "Salad"。
# TODO：找到索引並修改
# 提示：foods[?] = "Salad"
# 預期輸出（示例）：
# ['Burger', 'Salad', 'Fries']
# ==========
def q1_3():
    foods = ["Burger", "Pizza", "Fries"]
    # TODO: 把 Pizza 改成 Salad
    # foods[?] = "Salad"
    # print(foods)
    raise NotImplementedError("請完成 Q1-3")


# ==========
# Q1-4 List append / insert
# 題目描述：對 cart 做 append 與 insert 操作。
# TODO：append "milk"，在索引 1 insert "tea"
# 提示：cart.append()、cart.insert(index, item)
# 預期輸出（示例）：
# ['bread', 'tea', 'eggs', 'milk']
# ==========
def q1_4():
    cart = ["bread", "eggs"]
    # TODO: append 與 insert
    # cart.append(?)
    # cart.insert(?, ?)
    # print(cart)
    raise NotImplementedError("請完成 Q1-4")


# ==========
# Q1-5 List remove / pop
# 題目描述：移除 users 中的 "guest"，再 pop 最後一個並印出 last_one。
# TODO：使用 remove 與 pop
# 提示：users.remove("guest")；last_one = users.pop()
# 預期輸出（示例）：
# 移除後列表：['alice', 'bob']
# last_one：bob
# ==========
def q1_5():
    users = ["alice", "guest", "bob"]
    # TODO: 移除 guest，並 pop 最後一個
    # users.remove(?)
    # last_one = users.pop()
    # print("移除後列表：", users)
    # print("last_one：", last_one)
    raise NotImplementedError("請完成 Q1-5")


# ==========
# Q1-6 避免 IndexError
# 題目描述：安全讀取 nums[5]，若不存在印 "out of range"。
# TODO：使用條件判斷長度或 try/except
# 提示：len(nums) > 5 或 try/except IndexError
# 預期輸出（示例）：
# out of range
# ==========
def q1_6():
    nums = [10, 20, 30]
    # TODO: 安全讀取 nums[5]
    # if ...:
    #     print(nums[5])
    # else:
    #     print("out of range")
    raise NotImplementedError("請完成 Q1-6")


# ==========
# Q2-1 Tuple 取值
# 題目描述：gps = (25.04, 121.56)，印出緯度與經度。
# TODO：使用索引 0 與 1
# 提示：print("緯度：", gps[0])
# 預期輸出（示例）：
# 緯度： 25.04
# 經度： 121.56
# ==========
def q2_1():
    gps = (25.04, 121.56)
    # TODO: 印出緯度與經度
    # print("緯度：", ?)
    # print("經度：", ?)
    raise NotImplementedError("請完成 Q2-1")


# ==========
# Q2-2 Tuple 不可變
# 題目描述：示範 tuple 不可修改，捕捉 TypeError 並印提示。
# TODO：嘗試 gps[0] = 0 並用 try/except 捕捉
# 提示：except TypeError as e: print(...)
# 預期輸出（示例）：
# 發現錯誤：tuple 不可修改 -> 'tuple' object does not support item assignment
# ==========
def q2_2():
    gps = (25.04, 121.56)
    # TODO: 嘗試修改並捕捉 TypeError
    # try:
    #     gps[0] = 0
    # except TypeError as e:
    #     print("發現錯誤：tuple 不可修改 ->", e)
    raise NotImplementedError("請完成 Q2-2")


# ==========
# Q2-3 Tuple vs List 選擇題
# 題目描述：列舉情境並選擇適合 tuple 或 list，印出答案與一句理由。
# TODO：至少列出 1 個情境並印出
# 提示：固定座標/生日 -> tuple；會增減的待辦清單 -> list
# 預期輸出（示例）：
# 座標資料：tuple（因為座標固定不會改變）
# 待辦清單：list（因為會增減項目）
# ==========
def q2_3():
    # TODO: 印出情境與選擇原因
    # print("座標資料：tuple（原因：...）")
    # print("待辦清單：list（原因：...）")
    raise NotImplementedError("請完成 Q2-3")


# ==========
# Q3-1 Dict 取值
# 題目描述：student dict，印出 name。
# TODO：使用方括號或 get
# 提示：student["name"]
# 預期輸出（示例）：
# 姓名：Amy
# ==========
def q3_1():
    student = {"name": "Amy", "age": 18}
    # TODO: 印出姓名
    # print("姓名：", ?)
    raise NotImplementedError("請完成 Q3-1")


# ==========
# Q3-2 Dict 新增與修改
# 題目描述：修改 data["a"] = 2，新增 data["b"] = 3，印出結果。
# TODO：完成修改與新增
# 提示：直接賦值
# 預期輸出（示例）：
# {'a': 2, 'b': 3}
# ==========
def q3_2():
    data = {"a": 1}
    # TODO: 修改與新增
    # data["a"] = ?
    # data["b"] = ?
    # print(data)
    raise NotImplementedError("請完成 Q3-2")


# ==========
# Q3-3 Dict 刪除鍵
# 題目描述：刪除 data 中的 b。
# TODO：使用 del
# 提示：del data["b"]
# 預期輸出（示例）：
# {'a': 1}
# ==========
def q3_3():
    data = {"a": 1, "b": 2}
    # TODO: 刪除 b
    # del data["b"]
    # print(data)
    raise NotImplementedError("請完成 Q3-3")


# ==========
# Q3-4 Dict 安全讀取
# 題目描述：安全讀取不存在的 key，不要拋 KeyError。
# TODO：用 in 或 get 讀取 data["c"]
# 提示：data.get("c", "not found")
# 預期輸出（示例）：
# c 是否存在：False
# c 值：not found
# ==========
def q3_4():
    data = {"a": 1, "b": 2}
    # TODO: 安全讀取
    # exists = "c" in data
    # value = data.get("c", "not found")
    # print("c 是否存在：", exists)
    # print("c 值：", value)
    raise NotImplementedError("請完成 Q3-4")


# ==========
# Q4-1 Set 去重
# 題目描述：將 nums 轉成 set 去除重複並印出。
# TODO：使用 set(nums)
# 提示：print(set(nums))
# 預期輸出（示例）：
# {1, 2, 3, 4}
# ==========
def q4_1():
    nums = [1, 2, 2, 3, 4, 4]
    # TODO: 去重並印出
    # unique_nums = ?
    # print(unique_nums)
    raise NotImplementedError("請完成 Q4-1")


# ==========
# Q4-2 Set add / remove
# 題目描述：對 emails 進行 add（含重複）與 remove，觀察結果。
# TODO：加入重複值、移除一個值後印出
# 提示：emails.add(...)；emails.remove(...)
# 預期輸出（示例）：
# {'a@test.com', 'b@test.com'}
# ==========
def q4_2():
    emails = {"a@test.com"}
    # TODO: add 重複與新值，並 remove
    # emails.add("a@test.com")
    # emails.add("b@test.com")
    # emails.remove("a@test.com")
    # print(emails)
    raise NotImplementedError("請完成 Q4-2")


# ==========
# Q4-3 Set 聯集與交集（加分）
# 題目描述：對 a, b 做交集與聯集，印出結果。
# TODO：使用 a & b、a | b
# 提示：intersection = a & b；union = a | b
# 預期輸出（示例）：
# 交集：{3, 4}
# 聯集：{1, 2, 3, 4, 5}
# ==========
def q4_3():
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    # TODO: 計算交集與聯集
    # inter = ?
    # uni = ?
    # print("交集：", inter)
    # print("聯集：", uni)
    raise NotImplementedError("請完成 Q4-3")


# ==========
# Q5-1 情境選擇題
# 題目描述：針對不同情境選擇 List/Dict/Set/Tuple 並說明。
# TODO：至少列出 2 個情境並印出答案
# 提示：通訊錄（姓名+電話） -> Dict；彩票號碼（不重複） -> Set
# 預期輸出（示例）：
# 通訊錄：Dict（因為需要鍵值對存姓名與電話）
# 彩票號碼：Set（因為需要自動去重）
# ==========
def q5_1():
    # TODO: 印出情境與理由
    # print("通訊錄：Dict（原因：...）")
    # print("彩票號碼：Set（原因：...）")
    raise NotImplementedError("請完成 Q5-1")


# ==========
# Q5-2 小綜合：scores 分析
# 題目描述：計算平均、最高、最低、去重後平均。
# TODO：完成計算並印出
# 提示：max(scores), min(scores), set 去重
# 預期輸出（示例）：
# 平均：84.0
# 最高：100
# 最低：70
# 去重後平均：82.5
# ==========
def q5_2():
    scores = [90, 80, 100, 70, 80]
    # TODO: 計算平均、最高、最低、去重後平均
    # avg = ?
    # high = ?
    # low = ?
    # unique_avg = ?
    # print("平均：", avg)
    # print("最高：", high)
    # print("最低：", low)
    # print("去重後平均：", unique_avg)
    raise NotImplementedError("請完成 Q5-2")


def run_question(qid: str):
    mapping = QUESTIONS.get(qid)
    if not mapping:
        print(f"找不到題號：{qid}")
        return
    title = mapping["title"]
    func = mapping["func"]
    sample = mapping["sample"]
    print(f"\n=== {qid} {title} ===")
    try:
        func()
    except NotImplementedError:
        print("TODO 尚未完成，以下為範例輸出供參考：")
        print(sample)
    except Exception as exc:  # 避免某題錯誤中斷全部
        print(f"⚠️ 執行 {qid} 發生錯誤：{exc}")
        print("可參考範例輸出：")
        print(sample)


QUESTIONS = {
    "0-1": {
        "title": "變數與 list 的型態",
        "func": q0_1,
        "sample": "<class 'str'>\n<class 'list'>",
    },
    "0-2": {
        "title": "資料結構選擇",
        "func": q0_2,
        "sample": "單一地點座標：Tuple\n購物車商品列表：List\n會員資料：Dict\n不重複標籤：Set",
    },
    "1-1": {
        "title": "List 長度與平均",
        "func": q1_1,
        "sample": "長度： 5\n平均： 82.0",
    },
    "1-2": {
        "title": "List 索引練習",
        "func": q1_2,
        "sample": "第一個： apple\n最後一個： orange",
    },
    "1-3": {
        "title": "List 修改元素",
        "func": q1_3,
        "sample": "['Burger', 'Salad', 'Fries']",
    },
    "1-4": {
        "title": "List append / insert",
        "func": q1_4,
        "sample": "['bread', 'tea', 'eggs', 'milk']",
    },
    "1-5": {
        "title": "List remove / pop",
        "func": q1_5,
        "sample": "移除後列表： ['alice', 'bob']\nlast_one： bob",
    },
    "1-6": {
        "title": "避免 IndexError",
        "func": q1_6,
        "sample": "out of range",
    },
    "2-1": {
        "title": "Tuple 取值",
        "func": q2_1,
        "sample": "緯度： 25.04\n經度： 121.56",
    },
    "2-2": {
        "title": "Tuple 不可變",
        "func": q2_2,
        "sample": "發現錯誤：tuple 不可修改 -> 'tuple' object does not support item assignment",
    },
    "2-3": {
        "title": "Tuple vs List 選擇",
        "func": q2_3,
        "sample": "座標資料：tuple（因為座標固定不會改變）\n待辦清單：list（因為會增減項目）",
    },
    "3-1": {
        "title": "Dict 取值",
        "func": q3_1,
        "sample": "姓名： Amy",
    },
    "3-2": {
        "title": "Dict 新增與修改",
        "func": q3_2,
        "sample": "{'a': 2, 'b': 3}",
    },
    "3-3": {
        "title": "Dict 刪除鍵",
        "func": q3_3,
        "sample": "{'a': 1}",
    },
    "3-4": {
        "title": "Dict 安全讀取",
        "func": q3_4,
        "sample": "c 是否存在： False\nc 值： not found",
    },
    "4-1": {
        "title": "Set 去重",
        "func": q4_1,
        "sample": "{1, 2, 3, 4}",
    },
    "4-2": {
        "title": "Set add / remove",
        "func": q4_2,
        "sample": "{'a@test.com', 'b@test.com'}",
    },
    "4-3": {
        "title": "Set 聯集與交集",
        "func": q4_3,
        "sample": "交集： {3, 4}\n聯集： {1, 2, 3, 4, 5}",
    },
    "5-1": {
        "title": "情境選擇題",
        "func": q5_1,
        "sample": "通訊錄：Dict（因為需要鍵值對存姓名與電話）\n彩票號碼：Set（因為需要自動去重）",
    },
    "5-2": {
        "title": "小綜合：scores 分析",
        "func": q5_2,
        "sample": "平均： 84.0\n最高： 100\n最低： 70\n去重後平均： 82.5",
    },
}


if __name__ == "__main__":
    print("Python 資料結構基礎練習（輸入題號如 1-1；直接 Enter 跑全部）")
    user_choice = input("請輸入題號（或直接 Enter）：").strip()

    if user_choice:
        run_question(user_choice)
    else:
        for qid in QUESTIONS:
            run_question(qid)


# --- 解答區（請先自己寫再看） ---
# Q0-1 解答：
# def q0_1():
#     name = "Alice"
#     names = ["Bob", "Cindy"]
#     print(type(name))
#     print(type(names))
#
# Q0-2 解答：
# def q0_2():
#     print("單一地點座標：Tuple")
#     print("購物車商品列表：List")
#     print("會員資料：Dict")
#     print("不重複標籤：Set")
#
# Q1-1 解答：
# def q1_1():
#     scores = [80, 75, 90, 85, 80]
#     length = len(scores)
#     average = sum(scores) / length
#     print("長度：", length)
#     print("平均：", average)
#
# Q1-2 解答：
# def q1_2():
#     items = ["apple", "banana", "orange"]
#     print("第一個：", items[0])
#     print("最後一個：", items[-1])
#
# Q1-3 解答：
# def q1_3():
#     foods = ["Burger", "Pizza", "Fries"]
#     foods[1] = "Salad"
#     print(foods)
#
# Q1-4 解答：
# def q1_4():
#     cart = ["bread", "eggs"]
#     cart.append("milk")
#     cart.insert(1, "tea")
#     print(cart)
#
# Q1-5 解答：
# def q1_5():
#     users = ["alice", "guest", "bob"]
#     users.remove("guest")
#     last_one = users.pop()
#     print("移除後列表：", users)
#     print("last_one：", last_one)
#
# Q1-6 解答：
# def q1_6():
#     nums = [10, 20, 30]
#     if len(nums) > 5:
#         print(nums[5])
#     else:
#         print("out of range")
#
# Q2-1 解答：
# def q2_1():
#     gps = (25.04, 121.56)
#     print("緯度：", gps[0])
#     print("經度：", gps[1])
#
# Q2-2 解答：
# def q2_2():
#     gps = (25.04, 121.56)
#     try:
#         gps[0] = 0
#     except TypeError as e:
#         print("發現錯誤：tuple 不可修改 ->", e)
#
# Q2-3 解答：
# def q2_3():
#     print("座標資料：tuple（因為座標固定不會改變）")
#     print("待辦清單：list（因為會增減項目）")
#
# Q3-1 解答：
# def q3_1():
#     student = {"name": "Amy", "age": 18}
#     print("姓名：", student["name"])
#
# Q3-2 解答：
# def q3_2():
#     data = {"a": 1}
#     data["a"] = 2
#     data["b"] = 3
#     print(data)
#
# Q3-3 解答：
# def q3_3():
#     data = {"a": 1, "b": 2}
#     del data["b"]
#     print(data)
#
# Q3-4 解答：
# def q3_4():
#     data = {"a": 1, "b": 2}
#     exists = "c" in data
#     value = data.get("c", "not found")
#     print("c 是否存在：", exists)
#     print("c 值：", value)
#
# Q4-1 解答：
# def q4_1():
#     nums = [1, 2, 2, 3, 4, 4]
#     unique_nums = set(nums)
#     print(unique_nums)
#
# Q4-2 解答：
# def q4_2():
#     emails = {"a@test.com"}
#     emails.add("a@test.com")
#     emails.add("b@test.com")
#     emails.remove("a@test.com")
#     print(emails)
#
# Q4-3 解答：
# def q4_3():
#     a = {1, 2, 3, 4}
#     b = {3, 4, 5}
#     inter = a & b
#     uni = a | b
#     print("交集：", inter)
#     print("聯集：", uni)
#
# Q5-1 解答：
# def q5_1():
#     print("通訊錄：Dict（因為需要鍵值對存姓名與電話）")
#     print("彩票號碼：Set（因為需要自動去重）")
#
# Q5-2 解答：
# def q5_2():
#     scores = [90, 80, 100, 70, 80]
#     avg = sum(scores) / len(scores)
#     high = max(scores)
#     low = min(scores)
#     unique_avg = sum(set(scores)) / len(set(scores))
#     print("平均：", avg)
#     print("最高：", high)
#     print("最低：", low)
#     print("去重後平均：", unique_avg)
