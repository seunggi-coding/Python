import pandas as pd

# read_csv 메소드를 사용하면 자동으로 csv 파일의 첫 번째 행이 헤더로 들어간다.
iphone_df = pd.read_csv('D:/Github_Clone/Python/Pandas/iphone.csv', index_col=0)
print(iphone_df)