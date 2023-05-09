import requests
import pandas as pd
import boto3
from io import StringIO


def extract_data(raw_data):
    charge_points = []
    response = raw_data['ChargeDevice']
    for item in response:
        if item['ChargeDeviceModel'] is not None:  # it accepts " " string but not None
            postcode = item['ChargeDeviceLocation']['Address']['PostCode']
            month_updated = pd.to_datetime(item['DateUpdated'].split(" ")[0]).strftime("%Y-%m")
            charge_points.append({
                'ChargeDeviceManufacturer': item['ChargeDeviceManufacturer'],
                'LocationType': item['LocationType'],
                'ChargeDeviceModel': item['ChargeDeviceModel'],
                'PostCode': postcode,
                'MonthUpdated': month_updated,
                'count': 1
            })

    df_data = pd.DataFrame(charge_points)
    df_data = df_data.groupby(
        ['ChargeDeviceManufacturer', 'LocationType', 'ChargeDeviceModel', 'PostCode', 'MonthUpdated']).agg(
        {'count': 'sum'}).reset_index()
    return df_data


def get_data():
    url = 'https://chargepoints.dft.gov.uk/api/retrieve/registry/format/json'
    response = requests.get(url)
    return response.json()


def upload_s3(df):
    bucket_name = 'data-pugsurfing'
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket_name, 'charger_models_UK.csv').put(Body=csv_buffer.getvalue())


if __name__ == "__main__":
    data = get_data()
    df = extract_data(data)
    upload_s3(df)
