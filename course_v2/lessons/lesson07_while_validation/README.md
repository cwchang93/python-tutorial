# Lesson 07｜while 迴圈與輸入驗證

## 學習成果

- 能說明 `for` 與 `while` 的使用時機。
- 能用條件控制重複執行，並正確更新迴圈變數。
- 能使用 `break`、`continue` 結束或跳過一輪。
- 能設計登入重試、選單與「直到輸入正確」的互動流程。
- 能用 `try / except` 處理數字轉換錯誤，避免程式中斷。
- 能完成簡易 ATM 選單與訂票數量驗證。

## 180 分鐘腳本

| 時間 | 教學活動 | 教材 |
|---|---|---|
| 0–15 | Lesson 06 暖身：固定次數或未知次數 | learning 1–2 |
| 15–45 | while 條件、計數器與停止條件 | learning 3–6 |
| 45–70 | ⭐ 必做：倒數、累加、密碼重試 | exercises 1–5 |
| 70–80 | 檢討與休息 | exercises 1–5 |
| 80–110 | input 驗證、try / except、continue | learning 7–12 |
| 110–140 | ⭐⭐ 應用：年齡、價格、選單驗證 | exercises 6–10 |
| 140–165 | ATM 與訂票流程小作品 | learning 13–16 |
| 165–180 | ⭐⭐⭐ 挑戰與作業說明 | exercises 11–14 |

## 教材檔案

- `lesson07_learning.ipynb`：25 個完整示範例題。
- `lesson07_exercises.ipynb`：25 題分級課堂練習。
- `lesson07_solutions.ipynb`：與課堂練習逐題對應的 25 題解答。
- `lesson07_homework.ipynb`：4 題課後整合任務。

課堂可依進度先完成前 14 題，其餘題目作為加強練習與複習題庫。

## 常見卡點

- `while` 條件若永遠為 `True`，程式就不會停止。
- 計數器要在迴圈內更新，否則容易形成無限迴圈。
- `break` 結束整個迴圈；`continue` 回到下一輪。
- `input()` 一律得到字串；轉成數字時要預防輸入錯誤。
- 驗證成功後要明確 `break`，不要讓使用者重複輸入。
