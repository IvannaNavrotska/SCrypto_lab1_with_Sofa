import re
from prettytable import PrettyTable

def frequency_analysis(text, pomogator, russian_alphabet):
    ''' 
    Функція що рахує частоти
    '''
    for i in range(len(text)):
        for j in range(len(russian_alphabet)):
            if text[i]==russian_alphabet[j]:
                pomogator[j]+=1
                break


    return pomogator

def find_max(pomogator, russian_alphbet):
    '''
    Функція для виводу частот символів від найбільшого до найменшого
    '''
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
    '''
    Допоміжна штука для підрахунку біграм, видаляє всі пробіли з тексту
    '''
    text_without_probels=re.sub(r"\s+", "", text)
    return text_without_probels

    
def find_bigram_with_1(text, russian, table):
    '''
    Розрахунок таблиці для біграм із кроком 1
    '''
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
        print(text[h:h+2])


def find_bigram_with_2(text, russian, table):
    '''
    Розрахунок таблиці для біграм із кроком 2
    '''
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
        print(text[h:h+2])
    
def work_with_table(russian, tablix):
    '''
    Для офрмлення таблиць в людський вигляд
 '''
    table1=PrettyTable()
    table1.field_names=['', 'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
    for i in range(len(russian)):
        g=[russian[i]]+tablix[i]
        table1.add_row(g)

    return table1

        








with open("input.txt", "r", encoding="utf-8") as file:
    text_for_work = file.read()
pomogator=[0]*33
russian_alphabet1 = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
#russian_alphabet2 = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
tablix=[[0]*33 for _ in range(33)]

text_excpiriments=delete_fromtext_probel(text_for_work)
find_bigram_with_1(text_excpiriments, russian_alphabet1, tablix)
table=work_with_table(russian_alphabet1, tablix)
print(table)
tablix=[[0]*33 for _ in range(33)]
find_bigram_with_2(text_excpiriments, russian_alphabet1, tablix)
table=work_with_table(russian_alphabet1, tablix)
print(table)
fort=frequency_analysis(text_for_work, pomogator, russian_alphabet1)
find_max(fort, russian_alphabet1)
