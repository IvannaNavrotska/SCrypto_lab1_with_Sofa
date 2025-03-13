import re
from prettytable import PrettyTable
import math



def frequency_analysis(text, pomogator, russian_alphabet):
    for i in range(len(text)):
        for j in range(len(russian_alphabet)):
            if text[i]==russian_alphabet[j]:
                pomogator[j]+=1
                break


    return pomogator

def find_max(pomogator, russian_alphbet):
    for i in range(len(pomogator)):
        max=pomogator[0]
        k=0
        for j in range(len(pomogator)):
            if max<pomogator[j]:
                max=pomogator[j]
                k=j
        print(f" Літера \'{russian_alphbet[k]}\' зустрічається в тексті {pomogator[k]} разів")
        russian_alphbet.pop(k)
        pomogator.pop(k)



def delete_fromtext_probel(text):
    text_without_probels=re.sub(r"\s+", "", text)
    return text_without_probels

    
def find_bigram_with_1(text, russian, table):
    for i in range(len(text)-1):
        for j1 in range(len(russian)):
            if text[i]==russian[j1]:
                k1=j1
                h=i
                break
        for j2 in range(len(russian)):
            if text[i+1]==russian[j2]:
                k2=j2
                break
        table[k1][k2]+=1
        #print(text[h:h+2])


def find_bigram_with_2(text, russian, table):
    for i in range(0, len(text)-1, 2):
        for j1 in range(len(russian)):
            if text[i]==russian[j1]:
                k1=j1
                h=i
                break
        for j2 in range(len(russian)):
            if text[i+1]==russian[j2]:
                k2=j2
                break
        table[k1][k2]+=1
        #print(text[h:h+2])
    
def work_with_table(russian, tablix):
    table1=PrettyTable()
    table1.field_names=['', 'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    for i in range(len(russian)):
        g=[russian[i]]+tablix[i]
        table1.add_row(g)

    return table1

        

def find_H1(freq_list):

    sum_ = sum(freq_list)
    h1 = 0.0
    for i in freq_list:
        if i > 0:
            p = i/sum_
            h1 -= p*math.log2(p)
    return h1


def find_H2(bigram_table):

    sum_ = 0
    for row in bigram_table:
        sum_ += sum(row)
    h2 = 0.0
    for row in bigram_table:
        for i in row:
            if i>0:
                p = i/sum_
                h2 -= p*math.log2(p)
    return h2/2


    



with open("input.txt", "r", encoding="utf-8") as file:
    text_for_work = file.read()
pomogator=[0]*33
russian_alphabet1 = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
#russian_alphabet2 = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
text_excpiriments=delete_fromtext_probel(text_for_work)

#текст з пробілами
tablix=[[0]*33 for _ in range(33)]
find_bigram_with_1(text_for_work, russian_alphabet1, tablix) #для Н1
table=work_with_table(russian_alphabet1, tablix)
print(table)

#визначення ентропії Н1
freq_list = [0] * len(russian_alphabet1)
freq_list = frequency_analysis(text_for_work, freq_list, russian_alphabet1)
h1 = find_H1(freq_list)
print(f"H1 для тексту з пробілами: {h1:}")



tablix=[[0]*33 for _ in range(33)]
find_bigram_with_2(text_excpiriments, russian_alphabet1, tablix) 
table=work_with_table(russian_alphabet1, tablix)
print(table)

#визначення ентропії Н2
bigram_list = [[0]*len(russian_alphabet1) for i in range(len(russian_alphabet1))]
find_bigram_with_1(text_for_work, russian_alphabet1, bigram_list)
h2 = find_H2(bigram_list)
print(f"H2 для тексту з пробілами: {h2:}")


    
#тут текст без пробілів
tablix=[[0]*33 for _ in range(33)]
find_bigram_with_1(text_excpiriments, russian_alphabet1, tablix) 
table=work_with_table(russian_alphabet1, tablix)
print(table)

#визначення ентропії Н1
freq_list = [0] * len(russian_alphabet1)
freq_list = frequency_analysis(text_excpiriments, freq_list, russian_alphabet1)
h1 = find_H1(freq_list)
print(f"\nH1 для тексту без пробілів: {h1:}")


tablix=[[0]*33 for _ in range(33)]
find_bigram_with_2(text_excpiriments, russian_alphabet1, tablix) 
table=work_with_table(russian_alphabet1, tablix)
print(table)

#визначення ентропії Н2
bigram_list = [[0]*len(russian_alphabet1) for i in range(len(russian_alphabet1))]
find_bigram_with_1(text_excpiriments, russian_alphabet1, bigram_list)
h2 = find_H2(bigram_list)
print(f"H2 для тексту без пробілів: {h2:}")


fort=frequency_analysis(text_for_work, pomogator, russian_alphabet1)
find_max(fort, russian_alphabet1)
