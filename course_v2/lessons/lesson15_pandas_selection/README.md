# Lesson 15｜Pandas 選取與篩選

這一課延續 Lesson 14 的 DataFrame 健檢，開始回答「我只想看哪些資料？」。學生會先學欄位選取，再用條件建立布林遮罩，最後完成篩選、排序與新增欄位的完整流程。

## 學習目標

- 分辨選一欄得到 Series、選多欄得到 DataFrame
- 使用 `loc` 依標籤定位資料，使用 `iloc` 依整數位置定位資料
- 分辨 `loc` 與 `iloc` 切片是否包含終點
- 使用比較運算建立 True／False 條件
- 使用 `df[condition]` 篩選符合條件的列
- 使用 `&`、`|`、`~` 組合條件，並養成加括號的習慣
- 使用 `isin()` 與 `between()` 表達常見條件
- 使用 `sort_values()` 進行單欄與多欄排序
- 使用欄位運算新增 `revenue` 等衍生欄位
- 把選取、篩選、排序與新增欄位串成可讀的分析流程

## 教材檔案

- `lesson15_learning.ipynb`：28 個逐步示範
- `lesson15_exercises.ipynb`：28 題課堂練習
- `lesson15_solutions.ipynb`：教師版完整解答
- `lesson15_homework.ipynb`：整合型回家作業
- `lesson13_orders.csv`：已直接放在本課資料夾；只下載 Lesson 15 檔案也能執行

> 發給學生時，請讓 Notebook 與 `lesson13_orders.csv` 保持在同一個資料夾。程式直接使用相對路徑 `Path("lesson13_orders.csv")`。

## 建議教學順序

1. 先用「點餐單」比喻欄位選取：只拿需要看的欄位
2. 用「姓名找人」與「排隊號碼找人」比較 `loc`、`iloc`
3. 把布林條件比喻成門口驗票：True 才能留下
4. 先練單一條件，再組合兩個條件
5. 排序前先說清楚要依哪一欄、由大到小或由小到大
6. 最後新增營業額欄位，完成一次小型資料查詢

## 本課邊界

本課不處理缺失值、重複值與格式混亂，這些留到 Lesson 16；不做分類彙總與平均值比較，這些留到 Lesson 17。
