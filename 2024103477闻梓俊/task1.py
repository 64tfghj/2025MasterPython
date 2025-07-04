import time
import random
matrix_size = 10000
num_modifications = 10000
print("构造 list 矩阵...")
list_matrix = [[0] * matrix_size for _ in range(matrix_size)]
print("修改 list 矩阵...")
start_time_list = time.time()
for _ in range(num_modifications):
    i = random.randint(0, matrix_size - 1)
    j = random.randint(0, matrix_size - 1)
    list_matrix[i][j] += 1
end_time_list = time.time()
list_time = end_time_list - start_time_list
print(f"List 修改耗时: {list_time:.2f} 秒")
print("构造 tuple 矩阵（内部嵌套 list 便于模拟）...")
tuple_matrix = tuple([tuple([0] * matrix_size) for _ in range(matrix_size)])
print("模拟修改 tuple 矩阵（不可变模拟）...")
start_time_tuple = time.time()
for _ in range(num_modifications):
    i = random.randint(0, matrix_size - 1)
    j = random.randint(0, matrix_size - 1)
    row = list(tuple_matrix[i])
    row[j] += 1
    new_row = tuple(row)
    tuple_matrix = tuple(
        new_row if idx == i else tuple_matrix[idx]
        for idx in range(matrix_size)
    )
end_time_tuple = time.time()
tuple_time = end_time_tuple - start_time_tuple
print(f"Tuple 修改耗时: {tuple_time:.2f} 秒")
print("\n性能对比:")
print(f"List 修改时间： {list_time:.2f} 秒")
print(f"Tuple 模拟修改时间： {tuple_time:.2f} 秒")
