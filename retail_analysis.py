import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

# Raw messy data
data = """Transaction_ID,Store_ID,Store_City,Region,Transaction_Date,Product,Category,Quantity,Unit_Price,Discount,Payment_Type,Customer_Age,Customer_Tier,Return_Flag,Satisfaction_Score,Delivery_Days,Marketing_Channel,Employee_Name,Employee_Experience,Cost_Price
T001,S01,New York,East,2025-01-05,Laptop,Electronics,2,1200,0,Loyalty Card,32,Gold,No,4,3,Email,John Miller,5,900
T002,S02,Los Angeles,West,01/15/2025,Office Chair,Furniture,1,350,0.1,Credit Card,45,Silver,No,5,7,Social Media,Sarah Lee,3,250
T003,S03,Chicago,Midwest,2025-01-20,Desk Lamp,Electronics,-3,25,0.2,Cash,28,Bronze,Yes,2,N/A,TV Ad,,,18
T004,S01,New York,East,2025/01/25,Wireless Mouse,Electronics,5,45,0.15,PayPal,24,Gold,No,?,2,Email,John Miller,5,30
T005,S04,Houston,South,2025-01-30,Coffee Table,Furniture,1,150,,Credit Card,52,Silver,No,4,10,Social Media,Mike Brown,1,100
T006,S02,Los Angeles,West,2025-02-01,Monitor,Electronics,-1,300,0.2,Debit Card,34,Platinum,Yes,1,5,Email,Sarah Lee,3,220
T007,S05,Phoenix,West,2025/02/03,Desk,Furniture,1,450,0,Financing,41,Gold,No,3,12,Direct Mail,,,350
T008,S01,New York,East,02-05-2025,Keyboard,Electronics,3,75,0.5,Credit Card,29,Silver,No,5,2,SMS,John Miller,5,45
T009,S06,Philadelphia,East,2025-02-07,Notebook,Supplies,20,2.5,0,Cash,19,Bronze,No,4,1,In-Store,Emily Davis,2,1.5
T010,S03,Chicago,Midwest,2025-02-10,Gaming Chair,Furniture,1,400,0.15,,,Gold,No,4,8,Social Media,Mike Brown,1,280
T011,S07,San Antonio,South,2025-02-12,Smartphone,Electronics,1,999,0,,-1,Silver,Yes,?,4,Email,David Wilson,8,700
T012,S01,New York,East,2025-02-15,Tablet,Electronics,1,600,0.1,Credit Card,35,Platinum,No,5,1,Email,John Miller,5,450
T013,S08,San Diego,West,2025-02-18,Bookshelf,Furniture,2,200,0.2,PayPal,44,Bronze,Yes,2,14,Social Media,Sarah Lee,3,130
T014,S02,Los Angeles,West,2025-02-20,Chair Mat,Furniture,1,40,0.05,Cash,38,Silver,No,3,5,In-Store,,,25
T015,S09,Dallas,South,2025-02-22,HDMI Cable,Electronics,10,15,0,Debit Card,26,Bronze,No,5,1,Email,Tom Harris,0,10
T016,S03,Chicago,Midwest,2025-02-25,Standing Desk,Furniture,1,550,0,Financing,49,Gold,No,4,9,Direct Mail,Mike Brown,1,400
T017,S01,New York,East,2025-02-28,Mouse Pad,Supplies,-5,12,0.1,Cash,31,Silver,No,3,2,In-Store,John Miller,5,8
T018,S10,Miami,South,2025-03-01,Printer,Electronics,1,250,0,,-1,Bronze,No,?,5,Social Media,N/A,7,180
T019,S02,Los Angeles,West,2025-03-03,Desk Organizer,Supplies,2,35,0.25,Credit Card,27,Gold,No,5,3,Email,Sarah Lee,3,20
T020,S04,Houston,South,2025-03-05,Gaming Monitor,Electronics,1,400,0.1,PayPal,33,Silver,No,4,6,Social Media,Tom Harris,0,300
T021,S11,San Jose,West,2025-03-07,Office Lamp,Electronics,1,65,0,Credit Card,41,Gold,No,5,2,Email,Mike Brown,1,40
T022,S01,New York,East,2025-03-10,Laptop Stand,Accessories,2,30,0.1,Cash,29,Bronze,Yes,2,4,In-Store,John Miller,5,20
T023,S12,Austin,South,2025-03-12,Webcam,Electronics,1,80,0,Debit Card,36,Silver,No,4,3,Email,Emily Davis,2,55
T024,S03,Chicago,Midwest,2025-03-15,Cable Ties,Supplies,50,1,0.1,Cash,22,Bronze,No,3,1,In-Store,Mike Brown,1,0.5
T025,S02,Los Angeles,West,2025-03-18,Ergonomic Mouse,Electronics,2,90,0.3,Credit Card,47,Gold,No,5,2,SMS,Sarah Lee,3,60
T026,S13,Indianapolis,Midwest,2025-03-20,Desk Fan,Electronics,-2,45,0,PayPal,31,Silver,Yes,1,6,Email,,,30
T027,S01,New York,East,2025-03-22,Whiteboard,Office,1,120,0.15,Credit Card,53,Gold,No,4,5,Social Media,John Miller,5,80
T028,S14,Jacksonville,South,2025-03-25,Stapler,Supplies,3,20,0,Cash,25,Bronze,No,5,1,In-Store,Tom Harris,0,12
T029,S02,Los Angeles,West,2025-03-28,Monitor Arm,Accessories,1,85,0.2,Financing,39,Silver,No,?,4,Email,Sarah Lee,3,55
T030,S15,Columbus,Midwest,2025-03-30,Desk Drawer,Furniture,1,110,0.05,Credit Card,44,Gold,No,4,6,Direct Mail,Mike Brown,1,75
T031,S01,New York,East,2025-04-01,USB Hub,Electronics,4,25,0,Debit Card,28,Bronze,No,5,2,Email,John Miller,5,15
T032,S16,Charlotte,South,2025-04-03,Office Chair,Electronics,1,300,0.1,PayPal,37,Silver,Yes,3,9,Social Media,Emily Davis,2,210
T033,S03,Chicago,Midwest,2025-04-05,Standing Mat,Accessories,1,50,0,,-1,Gold,No,?,5,In-Store,Mike Brown,1,30
T034,S02,Los Angeles,West,2025-04-07,Desk Light,Electronics,2,35,0.1,Credit Card,34,Bronze,No,4,3,Email,Sarah Lee,3,20
T035,S17,Fort Worth,South,2025-04-10,Monitor Stand,Accessories,3,25,0.15,Cash,26,Silver,Yes,2,2,Social Media,Tom Harris,0,15
T036,S01,New York,East,2025-04-12,Laptop Bag,Accessories,1,55,0,Credit Card,42,Gold,No,5,1,Email,John Miller,5,35
T037,S18,Detroit,Midwest,2025-04-15,Desk Mat,Accessories,2,40,0.1,PayPal,29,Bronze,No,4,3,SMS,,,25
T038,S04,Houston,South,2025-04-17,Wireless Keyboard,Electronics,1,120,0,Debit Card,31,Silver,No,5,2,Email,Mike Brown,1,85
T039,S19,Memphis,South,2025-04-20,Phone Stand,Accessories,15,12,0.5,Cash,19,Bronze,Yes,1,4,In-Store,Emily Davis,2,8
T040,S02,Los Angeles,West,2025-04-22,Desk Organizer,Supplies,1,45,0,Credit Card,48,Gold,No,4,3,Email,Sarah Lee,3,30
T041,S20,Boston,East,2025-04-25,Gaming Desk,Furniture,1,600,0.2,Financing,35,Platinum,No,5,10,Social Media,David Wilson,8,420
T042,S01,New York,East,2025-04-27,Cable Management,Supplies,8,18,0.05,Cash,27,Bronze,No,3,1,In-Store,John Miller,5,12
T043,S03,Chicago,Midwest,2025-04-30,Office Phone,Electronics,1,250,0.1,Credit Card,52,Silver,No,4,5,Email,Mike Brown,1,180
T044,S21,Seattle,West,2025-05-02,Desk Drawer,Furniture,2,85,0,Cash,33,Gold,No,5,4,In-Store,,,55
T045,S02,Los Angeles,West,2025-05-04,Laptop Cooler,Electronics,1,40,0.15,PayPal,25,Bronze,No,5,2,Email,Sarah Lee,3,25
T046,S01,New York,East,2025-05-06,Standing Desk,Electronics,1,550,0.25,Credit Card,41,Platinum,Yes,1,3,Social Media,John Miller,5,400
T047,S22,Denver,West,2025-05-08,Desk Calendar,Supplies,2,25,0,Cash,38,Silver,No,4,1,In-Store,Tom Harris,0,15
T048,S04,Houston,South,2025-05-10,Mouse Pad,Supplies,-10,8,0.1,Debit Card,29,Bronze,Yes,2,3,Email,Mike Brown,1,5
T049,S03,Chicago,Midwest,2025-05-12,Desk Lamp,Electronics,2,45,0.2,Credit Card,44,Gold,No,3,4,Social Media,Mike Brown,1,30
T050,S23,Portland,West,2025-05-15,Office Chair,Electronics,1,350,0.05,Financing,36,Silver,No,5,8,Direct Mail,Emily Davis,2,250
"""

