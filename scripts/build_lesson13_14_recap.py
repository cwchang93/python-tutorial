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


PATH_SETUP = '''from pathlib import Path

csv_path = Path("lesson13_14_review_orders.csv")'''


def csv_rows_setup():
    return PATH_SETUP + '''

import csv

with csv_path.open(encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)'''


def pandas_setup():
    return PATH_SETUP + '''

import pandas as pd

df = pd.read_csv(csv_path)'''


QUESTIONS = [
    {
        "lesson": "Lesson 13",
        "title": "辨認列、欄與儲存格",
        "prompt": "觀察兩筆訂單。請印出資料列數、第一筆訂單的商品，以及第二筆訂單的數量。",
        "starter": "orders = [\n    {'order_id': 'A001', 'product': '拿鐵', 'quantity': 2},\n    {'order_id': 'A002', 'product': '貝果', 'quantity': 3},\n]\n\n# 請印出列數與指定儲存格",
        "answer": "orders = [\n    {'order_id': 'A001', 'product': '拿鐵', 'quantity': 2},\n    {'order_id': 'A002', 'product': '貝果', 'quantity': 3},\n]\n\nprint('資料列數：', len(orders))\nprint('第一筆商品：', orders[0]['product'])\nprint('第二筆數量：', orders[1]['quantity'])",
    },
    {
        "lesson": "Lesson 13",
        "title": "欄位名稱與資料意義",
        "prompt": "完成 columns，讓每個欄名都對應正確用途，再逐筆印出。",
        "starter": "columns = {\n    'order_id': '',\n    'product': '',\n    'quantity': '',\n    'unit_price': '',\n}\n\n# 請填入說明並逐筆印出",
        "answer": "columns = {\n    'order_id': '訂單編號',\n    'product': '商品名稱',\n    'quantity': '購買數量',\n    'unit_price': '商品單價',\n}\n\nfor column, meaning in columns.items():\n    print(column, '：', meaning)",
    },
    {
        "lesson": "Lesson 13",
        "title": "從原始欄位算出營業額",
        "prompt": "使用 for 逐筆計算 `quantity * unit_price`，把結果存入每筆訂單的 `revenue`，最後印出訂單。",
        "starter": "orders = [\n    {'product': '拿鐵', 'quantity': 2, 'unit_price': 120},\n    {'product': '貝果', 'quantity': 3, 'unit_price': 65},\n]\n\n# 請逐筆新增 revenue",
        "answer": "orders = [\n    {'product': '拿鐵', 'quantity': 2, 'unit_price': 120},\n    {'product': '貝果', 'quantity': 3, 'unit_price': 65},\n]\n\nfor order in orders:\n    revenue = order['quantity'] * order['unit_price']\n    order['revenue'] = revenue\n\nfor order in orders:\n    print(order)",
    },
    {
        "lesson": "Lesson 13",
        "title": "使用 DictReader 讀取 CSV",
        "prompt": "讀取本複習提供的 CSV，印出欄名、資料筆數與第一筆資料。提醒：DictReader 讀出的每一列是 Dict。",
        "starter": PATH_SETUP + "\n\nimport csv\n\n# 請使用 csv.DictReader 讀取資料",
        "answer": csv_rows_setup() + "\n\nprint('欄名：', reader.fieldnames)\nprint('資料筆數：', len(rows))\nprint('第一筆：', rows[0])",
    },
    {
        "lesson": "Lesson 13",
        "title": "CSV 數字欄位需要轉型",
        "prompt": "CSV 的 quantity 與 unit_price 讀進來是字串。請轉成 int，逐筆計算並累加總營業額。",
        "starter": csv_rows_setup() + "\n\ntotal_revenue = 0\n# 請逐筆轉型並累加",
        "answer": csv_rows_setup() + "\n\ntotal_revenue = 0\nfor row in rows:\n    quantity = int(row['quantity'])\n    unit_price = int(row['unit_price'])\n    revenue = quantity * unit_price\n    total_revenue += revenue\n\nprint('總營業額：', total_revenue)",
    },
    {
        "lesson": "Lesson 13",
        "title": "用 Dict 累計商品銷量",
        "prompt": "逐筆讀取 CSV，用 Dict 累加每種商品的 quantity，最後逐項印出商品與總數量。",
        "starter": csv_rows_setup() + "\n\nproduct_quantity = {}\n# 請完成累加",
        "answer": csv_rows_setup() + "\n\nproduct_quantity = {}\nfor row in rows:\n    product = row['product']\n    quantity = int(row['quantity'])\n\n    if product not in product_quantity:\n        product_quantity[product] = 0\n\n    product_quantity[product] += quantity\n\nfor product, quantity in product_quantity.items():\n    print(product, quantity)",
    },
    {
        "lesson": "Lesson 13",
        "title": "用 Set 找不重複城市",
        "prompt": "逐筆把 city 加入 Set，最後印出城市數量與排序後的城市。",
        "starter": csv_rows_setup() + "\n\ncities = set()\n# 請完成",
        "answer": csv_rows_setup() + "\n\ncities = set()\nfor row in rows:\n    cities.add(row['city'])\n\nprint('城市數量：', len(cities))\nprint('城市：', sorted(cities))",
    },
    {
        "lesson": "Lesson 13",
        "title": "檢查空白與重複編號",
        "prompt": "檢查 dirty_orders：找出含空白欄位的資料，並找出重複的 order_id。請保留完整步驟。",
        "starter": "dirty_orders = [\n    {'order_id': 'A001', 'product': '拿鐵', 'city': '台北'},\n    {'order_id': 'A002', 'product': '', 'city': '台中'},\n    {'order_id': 'A001', 'product': '貝果', 'city': '高雄'},\n]\n\nblank_rows = []\nduplicate_ids = []\nseen_ids = set()\n# 請完成檢查",
        "answer": "dirty_orders = [\n    {'order_id': 'A001', 'product': '拿鐵', 'city': '台北'},\n    {'order_id': 'A002', 'product': '', 'city': '台中'},\n    {'order_id': 'A001', 'product': '貝果', 'city': '高雄'},\n]\n\nblank_rows = []\nduplicate_ids = []\nseen_ids = set()\n\nfor order in dirty_orders:\n    has_blank = False\n    for value in order.values():\n        if value == '':\n            has_blank = True\n\n    if has_blank:\n        blank_rows.append(order)\n\n    order_id = order['order_id']\n    if order_id in seen_ids:\n        duplicate_ids.append(order_id)\n    else:\n        seen_ids.add(order_id)\n\nprint('空白資料：', blank_rows)\nprint('重複編號：', duplicate_ids)",
    },
    {
        "lesson": "Lesson 14",
        "title": "用 Pandas 讀入 DataFrame",
        "prompt": "使用 `pd.read_csv()` 讀取複習 CSV，印出物件型態與前 5 列。",
        "starter": PATH_SETUP + "\n\nimport pandas as pd\n\n# 請讀取成 df 並查看型態與前 5 列",
        "answer": pandas_setup() + "\n\nprint(type(df))\nprint(df.head())",
    },
    {
        "lesson": "Lesson 14",
        "title": "用 shape 回答表格大小",
        "prompt": "讀取 DataFrame，將 shape 拆成 rows 與 columns，再用完整文字輸出列數與欄數。",
        "starter": pandas_setup() + "\n\n# 請拆開 df.shape",
        "answer": pandas_setup() + "\n\nrows, columns = df.shape\nprint('資料列數：', rows)\nprint('資料欄數：', columns)",
    },
    {
        "lesson": "Lesson 14",
        "title": "確認欄名與資料型態",
        "prompt": "印出 columns 與 dtypes，並確認 quantity 是不是整數型態。",
        "starter": pandas_setup() + "\n\n# 請查看欄名與資料型態",
        "answer": pandas_setup() + "\n\nprint('欄名：', list(df.columns))\nprint('資料型態：')\nprint(df.dtypes)\nprint('quantity 型態：', df['quantity'].dtype)",
    },
    {
        "lesson": "Lesson 14",
        "title": "分辨 Series 與 DataFrame",
        "prompt": "分別選取單一 product 欄，以及 product、quantity 兩欄；印出兩個結果的型態與 shape。",
        "starter": pandas_setup() + "\n\n# 單中括號選一欄；雙中括號選多欄",
        "answer": pandas_setup() + "\n\nproduct_series = df['product']\nproduct_table = df[['product', 'quantity']]\n\nprint(type(product_series))\nprint(product_series.shape)\nprint(type(product_table))\nprint(product_table.shape)",
    },
    {
        "lesson": "Lesson 14",
        "title": "從頭、尾與隨機位置抽查",
        "prompt": "依序使用 head(3)、tail(3)、sample(3, random_state=42) 抽查資料，並加上清楚標題。",
        "starter": pandas_setup() + "\n\n# 請使用三種抽查方式",
        "answer": pandas_setup() + "\n\nprint('前 3 列：')\nprint(df.head(3))\n\nprint('最後 3 列：')\nprint(df.tail(3))\n\nprint('隨機 3 列：')\nprint(df.sample(3, random_state=42))",
    },
    {
        "lesson": "Lesson 14",
        "title": "檢查缺值與重複資料",
        "prompt": "印出每欄缺值數量、完整重複列數量，以及重複 order_id 的數量。",
        "starter": pandas_setup() + "\n\n# 請使用 isna、duplicated",
        "answer": pandas_setup() + "\n\nprint('每欄缺值：')\nprint(df.isna().sum())\nprint('完整重複列：', df.duplicated().sum())\nprint('重複訂單編號：', df.duplicated(subset=['order_id']).sum())",
    },
    {
        "lesson": "Lesson 14",
        "title": "閱讀數值摘要與類別數量",
        "prompt": "使用 describe() 查看數值摘要，再用 nunique() 查看商品、城市與付款方式各有幾種。",
        "starter": pandas_setup() + "\n\n# 請查看數值摘要與類別數量",
        "answer": pandas_setup() + "\n\nprint('數值摘要：')\nprint(df[['quantity', 'unit_price']].describe())\n\nprint('不重複值數量：')\nprint(df[['product', 'city', 'payment']].nunique())",
    },
    {
        "lesson": "Lesson 13–14",
        "title": "整合練習：從 CSV 到第一份資料健檢報告",
        "prompt": "建立 `check_dataframe(df)`：回傳資料大小、欄名、型態、缺值、重複列、重複 order_id 與各城市訂單筆數。呼叫後印出前三列和報告，最後用一句話說明資料是否適合進入下一步分析。",
        "starter": pandas_setup() + "\n\ndef check_dataframe(df):\n    # 請完成並 return 報告\n    pass\n\nreport = check_dataframe(df)\n# 請印出前三列、報告與判斷結果",
        "answer": pandas_setup() + "\n\ndef check_dataframe(df):\n    rows, columns = df.shape\n    report = {\n        'rows': rows,\n        'columns': columns,\n        'column_names': list(df.columns),\n        'data_types': df.dtypes.astype(str).to_dict(),\n        'missing': int(df.isna().sum().sum()),\n        'duplicate_rows': int(df.duplicated().sum()),\n        'duplicate_order_ids': int(df.duplicated(subset=['order_id']).sum()),\n        'orders_by_city': df['city'].value_counts().to_dict(),\n    }\n    return report\n\n\nreport = check_dataframe(df)\nprint('前三列：')\nprint(df.head(3))\nprint('健康檢查報告：')\nfor item, value in report.items():\n    print(item, '：', value)\n\nif report['missing'] == 0 and report['duplicate_rows'] == 0:\n    print('初步檢查完成：資料可以進入下一步分析。')\nelse:\n    print('資料還有品質問題，應先確認與清理。')",
    },
]


