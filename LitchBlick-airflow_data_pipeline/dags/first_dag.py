from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import os
import re

from random import randint
from datetime import datetime
import pandas as pd

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

def _read_csv_data(**context):
       data_interval_start = context['data_interval_start'].isoformat()
       print("data_interval_start is printed", data_interval_start.split("T")[0].replace("-",""))
       date_match = data_interval_start.split("T")[0].replace("-","")
       path = "/opt/airflow/raw_data/"
       table_names = ["prices", "contracts", "products"]
       file_name_extracted = None
       # Loop through each file in the directory
       for filename in os.listdir(path):
            if filename.endswith(".csv"):
                for tn in table_names:
                    if (tn in filename) & date_is_matched(filename, date_match):
                        file_name_extracted = get_file_for_each_table(filename, date_match)  
                        file = file_name_extracted+"_"+tn+".csv"
                        print(file)
                        df = pd.read_csv(file)
                        print(df)  

def date_is_matched(filename: str, date_match):
    reg_ex = date_match+"\d*"
    match = re.search(reg_ex, filename)
    if match:
        return True
    return False

def get_file_for_each_table(filename, date_match):
    reg_ex = date_match+"\d*"
    match = re.search(reg_ex, filename)
    if match:
        sub_string = match.group()
        return sub_string
    return None
     

with DAG(
    'read_read',
    default_args=default_args,
    start_date=datetime(year=2020, month=9, day=2),
    schedule_interval='@monthly',
    end_date=datetime(year=2021, month=1, day=2),
    catchup=True,
) as dag:
    
    
    read_dag = PythonOperator(
    task_id='read_csv',
    python_callable=_read_csv_data,
    dag=dag,
    provide_context=True,
    )




    read_dag


