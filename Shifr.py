alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
a='RU'
b='EU'
#Проверка правильности написания 
while True:
    try:
        smeshenie = int(input('Введите число, равное смещению : '))
        if smeshenie == int(smeshenie) and smeshenie >= 0:
            break
    except :
        print("Ошибка - это не число")
message = input("Введите сообщение: ").upper()
itog = ''
#Проверка правильности написания 
while True:
    try:
        language = input('Выберите язык RU/EU: ').upper()   
        if language == a or language == b:
            break
    except :
        print("Введите RU(Русский язык) или EU(Английский язык)")
#Блок высчитывания шифра Цезаря для Русского алфавита
if language == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_RU:
            itog += alfavit_RU[new_mesto]
        else:
            itog += i
#Блок высчитывания шифра Цезаря для Русского алфавита
else: 
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else:
            itog += i
print ("Введенное сообщение: ", message)
print ("Зашифрованное сообщение: ", itog)