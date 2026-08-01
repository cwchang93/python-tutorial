import json
from pathlib import Path

ROOT = Path(__file__).parent / "lessons"


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in text.split("\n")]}


def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + "\n" for line in text.split("\n")]}


def notebook(title, intro, items):
    cells = [md(f"# {title}\n\n{intro}")]
    for i, (heading, snippet) in enumerate(items, 1):
        cells.extend([md(f"## 例題 {i:02d}｜{heading}"), code(snippet)])
    return {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.x"}}, "nbformat": 4, "nbformat_minor": 5}


lesson09_learning = [
    ("錯誤訊息是線索", "print('先看最後一行錯誤類型')\nprint('再回頭找發生錯誤的程式碼')"),
    ("SyntaxError 語法錯誤", "# print('少一個右括號'\nprint('修正括號後就能執行')"),
    ("NameError 名稱不存在", "user_name = 'Amy'\nprint(user_name)"),
    ("TypeError 型別不相容", "price = 100\nquantity = 2\nprint(price * quantity)"),
    ("ValueError 內容無法轉換", "text = '42'\nnumber = int(text)\nprint(number + 8)"),
    ("IndexError 索引超出範圍", "colors = ['紅', '藍']\nprint(colors[0])\nprint(len(colors))"),
    ("KeyError 字典 key 不存在", "profile = {'name': 'Amy'}\nprint(profile.get('email', '未提供 email'))"),
    ("ZeroDivisionError 除以零", "total = 100\npeople = 0\nif people != 0:\n    print(total / people)\nelse:\n    print('人數不能是 0')"),
    ("try 保護可能失敗的程式", "try:\n    age = int('20')\n    print(age)\nexcept ValueError:\n    print('年齡格式錯誤')"),
    ("except 捕捉指定錯誤", "try:\n    score = int('abc')\nexcept ValueError:\n    print('請輸入整數分數')"),
    ("多種錯誤分開處理", "try:\n    numbers = [10, 20]\n    index = int('1')\n    print(numbers[index])\nexcept ValueError:\n    print('索引必須是整數')\nexcept IndexError:\n    print('索引超出範圍')"),
    ("except Exception 作為最後防線", "try:\n    result = 10 / 2\nexcept Exception as error:\n    print('發生錯誤：', error)\nelse:\n    print('結果：', result)"),
    ("else 只在成功時執行", "try:\n    number = int('25')\nexcept ValueError:\n    print('轉換失敗')\nelse:\n    print('轉換成功：', number)"),
    ("finally 一定會執行", "try:\n    print('開始處理')\nfinally:\n    print('清理或結束提示')"),
    ("錯誤時提供預設值", "try:\n    discount = float('abc')\nexcept ValueError:\n    discount = 0\nprint('折扣：', discount)"),
    ("安全輸入整數", "def read_int(text):\n    try:\n        return int(text)\n    except ValueError:\n        return None\n\nprint(read_int('18'))\nprint(read_int('十八'))"),
    ("驗證分數範圍", "def read_score(text):\n    try:\n        score = int(text)\n        if not 0 <= score <= 100:\n            return None\n        return score\n    except ValueError:\n        return None\n\nprint(read_score('88'))"),
    ("raise 主動提出錯誤", "def set_quantity(quantity):\n    if quantity < 0:\n        raise ValueError('數量不能是負數')\n    return quantity\n\nprint(set_quantity(3))"),
    ("捕捉自己提出的錯誤", "try:\n    raise ValueError('資料不完整')\nexcept ValueError as error:\n    print('請修正：', error)"),
    ("清楚顯示錯誤原因", "try:\n    amount = int('100')\n    print(1000 / amount)\nexcept (ValueError, ZeroDivisionError) as error:\n    print('輸入或計算錯誤：', error)"),
    ("清單逐筆轉換並略過錯誤", "raw_scores = ['90', 'abc', '75']\nscores = []\nfor raw in raw_scores:\n    try:\n        scores.append(int(raw))\n    except ValueError:\n        print('略過：', raw)\nprint(scores)"),
    ("保護字典查詢", "orders = {'A001': 120}\norder_id = 'A002'\ntry:\n    print(orders[order_id])\nexcept KeyError:\n    print('找不到訂單：', order_id)"),
    ("保護檔案開啟概念", "try:\n    file = open('not_found.txt', encoding='utf-8')\nexcept FileNotFoundError:\n    print('檔案不存在')"),
    ("錯誤紀錄清單", "errors = []\nfor value in ['10', 'x', '20']:\n    try:\n        int(value)\n    except ValueError:\n        errors.append(value)\nprint('錯誤資料：', errors)"),
    ("完整的資料輸入流程", "def parse_price(text):\n    try:\n        price = float(text)\n        if price < 0:\n            raise ValueError('價格不能小於 0')\n        return price\n    except ValueError as error:\n        print('價格錯誤：', error)\n        return None\n\nprint(parse_price('199.5'))"),
]

lesson09_ex = [
    ("安全轉換年齡", "把字串轉成整數；失敗時輸出『年齡格式錯誤』。"),
    ("安全計算平均", "當人數為 0 時不要除法，輸出『沒有資料』。"),
    ("清單索引防呆", "讓使用者輸入索引，捕捉 ValueError 與 IndexError。"),
    ("字典查詢防呆", "查詢會員 email，找不到時輸出『查無會員』。"),
    ("分數範圍驗證", "分數非 0～100 或不是整數時都視為錯誤。"),
    ("輸入折扣", "把折扣轉成 float，失敗時使用 0。"),
    ("try else", "成功讀取商品數量才計算小計，失敗時顯示提示。"),
    ("finally 提示", "模擬開始與結束工作，無論結果都印出『流程結束』。"),
    ("負數數量", "用 raise ValueError 阻止負數數量。"),
    ("捕捉自訂錯誤", "呼叫上題函式並捕捉 ValueError。"),
    ("多筆分數", "從字串清單轉成整數，略過無法轉換的項目。"),
    ("錯誤統計", "統計一批輸入中成功與失敗的筆數。"),
    ("訂單編號", "字典查詢訂單，不存在時輸出清楚訊息。"),
    ("檔案不存在", "開啟不存在的文字檔並捕捉 FileNotFoundError。"),
    ("多種例外", "同時處理 ValueError 與 ZeroDivisionError。"),
    ("安全平均函式", "寫一個函式，空清單回傳 None，否則回傳平均。"),
    ("安全價格函式", "價格不能為負，錯誤時回傳 None。"),
    ("錯誤訊息紀錄", "把每筆錯誤文字收集到 errors 清單。"),
    ("輸入三次", "處理三筆年齡資料並列出無效輸入。"),
    ("購物車小計", "數量或價格錯誤時不讓程式中斷。"),
    ("成績報表", "轉換成績並輸出最高分、最低分與錯誤筆數。"),
    ("安全除法", "寫 safe_divide(a, b)，b 為 0 回傳 None。"),
    ("錯誤分類", "將輸入錯誤分類為格式錯誤或範圍錯誤。"),
    ("資料驗證流程", "先轉換、再驗證範圍，成功才加入清單。"),
    ("綜合訂單檢查", "處理商品、數量與價格，輸出有效訂單總額。"),
]

lesson09_sol = [
    "try:\n    age = int('20')\nexcept ValueError:\n    print('年齡格式錯誤')",
    "total, people = 100, 0\nif people == 0:\n    print('沒有資料')\nelse:\n    print(total / people)",
    "items = ['a', 'b']\ntry:\n    index = int('3')\n    print(items[index])\nexcept ValueError:\n    print('索引格式錯誤')\nexcept IndexError:\n    print('索引超出範圍')",
    "members = {'Amy': 'amy@example.com'}\nprint(members.get('Bob', '查無會員'))",
    "try:\n    score = int('101')\n    if not 0 <= score <= 100:\n        raise ValueError\nexcept ValueError:\n    print('分數錯誤')",
    "try:\n    discount = float('x')\nexcept ValueError:\n    discount = 0\nprint(discount)",
    "try:\n    quantity = int('2')\nexcept ValueError:\n    print('數量格式錯誤')\nelse:\n    print('小計：', quantity * 50)",
    "try:\n    print('開始工作')\nfinally:\n    print('流程結束')",
    "def set_quantity(q):\n    if q < 0:\n        raise ValueError('數量不能為負')\n    return q",
    "try:\n    set_quantity(-1)\nexcept ValueError as error:\n    print(error)",
    "values = ['80', 'x', '95']\nscores = []\nfor value in values:\n    try:\n        scores.append(int(value))\n    except ValueError:\n        continue\nprint(scores)",
    "success = failed = 0\nfor value in ['1', 'x', '2']:\n    try:\n        int(value); success += 1\n    except ValueError:\n        failed += 1\nprint(success, failed)",
    "orders = {'A001': 300}\norder_id = 'A002'\ntry:\n    print(orders[order_id])\nexcept KeyError:\n    print('查無訂單')",
    "try:\n    open('missing.txt', encoding='utf-8')\nexcept FileNotFoundError:\n    print('檔案不存在')",
    "try:\n    result = int('x') / 0\nexcept ValueError:\n    print('格式錯誤')\nexcept ZeroDivisionError:\n    print('不能除以 0')",
    "def average(values):\n    if not values:\n        return None\n    return sum(values) / len(values)\nprint(average([]))",
    "def parse_price(text):\n    try:\n        price = float(text)\n        if price < 0:\n            raise ValueError\n        return price\n    except ValueError:\n        return None",
    "errors = []\nfor value in ['1', 'x']:\n    try:\n        int(value)\n    except ValueError:\n        errors.append(value)\nprint(errors)",
    "invalid = []\nfor text in ['20', 'abc', '30']:\n    try:\n        int(text)\n    except ValueError:\n        invalid.append(text)\nprint('無效：', invalid)",
    "def line_total(price_text, qty_text):\n    try:\n        price, qty = float(price_text), int(qty_text)\n        return price * qty\n    except (ValueError, TypeError):\n        return None\nprint(line_total('50', '2'))",
    "scores, errors = [], 0\nfor text in ['90', 'x', '70']:\n    try:\n        scores.append(int(text))\n    except ValueError:\n        errors += 1\nprint('最高分：', max(scores))\nprint('最低分：', min(scores))\nprint('錯誤筆數：', errors)",
    "def safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\nprint(safe_divide(10, 0))",
    "try:\n    value = int('abc')\nexcept ValueError:\n    print('格式錯誤')\nelse:\n    if not 0 <= value <= 100:\n        print('範圍錯誤')",
    "valid = []\nfor text in ['10', '120', '30']:\n    try:\n        value = int(text)\n        if not 0 <= value <= 100:\n            raise ValueError\n        valid.append(value)\n    except ValueError:\n        pass\nprint(valid)",
    "orders = [('咖啡', '50', '2'), ('蛋糕', 'x', '1')]\ntotal = 0\nfor name, price, qty in orders:\n    try:\n        total += float(price) * int(qty)\n    except ValueError:\n        print('略過：', name)\nprint('有效訂單總額：', total)",
]

lesson10_learning = [
    ("為什麼需要模組", "# 模組把常用功能整理到一起\nprint('需要時 import，程式更清楚')"),
    ("import math", "import math\nprint(math.sqrt(81))\nprint(math.ceil(3.2))"),
    ("from 模組 import 函式", "from math import pi, ceil\nprint(pi)\nprint(ceil(4.1))"),
    ("模組別名", "import statistics as stats\nprint(stats.mean([80, 90, 100]))"),
    ("random 產生抽樣", "import random\nrandom.seed(7)\nprint(random.randint(1, 6))"),
    ("choice 選擇項目", "import random\nrandom.seed(2)\nprint(random.choice(['紅茶', '咖啡', '果汁']))"),
    ("datetime 取得日期", "from datetime import date\ntoday = date(2026, 8, 1)\nprint(today.isoformat())"),
    ("日期格式化", "from datetime import datetime\ncreated = datetime(2026, 8, 1, 9, 30)\nprint(created.strftime('%Y-%m-%d %H:%M'))"),
    ("Path 建立路徑", "from pathlib import Path\nfolder = Path('data')\nfile_path = folder / 'notes.txt'\nprint(file_path)"),
    ("寫入文字檔", "from pathlib import Path\nPath('hello.txt').write_text('Hello Python\\n', encoding='utf-8')"),
    ("讀取文字檔", "from pathlib import Path\nPath('hello.txt').write_text('第一行\\n第二行', encoding='utf-8')\ntext = Path('hello.txt').read_text(encoding='utf-8')\nprint(text)"),
    ("with open 自動關閉", "with open('log.txt', 'w', encoding='utf-8') as file:\n    file.write('開始記錄\\n')\nprint('檔案已關閉')"),
    ("逐行讀取", "with open('log.txt', 'w', encoding='utf-8') as file:\n    file.write('A\\nB\\n')\nwith open('log.txt', encoding='utf-8') as file:\n    for line in file:\n        print(line.strip())"),
    ("附加文字", "with open('log.txt', 'a', encoding='utf-8') as file:\n    file.write('新增一行\\n')"),
    ("檢查檔案存在", "from pathlib import Path\npath = Path('log.txt')\nprint(path.exists())\nprint(path.is_file())"),
    ("CSV 的概念", "import csv\nrows = [['name', 'score'], ['Amy', 90]]\nwith open('scores.csv', 'w', newline='', encoding='utf-8') as file:\n    csv.writer(file).writerows(rows)"),
    ("csv.writer 寫入資料", "import csv\nwith open('sales.csv', 'w', newline='', encoding='utf-8') as file:\n    writer = csv.writer(file)\n    writer.writerow(['item', 'amount'])\n    writer.writerow(['coffee', 120])"),
    ("csv.reader 讀取資料", "import csv\nwith open('sales.csv', encoding='utf-8') as file:\n    for row in csv.reader(file):\n        print(row)"),
    ("DictWriter 寫入欄位", "import csv\nrows = [{'name': 'Amy', 'score': 90}]\nwith open('scores.csv', 'w', newline='', encoding='utf-8') as file:\n    writer = csv.DictWriter(file, fieldnames=['name', 'score'])\n    writer.writeheader()\n    writer.writerows(rows)"),
    ("DictReader 以欄位讀取", "import csv\nwith open('scores.csv', encoding='utf-8') as file:\n    for row in csv.DictReader(file):\n        print(row['name'], row['score'])"),
    ("清理 CSV 數字", "import csv\nwith open('scores.csv', encoding='utf-8') as file:\n    scores = [int(row['score']) for row in csv.DictReader(file)]\nprint('平均：', sum(scores) / len(scores))"),
    ("Path.glob 找檔案", "from pathlib import Path\nfor path in Path('.').glob('*.txt'):\n    print(path.name)"),
    ("os.environ 讀取環境概念", "import os\nprint('目前資料夾：', os.getcwd())"),
    ("模組與檔案整合", "from pathlib import Path\nimport csv\npath = Path('report.csv')\nwith path.open('w', newline='', encoding='utf-8') as file:\n    csv.writer(file).writerows([['month', 'sales'], ['Jan', 1200]])\nprint(path.exists())"),
    ("用函式整理檔案流程", "from pathlib import Path\n\ndef save_note(path, text):\n    Path(path).write_text(text, encoding='utf-8')\n\nsave_note('note.txt', '模組與檔案可以組合使用')\nprint(Path('note.txt').read_text(encoding='utf-8'))"),
]

lesson10_ex = [
    ("math 平方根", "使用 math.sqrt 計算 144 的平方根。"),
    ("ceil 與 floor", "使用 math.ceil 與 math.floor 比較 4.6。"),
    ("統計平均", "使用 statistics.mean 計算三筆成績平均。"),
    ("隨機抽籤", "使用 random.choice 從三個名字抽出一人。"),
    ("日期格式", "建立日期並輸出 YYYY/MM/DD。"),
    ("建立文字檔", "建立 memo.txt 並寫入三行待辦事項。"),
    ("讀取文字檔", "讀取 memo.txt 並逐行輸出。"),
    ("附加紀錄", "用 append 模式新增一行。"),
    ("檔案存在", "用 Path.exists 檢查資料檔。"),
    ("寫入 CSV", "寫入商品、數量、價格三欄 CSV。"),
    ("讀取 CSV", "讀取 CSV 並輸出每一列。"),
    ("CSV 小計", "讀取數量與價格，計算總額。"),
    ("DictWriter", "用 DictWriter 寫入兩筆會員資料。"),
    ("DictReader", "用欄位名稱讀取會員資料。"),
    ("CSV 篩選", "只輸出金額大於 1000 的列。"),
    ("Path 組合", "組合 data 與 sales.csv 路徑。"),
    ("列出文字檔", "用 glob 找出目前資料夾所有 txt。"),
    ("目前資料夾", "用 os.getcwd 顯示工作目錄。"),
    ("報表日期", "在 CSV 報表加入今天日期欄位。"),
    ("文字檔統計", "讀取文字檔並計算行數。"),
    ("CSV 平均", "計算 CSV 分數平均並標示最高分。"),
    ("random 模擬", "產生 10 次 1～6 點骰子結果並計數。"),
    ("模組別名", "使用 statistics as stats 完成平均。"),
    ("檔案備份", "把文字檔內容讀出後寫入 backup.txt。"),
    ("綜合銷售報表", "建立 CSV、讀回資料、計算總銷售額並輸出。"),
]

lesson10_sol = [
    "import math\nprint(math.sqrt(144))",
    "import math\nprint(math.ceil(4.6))\nprint(math.floor(4.6))",
    "from statistics import mean\nprint(mean([80, 90, 100]))",
    "import random\nrandom.seed(1)\nprint(random.choice(['Amy', 'Bob', 'Cindy']))",
    "from datetime import date\nd = date(2026, 8, 1)\nprint(d.strftime('%Y/%m/%d'))",
    "from pathlib import Path\nPath('memo.txt').write_text('買牛奶\\n回信\\n整理資料', encoding='utf-8')",
    "with open('memo.txt', encoding='utf-8') as file:\n    for line in file:\n        print(line.strip())",
    "with open('memo.txt', 'a', encoding='utf-8') as file:\n    file.write('完成練習\\n')",
    "from pathlib import Path\nprint(Path('memo.txt').exists())",
    "import csv\nwith open('products.csv', 'w', newline='', encoding='utf-8') as file:\n    writer = csv.writer(file)\n    writer.writerow(['商品', '數量', '價格'])\n    writer.writerow(['咖啡', 2, 50])",
    "import csv\nwith open('products.csv', encoding='utf-8') as file:\n    for row in csv.reader(file):\n        print(row)",
    "import csv\ntotal = 0\nwith open('products.csv', encoding='utf-8') as file:\n    next(file)\n    for item, qty, price in csv.reader(file):\n        total += int(qty) * int(price)\nprint('總額：', total)",
    "import csv\nrows = [{'name': 'Amy', 'level': 'A'}, {'name': 'Bob', 'level': 'B'}]\nwith open('members.csv', 'w', newline='', encoding='utf-8') as file:\n    writer = csv.DictWriter(file, fieldnames=['name', 'level'])\n    writer.writeheader(); writer.writerows(rows)",
    "import csv\nwith open('members.csv', encoding='utf-8') as file:\n    for row in csv.DictReader(file):\n        print(row['name'], row['level'])",
    "import csv\nwith open('sales.csv', encoding='utf-8') as file:\n    for row in csv.DictReader(file):\n        if float(row['amount']) > 1000:\n            print(row)",
    "from pathlib import Path\nprint(Path('data') / 'sales.csv')",
    "from pathlib import Path\nfor path in Path('.').glob('*.txt'):\n    print(path.name)",
    "import os\nprint(os.getcwd())",
    "from datetime import date\nimport csv\ntoday = date.today().isoformat()\nwith open('dated.csv', 'w', newline='', encoding='utf-8') as file:\n    csv.writer(file).writerows([['date', 'amount'], [today, 100]])",
    "from pathlib import Path\nlines = Path('memo.txt').read_text(encoding='utf-8').splitlines()\nprint('行數：', len(lines))",
    "import csv\nwith open('scores.csv', encoding='utf-8') as file:\n    scores = [int(row['score']) for row in csv.DictReader(file)]\nprint('平均：', sum(scores) / len(scores))\nprint('最高分：', max(scores))",
    "import random\nrandom.seed(4)\nrolls = [random.randint(1, 6) for _ in range(10)]\nprint(rolls)\nprint({n: rolls.count(n) for n in range(1, 7)})",
    "import statistics as stats\nprint(stats.mean([70, 80, 90]))",
    "from pathlib import Path\ntext = Path('memo.txt').read_text(encoding='utf-8')\nPath('backup.txt').write_text(text, encoding='utf-8')",
    "import csv\nrows = [['month', 'sales'], ['Jan', '1200'], ['Feb', '900']]\nwith open('report.csv', 'w', newline='', encoding='utf-8') as file:\n    csv.writer(file).writerows(rows)\nwith open('report.csv', encoding='utf-8') as file:\n    data = list(csv.DictReader(file))\nprint('總銷售額：', sum(int(row['sales']) for row in data))",
]


def write_lesson(number, slug, title, intro, learning, exercises, solutions, homework):
    folder = ROOT / f"lesson{number:02d}_{slug}"
    folder.mkdir(parents=True, exist_ok=True)
    for suffix, items in [("learning", learning), ("exercises", [(h, f"# {desc}") for h, desc in exercises]), ("solutions", [(h, s) for (h, _), s in zip(exercises, solutions)])]:
        (folder / f"lesson{number:02d}_{suffix}.ipynb").write_text(json.dumps(notebook(title, intro, items), ensure_ascii=False, indent=2), encoding="utf-8")
    (folder / f"lesson{number:02d}_homework.ipynb").write_text(json.dumps(notebook(title, intro, [(h, f"# {d}") for h, d in homework]), ensure_ascii=False, indent=2), encoding="utf-8")
    readme = f"# {title}\n\n## 學習成果\n\n- 能辨識本課程的核心概念並用生活化案例說明。\n- 能完成 25 個 learning 示範、25 題 exercises 與對應 solutions。\n- 能把語法放進小型資料處理流程。\n\n## 教材檔案\n\n- `lesson{number:02d}_learning.ipynb`：25 個完整示範例題。\n- `lesson{number:02d}_exercises.ipynb`：25 題分級課堂練習。\n- `lesson{number:02d}_solutions.ipynb`：與課堂練習逐題對應的 25 題解答。\n- `lesson{number:02d}_homework.ipynb`：課後整合任務。\n\n## 教學提醒\n\n{intro}\n"
    (folder / "README.md").write_text(readme, encoding="utf-8")


write_lesson(9, "error_handling", "Lesson 09｜錯誤處理", "先讀懂錯誤，再用 try、except、else、finally 保護程式。", lesson09_learning, lesson09_ex, lesson09_sol, [("錯誤處理報表", "讀取一批成績字串，輸出有效資料、錯誤筆數與平均。"), ("安全購物車", "處理商品價格與數量輸入，錯誤資料要有清楚提示。"), ("檔案防呆", "開啟檔案並處理不存在、編碼或內容格式問題。"), ("綜合驗證函式", "寫一個函式完成轉換、範圍驗證與錯誤回傳。")])
write_lesson(10, "modules_files", "Lesson 10｜模組與檔案", "用標準函式庫與文字檔、CSV 保存資料，為後續資料分析準備素材。", lesson10_learning, lesson10_ex, lesson10_sol, [("CSV 銷售分析", "讀取銷售 CSV，計算總額、平均與最高單筆。"), ("文字檔日誌", "把每日工作紀錄附加到文字檔並統計行數。"), ("隨機抽樣報告", "使用 random 產生樣本，輸出各類別出現次數。"), ("小型資料管線", "建立 CSV、讀取、清理數字並輸出摘要報表。")])
