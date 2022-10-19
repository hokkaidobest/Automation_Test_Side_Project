import numpy

def check_bmi(height, weight):
    # your code here

    # 利用 square 將身高處理成平方
    square_height = numpy.square(height)

    # 體重除以身高的平方
    result = weight / square_height

    # 結果若介於 18.5 到 24 間，回傳 True；若否則回傳 False
    if result >= 18.5 and result < 24:
        return True
    else:
        return False

print(check_bmi(1.6, 60))   # print True
print(check_bmi(1.6, 40))   # print False
print(check_bmi(1.6, 100))  # print False