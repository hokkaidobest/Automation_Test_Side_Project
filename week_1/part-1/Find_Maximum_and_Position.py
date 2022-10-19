def find_max(numbers):
    # your code here

    # 先將第一個值記錄下來
    largest_number = numbers[0]

    # 利用 for 迴圈跑完所有數字
    for number in numbers:
        # 若跑到的數字比存起來的大，就將最大值複寫
        if number > largest_number:
            largest_number = number
    
    # 回傳最大值結果
    return largest_number

def find_position(numbers, target):
    # your code here

    # 利用 enumerate 將 key => value 替代為 i, j
    for i, j in enumerate(numbers):
        
        # 如果 target match 到 list 的 value，就回傳 key
        if j == target:
            return i
        # 若 target 沒有 match 到任何一個 value，就回傳 -1
        elif target not in numbers:
            return -1

print(find_max([1, 2, 4, 5]) ) 	            # should print 5 
print(find_max([5, 2, 7, 1, 6]) )           # should print 7 
print(find_position([5, 2, 7, 1, 6], 5))    # should print 0 
print(find_position([5, 2, 7, 1, 6], 7))    # should print 2 
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))  # should print 2 (the first one) 
print(find_position([5, 2, 7, 1, 6], 8))    # should print -1