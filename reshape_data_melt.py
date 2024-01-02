"""
Input:
+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
Output:
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+
Explanation:
The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.
"""
import pandas as pd 

data = {
    "products": [
        {
            "product": "Umbrella",
            "quarter_1": 417,
            "quarter_2": 224,
            "quarter_3": 379,
            "quarter_4": 611
        },
        {
            "product": "SleepingBag",
            "quarter_1": 800,
            "quarter_2": 936,
            "quarter_3": 93,
            "quarter_4": 875
        }
    ]
}

product_data = data['products']

# Create a DataFrame
df = pd.DataFrame(product_data)

# Beats 81.76 % of users with Pandas 
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
                    #   source ,  id_vars=columns leave unchanged #var_name new column                                                                # new column                    
    new_report = pd.melt(frame=report, id_vars="product", var_name="quarter",value_vars=['quarter_1','quarter_2','quarter_3','quarter_3','quarter_4'],value_name = 'sales')
    return new_report

# Beats 8 % of users with Pandas 
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    new_report = pd.melt(frame=report, id_vars="product", var_name="quarter",value_vars=['quarter_1','quarter_2','quarter_3','quarter_3','quarter_4'],value_name = "sales")
    new_report.rename(columns={"value": "sales"}, inplace=True)
    return new_report    

ans = meltTable(df)
print(ans)