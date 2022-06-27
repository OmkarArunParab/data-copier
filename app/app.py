import os
import sys
import pandas
from read import get_json_reader
from write import load_db_table


def main():
    table_names = sys.argv[1].split(',')
    print(table_names)
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["USER"]}:{configs["PASS"]}@{configs["HOST"]}:{configs["PORT"]}/{configs["DB_NAME"]}'
    for table_name in table_names:
        print(table_name)
        for df in get_json_reader(configs['BASE_DIR'], table_name):
            print(table_name)
            load_db_table(df, conn, table_name, df.columns[0])


if __name__=='__main__':
    main()