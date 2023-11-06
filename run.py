import sys  
  
def read_file_content(filename):  
    try:  
        with open(filename + ".txt", 'r') as file:  
            content = file.read()  
            print(content)  
    except FileNotFoundError:  
        print(f"文件 '{filename}' 不存在。请创建介绍txt文本")  
  
if __name__ == '__main__':  
    if len(sys.argv) != 2:  
        print("请提供一个文件名作为参数。")  
    else:  
        filename = sys.argv[1]  
        read_file_content(filename)  