# Lesson 12｜Python 小專案：個人記帳工具

## 學習成果

- 能用自己的話說明本課的核心流程。
- 能完成 25 個 learning 示範、25 題 exercises 與對應 solutions。
- 能把前面學過的語法放進可保存、可分享的小型作品。

## 教材檔案

- `lesson12_learning.ipynb`：25 個逐步示範。
- `lesson12_exercises.ipynb`：25 題課堂練習。
- `lesson12_solutions.ipynb`：逐題完整解答。
- `lesson12_homework.ipynb`：課後整合任務。

## 教學提醒

Lesson 12 不是單獨再教一次 CSV，而是用「個人記帳工具」整合前面學過的 Python 基礎：List、Dict、`for`、`if`、函式、`return`、錯誤處理與 `Path`。CSV 在本課扮演資料保存與讀回的角色，讓程式關閉後資料仍然保留。

建議教學順序：

1. 先用 List、Dict 建立交易資料。
2. 用迴圈、條件判斷與函式完成新增、查詢、統計。
3. 用 `try`、`except` 驗證日期、分類與金額輸入。
4. 用 `Path` 建立資料路徑，再用 `csv.DictWriter` 保存資料。
5. 用 `csv.DictReader` 讀回資料，最後整合成選單與報表。

CSV 的完整資料分析會在 Lesson 13 開始；Lesson 12 先讓同學完成一個可以操作、可以保存、可以讀回的小作品。
