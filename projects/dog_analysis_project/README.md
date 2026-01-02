# 🐶 Dog Shelter Analysis Project

A beginner-friendly Python data analysis project for learning modules, data processing, and visualization.

## 📁 Project Structure

```
dog_analysis_project/
├── data/
│   ├── dogs.csv              # Original data (35 records)
│   └── dogs_cleaned.csv      # Cleaned data (generated)
├── notebooks/
│   └── 01_eda.ipynb          # Exploratory data analysis notebook
├── src/
│   ├── __init__.py           # Makes src a Python package
│   ├── dog.py                # Reusable functions (module)
│   └── main.py               # Main entry point (CLI)
├── output/
│   └── README.md             # Output folder for charts/reports
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

---

## 🚀 Quick Start (Windows & macOS)

### Step 1: Install Dependencies

Run the following command from the project root directory:

```bash
python -m pip install -r requirements.txt
```

**Important**: Use `python -m pip` instead of just `pip` to ensure packages are installed in the correct environment.

### Step 2: Run the Analysis

```bash
python src/main.py
```

This will:

- ✅ Read and clean the data
- ✅ Generate statistics
- ✅ Create a chart (`output/top_breeds.png`)
- ✅ Save cleaned data (`data/dogs_cleaned.csv`)

---

## 📊 Usage Examples

### Example 1: Basic Analysis (No Filters)

```bash
python src/main.py
```

### Example 2: Filter by City

```bash
python src/main.py --city 台北
```

### Example 3: Filter by Age Range

```bash
python src/main.py --min-age 2 --max-age 5
```

### Example 4: Show Only Adopted Dogs

```bash
python src/main.py --adopted true --sort-by age
```

### Example 5: Complex Filter with Sorting

```bash
python src/main.py --city 台中 --min-age 3 --sort-by weight_kg --desc
```

---

## 🎯 Command Line Options

| Option      | Description               | Example                                  |
| ----------- | ------------------------- | ---------------------------------------- |
| `--city`    | Filter by city name       | `--city 台北`                            |
| `--min-age` | Minimum age (years)       | `--min-age 2`                            |
| `--max-age` | Maximum age (years)       | `--max-age 5`                            |
| `--adopted` | Filter by adoption status | `--adopted true` or `--adopted false`    |
| `--sort-by` | Sort by column            | `--sort-by age` or `--sort-by weight_kg` |
| `--desc`    | Sort in descending order  | `--desc`                                 |

---

## 🔧 Troubleshooting

### Problem 1: `python` command not found

**Solution**: Try using `python3` instead:

```bash
python3 -m pip install -r requirements.txt
python3 src/main.py
```

### Problem 2: `ModuleNotFoundError: No module named 'pandas'`

**Cause**: Dependencies not installed or installed in wrong environment.

**Solution**:

1. Check your Python version:

   ```bash
   python --version
   ```

   Should be Python 3.7 or higher.

2. Install dependencies again:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. If still not working, try:
   ```bash
   python -m pip install --user pandas numpy matplotlib
   ```

### Problem 3: `FileNotFoundError: data/dogs.csv not found`

**Cause**: Running the script from the wrong directory.

**Solution**: Make sure you're in the project root directory:

```bash
cd path/to/dog_analysis_project
python src/main.py
```

### Problem 4: Charts not displaying in Jupyter Notebook

**Solution**: Add this at the top of your notebook:

```python
%matplotlib inline
```

### Problem 5: Import error when running `dog.py` directly

**Cause**: Path issue when running from different directories.

**Solution**: Always run from project root:

```bash
# From project root
python src/dog.py    # Self-test mode
```

---

## 📓 Working with Jupyter Notebooks

### Step 1: Launch Jupyter

```bash
jupyter notebook
```

### Step 2: Open Notebook

Navigate to `notebooks/01_eda.ipynb` in the browser.

### Step 3: Run Cells

Execute cells one by one to explore the data interactively.

---

## 📚 Learning Objectives

By completing this project, you will learn:

1. ✅ **Module Creation**: How to organize code into reusable modules (`dog.py`)
2. ✅ **Data Processing**: Clean, filter, and transform data with pandas
3. ✅ **Error Handling**: Use try/except to handle errors gracefully
4. ✅ **CLI Development**: Create command-line tools with argparse
5. ✅ **Visualization**: Generate charts with matplotlib
6. ✅ **Cross-platform Code**: Write code that works on Windows and macOS
7. ✅ **Project Structure**: Organize a real-world Python project

---

## 📝 Assignment Tasks

Complete the following tasks to practice your skills:

### Task 1: Basic (Data Exploration)

**Goal**: Find all dogs in "高雄" (Kaohsiung).

**Command**:

```bash
python src/main.py --city 高雄
```

**Question**: How many dogs are in Kaohsiung? What's the adoption rate?

---

### Task 2: Filtering (Age Range)

**Goal**: Find puppies (1 year old or younger).

**Command**:

```bash
python src/main.py --max-age 1
```

**Question**: How many puppies are there? Which breeds are they?

---

### Task 3: Sorting (Heaviest Dogs)

**Goal**: Find the 5 heaviest dogs.

**Command**:

```bash
python src/main.py --sort-by weight_kg --desc
```

**Question**: What are the names of the top 5 heaviest dogs?

---

### Task 4: Complex Filter

**Goal**: Find adopted dogs in "台北" that are between 2-4 years old.

**Command**:

```bash
python src/main.py --city 台北 --min-age 2 --max-age 4 --adopted true
```

**Question**: How many dogs match this criteria?

---

### Task 5: Code Modification (Easy)

**Goal**: Modify `src/dog.py` to add a new statistic.

**Instructions**:

1. Open `src/dog.py`
2. Find the `stats_summary()` function
3. Add a new statistic: `min_age` (minimum age)
4. Add another: `max_age` (maximum age)
5. Run `python src/main.py` to see your changes

**Expected Output**: The statistics summary should now include:

```
Minimum Age: X years
Maximum Age: Y years
```

---

### Task 6: Code Modification (Medium)

**Goal**: Add a new filter function to find unvaccinated dogs.

**Instructions**:

1. Open `src/dog.py`
2. Add a new parameter to `filter_dogs()`: `vaccinated` (bool, optional)
3. Implement the filter logic
4. Test with: `python src/main.py --vaccinated false` (you'll need to add this to main.py too)

**Hint**: Follow the same pattern as the `adopted` filter.

---

### Bonus Task 7: Visualization (Advanced)

**Goal**: Create a new chart showing age distribution.

**Instructions**:

1. Open `notebooks/01_eda.ipynb`
2. Create a new cell at the bottom
3. Use `matplotlib` to create a histogram of dog ages
4. Save the chart to `output/age_distribution.png`

**Example Code**:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hist(df_clean['age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Dogs')
plt.xlabel('Age (years)')
plt.ylabel('Count')
plt.savefig(project_root / 'output' / 'age_distribution.png')
plt.show()
```

