import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD DATA
# ============================================================

df = pd.read_csv("raw_sales.csv")

print("=" * 60)
print("CUSTOMER SALES ANALYSIS")
print("=" * 60)

print("\nDataset shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 2. INITIAL EXPLORATION
# ============================================================

print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())


# ============================================================
# 3. REMOVE DUPLICATES
# ============================================================

df = df.drop_duplicates().copy()

print("\nDataset shape after removing duplicates:", df.shape)


# ============================================================
# 4. DATA TYPES
# ============================================================

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")


# ============================================================
# 5. STANDARDIZE CATEGORICAL DATA
# ============================================================

categorical_columns = [
    "Product",
    "Category",
    "Region",
    "Payment_Method"
]

for column in categorical_columns:
    df[column] = df[column].astype("string").str.strip()


# Standardize category
df["Category"] = df["Category"].str.title()

# Standardize region
df["Region"] = df["Region"].str.title()

# Standardize payment method
df["Payment_Method"] = df["Payment_Method"].str.title()


# ============================================================
# 6. HANDLE MISSING VALUES
# ============================================================

# Missing regions
df["Region"] = df["Region"].fillna("Unknown")

# Missing payment methods
df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")


# ============================================================
# 7. RECONSTRUCT MISSING UNIT PRICES
# ============================================================

# Revenue = Quantity × Unit_Price
# Therefore:
# Unit_Price = Revenue / Quantity

missing_price = df["Unit_Price"].isna()

df.loc[missing_price, "Unit_Price"] = (
    df.loc[missing_price, "Revenue"]
    / df.loc[missing_price, "Quantity"]
)

df["Unit_Price"] = df["Unit_Price"].round(2)


# ============================================================
# 8. VALIDATE REVENUE
# ============================================================

df["Calculated_Revenue"] = (
    df["Quantity"] * df["Unit_Price"]
).round(2)

revenue_errors = (
    df["Revenue"].round(2)
    != df["Calculated_Revenue"]
)

print("\nRevenue calculation errors:", revenue_errors.sum())


# ============================================================
# 9. REMOVE TEMPORARY COLUMN
# ============================================================

df = df.drop(columns=["Calculated_Revenue"])


# ============================================================
# 10. SAVE CLEAN DATA
# ============================================================

df.to_csv("clean_sales.csv", index=False)

print("\nClean dataset saved as: clean_sales.csv")

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ============================================================
# 11. KEY PERFORMANCE INDICATORS
# ============================================================

total_orders = df["Order_ID"].nunique()
total_revenue = df["Revenue"].sum()
total_units = df["Quantity"].sum()
average_order_value = total_revenue / total_orders

total_customers = df["Customer_ID"].nunique()

print("\n" + "=" * 60)
print("KEY PERFORMANCE INDICATORS")
print("=" * 60)

print(f"Total orders       : {total_orders}")
print(f"Total customers    : {total_customers}")
print(f"Units sold         : {total_units}")
print(f"Total revenue      : ${total_revenue:,.2f}")
print(f"Average order value: ${average_order_value:,.2f}")


# ============================================================
# 12. SALES BY PRODUCT
# ============================================================

sales_by_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by product:")
print(sales_by_product)


# ============================================================
# 13. SALES BY CATEGORY
# ============================================================

sales_by_category = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by category:")
print(sales_by_category)


# ============================================================
# 14. SALES BY REGION
# ============================================================

sales_by_region = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by region:")
print(sales_by_region)


# ============================================================
# 15. SALES BY CUSTOMER
# ============================================================

sales_by_customer = (
    df.groupby("Customer_ID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 customers:")
print(sales_by_customer.head(10))


# ============================================================
# 16. MONTHLY SALES
# ============================================================

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Revenue"]
    .sum()
)

print("\nMonthly revenue:")
print(monthly_sales)


# ============================================================
# 17. TOP PRODUCT
# ============================================================

top_product = sales_by_product.idxmax()
top_product_revenue = sales_by_product.max()

print("\nTop product:")
print(f"{top_product} - ${top_product_revenue:,.2f}")


# ============================================================
# 18. TOP CATEGORY
# ============================================================

top_category = sales_by_category.idxmax()
top_category_revenue = sales_by_category.max()

print("\nTop category:")
print(f"{top_category} - ${top_category_revenue:,.2f}")


# ============================================================
# 19. TOP REGION
# ============================================================

