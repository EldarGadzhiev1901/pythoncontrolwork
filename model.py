import fileinput
import os
def get_data():
    # with open('file.txt', 'r') as file:
    #     data = file.read().split('\n')
    #     file.close()
    path = 'file.md'
    data = open(path, 'r')
    data.readlines()
    data.close()



def add_contact(note):
    with open ('file.md', 'a', encoding='utf-8') as file:
        file.write(note)
        file.write('\n')

        file.close
    

def search(word):
    with open('file.md', 'r', encoding='utf-8') as file:
        found = False
        for line in file:
            if word in line:
                print(line, end='')
                found = True
        if found == False:
            print("По вашему запросу ничего не найдено ")
        # for line in file:
        #     if word in line:
        #         print(line, end='')
        #         break
        #     else:
        #         print("По вашему запросу ничего не найдено ")
        #         print('\n')
            

def change(title, new):
    with open('file.md', 'r', encoding='utf-8') as file:
        
        filedata = file.read()
        file.close()
    with open('file.md', 'w', encoding='utf-8') as file:
        filedata = filedata.replace(title, new)
        file.write(filedata)
        file.close()
        

def delete(contact):
    with open('file.md', 'r', encoding='utf-8') as file:
        
        filedata = file.read()
        file.close()
    with open('file.md', 'w', encoding='utf-8') as file:
        null = ""
        filedata = filedata.replace(contact, null)
        filedata = filedata.replace('\n\n','\n')
        file.write(filedata)
        file.close()
        
    
         