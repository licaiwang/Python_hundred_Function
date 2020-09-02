import csv
import os
import pandas as pd


def openDataCsv(filename: str, encode: str, returnType: str):
    """
    Args:
        filename    (str): 檔案名稱.
        encode      (str): 編碼方式 
        returnType  (str): 回傳格式 (list, dataFrame ...)
    Returns:
        : 讀取的 CSV 檔.
    """
    loc = getDataFile("test.csv")
    datas = []
    if os.path.isfile(filename):
        if returnType == "list":
            with open(loc, "r", newline="", encoding=encode) as source:
                for data in csv.reader(source):
                    datas.append(data)
            return datas
        if returnType == "dataFrame":
            return pd.read_csv(loc)
    else:
        raise FileNotFoundError


def getDataFile(name: str) -> str:
    """
    Args:
        name (int): 檔案名稱.

    Returns:
        : 現在目錄的相對路徑 + 檔案名稱.
    """
    dic = os.path.join(os.path.dirname(__file__), "testData")
    return f"{dic}\\{name}"
