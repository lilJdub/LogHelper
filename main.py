# This is a sample Python Project for csv merging tool
import time

if __name__ == '__main__':
    import os
    import pandas as pd
    # 取得目前執行的Python檔案的路徑
    current_file_path = os.path.abspath(__file__)

    # 提取資料夾路徑
    folder_path = os.path.dirname(current_file_path)

    # 全域變數dataframe
    global_df = pd.DataFrame()
    flag = True

    # 遍歷資料夾中的檔案
    for file_name in os.listdir(folder_path):
        print(file_name)
        # 檢查檔案是否為CSV檔案
        if file_name.endswith('.csv'):
            # 構建完整的檔案路徑
            file_path = os.path.join(folder_path, file_name)
            print(file_path)
            # header df for merging
            if flag:
                global_df = pd.read_csv(file_path)
                flag = False
            else:
                # 讀取CSV檔案
                df = pd.read_csv(file_path)
                # 把df outer join起來
                global_df = global_df.merge(df, on='Timestamp', how='outer')

    print(global_df)
    global_df.to_csv(str(time.time())+'merged_data.csv', index=False)

    print("DataFrame已保存为merged_data.csv")