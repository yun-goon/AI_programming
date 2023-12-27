f = open('hw2.csv','r', encoding='UTF8') #파일 열기 read로
index_list = f.readline() #처음 한줄 때기
a = f.readlines() # 나머지 줄 때기 list
print(index_list)
index_list = index_list.split(',') #첫번째 줄 , 기준으로 list 재정렬

dict1 ={} #야구선수 key : 이름. value : 데이터

for line in a:
    line = line.strip() #개행문자 제거
    string = line.split(',') # , 기준으로 나눔
    dict1[string[0]] = string[1:] # 딕셔너리에 넣기 key : 선수이름, value : 데이터

def Name(name): #mode 1 이름
    if name not in dict1:
        print("없는 선수")
        return 0
    print(dict1[name])

#mode 2 이름, 항목
def Name_Score(name,hangmok):
    if name not in dict1:
        print("없는 선수")
        return 0
    if hangmok not in index_list:
        print("없는 항목")
        return 0
    temp_list = dict1[name]
    temp_n = index_list.index(hangmok)
    print(temp_list[temp_n-1])

#mode 3 항목
def Hangmok(hangmok):
    if hangmok not in index_list:
        print("없는 항목")
        return 0
    temp_n = index_list.index(hangmok)
    hangmok_list = []
    for i in dict1.values():
        hangmok_list.append(i[temp_n-1])
    hangmok_list.sort(reverse=True)
    print(hangmok_list)

while(True):
    mode_num = int(input("모드설정(1,2,3,4) : "))
    if mode_num == 1:
        name = input("이름 : ")
        Name(name)
    elif mode_num == 2:
        name = input("이름 : ")
        hangmok = input("항목 : ")
        Name_Score(name,hangmok)
    elif mode_num == 3:
        hangmok = input("항목 : ")
        Hangmok(hangmok)
    elif mode_num == 4:
        break

f.close()