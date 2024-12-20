import csv
import json

csv_file = '202106241624549419156181.csv'
json_file = 'json_table.json'

# 读取CSV文件并转换为字典列表
data = []
with open(csv_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 跳过第一行
    next(reader)
    # 读取并使用CSV文件的第二行的每一列作为列名
    fieldnames = next(reader)
    for row in reader:
        data.append(dict(zip(fieldnames, row)))

# 将字典列表转换为JSON并保存到文件
with open(json_file, 'w', encoding='utf-8') as jfile:
    json.dump(data, jfile, indent=4, ensure_ascii=False)