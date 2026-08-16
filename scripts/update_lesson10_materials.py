import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "course_v2" / "lessons" / "lesson10_modules_files"


def source(text):
    return [line + "\n" for line in text.splitlines()]


def replace_pairs(path, replacements):
    data = json.loads(path.read_text(encoding="utf-8"))
    for number, title, prompt, code_text in replacements:
        markdown_index = 1 + (number - 1) * 2
        code_index = markdown_index + 1
        data["cells"][markdown_index]["source"] = source(
            f"## 例題 {number:02d}｜{title}\n\n{prompt}"
        )
        data["cells"][code_index]["source"] = source(code_text)
        data["cells"][code_index]["execution_count"] = None
        data["cells"][code_index]["outputs"] = []
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


learning = [
    (1, "模組與套件的種類", "先分辨內建功能、標準函式庫、第三方套件與自訂模組。", "module_types = {\n    '內建功能': 'print、len，不用 import',\n    '標準函式庫': 'math、random，只要 import',\n    '第三方套件': 'pandas、requests，通常要先安裝',\n    '自訂模組': '自己建立的 .py 檔案',\n}\n\nfor name, description in module_types.items():\n    print(name, '：', description)"),
    (2, "import math", "標準函式庫不需要 pip install；匯入後使用「模組名稱.功能」。", "import math\n\nprint('平方根：', math.sqrt(81))\nprint('無條件進位：', math.ceil(3.2))\nprint('圓周率：', math.pi)"),
    (3, "from 模組 import 名稱", "只匯入需要的名稱，呼叫時不用再寫模組前綴。", "from math import sqrt\n\nprint('平方根：', sqrt(144))"),
    (4, "使用 as 設定別名", "別名適合名稱較長或已有慣用縮寫的模組。", "import datetime as dt\n\ntoday = dt.date.today()\nprint('今天日期：', today)"),
    (5, "避免 import 星號", "`from module import *` 會讓名稱來源不清楚，也容易發生命名衝突。", "from math import sqrt\n\n# 保留自己的變數名稱，也能清楚知道 sqrt 來自 math\nsqrt_result = sqrt(49)\nprint('平方根：', sqrt_result)"),
    (6, "什麼時候需要 pip", "標準函式庫可直接 import；第三方套件才需要另外安裝。Notebook 中先顯示指令，不直接安裝。", "standard_library = ['math', 'random', 'datetime', 'csv', 'pathlib']\nthird_party = ['pandas', 'requests']\n\nprint('標準函式庫：', standard_library)\nprint('第三方套件：', third_party)\nprint('安裝範例：python -m pip install pandas')"),
    (7, "建立自訂模組", "一個 `.py` 檔案就是模組。將可重複使用的函式放在另一個檔案，再由主程式匯入。", "from pathlib import Path\nimport importlib\n\nmodule_path = Path('lesson10_tools.py')\nmodule_path.write_text(\n    \"def add(a, b):\\n\"\n    \"    return a + b\\n\",\n    encoding='utf-8'\n)\n\nimport lesson10_tools\nimportlib.reload(lesson10_tools)\nprint('加總：', lesson10_tools.add(3, 5))"),
    (8, "random 隨機抽籤", "使用 random.choice 從 List 中選出一個項目。", "import random\n\nstudents = ['Amy', 'Bob', 'Cindy', 'David']\nwinner = random.choice(students)\nprint('抽中：', winner)"),
    (9, "Path 組合路徑", "使用 `/` 組合資料夾與檔名，比手動拼接字串更清楚。", "from pathlib import Path\n\ndata_path = Path('../../data') / 'lesson10_sales.csv'\nprint('資料路徑：', data_path)\nprint('檔案存在：', data_path.exists())"),
    (10, "檔案模式 r、w、a", "`r` 讀取、`w` 重新寫入、`a` 保留舊內容並追加。", "file_modes = {\n    'r': '讀取；檔案不存在會報錯',\n    'w': '重新寫入；舊內容會被清空',\n    'a': '追加內容；保留原本資料',\n}\n\nfor mode, meaning in file_modes.items():\n    print(mode, '：', meaning)"),
    (11, "with open 自動關閉", "離開 with 區塊後，Python 會自動關閉檔案。", "from pathlib import Path\n\nnote_path = Path('lesson10_note.txt')\nwith note_path.open('w', encoding='utf-8') as file:\n    file.write('今天開始學檔案處理\\n')\n\nprint('已寫入：', note_path)"),
    (12, "read、readline、readlines", "三種方法的回傳結果不同；重新開啟檔案，避免讀取游標已在結尾。", "with note_path.open('r', encoding='utf-8') as file:\n    content = file.read()\nprint('read：', repr(content))\n\nwith note_path.open('r', encoding='utf-8') as file:\n    first_line = file.readline()\nprint('readline：', repr(first_line))\n\nwith note_path.open('r', encoding='utf-8') as file:\n    lines = file.readlines()\nprint('readlines：', lines)"),
    (13, "使用 for 逐行讀取", "大型檔案通常直接逐行處理，不需要先把所有內容放進 List。", "with note_path.open('r', encoding='utf-8') as file:\n    for line in file:\n        clean_line = line.strip()\n        print('一行內容：', clean_line)"),
    (14, "write、writelines、print(file=)", "write 與 writelines 不會自動換行；print 寫入時會自動加入換行。", "write_path = Path('lesson10_write_demo.txt')\nwith write_path.open('w', encoding='utf-8') as file:\n    file.write('第一行\\n')\n    file.writelines(['第二行\\n', '第三行\\n'])\n    print('第四行', file=file)\n\nprint(write_path.read_text(encoding='utf-8'))"),
    (15, "使用 a 模式追加文字", "`a` 会從檔案結尾新增內容，不會清空原本資料。", "with write_path.open('a', encoding='utf-8') as file:\n    file.write('第五行：追加內容\\n')\n\nprint(write_path.read_text(encoding='utf-8'))"),
]


