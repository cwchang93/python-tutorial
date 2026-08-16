import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in text.splitlines()]}


def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [line + "\n" for line in text.splitlines()]}


def notebook(title, intro, items, solved=False):
    cells = [md(f"# {title}\n\n{intro}")]
    for index, item in enumerate(items, 1):
        cells.append(md(f"## {'解答' if solved else '題目'} {index:02d}｜{item['title']}\n\n{item['prompt']}"))
        cells.append(code(item['answer'] if solved else item.get('starter', '# 請在這裡完成')))
    return {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3"}}, "nbformat": 4, "nbformat_minor": 5}


def write_nb(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


lesson11 = [
    ("確認 Git 是否安裝", "執行指令並觀察 Git 版本。", "!git --version"),
    ("查看目前資料夾", "確認 Notebook 目前所在位置。", "from pathlib import Path\nprint('目前資料夾：', Path.cwd())"),
    ("建立專案資料夾", "建立 practice_git_project 資料夾。", "from pathlib import Path\nproject = Path('practice_git_project')\nproject.mkdir(exist_ok=True)\nprint('專案位置：', project.resolve())"),
    ("Git 初始化", "把資料夾變成 Git Repository。", "!git -C practice_git_project init"),
    ("查看狀態", "使用 status 查看目前版本狀態。", "!git -C practice_git_project status --short"),
    ("建立第一個程式", "建立 hello.py，作為第一個版本。", "from pathlib import Path\nPath('practice_git_project/hello.py').write_text(\"print('Hello Git')\\n\", encoding='utf-8')\nprint('hello.py 已建立')"),
    ("辨識未追蹤檔案", "再次查看狀態，找出 ?? 的意義。", "!git -C practice_git_project status --short"),
    ("加入暫存區", "使用 git add 選擇要放進下一個版本的檔案。", "!git -C practice_git_project add hello.py\n!git -C practice_git_project status --short"),
    ("建立 Commit", "為目前版本建立清楚的訊息。", "!git -C practice_git_project commit -m \"feat: add first Python program\""),
    ("查看版本紀錄", "用精簡格式查看 Commit。", "!git -C practice_git_project log --oneline"),
    ("修改程式", "替 hello.py 加入第二行內容。", "from pathlib import Path\npath = Path('practice_git_project/hello.py')\npath.write_text(\"print('Hello Git')\\nprint('第二個版本')\\n\", encoding='utf-8')\nprint(path.read_text(encoding='utf-8'))"),
    ("查看差異", "用 diff 比較工作區與上次 Commit。", "!git -C practice_git_project diff"),
    ("提交第二版", "把修改加入暫存區並建立第二個 Commit。", "!git -C practice_git_project add hello.py\n!git -C practice_git_project commit -m \"feat: add version message\""),
    ("建立 README", "寫下專案用途與執行方式。", "from pathlib import Path\nreadme = '# 我的第一個 Git 專案\\n\\n執行方式：`python hello.py`\\n'\nPath('practice_git_project/README.md').write_text(readme, encoding='utf-8')\nprint(readme)"),
    ("忽略暫存檔", "建立 .gitignore，避免提交 cache 與暫存檔。", "from pathlib import Path\nPath('practice_git_project/.gitignore').write_text('__pycache__/\\n*.tmp\\n', encoding='utf-8')\nprint('忽略規則已建立')"),
    ("一次檢查所有狀態", "確認 README 與 .gitignore 尚未提交。", "!git -C practice_git_project status --short"),
    ("提交文件", "將 README 與 .gitignore 放入同一個文件 Commit。", "!git -C practice_git_project add README.md .gitignore\n!git -C practice_git_project commit -m \"docs: add project instructions\""),
    ("理解 GitHub Remote", "列出目前遠端；尚未設定時不會顯示內容。", "!git -C practice_git_project remote -v"),
    ("設定遠端示範", "請把網址換成自己的 GitHub Repository；本格只示範指令，不直接執行。", "remote_command = 'git remote add origin https://github.com/USERNAME/REPOSITORY.git'\nprint(remote_command)"),
    ("Push 指令示範", "第一次 Push 通常要指定 origin 與 main。", "push_command = 'git push -u origin main'\nprint(push_command)"),
    ("Clone 指令示範", "Clone 是把遠端 Repository 完整複製到本機。", "clone_command = 'git clone https://github.com/USERNAME/REPOSITORY.git'\nprint(clone_command)"),
    ("Pull 指令示範", "Pull 是把遠端的新版本同步回目前資料夾。", "pull_command = 'git pull origin main'\nprint(pull_command)"),
    ("比較 Push、Pull、Clone", "用 Dict 整理三個指令的用途。", "commands = {'push': '本機 → GitHub', 'pull': 'GitHub → 既有本機專案', 'clone': '第一次完整下載'}\nfor name, meaning in commands.items():\n    print(name, '：', meaning)"),
    ("安全操作檢查表", "輸出操作前的三項檢查。", "checks = ['確認所在資料夾', '先看 git status', 'Commit 訊息說明改了什麼']\nfor index, item in enumerate(checks, 1):\n    print(index, item)"),
    ("完成版本歷史", "查看完整練習專案的精簡版本紀錄。", "!git -C practice_git_project log --oneline --decorate"),
]

lesson12 = [
    ("建立交易資料", "先用 List 與 Dict 表示三筆收入／支出。", "records = [\n    {'date': '2026-08-01', 'category': '餐飲', 'amount': -120, 'note': '午餐'},\n    {'date': '2026-08-01', 'category': '薪資', 'amount': 30000, 'note': '薪水'},\n    {'date': '2026-08-02', 'category': '交通', 'amount': -50, 'note': '捷運'},\n]\nprint('筆數：', len(records))"),
    ("逐筆顯示", "使用 for 迴圈印出日期、分類與金額。", "for record in records:\n    print(record['date'], record['category'], record['amount'])"),
    ("計算總餘額", "使用迴圈計算所有金額。", "balance = 0\nfor record in records:\n    balance += record['amount']\nprint('目前餘額：', balance)"),
    ("分開收入與支出", "以條件判斷分別加總正數與負數。", "income = 0\nexpense = 0\nfor record in records:\n    if record['amount'] >= 0:\n        income += record['amount']\n    else:\n        expense += abs(record['amount'])\nprint('收入：', income)\nprint('支出：', expense)"),
    ("新增交易函式", "用函式集中建立資料的規則。", "def add_record(records, date, category, amount, note):\n    record = {'date': date, 'category': category, 'amount': amount, 'note': note}\n    records.append(record)\n    return record\n\nnew_record = add_record(records, '2026-08-03', '購物', -350, '生活用品')\nprint('新增：', new_record)"),
    ("驗證空白分類", "分類不可為空白，否則主動 raise。", "def validate_category(category):\n    if category.strip() == '':\n        raise ValueError('分類不可空白')\n    return category.strip()\n\nprint(validate_category(' 餐飲 '))"),
    ("轉換金額", "將文字金額安全轉成 float。", "def parse_amount(text):\n    try:\n        return float(text)\n    except ValueError:\n        print('金額格式錯誤')\n        return None\n\nprint(parse_amount('250'))"),
    ("顯示單筆交易", "用函式建立一致的輸出格式。", "def format_record(record):\n    return f\"{record['date']}｜{record['category']}｜{record['amount']}｜{record['note']}\"\n\nprint(format_record(records[0]))"),
    ("顯示全部交易", "重複使用 format_record。", "def show_records(records):\n    if not records:\n        print('目前沒有資料')\n        return\n    for index, record in enumerate(records, 1):\n        print(index, format_record(record))\n\nshow_records(records)"),
    ("分類支出統計", "使用 Dict 累加各分類支出。", "def expense_by_category(records):\n    summary = {}\n    for record in records:\n        if record['amount'] < 0:\n            category = record['category']\n            summary[category] = summary.get(category, 0) + abs(record['amount'])\n    return summary\n\nprint(expense_by_category(records))"),
    ("找出最大支出", "只比較支出資料，輸出金額最高的一筆。", "largest = None\nfor record in records:\n    if record['amount'] < 0:\n        if largest is None or record['amount'] < largest['amount']:\n            largest = record\nif largest is not None:\n    print('最大支出：', format_record(largest))\nelse:\n    print('沒有支出資料')"),
    ("依日期篩選", "寫函式找出指定日期的交易。", "def filter_by_date(records, target_date):\n    result = []\n    for record in records:\n        if record['date'] == target_date:\n            result.append(record)\n    return result\n\nshow_records(filter_by_date(records, '2026-08-01'))"),
    ("依分類篩選", "不分前後空白搜尋指定分類。", "def filter_by_category(records, target):\n    target = target.strip()\n    result = []\n    for record in records:\n        if record['category'] == target:\n            result.append(record)\n    return result\n\nshow_records(filter_by_category(records, '餐飲'))"),
    ("準備 CSV 路徑", "建立 data 資料夾與檔案路徑。", "from pathlib import Path\ndata_dir = Path('lesson12_project_data')\ndata_dir.mkdir(exist_ok=True)\ncsv_path = data_dir / 'records.csv'\nprint('資料位置：', csv_path.resolve())"),
    ("寫入 CSV", "使用 DictWriter 保存交易。", "import csv\n\nwith csv_path.open('w', newline='', encoding='utf-8-sig') as file:\n    writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'note'])\n    writer.writeheader()\n    writer.writerows(records)\nprint('已保存：', csv_path)"),
    ("讀取 CSV", "讀取後把 amount 轉回 float。", "def load_records(path):\n    loaded = []\n    if not path.exists():\n        return loaded\n    with path.open(encoding='utf-8-sig') as file:\n        for row in csv.DictReader(file):\n            row['amount'] = float(row['amount'])\n            loaded.append(row)\n    return loaded\n\nloaded_records = load_records(csv_path)\nshow_records(loaded_records)"),
    ("保存函式", "把 CSV 寫入步驟整理成可重複使用的函式。", "def save_records(records, path):\n    with path.open('w', newline='', encoding='utf-8-sig') as file:\n        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'note'])\n        writer.writeheader()\n        writer.writerows(records)\n    return len(records)\n\nprint('保存筆數：', save_records(records, csv_path))"),
    ("摘要函式", "回傳收入、支出與餘額。", "def calculate_summary(records):\n    income = 0\n    expense = 0\n    for record in records:\n        if record['amount'] >= 0:\n            income += record['amount']\n        else:\n            expense += abs(record['amount'])\n    return {'income': income, 'expense': expense, 'balance': income - expense}\n\nsummary = calculate_summary(records)\nprint('收入：', summary['income'])\nprint('支出：', summary['expense'])\nprint('餘額：', summary['balance'])"),
    ("刪除交易", "使用編號刪除前先驗證範圍。", "def delete_record(records, number):\n    index = number - 1\n    if index < 0 or index >= len(records):\n        raise IndexError('交易編號不存在')\n    return records.pop(index)\n\ndemo_records = records.copy()\nremoved = delete_record(demo_records, 1)\nprint('刪除：', format_record(removed))"),
    ("選單畫面", "建立清楚的文字選單。", "def show_menu():\n    print('1. 新增交易')\n    print('2. 查看交易')\n    print('3. 查看摘要')\n    print('4. 保存資料')\n    print('0. 結束')\n\nshow_menu()"),
    ("處理選單選擇", "用 Dict 對照選項與功能名稱。", "menu = {'1': '新增交易', '2': '查看交易', '3': '查看摘要', '4': '保存資料', '0': '結束'}\nchoice = '3'\nif choice in menu:\n    print('你選擇：', menu[choice])\nelse:\n    print('沒有這個選項')"),
    ("輸入日期驗證", "使用 datetime 檢查 YYYY-MM-DD。", "from datetime import datetime\n\ndef validate_date(text):\n    try:\n        datetime.strptime(text, '%Y-%m-%d')\n        return True\n    except ValueError:\n        return False\n\nprint(validate_date('2026-08-15'))\nprint(validate_date('2026/08/15'))"),
    ("產生文字報表", "把摘要整理成容易閱讀的文字。", "def build_report(records):\n    summary = calculate_summary(records)\n    lines = [\n        '記帳摘要',\n        f\"收入：{summary['income']:.0f}\",\n        f\"支出：{summary['expense']:.0f}\",\n        f\"餘額：{summary['balance']:.0f}\",\n    ]\n    return '\\n'.join(lines)\n\nprint(build_report(records))"),
    ("輸出報表檔案", "把摘要保存成 summary.txt。", "report_path = data_dir / 'summary.txt'\nreport_path.write_text(build_report(records), encoding='utf-8')\nprint('報表位置：', report_path.resolve())"),
    ("整合專案流程", "載入資料、加入一筆、保存並顯示摘要。", "project_records = load_records(csv_path)\nadd_record(project_records, '2026-08-15', '餐飲', -180, '晚餐')\nsave_records(project_records, csv_path)\nshow_records(project_records)\nprint(build_report(project_records))"),
]


def build_items(raw):
    return [{"title": t, "prompt": p, "answer": a, "starter": "# " + p + "\n# 請在這裡完成"} for t, p, a in raw]


def lesson_readme(number, title, description):
    return f"""# Lesson {number}｜{title}\n\n## 學習成果\n\n- 能用自己的話說明本課的核心流程。\n- 能完成 25 個 learning 示範、25 題 exercises 與對應 solutions。\n- 能把前面學過的語法放進可保存、可分享的小型作品。\n\n## 教材檔案\n\n- `lesson{number}_learning.ipynb`：25 個逐步示範。\n- `lesson{number}_exercises.ipynb`：25 題課堂練習。\n- `lesson{number}_solutions.ipynb`：逐題完整解答。\n- `lesson{number}_homework.ipynb`：課後整合任務。\n\n## 教學提醒\n\n{description}\n"""


for number, slug, title, description, raw in [
    ("11", "git_github", "Git 與 GitHub 入門", "先建立本機版本觀念，再帶到 GitHub。課堂只教 init、status、add、commit、log、remote、push、pull、clone，不加入分支與多人協作。", lesson11),
    ("12", "expense_project", "Python 小專案：個人記帳工具", "以一個可完成的專案整合 List、Dict、迴圈、函式、錯誤處理、Path 與 CSV。先完成最小版本，再逐步加入統計、搜尋與報表。", lesson12),
]:
    folder = ROOT / 'course_v2' / 'lessons' / f'lesson{number}_{slug}'
    items = build_items(raw)
    write_nb(folder / f'lesson{number}_learning.ipynb', notebook(f'Lesson {number}｜{title}', description, items, solved=True))
    write_nb(folder / f'lesson{number}_exercises.ipynb', notebook(f'Lesson {number}｜課堂練習', '先獨立完成，再逐題檢討。每題都延續 learning 的同一條學習主線。', items, solved=False))
    write_nb(folder / f'lesson{number}_solutions.ipynb', notebook(f'Lesson {number}｜課堂練習解答', '解答保留完整步驟，避免使用不利初學者閱讀的一行寫法。', items, solved=True))
    homework = [{"title": "完成可展示版本", "prompt": "整理今天的成果，加入清楚輸出、錯誤處理與 README 說明。", "starter": "# 請完成你的課後作品", "answer": raw[-1][2]}]
    write_nb(folder / f'lesson{number}_homework.ipynb', notebook(f'Lesson {number}｜課後整合任務', '完成後請重新啟動 Kernel 並從頭執行，確認作品可以獨立運作。', homework, solved=False))
    (folder / 'README.md').write_text(lesson_readme(number, title, description), encoding='utf-8')

print('Lesson 11 and 12 notebooks created.')