top_region = sales_by_region.idxmax()
top_region_revenue = sales_by_region.max()

print("\nTop region:")
print(f"{top_region} - ${top_region_revenue:,.2f}")


# ============================================================
# 20. BEST SALES MONTH
# ============================================================

best_month = monthly_sales.idxmax()
best_month_revenue = monthly_sales.max()

print("\nBest sales month:")
print(f"{best_month} - ${best_month_revenue:,.2f}")


# ============================================================
# 21. VISUALIZATION - SALES BY PRODUCT
# ============================================================

plt.figure(figsize=(10, 6))

sales_by_product.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("sales_by_product.png", dpi=150)
plt.show()


# ============================================================
# 22. VISUALIZATION - SALES BY CUSTOMER
# ============================================================

top_customers = sales_by_customer.head(10).sort_values()

plt.figure(figsize=(10, 6))

top_customers.plot(kind="barh")

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Revenue ($)")
plt.ylabel("Customer")

plt.tight_layout()

plt.savefig("sales_by_customer.png", dpi=150)
plt.show()


# ============================================================
# 23. VISUALIZATION - SALES BY REGION
# ============================================================

plt.figure(figsize=(8, 5))

sales_by_region.plot(kind="bar")

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue ($)")

plt.tight_layout()

plt.savefig("sales_by_region.png", dpi=150)
plt.show()


# ============================================================
# 24. VISUALIZATION - MONTHLY SALES
# ============================================================

plt.figure(figsize=(12, 6))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("monthly_sales.png", dpi=150)
plt.show()


# ============================================================
# 25. SALES DASHBOARD
# ============================================================

fig = plt.figure(figsize=(14, 10))

fig.suptitle(
    "CUSTOMER SALES ANALYSIS DASHBOARD",
    fontsize=20,
    fontweight="bold"
)

# KPI 1
fig.text(
    0.15, 0.88,
    f"TOTAL ORDERS\n{total_orders:,}",
    ha="center",
    fontsize=15,
    fontweight="bold"
)

# KPI 2
fig.text(
    0.38, 0.88,
    f"TOTAL REVENUE\n${total_revenue:,.0f}",
    ha="center",
    fontsize=15,
    fontweight="bold"
)

# KPI 3
fig.text(
    0.62, 0.88,
    f"UNITS SOLD\n{total_units:,}",
    ha="center",
    fontsize=15,
    fontweight="bold"
)

# KPI 4
fig.text(
    0.85, 0.88,
    f"AVG ORDER\n${average_order_value:,.0f}",
    ha="center",
    fontsize=15,
    fontweight="bold"
)


# Product chart
ax1 = fig.add_axes([0.08, 0.48, 0.40, 0.30])

sales_by_product.plot(
    kind="bar",
    ax=ax1
)

ax1.set_title("Revenue by Product")
ax1.set_xlabel("")
ax1.set_ylabel("Revenue ($)")
ax1.tick_params(axis="x", rotation=45)


# Region chart
ax2 = fig.add_axes([0.56, 0.48, 0.35, 0.30])

sales_by_region.plot(
    kind="bar",
    ax=ax2
)

ax2.set_title("Revenue by Region")
ax2.set_xlabel("")
ax2.set_ylabel("Revenue ($)")


# Monthly chart
ax3 = fig.add_axes([0.12, 0.08, 0.76, 0.28])

monthly_sales.plot(
    kind="line",
    marker="o",
    ax=ax3
)

ax3.set_title("Monthly Revenue Trend")
ax3.set_xlabel("Month")
ax3.set_ylabel("Revenue ($)")
ax3.tick_params(axis="x", rotation=45)

ax3.grid(True, alpha=0.3)

plt.savefig(
    "sales_dashboard.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 26. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("FINAL ANALYSIS")
print("=" * 60)

print(f"Total revenue : ${total_revenue:,.2f}")
print(f"Total orders  : {total_orders:,}")
print(f"Customers     : {total_customers:,}")
print(f"Units sold    : {total_units:,}")

print(
    f"\nTop product   : {top_product} "
    f"(${top_product_revenue:,.2f})"
)

print(
    f"Top category  : {top_category} "
    f"(${top_category_revenue:,.2f})"
)

print(
    f"Top region    : {top_region} "
    f"(${top_region_revenue:,.2f})"
)

print(
    f"Best month    : {best_month} "
    f"(${best_month_revenue:,.2f})"
)

print("\nAnalysis completed successfully.")