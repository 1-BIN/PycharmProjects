import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd

def get_stock(p_code, p_start, p_end):
    df = fdr.DataReader(p_code, p_start, p_end)
    # df['Close'].plot()
    # plt.show()
    df = df.reset_index()
    seq = df['index'].dt.strftime("%Y-%m-%d")
    x_data = df[['Close']].astype(str)
    x_data['Date'] = seq
    file_nm = f"{p_code}_{p_start.replace('-','')}_{p_end.replace('-','')}.xlsx"
    x_data.to_excel(file_nm)

if __name__ == '__main__':
    # get_stock('AAPL', '2010-01-01', '2024-10-10')
    get_stock('AAPL', '2024-08-05', '2024-10-15')