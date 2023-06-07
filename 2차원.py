# 배열
# 3차원 list of list
matrix = [
        [
            [1,2,3], 
            [4,5,6]],
        [
            [7,8,9],
            [10,11,12]]
    ]
print(matrix)
print()
print(matrix[0])  # 1행
print(matrix[1])  # 2행

print(matrix[0][0])  # 1행 1열
print(matrix[0][1])  # 1행 2열
# print(matrix[0][2])  # 1행 3열

# 2차원
for i in range(0,2):
    for j in range(0,2):
        print(matrix[i][j], end = '')
    print()
    
# 3차원
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,3):
            print(matrix[i][j][k], end = '')
        print()
    print()