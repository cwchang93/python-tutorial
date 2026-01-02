# Output Folder

This folder contains generated files from the analysis:

- **Charts**: PNG images of visualizations
- **Reports**: Cleaned data and analysis results

## 📁 Generated Files

When you run the analysis, the following files will be created here:

- `top_breeds.png` - Chart showing the most common dog breeds
- Any other visualizations you create in the notebooks

## ⚠️ Important Note

**These files are generated automatically and should NOT be committed to Git.**

The `.gitignore` file (if present) will exclude these files from version control, keeping your repository clean.

## 🧹 Cleanup

To remove all generated files:

**Windows**:

```cmd
del /Q *
```

**macOS/Linux**:

```bash
rm -f *.png *.csv *.txt
```

Or simply delete the files manually through your file explorer.
