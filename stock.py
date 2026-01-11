import FinanceDataReader as fdr
import pandas as pd

print("코스피 데이터를 가져오고 있습니다...")

# 데이터를 가져옵니다 (2025.11.01 ~ 2026.01.09)
df = fdr.DataReader('KS11', '2025-11-01', '2026-01-09')

# 파일로 저장합니다
df[['Close']].to_csv('kospi_data.csv')

print("데이터 저장이 완료되었습니다!")
print("성공했습니다!")