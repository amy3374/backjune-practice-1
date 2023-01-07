from random import *
from math import *
print(5)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋ")
print("ㅋ"*5)
# <불리안>
print(5 > 10)
print(not True)
print(not False)

# <변수 (애완동물 소개)>
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

'''여러문장 주석은
작은따음표 3개
또는 ctr+/'''

# <Q1>
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

# <연산자>
print(1+1)  # 2
print(3-2)  # 1
print(5*2)  # 10
print(6/3)  # 2

print(2**3)  # 2^3=8
print(5 % 3)  # 나머지 = 2
print(10 % 3)  # 나머지 = 1
print(5//3)  # 몫 = 1
print(10//3)  # 몫 = 3

print(10 > 3)  # true
print(4 >= 7)  # false
print(10 < 3)  # false
print(5 <= 5)  # true

print(3 == 3)  # true
print(4 == 2)  # false
print(4+3 == 7)  # true
print(1 != 3)  # true
print(not (1 != 3))  # false

print((3 > 0) and (3 < 5))  # true
print((3 > 0) & (3 < 5))  # true

print((3 > 0) or (3 > 5))  # true
print((3 > 0) | (3 > 5))  # true

print((5 > 4 > 3))  # true

# <간단한 수식>
print(2+3*4)  # 14
print((2+3)*4)  # 20
number = 2+3*4  # 14
print(number)
number = number + 2  # 16
print(number)
number += 2  # 18
print(number)
number *= 2  # 36
print(number)
number /= 2  # 18
print(number)
number -= 2  # 16
print(number)
number %= 2  # 0
print(number)

# <숫자처리 함수>
print(abs(-5))  # 절댓값 5
print(pow(4, 2))  # 4^2 = 16
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.14))  # 반올림 3
print(round(4.99))  # 반올림 4

print(floor(4.99))  # 내림 4
print(ceil(3.14))  # 올림 4
print(sqrt(16))  # 제곱근 4

# <랜덤함수>

print(random())  # 0.0이상 1.0미만의 임의의 값 생성
print(random()*10)  # 0.0이상 10.0미만의 임의의 값 생성
print(int(random()*10))  # 0이상 10미만의 임의의 값 생성
print(int(random()*10+1))  # 1이상 10미만의 임의의 값 생성

print(int(random()*45 + 1))  # 1이상 45이하의 임의의 값 생성
print(randrange(1, 46))  # 1이상 46미만(45이하)의 임의의 값 생성
print(randint(1, 45))  # 1이상 45이하의 임의의 값 생성

# <Q2 코딩 스터디 개최>
# 월 4회 스터디를 하는데 3번은 온라인으로, 1본은 오프라인으로 함

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜가 다름을 감안하여 28일 이내로 정함
# 조건3 : 매월 1~3일은 제외

# 출력문 예제
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.


date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# <문자열>
sentence = '나는 소년입니다'
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

# <슬라이싱>
jumin = "991213-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # 0부터 2직전 = 0,1
print("월 : " + jumin[2:4])  # 2,3
print("일 : " + jumin[4:6])  # 4,5
print("생년월일 : " + jumin[:6])  # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:])  # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  # 맨뒤에가 -1
print(jumin[::-1])  # 역순

# <문자열 처리함수>
python = "Python is Amazing"
print(python.lower())  # 대문자를 소문자로 출력
print(python.upper())  # 소문자를 대문자로 출력
print(python[0].isupper())  # python의 0번째가 대문자가 맞는지?
print(len(python))  # 길이 출력
print(python.replace("Python", "Java"))  # Python을 Java로 대체

index = python.index("n")  # python이란 변수에서 n이란 글자가 몇번째 위치했는지
print(index)
index = python.index("n", index + 1)  # index+1은 시작위치 즉 n을 6번째부터 찾을 수 있음
print(index)

print(python.find("n"))
print(python.find("Java"))  # find에서는 원하는 값이 없을 때는 -1이 출력
# print(python.index("Java")) index에서는 원하는 값이 없으면 오류

print(python.count("n"))  # n이 몇번 등장하는지

# <문자열 포맷>
# 방법 1
print("나는 %d살 입니다." % 24)  # %d는 정수
print("나는 %s을 좋아해요." % "파이썬")  # 문자열
print("Apple은 %c로 시작해요." % "A")  # 한글자

print("나는 %s색과 %s색을 좋아해요." % ("파랑", "빨강"))

# 방법 2
print("나는 {}살 입니다.".format(24))
print("나는 {}색과 {}색을 좋아해요.".format("파랑", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=24, color="빨강"))

# 방법4
age = 24
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# <탈출문자>
print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")  # \" \' : 문장 내에서 따옴표

