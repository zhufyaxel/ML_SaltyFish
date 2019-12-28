import numpy as np
file_a = open("/Users/chenxinranshen/Desktop/ML/ML_homework.notsync/NTU-Machine-learning/李宏毅机器学习-作业/HW0/01-Data/matrixA.txt","r")
file_b = open("/Users/chenxinranshen/Desktop/ML/ML_homework.notsync/NTU-Machine-learning/李宏毅机器学习-作业/HW0/01-Data/matrixB.txt","r")

# a = file_a.readlines();
# b = file_b.readlines();
#
# matrix_a = np.matrix(a)
# matrix_b = np.matrix(b)
# print(matrix_a)
# print(matrix_b)
A = np.asmatrix(np.loadtxt(file_a, delimiter=','))
B = np.asmatrix(np.loadtxt(file_b, delimiter=','))

c = A.dot(B)
c.sort(axis=-1)
print(c)
np.savetxt("Q1_ans.txt", c, fmt="%d", delimiter="\r\n")