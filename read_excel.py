### ✅ **Code Example with `dtype` Specifications**

```python
import pandas as pd

# Define the file path
file_path = r'C:\downloads\excel1.xlsx'

# Define data types for Worksheet 1
worksheet1_dtype = {
    'CMCP ID': str,
    'CIF ID': int,
    'Name': str,
    'identification number': str,
    'Vaild to': pd.to_datetime,  # Pandas will infer datetime
    'Identification type': 'category',
    'issue Country': 'category',
    'UnitPrice': float,    
    'LastPurchaseDate': pd.to_datetime,    
    'IsVIP': bool,
}

# Define data types for Worksheet 2
worksheet2_dtype = {
    'CMCP_ID': str,
    'CIF_ID': str,
    'Name': str,
    'identification_number': str,
    'Vaild_to': pd.to_datetime,  # Pandas will infer datetime
    'Identification_type': 'category',
    'issue_Country': 'category',
    'UnitPrice': float,    
    'LastPurchaseDate': pd.to_datetime,    
    'IsVIP': bool,
}

# Read data from both worksheets with specified data types
df1 = pd.read_excel(
    file_path,
    sheet_name='Worksheet 1',
    header=0,
    dtype=worksheet1_dtype
)

df2 = pd.read_excel(
    file_path,
    sheet_name='Worksheet 2',
    header=0,
    dtype=worksheet2_dtype
)

# Merge the two DataFrames on the 'CIF_ID' column
merged_df = pd.merge(df1, df2, on='CIF_ID', how='inner')

# Output the mapped data
print("Mapped Data:\n", merged_df)
```


# 1. Define filter criteria (e.g., filter by IsVIP = True)
filtered_df = df1[df1['Identification type'] == Passport]

# 2. Create pivot table: group by CIF_ID, count occurrences
pivot_table = filtered_df.groupby('CIF_ID').size().reset_index(name='Count of CIF')

# 3. Write pivot table to a new worksheet (Worksheet 3)
with pd.ExcelWriter(file_path, mode='a', engine='openpyxl') as writer:
    pivot_table.to_excel(writer, sheet_name='Worksheet 3', index=False, header=True)

print("Pivot Table created successfully in Worksheet 3.")


---

### 📌 **Why Use These Data Types?**

| Data Type | Purpose |
|----------|--------|
| `int`    | Efficient for numeric identifiers, counts, and flags. |
| `float`  | For monetary values, tax rates, or decimal quantities. |
| `str`    | For text-based fields like names, addresses, and emails. |
| `datetime` | For date/time fields to enable time-based analysis. |
| `bool`   | For binary flags (e.g., VIP status). |
| `category` | For categorical data with limited unique values to reduce memory usage. |

---

### 📌 **Performance Benefits**

- **Memory Efficiency**: Using `category` for strings with repeated values reduces memory usage.
- **Speed**: Operations like filtering, sorting, and joining are faster with typed data.
- **Data Integrity**: Ensures correct storage of numeric, string, and datetime values.

This structure is ideal for large datasets and ensures optimal performance for data analysis and processing.