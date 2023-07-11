from datetime import datetime
import re

import os
import pandas as pd



# now = datetime.today().isoformat()
# print(now.split("T")[0].replace("-",""))
# date_match = now.split("T")[0].replace("-","")
# reg_ex = date_match+"\d*"
# print(reg_ex)
# extractStr = "jashasu uasusa 20230513220144_contracts jajsas ujsdhjhad jhjhsaja"
# match = re.search(reg_ex, extractStr)
# if match:
#     sub_string = match.group()
#     print(sub_string)
date_match = "20201001"

path = "C:\\Users\\Hinakoushar\\OneDrive\\Desktop\\LichtBlick\\src_data\\src_data\\"
table_names = ["prices", "contracts", "products"] 
dfs = {}
def date_is_matched(filename: str):
    reg_ex = date_match+"\d*"
    match = re.search(reg_ex, filename)
    if match:
        return True
    return False

def get_file_for_each_table(filename):
    reg_ex = date_match+"\d*"
    match = re.search(reg_ex, filename)
    if match:
        sub_string = match.group()
        return sub_string


for tn in table_names:
    print(tn)
    if date_is_matched(filename):
        date_var = get_file_for_each_table(filename)  

        file = date_var+"_"+tn+".csv"
        print(file)

# Loop through each file in the directory
for filename in os.listdir(path):
    print(path,filename)
    if filename.endswith(".csv"):
        for tn in table_names:
            print(tn)
            if (tn in filename) & date_is_matched(filename):
               date_var = get_file_for_each_table(filename)  

               file = date_var+"_"+tn+".csv"
               print(file)
               df_prices = pd.read_csv(file)
               print(df_prices)

#         # Convert the date string to a pandas datetime object
#         try:
#             date = pd.to_datetime(date_str, format="%Y%m%d%H%M%S")
#         except ValueError:
#             continue

#         # Group the files by month
#         month = pd.to_datetime(date.strftime("%Y-%m"))
#         if month not in dfs:
#             dfs[month] = {}
#         if table_name not in dfs[month]:
#             dfs[month][table_name] = []

#         # Read the file into a pandas dataframe and add it to the appropriate group
#         file_path = os.path.join(path, filename)
#         df = pd.read_csv(file_path)
#         dfs[month][table_name].append(df)

# # Process each month's data
# for month, month_data in dfs.items():
#     for table_name, table_data in month_data.items():
#         # Combine the dataframes for this table from this month
#         if len(table_data) == 0:
#             continue
#         if len(table_data) == 1:
#             combined_df = table_data[0]
#         else:
#             combined_df = pd.concat(table_data)

#         # Do whatever processing you need to do with the combined dataframe here
#         # For example, you could write it to a new CSV file:
#         output_path = os.path.join(path, f"{month.strftime('%Y%m')}_combined_{table_name}.csv")
#         combined_df.to_csv(output_path, index=False)

