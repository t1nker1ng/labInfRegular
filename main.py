import re
print("------------------")
print("ЗАДАНИЕ 1")
print("------------------")
print("Введите номер ИСУ:")
num = int(input())
print("Введите текст")
text1=input()
test1=335005 #X-{|
test2=343510 #:-{P
test3=310014 #8<\
test4=30 #X-|
test5=123122 #X-{P
def smile(num):
    if num<0:
        return "ISU is incorrect"
    eyes = [":", ";", "X", "8", "="]
    nose = ["-", "<", "-{", "<{"]
    mouth = ["(", ")", "O", "|", "\\", "/", "P"]
    return (eyes[num % len(eyes)] + nose[num % len(nose)] + mouth[num % len(mouth)])
print(smile(test1),smile(test2),smile(test3),smile(test4),smile(test5))
def tests(text):
    otv=smile(text)
    number = re.findall(otv,text1)
    return len(number)
print(tests(test1))
print(tests(test2))
print(tests(test3))
print(tests(test4))
print(tests(test5))
print("------------------")
print("Результаты Тестов")
print("------------------")
if smile(test1)=="X-{|":
    print('Test 1 Passed')
else:
    print('Test 1 not Passed')
if smile(test2)==":-{P":
    print('Test 2 Passed')
else:
    print('Test 2 not Passed')
if smile(test3)=="8<\\":
    print('Test 3 Passed')
else:
    print('Test 3 not Passed')
if smile(test4)=="ISU is incorrect":
    print('Test 4 Passed')
else:
    print('Test 4 not Passed')
if smile(test5)=="8<{(":
    print('Test 5 Passed')
else:
    print('Test 5 not Passed')
print("-------------------------")
print("ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ 1")
print("-------------------------")
print(num,"% 4 = ",num%4, " - вариант")
print("Введите текст:")
text=input()
def Task2(text):
    symbols_test = re.findall("\W",text)
    a=' '
    symbols=[]
    result1 = re.search(r"ВТ",text)
    result2 = re.search(r"ИТМО",text)
    if result1 == None or result2 == None:
        return "Вы не ввели ИТМО или ВТ"
    for i in range(len(symbols_test)):
        if symbols_test[i] != a:
            symbols.append(symbols_test[i])
    symbols = list(set(symbols))
    const2=const1=0
    for i in range(len(symbols)):
        text=re.sub(symbols[i],"",text)
    text=text.split()
    for i in range(len(text)):
        if text[i]==result1.group(0):
            const1=i
        if text[i]==result2.group(0):
            const2=i
    if const2 - const1 > 4:
        return "Вы ввели между ИТМО и ВТ больше 5 слов"
    else:
        s=''
        if const2!=const1:
            for i in range(const1,const2+1):
                s+=text[i]
                s+=' '
            return s
        else:
            return text
print(Task2(text))
print("-------------------------")
print("ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ 2")
print("-------------------------")
print(num,"% 6 = ",num%6, " - вариант")
print("Введите уравнение:")
ravn=input()
def Task3(ravn):
    symbols_test = re.findall("\W",ravn)
    a=' '
    symbols=[]
    for i in range(len(symbols_test)):
        if symbols_test[i] != a:
            symbols.append(symbols_test[i])
    symbols = list(set(symbols))
    def Task3_dop(ravn1):
        ravn1 = ravn1.split()
        for i in range(len(ravn1)):
            flag = True
            for j in range(len(symbols)):
                if ravn1[i]==symbols[j]:
                    flag = False
            if flag == True:
                ravn1[i] = str(3 * ((int(ravn1[i])) ** 2) + 5)
        s=''
        for i in range(len(ravn1)):
            s+=ravn1[i]+' '
        return s
    return Task3_dop(ravn)
print(Task3(ravn))
print("------------------")
print("Результаты Тестов")
print("------------------")
test1="21 + 22 = 23"
test2="22 - 21 = 1"
test3="40 * 2 - 1 = 79"
test4="0 = 0"
test5="1"
if Task3(test1) == "1328 + 1457 = 1592 ":
    print("Test 1 Passed")
else:
    print("Test  1 Failed")
if Task3(test2) == "1457 - 1328 = 8 ":
    print("Test 2 Passed")
else:
    print("Test  2 Failed")
if Task3(test3) == "4805 * 17 - 8 = 18728 ":
    print("Test 3 Passed")
else:
    print("Test  3 Failed")
if Task3(test4) == "5 = 5 ":
    print("Test 4 Passed")
else:
    print("Test  4 Failed")
if Task3(test5) == "8 ":
    print("Test 5 Passed")
else:
    print("Test  5 Failed")