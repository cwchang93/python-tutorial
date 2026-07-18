# Python 課程盤點報告

> 範圍：repo 全文件掃描 + git 歷史。純客觀盤點，不含優化建議或好壞評價。

---

## 1. 課程結構總覽

### 1.1 目錄結構

| 目錄 | 檔案類型 | 檔案數 |
|---|---|---|
| `lesson02_basics` | `.py`（唯一使用 .py 而非 .ipynb 的模組）+ README.md | 6 個 .py + 1 test.ipynb |
| `lesson03_strings_lists_conditions` | `.ipynb`（exercises/solutions 成對） | 5 |
| `lesson04_for_loops` | `.ipynb`（含「基礎」「30題」「進階」三套） | 9 |
| `lesson05_recursive_exception_def` | `.ipynb`（3 子主題 × learning/exercises/solutions） | 9 |
| `lesson06_dict_try_catch` | `.ipynb`（3 子主題 × learning/exercises/solutions） | 9 |
| `lesson07_file` | `.ipynb` | 3 |
| `lesson08_module` | `.ipynb` | 3 |
| `lesson09_oop` | `.ipynb` | 3 |
| `lesson11_12_data` | `.ipynb` + 1 個 `.txt`（內容其實是 notebook JSON） | 4 + exercise 子目錄 2 |
| `lesson13_14_pandas` | `.ipynb` + `.csv` | 4 |
| `lesson15_16_numpy` | `.ipynb` | 2 |
| `lesson17_18_review` | `.ipynb`（跨 L02–L16 總複習） | 2 |
| `archive_lesson11_12_data` | `.ipynb`（與 `lesson11_12_data` 平行存在的舊版內容） | 11 |
| `review/` | `.ipynb` + `.txt`（各單元隨堂複習卷） | 14 |
| `projects/dog_analysis_project` | 獨立小專案（`src/`、`notebooks/`、`data/`、`requirements.txt`、README） | 8 |
| `tqc/` | 一份 `tqc.md`（題號列表）+ `tqc-110.py` | 2 |
| `data/` | 共用 csv/txt 資料集 | 3 |

- **不存在 lesson01 與 lesson10**：lesson01 可能併入 lesson02（README 標註「完全零基礎的起點」），lesson10 缺口與 `review/L7_L8_review.txt`、`L11_L12_review.txt` 中出現的 git 作業說明（git init / add / commit / push 到 GitHub）時間點吻合，推測 Git 操作是口頭教學搭配這兩份 `.txt` 回家作業，repo 中沒有對應的教學 notebook。
- 沒有投影片檔（找不到 `.pdf` / `.pptx` / `.key`）。`lesson02_basics/README.md` 內文提到「投影片對應章節」，代表投影片是外部檔案，repo 內查無其實體或連結。

### 1.2 每小時對應量

- repo 內找不到任何標註課程總時數、每堂課時數，或明確的 syllabus / 教學計畫文件。
- 唯一線索是 `lesson02_basics/README.md`（唯一一份模組級教學指引），其餘模組沒有對應文件。
- 用 git commit 時間推算実際開課節奏：2025-12-15 起課，2026-03-14 完成初版全部內容（lesson02 → lesson17_18 + review），約 13 週。之後在 2026-05-25 有兩筆小幅修訂（見 5.3），本次分析請求日為 2026-07-08。
- 目錄命名多以「兩堂合一」呈現（`lesson11_12`、`lesson13_14`、`lesson15_16`、`lesson17_18`），暗示每次上課涵蓋兩個 lesson number，但沒有文件明確標註每個 lesson number 對應幾小時。

### 1.3 檔案類型統計（每模組 code / markdown cell 數，`.ipynb` 加總）

