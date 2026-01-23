import pandas as pd
import numpy as np

# 固定亂數種子，確保每次生成的資料相同
np.random.seed(42)

# 設定資料筆數
n_orders = 500

# 定義產品類別與對應的產品清單
products_by_category = {
    'Monitor': ['RD280UG', 'U2720Q', 'LG-4K'],
    'Keyboard': ['K980', 'MX Keys', 'Keychron K3'],
    'Mouse': ['MX Master', 'M185', 'Logitech G Pro'],
    'Headset': ['Sony WH', 'Bose QC', 'AirPods Max']
}

# 定義各產品的價格與成本（成本永遠低於售價）
product_pricing = {
    # Monitor - 高價位，利潤率中等
    'RD280UG': {'price': 8900, 'cost': 6500},
    'U2720Q': {'price': 12500, 'cost': 9200},
    'LG-4K': {'price': 15800, 'cost': 11500},
    # Keyboard - 中價位，利潤率較高
    'K980': {'price': 3200, 'cost': 1800},
    'MX Keys': {'price': 2900, 'cost': 1600},
    'Keychron K3': {'price': 2500, 'cost': 1300},
    # Mouse - 低到中價位，利潤率高
    'MX Master': {'price': 2800, 'cost': 1400},
    'M185': {'price': 450, 'cost': 180},
    'Logitech G Pro': {'price': 3500, 'cost': 1900},
    # Headset - 高價位，利潤率較低（競爭激烈）
    'Sony WH': {'price': 8900, 'cost': 7100},
    'Bose QC': {'price': 10500, 'cost': 8800},
    'AirPods Max': {'price': 18900, 'cost': 16200}
}

# 生成訂單編號
order_ids = list(range(1, n_orders + 1))

# 生成日期（2024-01-01 到 2024-06-30）
dates = pd.date_range('2024-01-01', '2024-06-30', periods=n_orders)
dates = np.random.choice(dates, n_orders, replace=True)

# 生成類別（Monitor 和 Headset 較熱門）
categories = np.random.choice(
    ['Monitor', 'Keyboard', 'Mouse', 'Headset'],
    n_orders,
    p=[0.30, 0.20, 0.25, 0.25]
)

# 根據類別生成產品名稱
products = []
prices = []
costs = []

for category in categories:
    # 從該類別中隨機選擇一個產品
    product = np.random.choice(products_by_category[category])
    products.append(product)
    
    # 在基礎價格上增加一些隨機變動（模擬促銷或漲價）
    base_price = product_pricing[product]['price']
    base_cost = product_pricing[product]['cost']
    
    # 價格變動範圍：-10% 到 +5%
    price_variation = np.random.uniform(-0.10, 0.05)
    adjusted_price = int(base_price * (1 + price_variation))
    
    # 成本保持相對穩定，僅 ±3% 變動
    cost_variation = np.random.uniform(-0.03, 0.03)
    adjusted_cost = int(base_cost * (1 + cost_variation))
    
    # 確保成本永遠小於售價
    if adjusted_cost >= adjusted_price:
        adjusted_cost = int(adjusted_price * 0.7)
    
    prices.append(adjusted_price)
    costs.append(adjusted_cost)

# 生成數量（1-4 件，大多數是 1-2 件）
quantities = np.random.choice([1, 2, 3, 4], n_orders, p=[0.50, 0.30, 0.15, 0.05])

# 生成通路（Online 較多）
channels = np.random.choice(['Online', 'Store'], n_orders, p=[0.65, 0.35])

# 生成地區（Taipei 最多，其他地區較均勻）
regions = np.random.choice(
    ['Taipei', 'NewTaipei', 'Taichung', 'Kaohsiung'],
    n_orders,
    p=[0.40, 0.25, 0.20, 0.15]
)

# 生成客戶 ID（模擬約 300 位客戶，有些客戶會重複購買）
customer_ids = np.random.randint(1000, 1300, n_orders)

# 建立 DataFrame
df = pd.DataFrame({
    'order_id': order_ids,
    'order_date': dates,
    'category': categories,
    'product': products,
    'price': prices,
    'cost': costs,
    'quantity': quantities,
    'channel': channels,
    'region': regions,
    'customer_id': customer_ids
})

# 依日期排序
df = df.sort_values('order_date').reset_index(drop=True)

# 輸出成 CSV 檔案（使用 utf-8-sig 確保 Excel 可正確開啟中文）
df.to_csv('ecommerce_sales.csv', index=False, encoding='utf-8-sig')

print("✓ ecommerce_sales.csv 已成功生成！")
print(f"✓ 共生成 {len(df)} 筆訂單資料")
print()
print("資料概覽：")
print(df.head(10))
print()
print("基本統計：")
print(f"- 日期範圍：{df['order_date'].min()} 至 {df['order_date'].max()}")
print(f"- 產品類別：{df['category'].unique().tolist()}")
print(f"- 銷售通路：{df['channel'].value_counts().to_dict()}")
print(f"- 銷售地區：{df['region'].value_counts().to_dict()}")
print(f"- 平均訂單金額：${(df['price'] * df['quantity']).mean():.2f}")
