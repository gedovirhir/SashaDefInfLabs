# %%
import math

# %%
def adolfHitler1(adolfHitler2, adolfHitler3, adolfHitler4 = False, **kwargs):
    adolfHitler5 = -adolfHitler3 if adolfHitler4 else adolfHitler3 #определяем отступ
    adolfHitler6 = ord("Z") - ord("A") + 1 #размер алфавита
    adolfHitler7 = ''
    for adolfHitler8 in adolfHitler2:
        if not adolfHitler8.isalpha():
            res += adolfHitler8
        elif adolfHitler8.isalpha() and adolfHitler8.islower(): #сдвигаем элемент по ascii таблице в зависимости от регистра
            adolfHitler7 += chr((ord(adolfHitler8) + adolfHitler5 - ord("a")) % adolfHitler6 + ord("a")) 
        elif adolfHitler8.isalpha():
            adolfHitler7 += chr((ord(adolfHitler8) + adolfHitler5 - ord("A")) % adolfHitler6 + ord("A"))
    return adolfHitler7

# %%
#Частота букв
adolfHitler9 = "zqjxkvbwypgumcfldhsirnoate" #1-граммы
adolfHitler9 = ['th', 'he', 'in', 'er', 'an', 're', 'on', 'at', 'en', 'nd', 'ti', 'es', 'or', 'te', 'of', 'ed', 'is', 'it', 'al', 'ar'] #2-граммы 
adolfHitler10 = [0.07, 0.11, 0.13, 0.15, 0.4, 0.9, 1.4, 1.5, 1.9, 1.9, 2, 2.4, 2.5, 2.7, 2.9, 3.4, 3.8, 5.2, 6.1, 6.3, 6.8, 7.1, 7.9, 8.1, 10.5, 13] #1-граммы
adolfHitler10 = [ #2-граммы
3.56,
3.07,
2.43,
2.05,
1.99,
1.85,
1.76,
1.49,
1.45,
1.35,
1.34,
1.34,
1.28,
1.20,
1.17,
1.17,
1.13,
1.12,
1.09,
1.07
]
adolfHitler11 = dict(zip(adolfHitler9, [round(adolfHitler8 / 100, 4) for adolfHitler8 in adolfHitler10])) #словарь соответствий

# %%
with open("text.txt") as f: #считываем текст из файла
    adolfHitler12 = f.read()

# %%
def adolfHitler13(adolfHitler14): #итератор по словам
    """
    adolfHitler17 - функция на обработку не буквенных символов
    """
    def f(adolfHitler15, adolfHitler16, adolfHitler17 = lambda x: x): 
        adolfHitler2 = ''
        for adolfHitler8 in adolfHitler15:
            if adolfHitler8.isalpha():
                adolfHitler2 += adolfHitler8.lower()
                if len(adolfHitler2) == adolfHitler16:
                    adolfHitler2 = adolfHitler14(adolfHitler2)
            else:
                adolfHitler17(adolfHitler2 + adolfHitler8)
                adolfHitler2 = ''
    return f

# %%
def adolfHitler16(adolfHitler15, adolfHitler18 = 1): #подсчет количества слов длины adolfHitler18
    adolfHitler6 = [0]
    @adolfHitler13
    def f(adolfHitler2):
        adolfHitler6[0] += 1
        return adolfHitler2[1:]
    f(adolfHitler15, adolfHitler18)
    return adolfHitler6[0]
def wordCount(adolfHitler15, adolfHitler18 = 1): #подсчитываем количественные отношения всех слов длины adolfHitler18 к общему кол-ву слов
    adolfHitler19 = dict({})
    adolfHitler6 = adolfHitler18(adolfHitler15, adolfHitler18)
    @adolfHitler13
    def f(adolfHitler2):
        if adolfHitler2 not in adolfHitler19:
            adolfHitler19.update({adolfHitler2 : 1 / adolfHitler6})
        else:
            adolfHitler19[adolfHitler2] += 1 / adolfHitler6
        return adolfHitler2[1:]
    f(adolfHitler15, adolfHitler18)
    return adolfHitler19

# %%
def adolfHitler20(adolfHitler21): #сортировка словаря по values
    return dict(sorted(adolfHitler21.items(), key= lambda x: x[1], reverse=True))

# %%
def adolfHitler27(adolfHitler15, adolfHitler16 = 1, adolfHitler11 = adolfHitler11, adolfHitler25 = ''): #дешифровка частотным методом, adolfHitler25 - символ для выделения измененных символов
    adolfHitler11 = adolfHitler20(adolfHitler11) #словарь введенных частот
    adolfHitler22 = adolfHitler20(wordCount(adolfHitler15, adolfHitler16)) #словрь подсчитанных в зашифрованном тексте
    adolfHitler23 = dict(zip(adolfHitler22.keys(), adolfHitler11.keys())) # словарь соответвия
    adolfHitler7 = ['']
    @adolfHitler13 #заменяем все слова соответствующие словарю соответствия
    def f(adolfHitler2):
        if adolfHitler2 in adolfHitler23:
            adolfHitler7[0] += adolfHitler25 +  adolfHitler23[adolfHitler2] + adolfHitler25
            return ''
        else:
            adolfHitler7[0] += adolfHitler2[0]
            return adolfHitler2[1:]
    def adolfHitler26(adolfHitler2):
        adolfHitler7[0] += adolfHitler2
    f(adolfHitler15, adolfHitler16, adolfHitler26)
    return adolfHitler7[0]

# %%
print(adolfHitler12, "\n")
print(adolfHitler1(adolfHitler12, 2), "\n")
print(adolfHitler27(adolfHitler1(adolfHitler12, 2), 2), "\n")


