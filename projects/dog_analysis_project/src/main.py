"""
Dog Analysis Project - Main Entry Point

This is the main script for analyzing dog shelter data.
Run from command line: python src/main.py [options]

Students: This shows how to create a CLI application!
"""

import argparse
import sys
from pathlib import Path

# Add src to path (for when running from project root)
sys.path.insert(0, str(Path(__file__).parent))

import dog


def print_banner():
    """Print a nice banner"""
    print("=" * 70)
    print("🐶  Dog Shelter Analysis Project  🐶".center(70))
    print("=" * 70)
    print()


def print_stats(stats):
    """Print statistics in a nice format"""
    print("\n" + "=" * 70)
    print("📊  STATISTICS SUMMARY".center(70))
    print("=" * 70)
    
    print(f"\n📈 Overall Statistics:")
    print(f"   • Total Dogs: {stats['total_dogs']}")
    print(f"   • Adopted: {stats['adopted_count']} ({stats['adoption_rate']:.1f}%)")
    print(f"   • Vaccinated: {stats['vaccinated_count']}")
    print(f"   • Average Age: {stats['avg_age']:.1f} years")
    print(f"   • Average Weight: {stats['avg_weight']:.1f} kg")
    print(f"   • Most Common Breed: {stats['most_common_breed']}")
    
    print(f"\n🏙️  Dogs by City:")
    for city, count in sorted(stats['cities'].items(), key=lambda x: x[1], reverse=True):
        print(f"   • {city}: {count} dogs")
    
    print(f"\n🐕 Dogs by Breed:")
    for breed, count in list(sorted(stats['breeds'].items(), key=lambda x: x[1], reverse=True))[:5]:
        print(f"   • {breed}: {count} dogs")
    
    print("\n" + "=" * 70 + "\n")


def main():
    """Main function"""
    print_banner()
    
    # Setup argument parser
    parser = argparse.ArgumentParser(
        description="Analyze dog shelter data with various filters and options",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python src/main.py
  python src/main.py --city 台北
  python src/main.py --min-age 2 --max-age 5
  python src/main.py --adopted true --sort-by age
  python src/main.py --city 台中 --desc --sort-by weight_kg
        """
    )
    
    parser.add_argument('--city', type=str, help='Filter by city name')
    parser.add_argument('--min-age', type=int, help='Minimum age')
    parser.add_argument('--max-age', type=int, help='Maximum age')
    parser.add_argument('--adopted', type=str, choices=['true', 'false'], help='Filter by adoption status')
    parser.add_argument('--sort-by', type=str, default='age', 
                        choices=['age', 'weight_kg', 'name'], 
                        help='Column to sort by (default: age)')
    parser.add_argument('--desc', action='store_true', help='Sort in descending order')
    
    args = parser.parse_args()
    
    try:
        # Define paths (works on both Windows and macOS)
        project_root = Path(__file__).parent.parent
        data_path = project_root / "data" / "dogs.csv"
        cleaned_path = project_root / "data" / "dogs_cleaned.csv"
        output_dir = project_root / "output"
        chart_path = output_dir / "top_breeds.png"
        
        # Step 1: Read data
        print("📂 Step 1: Reading data...")
        df = dog.read_dogs_csv(data_path)
        print()
        
        # Step 2: Clean data
        print("🧹 Step 2: Cleaning data...")
        df_clean = dog.clean_dogs_df(df)
        print()
        
        # Step 3: Save cleaned data
        print("💾 Step 3: Saving cleaned data...")
        dog.save_cleaned(df_clean, cleaned_path)
        print()
        
        # Step 4: Apply filters if specified
        df_filtered = df_clean.copy()
        
        if any([args.city, args.min_age, args.max_age, args.adopted]):
            print("🔍 Step 4: Applying filters...")
            
            # Convert adopted string to boolean if provided
            adopted_bool = None
            if args.adopted:
                adopted_bool = (args.adopted.lower() == 'true')
            
            df_filtered = dog.filter_dogs(
                df_clean,
                city=args.city,
                min_age=args.min_age,
                max_age=args.max_age,
                adopted=adopted_bool
            )
            print()
            
            if len(df_filtered) == 0:
                print("⚠️  No dogs match the filter criteria!")
                print("   Try different filter values.\n")
                return
        
        # Step 5: Sort data
        print(f"📋 Step 5: Sorting data by '{args.sort_by}'...")
        df_sorted = dog.sort_dogs(df_filtered, by=args.sort_by, ascending=not args.desc)
        print()
        
        # Step 6: Generate and print statistics
        print("📊 Step 6: Generating statistics...")
        stats = dog.stats_summary(df_sorted)
        print_stats(stats)
        
        # Step 7: Generate chart
        print("📈 Step 7: Generating breed chart...")
        dog.plot_top_breeds(df_sorted, top_n=5, save_path=chart_path)
        print()
        
        # Step 8: Show sample data
        print("👀 Sample Data (top 10 records):")
        print("-" * 70)
        display_cols = ['name', 'breed', 'age', 'weight_kg', 'city', 'adopted']
        available_cols = [col for col in display_cols if col in df_sorted.columns]
        print(df_sorted[available_cols].head(10).to_string(index=False))
        print()
        
        # Success message
        print("=" * 70)
        print("✅  Analysis completed successfully!".center(70))
        print("=" * 70)
        print(f"\n📁 Output files created:")
        print(f"   • {cleaned_path}")
        print(f"   • {chart_path}")
        print()
        
    except FileNotFoundError as e:
        print("\n" + "=" * 70)
        print("❌  ERROR: File Not Found".center(70))
        print("=" * 70)
        print(f"\n{str(e)}")
        print("\n💡 Troubleshooting:")
        print("   1. Make sure you're running from the project root directory")
        print("   2. Check if data/dogs.csv exists")
        print("   3. Try: python src/main.py (from project root)")
        print()
        sys.exit(1)
        
    except ImportError as e:
        print("\n" + "=" * 70)
        print("❌  ERROR: Missing Dependencies".center(70))
        print("=" * 70)
        print(f"\n{str(e)}")
        print("\n💡 Solution:")
        print("   Install required packages:")
        print("   python -m pip install -r requirements.txt")
        print()
        sys.exit(1)
        
    except Exception as e:
        print("\n" + "=" * 70)
        print("❌  ERROR: Something Went Wrong".center(70))
        print("=" * 70)
        print(f"\nError details: {str(e)}")
        print("\n💡 Please check:")
        print("   1. Your Python version (should be 3.7+)")
        print("   2. All dependencies are installed")
        print("   3. Data file is not corrupted")
        print()
        sys.exit(1)


if __name__ == "__main__":
    main()
