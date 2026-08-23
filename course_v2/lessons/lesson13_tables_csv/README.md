# Lesson 13｜資料分析入門：表格與 CSV

這一課先不急著使用 Pandas，而是把「資料表到底在表示什麼」講清楚。學生會從生活化的訂單表開始，理解列、欄、儲存格與 CSV，並使用 Python 內建的 `csv` 模組完成第一次小型分析。

## 學習目標

- 分辨資料表中的列（row）、欄（column）與儲存格（cell）
- 理解一列是一筆紀錄、一欄是一種固定意義的資料
- 看懂 CSV 的標題列與資料列
- 使用 `csv.reader` 與 `csv.DictReader` 讀取 CSV
- 知道 CSV 讀入後通常是字串，計算前要轉換型態
- 把分析問題轉成「需要哪些欄位、要做什麼計算」
- 進行遺漏值、重複編號等基本資料品質檢查

## 教材檔案

- `lesson13_learning.ipynb`：25 個逐步示範
- `lesson13_exercises.ipynb`：25 題課堂練習
- `lesson13_solutions.ipynb`：教師版完整解答
- `lesson13_homework.ipynb`：整合型回家作業
- `../../data/lesson13_orders.csv`：本課與 Lesson 14 共用的完整訂單資料

## 建議教學順序

1. 用通訊錄、點名表與訂單表解釋「一列一件事、一欄一種意義」
2. 先閱讀 CSV 文字，再用 Python 讀取
3. 比較 `reader` 的 list 與 `DictReader` 的 dict
4. 示範字串轉成數字後才能正確加總
5. 最後用「問題 → 欄位 → 方法 → 結果」整理分析流程

## 教學提醒

- CSV 是純文字格式，不等於 Excel 活頁簿。
- 這課優先建立資料觀念；Pandas 留到 Lesson 14。
- 課堂範例刻意採用一般 `if`、`for` 寫法，不用一行式技巧，讓初學者看得見每一步。
