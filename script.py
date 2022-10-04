import csv
import os
from re import I

class Comment:
    
    def __init__(self): #по умолчанию
        self.name = None
        self.comment = None
        self.mark = None

def get_dataset(path):
    dataset=list()
    for folder_num in range(1,6):
        folder_path = path+'\\'+str(folder_num)
        num_of_files = sum(os.path.isfile(os.path.join(folder_path, f)) for f in os.listdir(folder_path)) + 1
        for file_num in range(1,num_of_files):
            path_to_file = folder_path+f'\\{(file_num):04}'+'.txt'
            try:
                file = open(path_to_file, 'r', encoding='utf-8')
                print(f'{folder_num} : {(file_num):04}')
            except Exception as e:
                    print(e.args)
            comment = Comment()
            text = ""
            counter = 0
            for elem in range(0,5):
                line = file.readline()
                if not line:
                    try:
                        file.close()
                    except Exception as e:
                        print(e.args)
                    break
                if counter == 0 : comment.name = line
                else : text+=line
                counter += 1
            comment.mark = folder_num
            text = text.replace(u'\xa0', u' ')
            comment.comment = text.strip()
            dataset.append(comment)
    return dataset
            
if __name__=='__main__':
    
    path='C:\\application_programming\\first_lab\\dataset'
    dataset = get_dataset(path)
    
    print("Работа окончена")