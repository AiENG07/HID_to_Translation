import argparse
import sys
import json


# 函数，用于从HID数据中提取Usage ID
def get_usage_id(hid_data):
    return hid_data[:6][-2:].upper()

# 函数，用于查找keyname
def find_keyname(usage_id, hid_table):
    for item in hid_table:
        if item["HID Usage ID"].replace(" ","") == usage_id:
            return item["Key Name"]
    return 'Unknown'

# 解析命令行参数
parser = argparse.ArgumentParser(description='HID Data to Key Name Converter')
parser.add_argument('-hf', '--hid_file', type=str, help='File containing HID data', required=False, default='usbdata.txt')
parser.add_argument('-hid', '--hid', type=str, help='Single HID data', required=False)
parser.add_argument('-jf', '--json_file', type=str, help='loading Json File', required=False,default='json_table.json')
args = parser.parse_args()

# 读取JSON文件
if args.json_file:
    try:
        with open(args.json_file, 'r',encoding='utf-8') as file:
            hid_table = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {args.json_file} does not exist.")
        sys.exit(1)

# 从文件中读取HID数据
if args.hid_file:
    try:
        with open(args.hid_file, 'r') as file:
            results = []  # 创建一个列表来存储结果
            for line in file:
                hid_data = line.strip()
                if hid_data:  # 确保不处理空行
                    usage_id = get_usage_id(hid_data)
                    if usage_id != '00':
	                    key_name = find_keyname(usage_id,hid_table)
	                    print(f"The key name for HID data {hid_data} is: {key_name}")
	                    results.append(key_name)  # 将结果添加到列表中
            print(" ".join(results))  # 打印所有结果
    except FileNotFoundError:
        print(f"Error: The file {args.hid_file} does not exist.")
        sys.exit(1)

# # 处理单个HID数据
if args.hid:
    usage_id = get_usage_id(args.hid)
    key_name = find_keyname(usage_id, hid_table)
    print(f"The key name for HID data {args.hid} is: {key_name}")