from io import StringIO

df = pd.read_csv(StringIO(data))


def clean_data(df):
    df_clean = df.copy()

    # Fix quantity
    df_clean['Quantity'] = pd.to_numeric(df_clean['Quantity'], errors='coerce')
    df_clean['Quantity'] = df_clean['Quantity'].abs()
    df_clean['Quantity'] = df_clean['Quantity'].fillna(df_clean['Quantity'].median())

    # Fix prices
    df_clean['Unit_Price'] = pd.to_numeric(df_clean['Unit_Price'], errors='coerce')
    df_clean['Unit_Price'] = df_clean['Unit_Price'].fillna(df_clean['Unit_Price'].median())

    df_clean['Cost_Price'] = pd.to_numeric(df_clean['Cost_Price'], errors='coerce')
    df_clean['Cost_Price'] = df_clean['Cost_Price'].fillna(df_clean['Cost_Price'].median())

    # Fix discount
    df_clean['Discount'] = pd.to_numeric(df_clean['Discount'], errors='coerce')
    df_clean['Discount'] = df_clean['Discount'].fillna(0)

    # Calculate revenue and profit
    df_clean['Revenue'] = (
        df_clean['Quantity'] *
        df_clean['Unit_Price'] *
        (1 - df_clean['Discount'])
    )

    df_clean['Profit'] = (
        df_clean['Revenue'] -
        (df_clean['Quantity'] * df_clean['Cost_Price'])
    )

    # Fix dates
    def parse_date(date_str):
        if pd.isna(date_str):
            return np.nan

        date_str = str(date_str).strip()

        formats = ['%Y-%m-%d', '%m/%d/%Y', '%Y/%m/%d', '%m-%d-%Y']

        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue

        return np.nan

    df_clean['Transaction_Date'] = df_clean['Transaction_Date'].apply(parse_date)
    df_clean = df_clean.dropna(subset=['Transaction_Date'])

    # Fix customer age
    df_clean['Customer_Age'] = pd.to_numeric(
        df_clean['Customer_Age'],
        errors='coerce'
    )

    median_age = df_clean.loc[df_clean['Customer_Age'] >= 18, 'Customer_Age'].median()

    df_clean.loc[df_clean['Customer_Age'] < 18, 'Customer_Age'] = median_age
    df_clean['Customer_Age'] = df_clean['Customer_Age'].fillna(median_age)

    # Fix satisfaction score
    df_clean['Satisfaction_Score'] = pd.to_numeric(
        df_clean['Satisfaction_Score'],
        errors='coerce'
    )

    df_clean['Satisfaction_Score'] = df_clean['Satisfaction_Score'].fillna(
        df_clean['Satisfaction_Score'].median()
    )

    # Fix delivery days
    df_clean['Delivery_Days'] = pd.to_numeric(
        df_clean['Delivery_Days'],
        errors='coerce'
    )

    df_clean['Delivery_Days'] = df_clean['Delivery_Days'].fillna(
        df_clean['Delivery_Days'].median()
    )

    # Fix employee name and experience
    df_clean['Employee_Name'] = df_clean['Employee_Name'].fillna('Unassigned')
    df_clean['Employee_Name'] = df_clean['Employee_Name'].replace('', 'Unassigned')
    df_clean['Employee_Name'] = df_clean['Employee_Name'].replace('N/A', 'Unassigned')

    df_clean['Employee_Experience'] = pd.to_numeric(
        df_clean['Employee_Experience'],
        errors='coerce'
    )

    df_clean['Employee_Experience'] = df_clean['Employee_Experience'].fillna(0)

    # Fix customer tier
    df_clean['Customer_Tier'] = df_clean['Customer_Tier'].fillna('Bronze')
    df_clean['Customer_Tier'] = df_clean['Customer_Tier'].replace('', 'Bronze')

    # Fix payment type
    df_clean['Payment_Type'] = df_clean['Payment_Type'].fillna('Unknown')
    df_clean['Payment_Type'] = df_clean['Payment_Type'].replace('', 'Unknown')

    # Fix return flag
    df_clean['Return_Flag'] = df_clean['Return_Flag'].fillna('No')

    # Fix marketing channel
    df_clean['Marketing_Channel'] = df_clean['Marketing_Channel'].fillna('Unknown')

    return df_clean


