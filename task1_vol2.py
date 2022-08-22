from collections import defaultdict
from datetime import datetime
import glob
import os
import pandas as pd
#from styleframe import StyleFrame

amount_of_running = 0

words_list_from_files = []
symbols_list = [",", ".", "(", ")", ";", ":", '!', "*", "␋", "␋"]

def calculate_data_of_running():
    time = datetime.now()
    return time

def check_existing_file(file_name):
    if not os.path.exists(file_name):
        print("File does not exsist")

def calculate_amount_of_running(file_name):
    check_existing_file(file_name)
    try:
        global amount_of_running
        c = open(file_name, "r+")
        amount_of_running = int(c.readline())
        c.seek(0)   
        c.truncate()
        amount_of_running += 1
        c.write(str(amount_of_running))
        c.close()
    except FileNotFoundError:
        print('File does not open')
    
def read_all_sourse_files(file_list):
    for filename in glob.glob('D:\Course\QA\Task1\source files\*.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:  
         
            words_list = f.read().split()
            
            for word in words_list:
                file_list.append(word)
    return file_list
    

def to_lower_register(words_list):
    for word in range(len(words_list)):
        words_list[word] = words_list[word].lower()
    return words_list

def delete_outsiders_symbols(words_list, symbols_list):
    for word in range(len(words_list)):
        for symbol in range(len(symbols_list)):
            words_list[word] = words_list[word].replace(symbols_list[symbol], "")
    return words_list

def calculate_amount_of_words(words_list):
    word_count = defaultdict(int)
    for word in words_list:
        if word in word_count: 
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def write_result(name_result_file, start_data, dictionary, ):
    check_existing_file(name_result_file)    
    try:    
        with open(name_result_file,'w') as out:
            out.write("Data of start " + str(start_data) + " " + "Amount of running programm " + str(amount_of_running) + "\n")
            for key,val in dictionary.items():
                #print('{}:{}\n'.format(key,val))
                out.write('{}:{}\n'.format(key,val)) 
    except FileNotFoundError:
        print('File does not exsist')

def sort_dictionary(dictionary):
    sorted_dict = {}
    sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)
    
    for key in sorted_keys:
        sorted_dict[key] = dictionary[key]
    
    return sorted_dict

def to_exl(start_data, dictionary):
    df = pd.DataFrame({"Amount of running programm " : amount_of_running, "Data of start " : str(start_data), 
                              "Words " : dictionary.keys(), "Number of repetitions " : dictionary.values() })
# =============================================================================
#     excel_writer = StyleFrame.ExcelWriter('result.xlsx')
#     sf = StyleFrame(df)
#     sf.to_excel(excel_writer=excel_writer, row_to_add_filters=0, columns_and_rows_to_freeze='B2')
#     sf.set_column_width(columns=["Amount of running programm ", "Data of start ", "Words ", "Number of repetitions "], width=35.3)
#     excel_writer.save()
# 
# =============================================================================

    df.to_excel('D:\\Course\\QA\\Task1\\result.xlsx', sheet_name = 'Amount of word', index = False)
#     sheet.set_column_width(columns=["Amount of running programm ", "Data of start ", "Words ", "Number of repetitions "], width=35.3)
# # =============================================================================
# =============================================================================
#     sheet.to_excel({"Amount of running programm " : amount_of_running}, sheet_name = 'Amount of word', header = None, index = False, startcol = 3, startrow=2)
#     sheet.to_excel({"Data of start " : str(start_data)}, sheet_name = 'Amount of word', header = None, index = False, startcol = 4, startrow=2)
# =============================================================================
     
     
     
time = calculate_data_of_running()
calculate_amount_of_running('count.txt')
words_list_from_files = read_all_sourse_files(words_list_from_files)
words_list_from_files = to_lower_register(words_list_from_files)
words_list_from_files = delete_outsiders_symbols(words_list_from_files, symbols_list)
word_count = calculate_amount_of_words(words_list_from_files)
word_count = sort_dictionary(word_count)
write_result('result.txt', time, word_count)
to_exl(time, word_count)
#tests.run()

# =============================================================================
# for word in words_list_from_files:
#        print(word, word_count[word])
# =============================================================================


