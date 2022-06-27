import os
import pandas as pd
def get_json_reader(BASE_DIR,TABLE_NAME,chunksize=1000):
    file_name = os.listdir(f'{BASE_DIR}/{TABLE_NAME}')[0]
    file_path = f'{BASE_DIR}/{TABLE_NAME}/{file_name}'
    return pd.read_json(file_path,lines=True,chunksize=chunksize)

if __name__ == '__main__':
    BASE_DIR = os.environ.get('BASE_DIR')
    TABLE_NAME=os.environ.get('TABLE_NAME')
    json_reader=get_json_reader(BASE_DIR, TABLE_NAME)
    for idx, df in enumerate(json_reader):
        print(f'Chunk with index {idx} and records {df.shape[0]} is read')