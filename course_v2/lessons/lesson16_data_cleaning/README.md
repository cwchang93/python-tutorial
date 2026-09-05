# Lesson 16｜資料清理

真實資料很少一開始就乾淨。這一課使用刻意加入空白、重複、欄名不一致與錯誤格式的訂單 CSV，帶學生建立「先檢查、再修正、最後驗證」的清理習慣。

## 學習目標

- 使用 `isna()` 與 `sum()` 找出缺失值
- 依情境選擇 `dropna()` 或 `fillna()`
- 使用 `duplicated()` 與 `drop_duplicates()` 處理重複資料
- 清理欄位名稱的空白、大小寫與底線
- 使用 `rename()` 調整重要欄位名稱
- 使用 `.str.strip()`、`.str.replace()` 與 `.str.lower()` 統一文字
- 使用 `pd.to_datetime()` 轉換日期
- 使用 `pd.to_numeric()` 轉換數字並找出無法轉換的值
- 保留原始資料，另存清理後 CSV

## 教材檔案

- `lesson16_learning.ipynb`：25 個逐步示範
- `lesson16_exercises.ipynb`：25 題課堂練習
- `lesson16_solutions.ipynb`：教師版完整解答
- `lesson16_homework.ipynb`：整合型回家作業
- `lesson16_orders_dirty.csv`：隨課提供、刻意包含常見品質問題的練習資料

請把 Notebook 與 `lesson16_orders_dirty.csv` 保留在同一個資料夾。程式直接使用相對路徑 `Path("lesson16_orders_dirty.csv")`。

## 建議教學順序

1. 先把清理比喻成整理通訊錄：同一個人不能有三種名字
2. 每種問題都遵循「找出來 → 看明細 → 修正 → 再檢查」
3. 強調沒有唯一清理答案，要依欄位用途決定刪除或補值
4. 原始 DataFrame 用 `copy()` 保留，避免清理錯誤無法回復
5. 最後另存新 CSV，不覆蓋原始檔

## 本課邊界

本課專注資料品質與格式，不進行 `groupby` 分組統計；清理完成的資料會在 Lesson 17 用來分類彙總。
