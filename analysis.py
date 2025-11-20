import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Configuration ---
INPUT_FILE = 'sales_data.csv'
OUTPUT_IMAGE = 'sales_chart.png'

def analyze_data():
    print("📊 --- Sales Data Analysis --- 📊\n")

    # 1. Load the Data
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Error: '{INPUT_FILE}' not found. Please create it first!")
        return

    df = pd.read_csv(INPUT_FILE)
    print(f"✅ Loaded data from {INPUT_FILE}")
    print("\n--- First 5 Rows of Data ---")
    print(df.head())

    # 2. Basic Analysis
    total_revenue = df['Total Revenue'].sum()
    best_selling_product = df.groupby('Product')['Units Sold'].sum().idxmax()
    
    print(f"\n💰 Total Revenue: ${total_revenue:,.2f}")
    print(f"🏆 Best Selling Product: {best_selling_product}")

    # 3. Group Analysis (Revenue by Product)
    product_sales = df.groupby('Product')['Total Revenue'].sum().sort_values(ascending=False)
    print("\n--- Revenue by Product ---")
    print(product_sales)

    # 4. Visualization (Bar Chart)
    print(f"\n🎨 Generating chart: {OUTPUT_IMAGE}...")
    
    plt.figure(figsize=(10, 6))
    product_sales.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title('Total Revenue by Product', fontsize=16)
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the plot to a file
    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE)
    print(f"✅ Chart saved successfully to '{OUTPUT_IMAGE}'")
    print("\n✨ Analysis Complete! Open the image file to see your chart. ✨")

if __name__ == "__main__":
    analyze_data()
