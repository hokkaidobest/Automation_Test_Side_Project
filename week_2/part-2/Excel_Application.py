import pandas as pd

student_data = pd.DataFrame({
    "Student": ["Student A", "Student B", "Student C", "Student D", "Student E"],
    "Reading": [80, 88, 92, 81, 75],
    "Listening": [75, 86, 85, 88, 80],
    "Speaking": [88, 90, 92, 80, 78],
    "Writing": [80, 95, 98, 82, 80]
})

student_file = "/Users/nmp/code/Automation-Test-Program-Batch1/week_2/part-2/student.xlsx"
writer = pd.ExcelWriter(student_file, engine = 'xlsxwriter')
student_data.to_excel(writer, sheet_name = 'Sheet1', index = False)
writer.close()

reader = pd.read_excel(r"/Users/nmp/code/Automation-Test-Program-Batch1/week_2/part-2/student.xlsx")

average = [0.2, 0.25, 0.3, 0.25]

for i in range(reader["Student"].count()):
    # 取出每個學生需要計算的科目分數
    student_score = reader.loc[i, ["Reading", "Listening", "Speaking", "Writing"]]

    # 每個科目分別乘以不同的百分比
    student_each_score = student_score.mul(average)
    
    # 將每科計算後的分數加總
    result = student_each_score["Reading"] + student_each_score["Listening"] + student_each_score["Speaking"] + student_each_score["Writing"]
    
    print(f'student: {reader["Student"][i]}, score: {result}')