def build(solutions=False):
    title = "# Lesson 13–14 課前複習"
    intro = """從表格、CSV 與欄位型態開始，接著使用 Pandas 讀入 DataFrame 並完成第一次資料健康檢查。

- Lesson 13：題目 1–8，練習列、欄、CSV、型態轉換與基礎統計。
- Lesson 14：題目 9–15，練習 DataFrame、Series 與資料巡檢。
- 整合：題目 16，完成一份可讀的資料健康報告。

請把 `lesson13_14_review_orders.csv` 和 Notebook 放在同一資料夾。"""

    if solutions:
        title += "｜講師解答"
        intro = """每題保留完整步驟，方便逐行講解；不使用三元表達式或過度濃縮的一行寫法。

請把 `lesson13_14_review_orders.csv` 和 Notebook 放在同一資料夾。"""

    cells = [markdown(f"{title}\n\n{intro}")]
    for number, item in enumerate(QUESTIONS, 1):
        cells.append(
            markdown(
                f"## {item['lesson']}｜題目 {number}：{item['title']}\n\n{item['prompt']}"
            )
        )
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
    ("lesson13_14_review.ipynb", False),
    ("lesson13_14_review_solutions.ipynb", True),
]:
    path = RECAP / filename
    path.write_text(
        json.dumps(build(solutions), ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


source_csv = ROOT / "course_v2" / "data" / "lesson13_orders.csv"
recap_csv = RECAP / "lesson13_14_review_orders.csv"
recap_csv.write_bytes(source_csv.read_bytes())

print("Lesson 13–14 recap and local CSV created.")
