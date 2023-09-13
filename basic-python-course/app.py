# Programming logic

# Step 0 - Understand the challenge we want to solve

# Step 1 - Run all files from the database folder (Sales Folder)
import os
import pandas as pd

root_path = "D:/Rafael/Projects/Courses/Python/Sales"

file_list = os.listdir(root_path)

# Step 2 - Import the sales databases
total_table = pd.DataFrame()

for file in file_list:
    if "sales" in file.lower():
        table = pd.read_csv(f"{root_path}/{file}")
        total_table = total_table._append(table)

# Step 3 - Treat/Compile the databases
# print("Total_table")
# print(total_table)

# Step 4 - Calculate the best-selling product (in quantity)
products_table = total_table.groupby("Produto").sum()
products_table = products_table[["Quantidade Vendida", "Preco Unitario"]].sort_values(by="Quantidade Vendida", ascending=False)
print(products_table)

# Step 5 - Calculate the product that earned the most (in revenue)

# Step 6 - Calculate the store/city that sold the most (in revenue) - create a graph/dashboard