| 模組 | notebook 數 | code cells | markdown cells |
|---|---|---|---|
| lesson02_basics | 1（僅 test.ipynb；主要教材是 .py） | 2 | 0 |
| lesson03 | 5 | 132 | 156 |
| lesson04 | 9 | 252 | 317 |
| lesson05 | 9 | 174 | 261 |
| lesson06 | 9 | 227 | 292 |
| lesson07 | 3 | 73 | 58 |
| lesson08 | 3 | 50 | 95 |
| lesson09 | 3 | 73 | 72 |
| lesson11_12_data | 4 | 33 | 39 |
| lesson13_14_pandas | 4 | 208 | 136 |
| lesson15_16_numpy | 2 | 55 | 58 |
| lesson17_18_review | 2 | 62 | 73 |

---

## 2. 內容盤點

### 2.1 各模組核心主題

- lesson02：變數、資料型態、運算子、縮排、`if` 初步、list/tuple/dict/set 初步
- lesson03：字串方法、list 操作、條件判斷（if/elif/else）
- lesson04：for 迴圈（range 三種用法）、while 迴圈、break/continue、進階迴圈練習
- lesson05：遞迴（recursive）、錯誤訊息判讀（SyntaxError 等常見錯誤類型）、函式定義（def/return）
- lesson06：排序（sorted/sort）、字典（dict）、例外處理（try/except）
- lesson07：檔案讀寫（open/read/write/readline/readlines/writelines）
- lesson08：模組與 import（含自建模組專案 dog_analysis_project）
- lesson09：物件導向（class/`__init__`/self/屬性/方法/dataclass），迷你專案 TodoList
- lesson11_12：pandas 初體驗（read_csv、head、info、基礎欄位觀察）
- lesson13_14：pandas 進階（資料清理、缺值處理、分組統計、資料型別檢查）
- lesson15_16：NumPy（陣列運算、與 pandas 對照）+ 股價分析小專案
- lesson17_18：L02–L16 全範圍總複習

### 2.2 主題重複訊號

- **錯誤/例外相關主題被拆成兩個模組教**：lesson05 的 `05_02_error_learning.ipynb`（如何讀錯誤訊息、SyntaxError/常見錯誤類型）與 lesson06 的 `06_03_exception_learning.ipynb`（什麼是 Exception、try/except 機制）都圍繞「錯誤」概念，但拆在不同模組，且 lesson05 資料夾命名為 `recursive_exception_def`（暗示 exception 在這裡教完），實際 try/except 語法卻在 lesson06 才教。
- **pandas 讀取/檢視資料的起手式重複兩次**：`lesson11_12_data` 的內容（載入套件、read_csv、head、資料大小/欄位）與 `lesson13_14_pandas/lesson_13_learning.ipynb` 的 Section 0–3（環境檢查、快速回顧 DataFrame、讀取 CSV、`df.head()`/`df.tail()`）高度重疊，`lesson_13_learning.ipynb` 內文自稱是「快速回顧」，屬於刻意的鷹架式重複，非疏漏。
- **`archive_lesson11_12_data` 與 `lesson11_12_data` 兩份平行存在**：git log 顯示兩者同一天（2026-01-23）出現，`archive_lesson11_12_data` 有較重的 30 題練習 + solutions 全套，`lesson11_12_data` 則是較輕量的 practice notebook（僅 33 code cells）。兩者主題重疊（同樣是 pandas 基礎資料操作），目前並存於 repo，未標示何者為最終採用版本。

### 2.3 先後順序/難度曲線訊號

- **NumPy（lesson15_16）排在 pandas（lesson13_14）之後**：與一般「先教 NumPy 陣列運算基礎，再教建立在其上的 pandas」的慣例順序相反。教材本身在 `lesson_15_16_learning.ipynb` 開頭以「你已經會 Pandas，為什麼還要學 NumPy？」破題，顯示此順序是刻意安排，非隨機。
- **lesson04（for 迴圈）內容量明顯偏大**：9 個檔案、252 個 code cells，同時包含「基礎」「30題」「進階 30 題」三套題本，是所有單一模組中題本套數最多、cell 數最多的（詳見第 5 節）。
- **Git 版控操作**（`review/L7_L8_review.txt`、`L11_L12_review.txt`）在課程進行到 lesson08–09 附近才以回家作業形式出現，但沒有對應的先備教學 notebook，學生第一次接觸 `git init/add/commit` 是直接透過文字說明的作業指示。

