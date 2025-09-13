import openpyxl

file_path = '../Costumes.xlsx'

try:
    # 1. 加载已存在的工作簿
    workbook = openpyxl.load_workbook(file_path)

    # 2. 选择工作表
    #    选择活动工作表 (通常是文件打开时看到的第一个)
    sheet = workbook.active 
    #    或者通过名称来选择，更可靠：
    #    sheet = workbook['Sheet1'] 

    # 3. 定位到C7单元格并插入数据
    print(f"正在向文件 '{file_path}' 的工作表 '{sheet.title}' 中写入数据...")
    data_to_insert = "这是我的新数据"
    sheet['C7'] = data_to_insert

    # 4. 保存更改到原文件
    #    注意：请确保该文件当前没有被Excel程序打开，否则会保存失败
    workbook.save(file_path)

    print(f"成功！数据 '{data_to_insert}' 已写入单元格 C7。")

except FileNotFoundError:
    print(f"错误：找不到文件 '{file_path}'。请检查文件名和路径。")
except Exception as e:
    print(f"发生错误：{e}")