import argparse
import pandas_datareader.stooq as web

from datetime import datetime


def main():
    args = Parse()

    GetStockPrice(args)

    
    
def Parse():
    """
    Get CommandLine Arguments
    
    Note:
        Input Date: YYYYMMDD
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("start", type=str)
    parser.add_argument("end", type=str)
    parser.add_argument("-b", "--brand", type=str, default="TSLA")
    parser.add_argument("-s", "--savePath", type=str, default="./stock.csv")
    args = parser.parse_args()

    return args



def GetStockPrice(args):
    """
    Get Daily Stock Price Between $start and $end

    Args:
        args (argparse): CommandLine Arguments
    """

    # str -> datetime
    start = datetime.strptime(args.start, "%Y%m%d")
    end = datetime.strptime(args.end,  "%Y%m%d")

    # データ読み込み＆保存
    data = web.StooqDailyReader(args.brand, start=start, end=end)
    reader = data.read()
    reader.to_csv(args.savePath)


    
if __name__ == "__main__":
    main()
