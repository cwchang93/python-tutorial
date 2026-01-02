"""
Dog Analysis Module

This module provides reusable functions for analyzing dog shelter data.
Students: This demonstrates how to organize code into modules!
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path


def read_dogs_csv(path):
    """
    Read dogs CSV file with error handling.
    
    Args:
        path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: DataFrame containing dog data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        Exception: For other errors
    """
    try:
        df = pd.read_csv(path)
        print(f"✅ Successfully loaded {len(df)} records from {path}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File not found at '{path}'")
        print(f"   Please check if the file exists and the path is correct.")
        raise
    except pd.errors.EmptyDataError:
        print(f"❌ Error: The file '{path}' is empty.")
        raise
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        raise


def clean_dogs_df(df):
    """
    Clean the dogs DataFrame.
    
    Steps:
    - Handle missing values
    - Convert data types (vaccinated, adopted to boolean)
    - Convert intake_date to datetime
    - Fill empty notes with 'No note'
    
    Args:
        df (pd.DataFrame): Raw DataFrame
        
    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    df_clean = df.copy()
    
    # Convert boolean columns (handle 'true'/'false' strings)
    for col in ['vaccinated', 'adopted']:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.lower().map({'true': True, 'false': False})
    
    # Convert intake_date to datetime
    if 'intake_date' in df_clean.columns:
        df_clean['intake_date'] = pd.to_datetime(df_clean['intake_date'], errors='coerce')
    
    # Fill missing notes
    if 'note' in df_clean.columns:
        df_clean['note'] = df_clean['note'].fillna('No note')
    
    # Ensure numeric columns are correct type
    numeric_cols = ['age', 'weight_kg']
    for col in numeric_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    print(f"✅ Data cleaned: {len(df_clean)} records")
    return df_clean


def stats_summary(df):
    """
    Generate statistical summary of the dog data.
    
    Args:
        df (pd.DataFrame): Cleaned DataFrame
        
    Returns:
        dict: Dictionary containing summary statistics
    """
    summary = {
        'total_dogs': len(df),
        'adopted_count': df['adopted'].sum() if 'adopted' in df.columns else 0,
        'adoption_rate': (df['adopted'].sum() / len(df) * 100) if 'adopted' in df.columns else 0,
        'cities': df['city'].value_counts().to_dict() if 'city' in df.columns else {},
        'avg_age': df['age'].mean() if 'age' in df.columns else 0,
        'avg_weight': df['weight_kg'].mean() if 'weight_kg' in df.columns else 0,
        'most_common_breed': df['breed'].mode()[0] if 'breed' in df.columns and len(df) > 0 else 'N/A',
        'vaccinated_count': df['vaccinated'].sum() if 'vaccinated' in df.columns else 0,
        'breeds': df['breed'].value_counts().to_dict() if 'breed' in df.columns else {}
    }
    
    return summary


def filter_dogs(df, *, city=None, min_age=None, max_age=None, adopted=None):
    """
    Filter dogs by various criteria.
    
    Args:
        df (pd.DataFrame): DataFrame to filter
        city (str, optional): Filter by city name
        min_age (int, optional): Minimum age
        max_age (int, optional): Maximum age
        adopted (bool, optional): Filter by adoption status
        
    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    result = df.copy()
    
    if city is not None:
        result = result[result['city'] == city]
    
    if min_age is not None:
        result = result[result['age'] >= min_age]
    
    if max_age is not None:
        result = result[result['age'] <= max_age]
    
    if adopted is not None:
        result = result[result['adopted'] == adopted]
    
    print(f"🔍 Filter result: {len(result)} dogs match criteria")
    return result


def sort_dogs(df, by="age", ascending=True):
    """
    Sort dogs by a specific column.
    
    Args:
        df (pd.DataFrame): DataFrame to sort
        by (str): Column name to sort by (default: 'age')
        ascending (bool): Sort order (default: True)
        
    Returns:
        pd.DataFrame: Sorted DataFrame
    """
    if by not in df.columns:
        print(f"⚠️  Warning: Column '{by}' not found. Returning unsorted.")
        return df
    
    sorted_df = df.sort_values(by=by, ascending=ascending).reset_index(drop=True)
    print(f"📊 Sorted by '{by}' ({'ascending' if ascending else 'descending'})")
    return sorted_df


def save_cleaned(df, path):
    """
    Save cleaned DataFrame to CSV.
    
    Args:
        df (pd.DataFrame): DataFrame to save
        path (str): Output file path
    """
    try:
        # Ensure directory exists
        output_dir = Path(path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        df.to_csv(path, index=False)
        print(f"💾 Saved cleaned data to {path}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        raise


def plot_top_breeds(df, top_n=5, save_path=None):
    """
    Plot top N most common dog breeds.
    
    Args:
        df (pd.DataFrame): DataFrame containing dog data
        top_n (int): Number of top breeds to show (default: 5)
        save_path (str, optional): Path to save the plot
    """
    if 'breed' not in df.columns:
        print("⚠️  Warning: 'breed' column not found in DataFrame")
        return
    
    # Count breeds and get top N
    breed_counts = df['breed'].value_counts().head(top_n)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    breed_counts.plot(kind='bar', color='skyblue', edgecolor='navy')
    plt.title(f'Top {top_n} Most Common Dog Breeds', fontsize=16, fontweight='bold')
    plt.xlabel('Breed', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save or show
    if save_path:
        # Ensure directory exists
        output_dir = Path(save_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"📈 Chart saved to {save_path}")
    else:
        plt.show()
    
    plt.close()


# ============================================================
# Self-test demonstration (run this file directly to test)
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Running dog.py module self-test...")
    print("=" * 60)
    print()
    
    # Test: Read CSV
    print("📂 Test 1: Reading CSV file...")
    try:
        # Adjust path to work from src/ directory
        csv_path = Path(__file__).parent.parent / "data" / "dogs.csv"
        df = read_dogs_csv(csv_path)
        print(f"   Columns: {list(df.columns)}")
        print()
    except Exception as e:
        print(f"   Failed: {e}")
        print()
    
    # Test: Clean data
    print("🧹 Test 2: Cleaning data...")
    df_clean = clean_dogs_df(df)
    print(f"   Data types after cleaning:")
    print(f"   - vaccinated: {df_clean['vaccinated'].dtype}")
    print(f"   - adopted: {df_clean['adopted'].dtype}")
    print(f"   - intake_date: {df_clean['intake_date'].dtype}")
    print()
    
    # Test: Statistics
    print("📊 Test 3: Generating statistics...")
    stats = stats_summary(df_clean)
    print(f"   Total dogs: {stats['total_dogs']}")
    print(f"   Adopted: {stats['adopted_count']} ({stats['adoption_rate']:.1f}%)")
    print(f"   Average age: {stats['avg_age']:.1f} years")
    print(f"   Most common breed: {stats['most_common_breed']}")
    print()
    
    # Test: Filter
    print("🔍 Test 4: Filtering data...")
    filtered = filter_dogs(df_clean, city="台北", min_age=2, max_age=5)
    print(f"   Found {len(filtered)} dogs in 台北, age 2-5")
    print()
    
    # Test: Sort
    print("📋 Test 5: Sorting data...")
    sorted_df = sort_dogs(df_clean, by="age", ascending=False)
    print(f"   Top 3 oldest dogs:")
    print(sorted_df[['name', 'age', 'breed']].head(3).to_string(index=False))
    print()
    
    print("=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)
