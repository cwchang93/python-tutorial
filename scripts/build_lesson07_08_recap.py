import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECAP = ROOT / "course_v2" / "recap"


def markdown(text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.splitlines()],
    }


def code(text):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in text.splitlines()],
    }


QUESTIONS = [
    {
        "lesson": "Lesson 07",
        "title": "while 基本計數",
        "prompt": "使用 while 依序印出 1、2、3、4、5。記得在迴圈中更新計數變數。",
        "starter": "count = 1\n# 請完成",
        "answer": "count = 1\n\nwhile count <= 5:\n    print(count)\n    count += 1",
    },
    {
        "lesson": "Lesson 07",
        "title": "倒數計時",
        "prompt": "使用 while 印出 5、4、3、2、1，最後顯示「時間到」。",
        "starter": "count = 5\n# 請完成",
        "answer": "count = 5\n\nwhile count >= 1:\n    print(count)\n    count -= 1\n\nprint('時間到')",
    },
    {
        "lesson": "Lesson 07",
        "title": "累加到指定數字",
        "prompt": "使用 while 計算 1 到 5 的總和，最後清楚顯示總和。",
        "starter": "number = 1\ntotal = 0\n# 請完成",
        "answer": "number = 1\ntotal = 0\n\nwhile number <= 5:\n    total += number\n    number += 1\n\nprint('總和：', total)",
    },
    {
        "lesson": "Lesson 07",
        "title": "密碼重試三次",
        "prompt": "密碼為 python123。最多輸入三次；答對顯示「登入成功」並停止，三次都錯則顯示「帳號已鎖定」。",
        "starter": "password = 'python123'\nattempts = 0\n# 請完成",
        "answer": "password = 'python123'\nattempts = 0\n\nwhile attempts < 3:\n    user_input = input('請輸入密碼：')\n    attempts += 1\n\n    if user_input == password:\n        print('登入成功')\n        break\n    else:\n        print('密碼錯誤')\nelse:\n    print('帳號已鎖定')",
    },
    {
        "lesson": "Lesson 07",
        "title": "數字格式驗證",
        "prompt": "持續要求輸入整數。格式錯誤時顯示提示並重新輸入；成功後印出該數字並停止。",
        "starter": "while True:\n    text = input('請輸入整數：')\n    # 請完成",
        "answer": "while True:\n    text = input('請輸入整數：')\n\n    try:\n        number = int(text)\n        print('你輸入的數字：', number)\n        break\n    except ValueError:\n        print('格式錯誤，請重新輸入')",
    },
    {
        "lesson": "Lesson 07",
        "title": "合理範圍驗證",
        "prompt": "持續要求輸入 1 到 5 的滿意度。不是整數或超出範圍時重新輸入。",
        "starter": "# 請使用 while、try / except 與範圍判斷",
        "answer": "while True:\n    text = input('滿意度（1～5）：')\n\n    try:\n        score = int(text)\n    except ValueError:\n        print('請輸入整數')\n        continue\n\n    if score < 1 or score > 5:\n        print('請輸入 1 到 5')\n        continue\n\n    print('已記錄：', score)\n    break",
    },
    {
        "lesson": "Lesson 07",
        "title": "選單操作",
        "prompt": "建立選單：輸入 1 顯示餘額、輸入 2 顯示交易紀錄、輸入 0 結束；其他輸入顯示「沒有這個選項」。",
        "starter": "while True:\n    print('1. 查看餘額')\n    print('2. 查看紀錄')\n    print('0. 結束')\n    choice = input('請選擇：')\n    # 請完成",
        "answer": "while True:\n    print('1. 查看餘額')\n    print('2. 查看紀錄')\n    print('0. 結束')\n    choice = input('請選擇：')\n\n    if choice == '1':\n        print('目前餘額：1500')\n    elif choice == '2':\n        print('目前有 3 筆紀錄')\n    elif choice == '0':\n        print('程式結束')\n        break\n    else:\n        print('沒有這個選項')",
    },
    {
        "lesson": "Lesson 07",
        "title": "收集多筆成績",
        "prompt": "持續輸入成績並加入 scores；輸入 end 時停止。只接受 0 到 100 的數字，最後印出全部成績。",
        "starter": "scores = []\n# 請完成",
        "answer": "scores = []\n\nwhile True:\n    text = input('成績（end 結束）：')\n\n    if text == 'end':\n        break\n\n    try:\n        score = float(text)\n    except ValueError:\n        print('格式錯誤')\n        continue\n\n    if score < 0 or score > 100:\n        print('成績必須介於 0 到 100')\n        continue\n\n    scores.append(score)\n\nprint('全部成績：', scores)",
    },
    {
        "lesson": "Lesson 08",
        "title": "定義並呼叫函式",
        "prompt": "建立 greet() 函式，呼叫時顯示「歡迎來到 Python 課程」。",
        "starter": "# 請定義並呼叫 greet()",
        "answer": "def greet():\n    print('歡迎來到 Python 課程')\n\ngreet()",
    },
    {
        "lesson": "Lesson 08",
        "title": "使用兩個參數",
        "prompt": "建立 show_product(name, price)，清楚印出商品名稱與價格，並以「筆記本」、120 呼叫。",
        "starter": "# 請定義 show_product(name, price)",
        "answer": "def show_product(name, price):\n    print('商品：', name)\n    print('價格：', price)\n\nshow_product('筆記本', 120)",
    },
    {
        "lesson": "Lesson 08",
        "title": "return 回傳小計",
        "prompt": "建立 calculate_subtotal(price, quantity)，回傳商品小計；呼叫後把答案存入 subtotal 再印出。",
        "starter": "# 請定義 calculate_subtotal(price, quantity)",
        "answer": "def calculate_subtotal(price, quantity):\n    subtotal = price * quantity\n    return subtotal\n\nsubtotal = calculate_subtotal(120, 3)\nprint('商品小計：', subtotal)",
    },
    {
        "lesson": "Lesson 08",
        "title": "print 與 return",
        "prompt": "建立 get_discount_price(price)，計算九折並 return。用回傳結果再加上 60 元運費，清楚顯示應付金額。",
        "starter": "# 函式內要 return，不要只 print",
        "answer": "def get_discount_price(price):\n    discount_price = price * 0.9\n    return discount_price\n\nprice_after_discount = get_discount_price(1000)\ntotal = price_after_discount + 60\nprint('應付金額：', total)",
    },
    {
        "lesson": "Lesson 08",
        "title": "回傳布林值",
        "prompt": "建立 is_passed(score)，分數大於等於 60 時回傳 True，否則回傳 False；再用完整 if / else 顯示結果。",
        "starter": "# 請定義 is_passed(score) 並使用完整 if / else",
        "answer": "def is_passed(score):\n    if score >= 60:\n        return True\n    else:\n        return False\n\nresult = is_passed(72)\n\nif result == True:\n    print('及格')\nelse:\n    print('需要補強')",
    },
    {
        "lesson": "Lesson 08",
        "title": "預設參數",
        "prompt": "建立 greet_member(name, message='歡迎')。分別使用預設訊息與自訂「早安」呼叫一次。",
        "starter": "# 請定義含有預設參數的函式",
        "answer": "def greet_member(name, message='歡迎'):\n    print(message, name)\n\ngreet_member('Amy')\ngreet_member('Bob', '早安')",
    },
    {
        "lesson": "Lesson 08",
        "title": "處理 List",
        "prompt": "建立 calculate_average(scores)。空 List 回傳 0；有資料時回傳平均分數。請測試兩種情況。",
        "starter": "# 請定義 calculate_average(scores)",
        "answer": "def calculate_average(scores):\n    if len(scores) == 0:\n        return 0\n\n    total = 0\n    for score in scores:\n        total += score\n\n    average = total / len(scores)\n    return average\n\nprint('平均：', calculate_average([80, 90, 70]))\nprint('空資料平均：', calculate_average([]))",
    },
    {
        "lesson": "Lesson 07–08",
        "title": "整合練習：安全成績報表",
        "prompt": "持續輸入 0 到 100 的成績，輸入 end 結束。請用函式驗證範圍、計算平均，最後顯示筆數與平均；沒有資料時顯示「沒有成績」。",
        "starter": "scores = []\n\n# 請先定義驗證與平均函式，再使用 while 收集資料",
        "answer": "def is_valid_score(score):\n    if score >= 0 and score <= 100:\n        return True\n    else:\n        return False\n\n\ndef calculate_average(scores):\n    if len(scores) == 0:\n        return None\n\n    total = 0\n    for score in scores:\n        total += score\n\n    return total / len(scores)\n\n\nscores = []\n\nwhile True:\n    text = input('成績（end 結束）：')\n\n    if text == 'end':\n        break\n\n    try:\n        score = float(text)\n    except ValueError:\n        print('格式錯誤')\n        continue\n\n    if is_valid_score(score) == False:\n        print('成績必須介於 0 到 100')\n        continue\n\n    scores.append(score)\n\naverage = calculate_average(scores)\n\nif average is None:\n    print('沒有成績')\nelse:\n    print('成績筆數：', len(scores))\n    print('平均分數：', average)",
    },
]


def build(solutions=False):
    title = "# Lesson 07–08 課前複習"
    intro = "先複習 while 迴圈與輸入驗證，再複習函式、參數與回傳值。每題先閱讀需求，再逐步完成。"
    if solutions:
        title += "｜講師解答"
        intro = "每題保留完整步驟，方便逐行講解；不使用三元表達式或過度濃縮的一行寫法。"

    cells = [markdown(f"{title}\n\n{intro}")]
    for number, item in enumerate(QUESTIONS, 1):
        heading = f"## {item['lesson']}｜題目 {number}：{item['title']}"
        cells.append(markdown(f"{heading}\n\n{item['prompt']}"))
        cells.append(code(item["answer"] if solutions else item["starter"]))

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


for filename, solutions in [
    ("lesson07_08_review.ipynb", False),
    ("lesson07_08_review_solutions.ipynb", True),
]:
    path = RECAP / filename
    path.write_text(json.dumps(build(solutions), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

print("Lesson 07–08 recap created.")
