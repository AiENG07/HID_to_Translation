# HID Data to Key Name Converter

这是一个用于将HID数据转换为对应键名的Python脚本。它通过解析HID数据，并查找一个预定义的HID表来实现转换。

## 使用方法

### 命令行参数

- `-hf`, `--hid_file`: 包含HID数据的文件路径。文件中的每一行应该是一个HID数据，如果未指定，脚本默认加载`usbdata.txt`文件。
- `-hid`, `--hid`: 单个HID数据字符串。
- `-jf`, `--json_file`: 包含HID表的JSON文件路径。如果未指定，脚本将默认加载同一目录下的`json_table.json`文件。

### 运行脚本

您可以通过以下命令行方式运行此脚本：

```bash
python HID_to_Translation.py -hf usbdata.txt
```

或者，如果您有一个单独的HID数据：

```bash
python HID_to_Translation.py --hid "02001e0000000000"
```

### 输出

脚本会输出每个HID数据对应的键名。如果HID数据在HID表中找不到对应的键名，将输出`Unknown`。

## 代码说明

### 函数 `get_usage_id(hid_data)`

从HID数据中提取Usage ID。Usage ID是HID数据的最后两位十六进制数，并转换为大写。

### 函数 `find_keyname(usage_id, hid_table)`

在HID表中查找与Usage ID对应的键名。如果找不到，返回`Unknown`。

### 主程序

1. 读取HID表JSON文件。
2. 解析命令行参数。
3. 如果提供了文件路径，从文件中读取HID数据，并转换为键名。
4. 如果提供了单个HID数据，直接转换为键名。
5. 输出转换结果。

## 注意事项

- 确保HID表JSON文件`hid_table.json`位于脚本同一目录下，或者通过`-jf`参数指定其路径。
- HID数据文件应该是纯文本文件，每行一个HID数据。
- 脚本假设HID数据格式正确，不进行错误格式的检查。


## 目录树
```js
HID_to_Translation                
├─ 202106241624549419156181.csv   # xlsx转CSV生成的文件
├─ 202106241624549419156181.xlsx  # 键值与HID对应表
├─ csv_to_json.py                 # csv转json脚本
├─ hid1_11.pdf                    # HID 1.11 的设备类定义PDF文件
├─ HID_to_Translation.py          # HID转键值脚本
├─ hut1_5.pdf                     # HID使用表PDF
├─ json_table.json                # CSV转JSON生成的文件
├─ README.md                      
├─ test.pcapng                    # HID数据抓包文件
└─ usbdata.txt                    # 使用的HID数据
```
---

