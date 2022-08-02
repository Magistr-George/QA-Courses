from collections import defaultdict
from datetime import datetime

datetime = datetime.now()
amount_of_running = 0

try:
    c = open('count.txt', "r+")
    amount_of_running = int(c.readline())
    c.seek(0)   
    c.truncate()
    amount_of_running += 1
    c.write(str(amount_of_running))
    c.close()
except FileNotFoundError:
    print('File does not exsist')

try:
    f = open('text.txt')
    words_list = f.read().split()
    f.close()  
except FileNotFoundError:
    print('File does not exsist')
    
word_count = defaultdict(int)
#symbols_list = [",", ".", "(", ")"]
    
for word in words_list:
# =============================================================================
#     for symbol in range(len(symbols_list)):
#          word.translate({ord(symbols_list[symbol]): None})
#          word.replace(symbols_list[symbol], "")
#          print(word, symbols_list[symbol])
# =============================================================================

    word_count[word] = 1
    word_count[word] += 1
    #print(word, word_count[word])
try:    
    with open('result.txt','w') as out:
        out.write("Data of start " + str(datetime) + " " + "Amount of running programm " + str(amount_of_running) + "\n")
        for key,val in word_count.items():
            out.write('{}:{}\n'.format(key,val))
        out.close() 
except FileNotFoundError:
    print('File does not exsist')