# \\ : 문장 내에서 \
print("C:\\Users\\amy33\\OneDrive\\바탕 화면\\pythonworkspace>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# <Q3>
# 내 답
site = "http://naver.com"
pw = site.replace("http://", "")
# print(pw)
pw = pw[:-4]
# print(pw)
print("생성된 비밀번호 : " + pw[:3] + str(len(pw)) + str(pw.count("e")) + "!")

# 강의 답
# url = "http://naver.com"
# url = "http://daum.net"
url = "http://youtube.com"
my_str = url.replace("http://", "")  # 규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")]  # .이란 문자 찾아서 직전까지
# print(my_str)
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("생성된 비밀번호 : " + pw)

# <리스트>
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇번째 칸에 타고있는가?
print(subway.index("조세호"))

subway.append("하하")  # append는 맨 뒤에 추가
print(subway)

subway.insert(1, "정형돈")  # insert는 중간에 추가
print(subway)

print(subway.pop())  # 뒤에서부터 꺼냄
print(subway)

subway.append("유재석")
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 뒤집기도 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 4, 3, 2, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# <사전>
cabinet = {3: "유재석", "B-100": "김태호"}
print(cabinet[3])
print(cabinet.get(3))

# # print(cabinet[5]) #값이 없는 경우 프로그램이 종료됨
# print(cabinet.get(5)) #값이 없는 경우 NONE 이라 뜨고, 뒤의 hi도 나옴
print(cabinet.get(5, "사용가능"))
# print(hi)

print(3 in cabinet)  # 3이 cabinet에 있는가?
print(cabinet["B-100"])

print(cabinet)
cabinet[3] = "김종국"  # 키 3이 이미 있으므로 갱신
cabinet["c-20"] = "조세호"  # c-20키를 새로 만듬
print(cabinet)

del cabinet[3]  # 키 삭제
print(cabinet)

print(cabinet.keys())  # 키만 출력
print(cabinet.values())  # 값만 출력
print(cabinet.items())  # 키, 값 쌍으로 출력

cabinet.clear()  # 키 - 값 모두 삭제
print(cabinet)

# <튜플>
menu = ("돈까스", "치즈까스")
print(menu[0])  # 튜플은 값을 추가, 제거가 안됨
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# <세트(집합)>
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합(자바와 파이썬을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java-python)
print(java.difference(python))

python.add("김태호")
print(python)

java.remove("김태호")
print(java)

# <자료구조의 변경>
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

# <Q4>
# 출력 예제
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# 활용 예제
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# lst = range(1, 21)  /1부터 20까지 숫자 생성, but)타입은 range
# lst = list(type(lst))  /타입을 list로 바꿔줌
# print(type(lst))
# print(lst)
shuffle(lst)
winners = sample(lst, 4)  # 1명, 3명 뽑으면 중복될 확률이 있어서
print(" -- 당첨자 발표 --")
print(" 치킨 당첨자 : {0}".format(winners[0]))
print(" 커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 --")

# <if>
weather = input("오늘 날씨는 어때요?")
if weather == "비" or "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

tem = int(input("기온은 어때요?"))
if tem >= 30:
    print("너무 더워요. 나가지 마세요")
elif 10 <= tem < 30:
    print("괜찮은 날씨에요.")

elif 0 <= tem < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# <for>
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in range(5):  # 0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))

# <while>
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}님, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1  #무한루프, 강제 종료하려면 ctr + c

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

# <continue와 break>
    absent = [2, 5]
no_book = [7]
for student in range(1, 11):  # 1~10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# <한 줄 for문>
# 출석번호에 100을 붙이기로 함
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# <Q5>
cnt = 0  # 총 탑승 승객 수
for customer in range(1, 51):  # 1~50이라는 수 (승객)
    time = randrange(5, 51)  # 5~50분 소요 시간
    if 5 <= time <= 15:  # 5분~15분 이내의 손님, 탑승 승객 수 증가 처리
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
        cnt += 1
    else:  # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))

    print("총 탑승 승객 : {0} 분".format(cnt))

# <함수>


def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()

# <전달값과 반환값>


def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):  # 입금(잔액, 입금액)
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# <기본값>


def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업을 듣는다고 가정


def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))


profile("유재석")
profile("김태호")

# <가변인자>
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age),end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")

# <지역변수와 전역변수>
gun = 10


def checkpoint(soliders):
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# <Q6>


def std_weight(height, gender):  # 키는 m 단위로
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21


height = 175
gender = "남자"
weight = round(std_weight(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, weight))

# <표준 입출력>
print("python", "java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))  # 3개의 공간 확보 후 빈 공간은 0으로 채움

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")

# <다양한 출력 포맷>
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10공간 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬후, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마 찍기
print("{0:,}".format(100000000000))

# 3자리 마다 콤마찍고, + - 부호도 붙이기
print("{0:+,}".format(-100000000000))

# 3자리 마다 콤마찍고, + - 부호도 붙이고, 자릿수 확보하기, 빈자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 둘째자리까지 출력  (셋째자리에서 반올림)
print("{0:.2f}".format(5/3))

# <파일 입출력>
