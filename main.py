def merge_df(fn):
    # 看一下是否有final_log
    if os.path.exists("final_log.csv"):
        # 有的話把新df加到後面
        fir = pd.read_csv("final_log.csv")
        sec = pd.read_csv(fn)
        merged = pd.concat([sec, fir],axis=1)
        merged.to_csv("final_log.csv")
    else:
        # 沒有的話把新df做為表頭
        df = pd.read_csv(fn)
        visualize()
        df.to_csv("final_log.csv")


def visualize():
    return 0


if __name__ == '__main__':
    import os
    import pandas as pd

    # 取得目前執行的Python檔案的路徑
    current_file_path = os.path.abspath(__file__)

    # 提取資料夾路徑
    folder_path = os.path.dirname(current_file_path)

    # 遍歷資料夾中的檔案
    for file_name in os.listdir(folder_path):
        print(file_name)
        # 檢查檔案是否為CSV檔案
        if file_name.lower().endswith('.csv'):
            # 構建完整的檔案路徑
            file_path = os.path.join(folder_path, file_name)
            print(file_path)
            merge_df(file_name)
