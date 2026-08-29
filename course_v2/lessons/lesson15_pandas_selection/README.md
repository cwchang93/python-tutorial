# Lesson 15｜Pandas 選取與篩選

這一課延續 Lesson 14 的 DataFrame 健檢，開始回答「我只想看哪些資料？」。學生會先學欄位選取，再用條件建立布林遮罩，最後完成篩選、排序與新增欄位的完整流程。

## 學習目標

- 分辨選一欄得到 Series、選多欄得到 DataFrame
- 使用比較運算建立 True／False 條件
- 使用 `df[condition]` 篩選符合條件的列
- 使用 `&`、`|`、`~` 組合條件，並養成加括號的習慣
- 使用 `isin()` 與 `between()` 表達常見條件
- 使用 `sort_values()` 進行單欄與多欄排序
- 使用欄位運算新增 `revenue` 等衍生欄位
- 把選取、篩選、排序與新增欄位串成可讀的分析流程

## 教材檔案

- `lesson15_learning.ipynb`：25 個逐步示範
- `lesson15_exercises.ipynb`：25 題課堂練習
- `lesson15_solutions.ipynb`：教師版完整解答
- `lesson15_homework.ipynb`：整合型回家作業
- `../../data/lesson13_orders.csv`：延續 Lesson 13、14 的乾淨訂單資料

## 建議教學順序

1. 先用「點餐單」比喻欄位選取：只拿需要看的欄位
2. 把布林條件比喻成門口驗票：True 才能留下
3. 先練單一條件，再組合兩個條件
4. 排序前先說清楚要依哪一欄、由大到小或由小到大
5. 最後新增營業額欄位，完成一次小型資料查詢

## 本課邊界

本課不處理缺失值、重複值與格式混亂，這些留到 Lesson 16；不做分類彙總與平均值比較，這些留到 Lesson 17。