df_clean = clean_data(df)

# Visualization
fig = plt.figure(figsize=(20, 12))
fig.suptitle('RetailEase Business Dashboard', fontsize=16, fontweight='bold')

# 1. Profit by category
ax1 = plt.subplot(2, 3, 1)

cat_profit = df_clean.groupby('Category')['Profit'].sum()

colors = ['red' if x < 0 else 'green' for x in cat_profit.values]

cat_profit.plot(kind='barh', ax=ax1, color=colors)

ax1.set_xlabel('Profit ($)')
ax1.set_title('Profit by Category')

# 2. Satisfaction vs delivery days
ax2 = plt.subplot(2, 3, 2)

delivery_groups = df_clean.groupby(
    pd.cut(df_clean['Delivery_Days'], bins=[0, 2, 5, 10, 20, 50])
)['Satisfaction_Score'].mean()

delivery_groups.plot(kind='bar', ax=ax2, color='purple')

ax2.set_xlabel('Delivery Days')
ax2.set_ylabel('Satisfaction Score')
ax2.set_title('Delivery Impact on Satisfaction')
ax2.set_xticklabels(['0-2', '3-5', '6-10', '11-20', '21+'], rotation=45)

# 3. Employee performance
ax3 = plt.subplot(2, 3, 3)

emp_data = (
    df_clean[df_clean['Employee_Name'] != 'Unassigned']
    .groupby('Employee_Name')['Profit']
    .sum()
    .sort_values(ascending=False)
)

