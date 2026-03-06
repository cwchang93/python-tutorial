# Python Tutorial - Notebook HTML Deployment

這個專案可以用 `jupyter nbconvert` 將 Jupyter Notebook (`.ipynb`) 轉成可部署的 HTML 靜態頁面。

## 1) 安裝

建議先建立虛擬環境，再安裝需求：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-nbconvert.txt
```

## 2) 轉成 HTML（不用腳本）

單一檔案：

```bash
jupyter nbconvert --to html lesson13_14_pandas/lesson_13_learning.ipynb
```

指定輸出資料夾：

```bash
jupyter nbconvert --to html --template lab --output-dir site lesson13_14_pandas/lesson_13_learning.ipynb
```

同一資料夾一次轉多個檔案：

```bash
jupyter nbconvert --to html lesson13_14_pandas/*.ipynb --output-dir site
```

## 3) 本機預覽（模擬部署）

```bash
python3 -m http.server 8000 --directory site
```

打開：`http://127.0.0.1:8000`

## 4) 部署建議

`site/` 是靜態 HTML，可直接部署到：

- GitHub Pages
- Netlify
- Vercel（Static）
- 任何 Nginx/Apache 靜態站台
