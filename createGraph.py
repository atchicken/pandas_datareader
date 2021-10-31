import argparse
import csv
import math

import matplotlib.pyplot as plt

from datetime import datetime


def main():

    args = Parse()

    GetData(args)

    return


    
def GetData(args):
    """
    Read CSV Data Between $start and $end
    
    Args:
        args (argparse): CommandLine Arguments
    """

    start = datetime.strptime(args.start, "%Y%m%d")
    end = datetime.strptime(args.end, "%Y%m%d")
    
    f = open(args.csvPath, "r")
    reader = csv.reader(f, delimiter=",")

    # ヘッダを読み飛ばし
    header = next(reader)

    # data: [時刻, 終値]のリスト
    data = []
    for d in reader:
        t = datetime.strptime(d[0], "%Y-%m-%d")
        if start <= t and t <= end:
            data.append([t, float(d[4])])
            
    sortData = sorted(data, key=lambda t: t[0])

    CreateGraph(args, sortData, start, end)

    return



def CreateGraph(args, data, start, end):
    """
    Create Graph Using Data

    Args:
        args  (argparse): CommandLine Arguments
        data      (list): List of Time and Closing Price
        start (datetime): Start Time of Data
        end   (datetime): End Time of Data
    """

    x, y = [], []
    for d in data:
        x.append(d[0])
        y.append(d[1])
        
    # Y軸範囲指定（max: 切り上げ, min: 切り捨て）
    ymax, ymin = math.ceil(max(y)/100)*100, math.floor(min(y)/100)*100
    
    plt.xlim([start, end])
    plt.ylim([ymin, ymax])

    plt.xlabel('Time', fontsize=12)
    plt.ylabel('ClosingPrice[$]', fontsize=12)

    plt.title(args.brand + " StockPrice", fontsize=15)
    plt.grid(True)
    plt.plot(x, y, color="red")
    
    plt.savefig(args.savePath)
    plt.show()
    
    
    return



    
def Parse():
    """
    Get CommandLine Arguments

    Note:
        Input Date: YYYYMMDD
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("csvPath", type=str)
    parser.add_argument("start", type=str)
    parser.add_argument("end", type=str)
    parser.add_argument("-b", "--brand", type=str, default="TSLA")
    parser.add_argument("-s", "--savePath", type=str, default="./tsla.png")
    args = parser.parse_args()

    return args




if __name__ == "__main__":
    main()