exercises = [
    (1, "判斷模組類型", "建立 Dict，將 math、pandas、自己寫的 tools.py 分成標準函式庫、第三方套件、自訂模組並逐筆印出。", "# 請建立 module_types 並使用 for 迴圈印出"),
    (2, "math 平方根", "匯入 math，計算 225 的平方根並清楚顯示答案。", "# 請使用 import math 完成"),
    (3, "from import", "只從 statistics 匯入 mean，計算 [80, 90, 70] 的平均。", "scores = [80, 90, 70]\n# 請完成"),
    (4, "模組別名", "將 datetime 匯入為 dt，顯示今天日期。", "# 請使用 import ... as ... 完成"),
    (5, "自訂模組", "建立 `price_tools.py`，其中包含 subtotal(price, quantity)，再匯入並計算 120 × 3。", "from pathlib import Path\n# 請建立 price_tools.py，再匯入使用"),
    (6, "檔案模式比較", "建立 Dict，分別說明 r、w、a 的用途與檔案不存在時的行為。", "# 請建立 file_modes 並逐筆印出"),
    (7, "使用 w 建立文字檔", "用 with open 與 w 模式建立 practice_note.txt，寫入兩行內容。", "from pathlib import Path\npath = Path('practice_note.txt')\n# 請完成"),
    (8, "使用 a 追加紀錄", "在 practice_note.txt 結尾追加「第三行」，不可清空前兩行。", "# 請使用 a 模式完成"),
    (9, "比較三種讀取方法", "分別用 read、readline、readlines 讀取 practice_note.txt，清楚標示三種結果。", "# 每次比較前請重新開啟檔案"),
    (10, "逐行清理換行", "直接使用 for 逐行讀取 practice_note.txt，並用 strip() 移除換行。", "# 請使用 for line in file 完成"),
    (11, "三種寫入方式", "在同一個檔案中各使用一次 write、writelines、print(file=)。", "from pathlib import Path\npath = Path('write_methods.txt')\n# 請完成"),
]


