# Solutions 發布流程

課程進行期間，以下檔案由 `.gitignore` 保留在老師本機：

- `lesson01_solutions.ipynb`
- `lesson02_solutions.ipynb`
- `lesson02_2_solutions.ipynb`

一般執行 `git add .` 不會加入這些答案。

## 課程結束後發布

確認 Notebook 已清除不必要的執行輸出後，使用：

```bash
git add -f course_v2/lessons/lesson01_first_analysis/lesson01_solutions.ipynb
git add -f course_v2/lessons/lesson02_python_basics/lesson02_solutions.ipynb
git add -f course_v2/lessons/lesson02_data_structures/lesson02_2_solutions.ipynb
```

接著照正常流程 commit 與 push。

若未來希望答案持續和學生版分離，建議改放在私人教師 repository，學生版只保留題目。
