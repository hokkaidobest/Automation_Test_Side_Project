import pandas as pd

# 根據下面的其中考分數建立一個 DataFrame 並指派變數給 Scores

data = [
    {"Chinese": "", "English": 92, "Math": 83},
    {"Chinese": 85, "English": 78, "Math": 60},
    {"Chinese": 80, "English": "", "Math": 72},
    {"Chinese": 60, "English": "", "Math": ""},
    {"Chinese": 98, "English": 88, "Math": 91}
]

scores = pd.DataFrame(data, index = ["ID1", "ID2", "ID3", "ID4", "ID5"])

student_file = "Automation-Test-Program-Batch1/week_2/part-2/student.xlsx"
writer = pd.ExcelWriter(student_file, engine = 'xlsxwriter')
scores.to_excel(writer, sheet_name = 'Sheet1', index = False)
writer.close()

reader = pd.read_excel(r"Automation-Test-Program-Batch1/week_2/part-2/student.xlsx")

reader["Chinese"].fillna(value = 0, inplace = True)
reader["English"].fillna(value = 0, inplace = True)
reader["Math"].fillna(value = 0, inplace = True)

# 印出所有學生的國文和英文分數
print(reader["Chinese"].sum())
print(reader["English"].sum())

# 印出 ID5 的英文分數
print(reader.loc[4, ["English"]])

# 印出每位學生的總分，NaN 視為 0 分
for index, row in reader.iterrows():
    print(index, row.sum())