emp_data.plot(kind='bar', ax=ax3, color='skyblue')

ax3.set_xlabel('Employee')
ax3.set_ylabel('Total Profit ($)')
ax3.set_title('Employee Performance')
ax3.tick_params(axis='x', rotation=45)

# 4. Return rate by category
ax4 = plt.subplot(2, 3, 4)

return_rate = df_clean.groupby('Category').apply(
    lambda x: (x['Return_Flag'] == 'Yes').mean() * 100
)

return_rate.plot(kind='bar', ax=ax4, color='coral')

ax4.set_xlabel('Category')
ax4.set_ylabel('Return Rate (%)')
ax4.set_title('Return Rate by Category')
ax4.tick_params(axis='x', rotation=45)

# 5. Customer tier analysis
ax5 = plt.subplot(2, 3, 5)

tier_profit = df_clean.groupby('Customer_Tier')['Profit'].mean()

tier_profit.plot(kind='bar', ax=ax5, color='gold')

ax5.set_xlabel('Customer Tier')
ax5.set_ylabel('Avg Profit per Transaction ($)')
ax5.set_title('Profit by Customer Tier')

# 6. Marketing channel ROI
ax6 = plt.subplot(2, 3, 6)

channel_roi = df_clean.groupby('Marketing_Channel').apply(
    lambda x: (x['Profit'].sum() / x['Revenue'].sum()) * 100
)

