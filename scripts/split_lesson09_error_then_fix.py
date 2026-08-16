import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "course_v2" / "lessons" / "lesson09_error_handling" / "lesson09_learning.ipynb"


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


examples = {
    2: {
        "bad": "print('少一個右括號'",
        "note": "SyntaxError 會讓整格無法開始執行。補上右括號後，再執行修正版。",
        "fixed": "print('補上右括號後，可以正常執行')",
    },
    3: {
        "bad": "print(user_name)",
        "note": "先定義變數，再使用同一個變數名稱。",
        "fixed": "user_name = 'Amy'\nprint(user_name)",
    },
    4: {
        "bad": "price = 100\nquantity = '2'\nprint(price + quantity)",
        "note": "將文字轉成整數後，才能與其他數字進行加法。",
        "fixed": "price = 100\nquantity_text = '2'\nquantity = int(quantity_text)\nprint(price + quantity)",
    },
    5: {
        "bad": "text = '四十二'\nnumber = int(text)\nprint(number + 8)",
        "note": "確認文字內容是可轉換的數字，或在不確定資料時使用 try/except。",
        "fixed": "text = '四十二'\n\ntry:\n    number = int(text)\n    print(number + 8)\nexcept ValueError as error:\n    print('內容無法轉成整數：', error)",
    },
    6: {
        "bad": "colors = ['紅', '藍']\nprint(colors[2])",
        "note": "兩個元素只有索引 0 與 1。可先檢查長度，或捕捉 IndexError。",
        "fixed": "colors = ['紅', '藍']\n\ntry:\n    print(colors[2])\nexcept IndexError:\n    print('索引超出範圍，目前長度：', len(colors))",
    },
    7: {
        "bad": "profile = {'name': 'Amy'}\nprint(profile['email'])",
        "note": "不確定 key 是否存在時，可使用 get() 提供預設值。",
        "fixed": "profile = {'name': 'Amy'}\nemail = profile.get('email', '未提供 email')\nprint(email)",
    },
    8: {
        "bad": "total = 100\npeople = 0\nprint(total / people)",
        "note": "可以先用條件阻止除以零；也可以在輸入不可預期時捕捉 ZeroDivisionError。",
        "fixed": "total = 100\npeople = 0\n\ntry:\n    print(total / people)\nexcept ZeroDivisionError:\n    print('人數不能是 0')",
    },
}


data = json.loads(PATH.read_text(encoding="utf-8"))
new_cells = []
number = None

for cell in data["cells"]:
    if cell["cell_type"] == "markdown":
        first_line = "".join(cell.get("source", [])).strip().splitlines()[0]
        number = None
        if first_line.startswith("## 例題 "):
            number = int(first_line.split("例題 ", 1)[1].split("｜", 1)[0])
            if number in examples:
                original = "".join(cell["source"]).rstrip()
                cell["source"] = [line + "\n" for line in (
                    original + "\n\n### 第一步：先執行下一格，觀察真正的錯誤訊息"
                ).splitlines()]
        new_cells.append(cell)
        continue

    if cell["cell_type"] == "code" and number in examples:
        item = examples[number]
        new_cells.append(code(item["bad"]))
        new_cells.append(markdown(f"### 第二步：修正或安全處理\n\n{item['note']}"))
        new_cells.append(code(item["fixed"]))
        number = None
        continue

    new_cells.append(cell)
    number = None

data["cells"] = new_cells
PATH.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("Lesson 09 examples 02–08 split into error and fixed cells.")
