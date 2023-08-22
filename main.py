import os
import pandas as pd
import matplotlib.pyplot as plt


def merge_df(fn):
    # 看一下是否有final_log
    if os.path.exists("final_log.csv"):
        # 有的話把新df加到後面
        fir = pd.read_csv("final_log.csv")
        #  要過格式處理
        sec = pd.read_csv(fn)
        merged = pd.concat([sec, fir], axis=1)
        merged = merged.loc[:, ~merged.columns.str.contains('Unnamed: 0')]
        merged.to_csv("final_log.csv")
    else:
        # 沒有的話把新df做為表頭
        df = pd.read_csv(fn)
        # visualize()
        df.to_csv("final_log.csv")


def visualize_hw_info(df):
    names = ['Physical Memory Used [MB]', "Core VIDs (avg) [V]"]
    for name in names:
        plt.subplot()
        plt.title(name)
        plt.plot(df[name][:-2])
        # set ticks
        y_ticks = plt.yticks()[0]
        selected_ticks = y_ticks[::len(y_ticks) // 4]
        plt.yticks(selected_ticks)
        plt.show()


def visualize_furmark(df):
    g_df=df.groupby("Renderer")
    names = ['core_temp_fahrenheit']
    for name in names:
        plt.subplot()
        plt.title(name)
        for group_name, group_data in g_df:
            plt.plot(group_data[name], label=group_name)
        plt.xlabel('Index')
        plt.ylabel(name)
        plt.legend()
    plt.show()
"""
    names = []
    for name in names: 
        plt.subplot()
        plt.title(name)
        y_ticks = plt.yticks()[0]
        selected_ticks = y_ticks[::len(y_ticks) // 4]
        plt.yticks(selected_ticks)
        plt.show()
    """


if __name__ == '__main__':
    # 取得目前執行的Python檔案的路徑
    current_file_path = os.path.abspath(__file__)

    # 提取資料夾路徑
    folder_path = os.path.dirname(current_file_path)

    # 遍歷資料夾中的檔案
    for file_name in os.listdir(folder_path):
        # 檢查檔案是否為CSV檔案
        if file_name.lower().endswith('.csv'):
            """
            # 構建完整的檔案路徑
            file_path = os.path.join(folder_path, file_name)
            cdf = pd.read_csv(file_name)
            visualize(cdf)
            merge_df(file_name)
            """
            # 檔案分流
            cdf = pd.read_csv(file_name)
            match file_name:
                case "furmark-gpu-monitoring.csv":
                    print("furmark")
                    visualize_furmark(cdf)
                case "hwinfo.CSV":
                    print("hwinfo")
                    visualize_hw_info(cdf)