---

## 3. 練習題與範例品質

### 3.1 練習題數量（依檔名/標題自報數字）

| 模組/子主題 | 題數（依標題） |
|---|---|
| lesson03 條件 | 約 20 題（Q1 起） |
| lesson03 字串/list | 約 20+ 題 |
| lesson04 for 迴圈基礎 | 30 題 |
| lesson04 進階迴圈 | 30 題 |
| lesson04 while | 6 題（while_exercises_30 檔名雖標 30，實際標題只到題 06） |
| lesson05 遞迴 | 10 題 |
| lesson05 錯誤判讀 | 20 題 |
| lesson05 def | 30 題 |
| lesson06 排序 | 約 7 題起（exercises_20 檔名標 20，起始題號從 2 開始，缺題 1） |
| lesson06 dict | 30 題 |
| lesson06 exception | 30 題 |
| lesson07 file | 20 題 |
| lesson08 module | 6 題起 |
| lesson09 OOP | 約 10 題起 |
| lesson17_18 總複習 | 涵蓋 L02–L16 全部主題的整合題 |

- 多個檔名標「_20」「_30」但實際起始題號或結尾題號與檔名數字不完全一致（如 `06_01_sorting_exercises_20.ipynb` 標題從「題目 2」開始、`while_exercises_30.ipynb` 標題只到「題目 06」），檔名與內容題數可能不同步。

### 3.2 難度抽樣觀察

- lesson05「遞迴」練習仍保留大量 `# TODO: 請在這裡寫程式` 空白區塊（9 處），屬於典型「先講解後留白練習」格式，與同模組其他子主題（如 `def_exercises_30`）的完整題面＋TODO 格式一致。
- lesson06 `06_02_dict_exercises_30.ipynb` 中段（約 Q15 後）留有一則進度註記：「🎯 暫時完成前 15 題」「⏳ Section B/C（16–30題）- 待補充」，但檔案後續實際仍列出 Q16–Q30 的完整 TODO 區塊 —— 代表這則「待補充」註記在內容補齊後未被移除，屬於過時的草稿標記。
- lesson09 OOP 練習與教學內容主題對應（class/屬性/方法/計數器/溫度轉換/矩形類別），難度呈遞增排列。

### 3.3 缺解答/測試案例/說明不清狀況

- `review/L1_L4_review_test.ipynb`（45 cells）：無對應解答檔，也無內嵌解答。
- `review/L5_L6_review_test.ipynb`（61 cells）：無對應解答檔，也無內嵌解答。
- `review/L13_L14_review.ipynb`（14 cells）：僅 1 個 cell 帶有解答標記，其餘題目未見解答。
- 對照組（有配對解答的範例）：`L1_L4_review_test-2.ipynb` ↔ `L1_L4_review_test-ans-2.ipynb`、`L1_L8_review_test.ipynb` ↔ `L1_L8_review_ans.ipynb`、`260307_Python_review.ipynb` ↔ `260307_Python_solution.ipynb`、`L11_L12_review_test_data.ipynb`（內嵌「✅ 參考解答」）—— 顯示同一 `review/` 資料夾內解答配置方式不一致（有的獨立解答檔、有的內嵌、有的完全沒有）。
- `archive_lesson11_12_data/exercise/population_exercise_teacher.ipynb` 是 **0 bytes 的空檔案**（git log 有一筆 commit message 為「feat: remove teacher」，推測內容曾被清空但檔案本身留存）。

---

## 4. 技術債與過時內容

### 4.1 程式碼寫法

- 全文掃描未發現 Python 2 語法（`print` 無括號）、`.ix[` 索引、`.iteritems()`、`np.float`/`np.int` 等已棄用寫法／別名，也未發現 `distutils` 等已淘汰套件引用 —— 程式碼風格整體屬於現行 Python 3 慣例（有使用 f-string、`dataclass` 等較新寫法，如 lesson09 的 TodoItem 範例）。
- 全部 73 個 `.ipynb`（含 review、archive）中，**沒有任何函式使用型別註記（type hints，如 `-> int`）**，repo 內也沒有 `pyproject.toml`／`ruff`／`flake8`／`black` 等 lint/format 設定檔。

