# Python 資料分析實戰 V2

這是可重複開課的正式課程主線。舊教材保留在專案原有目錄，作為內容來源與歷史參考。

## 快速入口

- 講師先讀：[WEEK01_TEACHER_BRIEF.md](WEEK01_TEACHER_BRIEF.md)
- 完整課綱：[COURSE_SYLLABUS.md](COURSE_SYLLABUS.md)
- 通用教學規則：[TEACHER_GUIDE.md](TEACHER_GUIDE.md)
- 第一堂：[lessons/lesson01_first_analysis/README.md](lessons/lesson01_first_analysis/README.md)
- 第二堂：[lessons/lesson02_python_basics/README.md](lessons/lesson02_python_basics/README.md)

## 課程定位

- 對象：Python 零基礎或僅有少量程式經驗的成人學員
- 節數：21 堂
- 預設時數：每堂 3 小時，一天 2 堂
- 產出：一份可公開展示的 Python 資料分析作品
- 核心流程：提出問題 → 讀取資料 → 檢查與清理 → 分析 → 視覺化 → 解讀 → 發布

## 教材約定

每堂課固定提供：

1. `README.md`：講師備課入口與時間腳本
2. `*_learning.ipynb`：教師示範與課堂講解
3. `*_exercises.ipynb`：學生練習，不含答案
4. `*_solutions.ipynb`：教師解答
5. `*_homework.ipynb`：課後作業
6. `data/`：可離線使用的資料

正式教材不寫班級日期，以 Lesson 編號維持跨期通用性。

## 建議環境

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r course_v2/requirements.txt
jupyter lab
```

若本機環境安裝失敗，將 notebook 與 `data/` 一起上傳 Google Colab 即可。

