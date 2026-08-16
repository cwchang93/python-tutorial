# Lesson 10｜模組與檔案

## 學習成果

- 能辨識本課程的核心概念並用生活化案例說明。
- 能完成 25 個 learning 示範、25 題 exercises 與對應 solutions。
- 能把語法放進小型資料處理流程。

## 教材檔案

- `lesson10_learning.ipynb`：25 個完整示範例題。
- `lesson10_exercises.ipynb`：25 題分級課堂練習。
- `lesson10_solutions.ipynb`：與課堂練習逐題對應的 25 題解答。
- `lesson10_homework.ipynb`：課後整合任務。

## 共用資料

課堂範例使用 `course_v2/data/lesson10_sales.csv`，不需要另外搜尋或建立 CSV。

如果 Notebook 是從本資料夾啟動，請使用：

```python
from pathlib import Path

data_path = Path('../../data/lesson10_sales.csv')
```

CSV 讀取後，`quantity` 與 `unit_price` 仍是文字，進行計算前要先轉成 `int` 或 `float`。

## 教學提醒

- 先區分內建功能、標準函式庫、第三方套件與自訂模組；標準函式庫不需要 `pip install`。
- 比較 `import module`、`from module import name` 與 `import module as alias`，避免使用 `import *`。
- 檔案模式要清楚區分：`r` 讀取、`w` 覆寫、`a` 追加。
- `write()` 與 `writelines()` 不會自動換行；`print(..., file=file)` 會自動換行。
- 比較 `read()`、`readline()`、`readlines()`，並示範直接使用 `for line in file` 逐行處理。
- 用標準函式庫與文字檔、CSV 保存資料，為後續資料分析準備素材。
