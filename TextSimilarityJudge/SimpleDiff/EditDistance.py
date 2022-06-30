'''
计算两个字符串间的编辑距离
'''
def editDistance(str1,str2):
    matrix = [[0 for j in range(len(str2))] for i in range(str1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            x = 1
            if str1[i] != str2[j]:
                x = 0
            matrix[i][j] = max(matrix[i-1][j] + 1,matrix[i][j-1] + 1,matrix[i-1][j-1] + x)
    return matrix[len(str1) - 1][len(str2) - 1]