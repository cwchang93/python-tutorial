# Lesson 14｜Pandas 與 DataFrame

這一課把 Lesson 13 的 CSV 與表格觀念帶進 Pandas。重點不是立刻做複雜分析，而是學會把資料安全地載入 DataFrame，並在動手分析前完成基本巡檢。

## 學習目標

- 使用慣例 `import pandas as pd`
- 使用 `pd.read_csv()` 載入課程 CSV
- 理解 DataFrame 與 Series 的差異
- 使用 `head()`、`tail()`、`sample()` 查看資料
- 使用 `shape`、`columns`、`dtypes`、`index` 了解結構
- 使用 `info()` 與 `describe()` 做初步巡檢
- 檢查缺值、重複列與唯一值數量
- 建立可重複使用的 DataFrame 健康檢查函式

## 教材檔案

- `lesson14_learning.ipynb`：25 個逐步示範
- `lesson14_exercises.ipynb`：25 題課堂練習
- `lesson14_solutions.ipynb`：教師版完整解答
- `lesson14_homework.ipynb`：整合型回家作業
- `../../data/lesson13_orders.csv`：延續 Lesson 13 的訂單資料

## 建議教學順序

1. 先把 DataFrame 比喻成「Python 裡可操作的 Excel 工作表」
2. 讀檔後先看前後幾列，不急著直接分析
3. 依序回答：有幾列？有哪些欄？每欄是什麼型態？
4. 比較選一欄得到 Series、選多欄得到 DataFrame
5. 用完整健康檢查收尾，養成分析前先驗證資料的習慣

## 本課邊界

本課只負責「讀進來、看懂結構、確認健康」。欄位選取、條件篩選與排序會在 Lesson 15 詳講；缺值清理在 Lesson 16；分組彙總在 Lesson 17。
