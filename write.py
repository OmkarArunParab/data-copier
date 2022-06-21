def load_db_table(df,conn,TABLE_NAME,key):
    min = df[key].min()
    max = df[key].max()
    df.to_sql(TABLE_NAME, conn, if_exists='append', index=False)
    print(f'records {min} to {max} of {key} from {TABLE_NAME} are processed.')


if __name__=='__main__':
    import pandas as pd
    import os
    configs=dict(os.environ.items())
    data = [
        {'user_id': 1, 'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
        {'user_id': 2, 'user_first_name': 'Donald', 'user_last_name': 'Duck'}
    ]
    conn=f'postgresql://{configs["USER"]}:{configs["PASS"]}@{configs["HOST"]}:{configs["PORT"]}/{configs["DB_NAME"]}'
    df=pd.DataFrame(data)
    load_db_table(df,conn,'users','user_id')