### 4.2 版本與環境設定

- 多個 notebook metadata 記錄 kernel 版本為 **Python 3.9.6**（2021 年釋出；3.9 分支已於 2025-10 進入 EOL，不再有官方安全更新）。
- 主線課程（lesson02–17_18）**沒有任何 requirements.txt 或環境鎖定檔**；唯一有 `requirements.txt` 的是 `projects/dog_analysis_project`，且採用 `>=` 下限寫法（`pandas>=1.3.0`、`numpy>=1.21.0`、`matplotlib>=3.4.0`），未鎖定上限或精確版本。
- 根目錄 `requirements-nbconvert.txt`（僅用於 HTML 轉檔工具鏈）採用範圍鎖定（`>=7.16,<8.0` 等）。
- 環境設定說明僅存在於兩處：根目錄 `README.md`（僅涵蓋 nbconvert 部署流程，非課程環境）、`projects/dog_analysis_project/README.md`（含完整安裝與疑難排解步驟）。**lesson02–17_18 主線教材本身沒有一份統一的「如何安裝 Python/建立虛擬環境」教學文件**。

---

## 5. 潛在優化切入點（訊號盤點，不下結論）

### 5.1 內容量落差訊號

- lesson04（for 迴圈）：9 檔案／252 code cells／317 md cells，同時含「基礎」「30題」「進階30題」三套題本，是所有模組中規模最大者。
- lesson11_12_data：僅 4 檔案／33 code cells，是所有 `.ipynb` 模組中規模最小者，且明顯小於其平行存在的 `archive_lesson11_12_data`（11 檔案，含 30 題練習+解答全套）與其後續模組 lesson13_14_pandas（208 code cells）。
- lesson02_basics：三份 .py 練習檔並存但份量差異大（`exercises.py` 83 行 vs `02-01-data-2-exercises-3.py` 652 行），且格式不同（後者將解答直接內嵌在同一檔案的「解答區」段落，前兩者則是 exercises/solutions 分離成兩個檔案）。

### 5.2 疑似臨時加入、缺乏系統整理的訊號

- `lesson11_12_data/lesson11_learning_first_analysis.txt`：副檔名是 `.txt`，但檔案內容其實是完整的 Jupyter notebook JSON 結構。
- `lesson02_basics/02-01-data-2-exercises-3.py`：命名風格（`02-01-` 前綴＋流水號）與同資料夾其他檔案（`exercises.py`／`exercises-2.py`）不一致，且是三份平行練習檔中唯一「exercises+solutions 合併於一檔」的格式。
- `06_02_dict_exercises_30.ipynb` 內殘留的「暫時完成前 15 題／待補充」草稿註記（見 3.2）。
- `archive_lesson11_12_data` 與 `lesson11_12_data` 同日並存但無說明何者為最終版本。
- `population_exercise_teacher.ipynb` 空檔案殘留（見 3.3）。

### 5.3 學生回饋／TODO 註記線索

- repo 內沒有獨立的 issue tracker、feedback 檔案或 CHANGELOG。
- 唯一可辨識「課後回饋回饋教材」的痕跡，是 2026-05-25 的兩筆 commit（`Refine beginner lesson structure`、`Refine later lessons for beginners`）：分別對 lesson02–04 的少量 exercise 檔案，以及對 lesson05–09 全部 `_learning.ipynb` 檔案，插入了統一格式的「### 學習建議」段落（標註「核心先做」／「可先略過」／建議先備知識），例如 `05_01_recursive_learning.ipynb` 新增「遞迴的費氏數列效能比較對初學者容易超載」的提示。這些改動集中在 lesson02–09（前半段基礎語法），**lesson11 之後（pandas/numpy/review 區塊）未見同類型的retroactive 難度標註**。
- `06_02_dict_exercises_30.ipynb` 中殘留的「待補充」字樣（見上）是另一個可能反映「課程進行中臨時擴充題目」過程的痕跡。
