import os
import sys
import pandas
from read import get_json_reader
from write import load_db_table


def main():
    table_names = [sys.argv[1].split(',')[0]]
    configs = dict(os.environ.items())
    conn = f'postgresql://retail_user:itversity@localhost:5452/retail_db'
    for table_name in table_names:
        for df in get_json_reader(configs['BASE_DIR'], table_name):
            load_db_table(df, conn, table_name, df.columns[0])


if __name__=='__main__':
    main()