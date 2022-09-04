import pandas as pd

df1 = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '刘六', '齐四'],
    '号码': ['123', '456', '789', '987', '654']
})

df2 = pd.DataFrame({
    '姓名': ['张三', '张三', '张三', '李四', '李四', '李四', '李四', '王五', '王五', '刘玉', '胡军', '刘玉', '刘六', '刘六', '刘六', '刘六', '刘克', '刘玉', '齐七', '齐七', '齐七', '齐七', '冯亮', '刘玉', '王云'],

    '号码': ['123', '456', '789', '123', '123', '456', '456', '456', '456', '456', '741', '741', '741', '741', '741', '789', '789', '789', '789', '789', '852', '852', '852', '852', '852'],

    '日期': ['2022-03-13', '2022-03-06', '2022-01-30', '2022-01-04', '2022-02-26', '2022-03-26', '2022-03-06', '2022-01-30', '2022-01-29', '2022-03-13', '2022-03-06', '2022-02-19', '2022-02-04', '2022-03-10', '2022-04-19', '2022-03-10', '2022-01-29', '2022-02-19', '2022-03-06', '2022-03-26', '2022-01-04', '2022-02-04', '2022-04-19', '2022-02-26', '2022-03-06'],

    '方案': ['G1012', 'G1022', 'G1002', 'G1007', 'G1017', 'G1023', 'G1018', 'G1003', 'G1008', 'G1013', 'G1020', 'G1015', 'G1010', 'G1005', 'G1025', 'G1004', 'G1009', 'G1014', 'G1019', 'G1024', 'G1006', 'G1011', 'G1026', 'G1016', 'G1021']
})

df3 = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '刘六', '齐四'],
    '号码': ['123', '456', '789', '987', '654'],
	'年龄': ['25', '36', '41', '12', '54']
})

# 上下拼接
df = pd.concat([df1, df2, df3], axis=0)

# 左右拼接
df = pd.concat([df1, df2, df3], axis=0)

print(df)