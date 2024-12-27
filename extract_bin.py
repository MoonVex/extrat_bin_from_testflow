import re

def extract_bin_numbers(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # 使用正则表达式匹配"bin"后面的数字
            match = re.search(r'bin(\d+)', line)
            if match:
                # 提取匹配到的数字
                bin_number = match.group(1)
                # 将提取的数字写入输出文件，换行
                outfile.write(f"{bin_number}\n")

if __name__ == "__main__":
    input_file = "input.txt"  # 输入的txt文件
    output_file = "output.txt"  # 输出的txt文件
    extract_bin_numbers(input_file, output_file)
