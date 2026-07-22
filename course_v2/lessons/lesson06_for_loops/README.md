# Lesson 06｜for 迴圈與資料逐筆處理

## 學習成果

- 能使用 `for` 逐筆讀取 List。
- 能使用 `range()` 重複執行固定次數。
- 能使用累加器與計數器計算總和、平均與筆數。
- 能用 `if` 篩選資料，並用 `break`、`continue` 控制迴圈。
- 能使用 `enumerate()` 顯示編號，並走訪 Dict。
- 能完成簡單的銷售統計器。

## 180 分鐘腳本

| 時間 | 教學活動 | 教材 |
|---|---|---|
| 0–15 | Lesson 04–05 暖身：List、Dict、條件判斷 | learning 1–3 |
| 15–35 | `for item in list` 與生活點名比喻 | learning 1–3 |
| 35–55 | `range()` 與固定次數 | learning 4–5 |
| 55–75 | ⭐ 必做：逐筆讀取、總和、計數 | exercises 1–6 |
| 75–85 | 檢討與休息 | solutions 1–6 |
| 85–110 | 累加、平均、篩選與新 List | learning 6–10 |
| 110–135 | ⭐⭐ 應用題，老師巡堂 | exercises 7–12 |
| 135–150 | `break`、`continue`、`enumerate()` | learning 12–14 |
| 150–170 | Dict、List 裡的 Dict、銷售統計 | learning 15–18 |
| 170–180 | ⭐⭐⭐ 小作品與作業說明 | exercises 13–15 |

## 教學取捨

- 核心：`for`、`in`、`range()`、累加器、計數器、`if + for`。
- 認識：`break`、`continue`、`enumerate()`、`dict.items()`。
- 暫不深入：巢狀迴圈、List comprehension、複雜 `while`。

## 常見卡點

- `for` 下一行要縮排，且每一輪都會重新執行區塊。
- 累加器要在迴圈前先設為 `0`。
- `range(5)` 是 `0` 到 `4`，結束值不包含。
- `break` 結束整個迴圈；`continue` 只跳過這一輪。
- List 裡的 Dict 要先取出資料，再使用 `order['amount']`。