channel_roi.sort_values().plot(kind='barh', ax=ax6, color='teal')

ax6.set_xlabel('ROI (%)')
ax6.set_title('Marketing Channel ROI')

plt.tight_layout()
plt.show()

# Second set of visualizations
fig2 = plt.figure(figsize=(16, 8))

# 7. Monthly trend
ax7 = plt.subplot(1, 2, 1)

monthly = df_clean.groupby(
    df_clean['Transaction_Date'].dt.month
)['Profit'].sum()

monthly.plot(
    kind='line',
    marker='o',
    ax=ax7,
    color='green',
    linewidth=2
)

ax7.set_xlabel('Month')
ax7.set_ylabel('Total Profit ($)')
ax7.set_title('Monthly Profit Trend')
ax7.grid(True, alpha=0.3)

# 8. Experience vs profit
ax8 = plt.subplot(1, 2, 2)

exp_groups = df_clean.groupby(
    pd.cut(df_clean['Employee_Experience'], bins=[-1, 1, 3, 5, 10, 20])
)['Profit'].mean()

exp_groups.plot(kind='bar', ax=ax8, color='orange')

ax8.set_xlabel('Employee Experience (years)')
ax8.set_ylabel('Avg Profit per Transaction ($)')
ax8.set_title('Experience Impact on Profit')
ax8.set_xticklabels(['0-1', '2-3', '4-5', '6-10', '10+'], rotation=45)

plt.tight_layout()
plt.show()

# Print insights
print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

print(f"Total Revenue: ${df_clean['Revenue'].sum():,.2f}")
print(f"Total Profit: ${df_clean['Profit'].sum():,.2f}")

profit_margin = (
    df_clean['Profit'].sum() /
    df_clean['Revenue'].sum()
) * 100

print(f"Profit Margin: {profit_margin:.1f}%")

return_rate_total = (
    (df_clean['Return_Flag'] == 'Yes').mean()
) * 100

print(f"Return Rate: {return_rate_total:.1f}%")

print(f"Avg Satisfaction: {df_clean['Satisfaction_Score'].mean():.2f}/5")

print("\nProblem Areas:")

accessories_loss = df_clean[
    df_clean['Category'] == 'Accessories'
]['Profit'].sum()

print(f"- Accessories category losing ${accessories_loss:,.0f}")

electronics_return_rate = (
    (
        df_clean[df_clean['Category'] == 'Electronics']['Return_Flag']
        == 'Yes'
    ).mean()
) * 100

print(f"- Electronics return rate: {electronics_return_rate:.1f}%")

delivery_impact = (
    df_clean[df_clean['Delivery_Days'] > 5]['Satisfaction_Score'].mean()
    -
    df_clean[df_clean['Delivery_Days'] <= 5]['Satisfaction_Score'].mean()
)

print(f"- Delivery >5 days drops satisfaction by {delivery_impact:.1f} points")

experience_impact = (
    df_clean[df_clean['Employee_Experience'] < 2]['Profit'].mean()
)

print(
    f"- Employees with <2 years experience generate "
    f"${experience_impact:.0f} less per transaction"
)
