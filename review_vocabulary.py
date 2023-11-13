import random
import getch 
import os

print("\ntype SPACE to represent FORGOTTEN else ENTER . other to quit\n")

n = input("type which list you want to review, enter to choose randomly \n")

wrong  = []

max_k = 1

for file_name in os.listdir("./wordlist"):  
    if file_name.startswith("wordlist") and file_name.endswith(".txt"):  
        # 提取文件名中的k值  
        k = int(file_name[8:-4])  
        if k > max_k:  
            max_k = k 


if not n.isdigit():
    filename = "./wordlist/wordlist{}.txt".format(random.choice(range(1,max_k+1)))
else:
    filename = "./wordlist/wordlist{}.txt".format(int(n))

right = 0
error = 0
total = 0

with open (filename, "r") as file:
    content = file.read()
    content = list(content.split("\n"))
    content_dic = {}
    
    for word in content:
        itemLst = list(word.split(" "))
        english, chinese = itemLst[0], itemLst[1]
        content_dic[english] = chinese
    
    KEY = list(content_dic.keys())
    
    while True:
        english = random.choice(KEY)
        chinese = content_dic[english]
        
        print(english)
        answer = getch.getch()  
        print(chinese)
        print()
        total += 1
        if answer == " ":      
            wrong.append(english)
            error += 1
        elif answer == "\n":
            right += 1
        else:
            right += 1
            break
        
    print("A total of {} words were tested, of which {} were correct, {} were wrong and the correct rate was {:.2f}%".format(total,right,error,100*right/total))
    print("wrong words list")
    for item in wrong:
        print(item," ",content_dic[item])
    

        
        
    
    




