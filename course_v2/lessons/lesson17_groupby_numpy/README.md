# Lesson 17｜資料整理、統計與 NumPy 橋接

這一課把多筆交易整理成可回答問題的摘要。前半段以 Pandas `groupby` 為主，後半段補上 NumPy 的必要觀念，讓學生理解 Pandas 背後如何進行整批數值運算。

## 學習目標

- 使用 `groupby()` 依城市、分類等欄位分組
- 使用 `sum()`、`mean()`、`count()`、`size()` 與 `nunique()` 回答不同問題
- 使用 `agg()` 一次產生多項統計
- 分辨 Series 型結果與 `as_index=False` 的 DataFrame 型結果
- 使用多欄分組、`reset_index()`、篩選與排序整理報表
- 說明「訂單數」「顧客數」「平均訂單金額」的差異
- 使用 `np.array()` 建立 NumPy 陣列
- 查看 `shape`、`dtype`，進行向量化運算與布林遮罩
- 使用 `to_numpy()` 理解 Pandas 與 NumPy 的關係

## 教材檔案

- `lesson17_learning.ipynb`：25 個逐步示範
- `lesson17_exercises.ipynb`：25 題課堂練習
- `lesson17_solutions.ipynb`：教師版完整解答
- `lesson17_homework.ipynb`：城市銷售報表作業
- `lesson17_sales.csv`：48 筆跨城市、分類與月份的完整銷售資料

請把 Notebook 與 `lesson17_sales.csv` 放在同一資料夾。程式直接使用相對路徑 `Path("lesson17_sales.csv")`。

## 三小時建議節奏

1. 0～20 分鐘：從「一筆一列」走到「每個城市一列」
2. 20～80 分鐘：單欄分組、加總、平均、筆數與不重複顧客
3. 80～120 分鐘：`agg()`、多欄分組、排序與篩選
4. 120～150 分鐘：NumPy 陣列、向量化運算與布林遮罩
5. 150～180 分鐘：完成城市銷售摘要並檢討

## 生活化比喻

- `groupby` 像超商理貨：先依目的地把包裹分箱，再計算每箱數量或重量。
- `agg` 像店長的日報表：同一張表同時要總營業額、平均客單價與訂單數。
- NumPy 像一次調整整排商品標價：不用逐張改標籤，可以整批乘上折扣或稅率。

## 本課邊界

NumPy 只教資料分析需要的陣列、向量化、遮罩與 Pandas 銜接，不延伸到矩陣代數或廣播細節。圖表留到 Lesson 18。