solutions = [
    (1, "判斷模組類型", "建立 Dict，將 math、pandas、自己寫的 tools.py 分成標準函式庫、第三方套件、自訂模組並逐筆印出。", "module_types = {\n    'math': '標準函式庫',\n    'pandas': '第三方套件',\n    'tools.py': '自訂模組',\n}\n\nfor name, module_type in module_types.items():\n    print(name, '：', module_type)"),
    (2, "math 平方根", "匯入 math，計算 225 的平方根並清楚顯示答案。", "import math\n\nanswer = math.sqrt(225)\nprint('平方根：', answer)"),
    (3, "from import", "只從 statistics 匯入 mean，計算 [80, 90, 70] 的平均。", "from statistics import mean\n\nscores = [80, 90, 70]\naverage = mean(scores)\nprint('平均分數：', average)"),
    (4, "模組別名", "將 datetime 匯入為 dt，顯示今天日期。", "import datetime as dt\n\ntoday = dt.date.today()\nprint('今天日期：', today)"),
    (5, "自訂模組", "建立 `price_tools.py`，其中包含 subtotal(price, quantity)，再匯入並計算 120 × 3。", "from pathlib import Path\nimport importlib\n\nPath('price_tools.py').write_text(\n    \"def subtotal(price, quantity):\\n\"\n    \"    return price * quantity\\n\",\n    encoding='utf-8'\n)\n\nimport price_tools\nimportlib.reload(price_tools)\namount = price_tools.subtotal(120, 3)\nprint('商品小計：', amount)"),
    (6, "檔案模式比較", "建立 Dict，分別說明 r、w、a 的用途與檔案不存在時的行為。", "file_modes = {\n    'r': '讀取；不存在會報錯',\n    'w': '重新寫入；不存在會建立',\n    'a': '追加內容；不存在會建立',\n}\n\nfor mode, meaning in file_modes.items():\n    print(mode, '：', meaning)"),
    (7, "使用 w 建立文字檔", "用 with open 與 w 模式建立 practice_note.txt，寫入兩行內容。", "from pathlib import Path\n\npath = Path('practice_note.txt')\nwith path.open('w', encoding='utf-8') as file:\n    file.write('第一行\\n')\n    file.write('第二行\\n')\n\nprint('已建立：', path)"),
    (8, "使用 a 追加紀錄", "在 practice_note.txt 結尾追加「第三行」，不可清空前兩行。", "with path.open('a', encoding='utf-8') as file:\n    file.write('第三行\\n')\n\nprint(path.read_text(encoding='utf-8'))"),
    (9, "比較三種讀取方法", "分別用 read、readline、readlines 讀取 practice_note.txt，清楚標示三種結果。", "with path.open('r', encoding='utf-8') as file:\n    print('read：', repr(file.read()))\n\nwith path.open('r', encoding='utf-8') as file:\n    print('readline：', repr(file.readline()))\n\nwith path.open('r', encoding='utf-8') as file:\n    print('readlines：', file.readlines())"),
    (10, "逐行清理換行", "直接使用 for 逐行讀取 practice_note.txt，並用 strip() 移除換行。", "with path.open('r', encoding='utf-8') as file:\n    for line in file:\n        print(line.strip())"),
    (11, "三種寫入方式", "在同一個檔案中各使用一次 write、writelines、print(file=)。", "from pathlib import Path\n\npath = Path('write_methods.txt')\nwith path.open('w', encoding='utf-8') as file:\n    file.write('第一行\\n')\n    file.writelines(['第二行\\n', '第三行\\n'])\n    print('第四行', file=file)\n\nprint(path.read_text(encoding='utf-8'))"),
]


replace_pairs(BASE / "lesson10_learning.ipynb", learning)
replace_pairs(BASE / "lesson10_exercises.ipynb", exercises)
replace_pairs(BASE / "lesson10_solutions.ipynb", solutions)

homework_path = BASE / "lesson10_homework.ipynb"
homework = json.loads(homework_path.read_text(encoding="utf-8"))
homework["cells"][1]["source"] = source(
    "## 例題 01｜模組與檔案工具箱\n\n建立一個自訂模組 `report_tools.py`，至少包含計算總額與格式化摘要兩個函式；主程式匯入後讀取課程 CSV 並輸出報表。"
)
homework["cells"][2]["source"] = source(
    "# 請建立 report_tools.py，並在主程式中使用 import 呼叫\n# 報表至少要顯示資料筆數與銷售總額"
)
homework["cells"][3]["source"] = source(
    "## 例題 02｜文字日誌：w 與 a\n\n第一次執行用 w 建立日誌；第二次執行改用 a 追加內容。最後逐行讀取並移除換行。"
)
homework["cells"][4]["source"] = source("# 請使用 with open、w、a 與逐行讀取完成")
homework_path.write_text(json.dumps(homework, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

print("Lesson 10 code materials updated.")
