# Programming logic

# Step 0 - Understand the challenge we want to solve

# Step 1 - Run all files from the database folder (Sales Folder)
import os

root_path = "D:/Rafael/Projects/Courses/Python/Sales"

file_list = os.listdir(root_path)

# Step 2 - Import the sales databases
for file in file_list:
    if "sales" in file.lower():
        print(f"{root_path}/{file}")

# Step 3 - Treat/Compile the databases

# Step 4 - Calculate the best-selling product (in quantity)

# Step 5 - Calculate the product that earned the most (in revenue)

# Step 6 - Calculate the store/city that sold the most (in revenue) - create a graph/dashboard