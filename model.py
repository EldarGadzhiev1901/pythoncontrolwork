import fileinput
import os
import datetime
def get_data():
    # with open('file.txt', 'r') as file:
    #     data = file.read().split('\n')
    #     file.close()
    path = 'file.json'
    data = open(path, 'r')
    data.readlines()
    data.close()



def add_contact(note):
    with open ('file.json', 'a', encoding='utf-8') as file:
        file.write(note + " ")
        
        time = datetime.datetime.now()
        file.write('')
        
        
        
        file.write(str(time))
        file.write('\n')
        

        file.close
    

def search(word):
    with open('file.json', 'r', encoding='utf-8') as file:
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
    with open('file.json', 'r', encoding='utf-8') as file:
        
        filedata = file.read()
        file.close()
    with open('file.json', 'w', encoding='utf-8') as file:
        filedata = filedata.replace(title, new)
        file.write(filedata)
        file.close()
        

def delete(contact):
    with open('file.json', 'r', encoding='utf-8') as file:
        
        filedata = file.read()
        file.close()
    with open('file.json', 'w', encoding='utf-8') as file:
        null = ""
        filedata = filedata.replace(contact, null)
        filedata = filedata.replace('\n\n','\n')
        file.write(filedata)
        file.close()
        
    
         