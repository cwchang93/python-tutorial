import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "course_v2" / "lessons" / "lesson09_error_handling" / "lesson09_learning.ipynb"


def lines(text):
    return [line + "\n" for line in text.splitlines()]


updates = {
    1: (
        "錯誤訊息是線索",
        "先觸發並捕捉一個錯誤，觀察錯誤類型與訊息。實際 traceback 最後一行通常最重要。",
        "try:\n    int('abc')\nexcept ValueError as error:\n    print('錯誤類型：', type(error).__name__)\n    print('錯誤訊息：', error)\n    print('閱讀順序：先看錯誤類型，再回頭找出錯位置')",
    ),
    2: (
        "SyntaxError 語法錯誤",
        "SyntaxError 會讓整個 Cell 無法開始執行，因此使用 compile() 安全分析錯誤程式碼。",
        "bad_code = \"print('少一個右括號'\"\n\ntry:\n    compile(bad_code, '<example>', 'exec')\nexcept SyntaxError as error:\n    print('錯誤類型：', type(error).__name__)\n    print('錯誤訊息：', error.msg)\n    print('錯誤位置：第', error.lineno, '行')",
    ),
    3: (
        "NameError 名稱不存在",
        "使用尚未定義的名稱會觸發 NameError。",
        "try:\n    print(user_name_not_defined)\nexcept NameError as error:\n    print('錯誤類型：', type(error).__name__)\n    print('錯誤訊息：', error)\n\nuser_name = 'Amy'\nprint('修正後：', user_name)",
    ),
    4: (
        "TypeError 型別不相容",
        "數字與文字不能直接相加；先觀察 TypeError，再把文字轉成數字。",
        "price = 100\nquantity_text = '2'\n\ntry:\n    print(price + quantity_text)\nexcept TypeError as error:\n    print('錯誤類型：', type(error).__name__)\n    print('錯誤訊息：', error)\n\nquantity = int(quantity_text)\nprint('修正後總和：', price + quantity)",
    ),
    5: (
        "ValueError 內容無法轉換",
        "資料型態可以轉換，不代表內容一定符合格式。",
        "text = '四十二'\n\ntry:\n    number = int(text)\nexcept ValueError as error:\n    print('錯誤類型：', type(error).__name__)\n    print('錯誤訊息：', error)\n\ncorrect_text = '42'\nnumber = int(correct_text)\nprint('修正後：', number + 8)",
    ),
    6: (
        "IndexError 索引超出範圍",
        "兩個元素的 List 只有索引 0 與 1，讀取索引 2 會出錯。",
        "colors = ['紅', '藍']\n\ntry:\n    print(colors[2])\nexcept IndexError as error:\n    print('錯誤類型：', type(error).__name__)\n    print('錯誤訊息：', error)\n    print('目前長度：', len(colors))\n\nprint('修正後：', colors[1])",
    ),
    7: (
        "KeyError 字典 key 不存在",
        "使用不存在的 key 會觸發 KeyError；不確定欄位是否存在時可使用 get()。",
        "profile = {'name': 'Amy'}\n\ntry:\n    print(profile['email'])\nexcept KeyError as error:\n    print('錯誤類型：', type(error).__name__)\n    print('找不到欄位：', error)\n\nprint('安全查詢：', profile.get('email', '未提供 email'))",
    ),
    8: (
        "ZeroDivisionError 除以零",
        "先實際觸發除以零，再示範用條件判斷預防。",
        "total = 100\npeople = 0\n\ntry:\n    print(total / people)\nexcept ZeroDivisionError as error:\n    print('錯誤類型：', type(error).__name__)\n    print('錯誤訊息：', error)\n\nif people != 0:\n    print('平均：', total / people)\nelse:\n    print('預防方式：人數不能是 0')",
    ),
    9: (
        "try 保護可能失敗的程式",
        "把可能失敗的轉換放進 try；錯誤發生時由 except 接手。",
        "try:\n    age = int('二十')\n    print('年齡：', age)\nexcept ValueError as error:\n    print('年齡格式錯誤：', error)",
    ),
    10: (
        "except 捕捉指定錯誤",
        "只捕捉預期的 ValueError，並保留清楚的使用者提示。",
        "try:\n    score = int('abc')\nexcept ValueError as error:\n    print('請輸入整數分數')\n    print('技術訊息：', error)",
    ),
    11: (
        "多種錯誤分開處理",
        "同一段流程可能遇到格式錯誤或索引錯誤，應分開處理並提供不同提示。",
        "numbers = [10, 20]\n\nfor raw_index in ['abc', '5', '1']:\n    print('測試輸入：', raw_index)\n    try:\n        index = int(raw_index)\n        print('取得數字：', numbers[index])\n    except ValueError:\n        print('索引必須是整數')\n    except IndexError:\n        print('索引超出範圍')",
    ),
    12: (
        "except Exception 作為最後防線",
        "Exception 可以作為最後防線，但平常仍應優先捕捉具體錯誤。",
        "for divisor in [2, 0]:\n    try:\n        result = 10 / divisor\n    except Exception as error:\n        print('最後防線捕捉：', type(error).__name__, error)\n    else:\n        print('成功結果：', result)",
    ),
    13: (
        "else 只在成功時執行",
        "try 沒有發生錯誤時才會執行 else。",
        "for text in ['25', '二十五']:\n    try:\n        number = int(text)\n    except ValueError:\n        print(text, '轉換失敗')\n    else:\n        print(text, '轉換成功：', number)",
    ),
    14: (
        "finally 一定會執行",
        "不論成功或失敗，finally 都會執行，適合放清理與結束工作。",
        "for divisor in [2, 0]:\n    print('測試除數：', divisor)\n    try:\n        print('結果：', 10 / divisor)\n    except ZeroDivisionError:\n        print('不能除以 0')\n    finally:\n        print('finally：本次處理結束')",
    ),
    17: (
        "驗證分數範圍",
        "同時測試有效分數、超出範圍與格式錯誤。",
        "def read_score(text):\n    try:\n        score = int(text)\n        if score < 0 or score > 100:\n            return None\n        return score\n    except ValueError:\n        return None\n\nfor text in ['88', '120', '八十八']:\n    print(text, '→', read_score(text))",
    ),
    18: (
        "raise 主動提出錯誤",
        "當資料不符合商業規則時，可以用 raise 主動提出清楚的錯誤。",
        "def set_quantity(quantity):\n    if quantity < 0:\n        raise ValueError('數量不能是負數')\n    return quantity\n\nfor quantity in [3, -1]:\n    try:\n        print('設定數量：', set_quantity(quantity))\n    except ValueError as error:\n        print('設定失敗：', error)",
    ),
    20: (
        "清楚顯示錯誤原因",
        "測試成功、格式錯誤與除以零三種情況。",
        "for text in ['100', 'abc', '0']:\n    print('測試輸入：', text)\n    try:\n        amount = int(text)\n        print('計算結果：', 1000 / amount)\n    except ValueError as error:\n        print('格式錯誤：', error)\n    except ZeroDivisionError as error:\n        print('計算錯誤：', error)",
    ),
    23: (
        "保護檔案開啟概念",
        "使用 with open 確保檔案成功開啟時也會自動關閉。",
        "try:\n    with open('not_found.txt', encoding='utf-8') as file:\n        content = file.read()\n        print(content)\nexcept FileNotFoundError as error:\n    print('檔案不存在：', error.filename)",
    ),
    25: (
        "完整的資料輸入流程",
        "整合格式轉換、範圍規則、raise 與清楚錯誤訊息。",
        "def parse_price(text):\n    try:\n        price = float(text)\n        if price < 0:\n            raise ValueError('價格不能小於 0')\n        return price\n    except ValueError as error:\n        print(text, '價格錯誤：', error)\n        return None\n\nfor text in ['199.5', '-20', '一百元']:\n    result = parse_price(text)\n    print(text, '→', result)",
    ),
}


data = json.loads(PATH.read_text(encoding="utf-8"))
for number, (title, description, code) in updates.items():
    markdown_index = 1 + (number - 1) * 2
    code_index = markdown_index + 1
    data["cells"][markdown_index]["source"] = lines(
        f"## 例題 {number:02d}｜{title}\n\n{description}"
    )
    data["cells"][code_index]["source"] = lines(code)
    data["cells"][code_index]["execution_count"] = None
    data["cells"][code_index]["outputs"] = []

PATH.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("Lesson 09 error examples updated.")
