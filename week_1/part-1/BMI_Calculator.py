# coding=utf-8

def check_bmi(height, weight):
    # your code here
    height = float(height)
    weight = float(weight)

    result = weight/(height)**2

    if result>=18.5 and result<24:
        return True
    else:
        return False

print(check_bmi(1.6, 60))   # print True
print(check_bmi(1.6, 40))   # print False
print(check_bmi(1.6, 100))  # print False