---

## 🎓 Key Concepts Demonstrated

### 1. Module Design (`src/dog.py`)

- Functions are organized by purpose
- Each function has clear input/output
- Error handling with try/except
- Self-test with `if __name__ == "__main__"`

### 2. CLI Design (`src/main.py`)

- Argument parsing with `argparse`
- User-friendly error messages
- Step-by-step execution with logging
- Cross-platform path handling

### 3. Data Processing

- Reading CSV with pandas
- Data cleaning (type conversion, missing values)
- Filtering and sorting
- Statistical analysis

### 4. Project Organization

- Separation of concerns (data / code / notebooks / output)
- Reusable modules
- Configuration management

---

## 🔍 Code Quality Checklist

When writing your own projects, check:

- [ ] Functions have clear names and docstrings
- [ ] Error handling for file operations
- [ ] Cross-platform paths (use `pathlib.Path`)
- [ ] Dependencies listed in `requirements.txt`
- [ ] README with installation and usage instructions
- [ ] Example commands provided
- [ ] Code is organized into modules
- [ ] No hardcoded paths or values
- [ ] User-friendly error messages

---

## 🌟 What's Next?

After completing this project, you can:

1. **Extend the Analysis**:

   - Add more data columns (e.g., color, size)
   - Implement data validation
   - Add unit tests

2. **Learn More Modules**:

   - `datetime` for date analysis
   - `json` for configuration files
   - `requests` for API integration

3. **Build Your Own Project**:
   - Apply these patterns to your own data
   - Create a portfolio project
   - Share on GitHub

---

## 📞 Support

If you encounter any issues:

1. Check the "Troubleshooting" section above
2. Review the error messages carefully
3. Make sure you're in the correct directory
4. Verify all dependencies are installed
5. Check your Python version (`python --version`)

---

## 📄 License

This project is for educational purposes. Feel free to modify and use it for learning!

---

**Happy Learning! 🎉**

Made with ❤️ for Python beginners
