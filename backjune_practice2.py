# 1차원 배열
# 10807 개수 세기
# n = int(input())
# input_data = list(map(int, input().split()))
# v = int(input())
# print(input_data.count(v))


# 10871 x보다 작은 수
# n, x = map(int, input().split())
# input_data = list(map(int, input().split()))

# for i in input_data:
#     if x > i:
#         print(i, end=" ")


# 10818 최소, 최대
# n = int(input())
# input_data = list(map(int, input().split()))
# print(min(input_data), max(input_data))


# 2562 최댓값
# num_list = []
# for i in range(9):
#     num_list.append(int(input()))
# print(max(num_list))
# index = num_list.index(max(num_list))
# print(index+1)


# 5597 과제 안 내신 분..?
# num_list = [i for i in range(1, 31)]
# for i in range(28):
#     num_list.remove(int(input()))
# print(min(num_list))
# print(max(num_list))


# 3052 나머지
# num_list = []
# for i in range(10):
#     i = int(input())
#     num_list.append(i % 42)
# num_list = set(num_list) #set는 중복제거 해주는 역할
# print(len(num_list))


# 1546 평균
# n = int(input())
# score = list(map(int, input().split()))
# max_score = max(score)
# new_score = []
# for i in score:
#     new_score.append(i/max_score*100)  # 새로운 점수 생성
# avg = sum(new_score)/n
# print(avg)


# 8958 OX퀴즈
# n = int(input())
# for i in range(n):
#     ox_list = list(input())
#     score = 0
#     sum_score = 0
#     for ox in ox_list:
#         if ox == "O":
#             score += 1  # O가 연속되면 1씩 커진다
#             sum_score += score
#         else:
#             score = 0  # X가 나오면 점수 리셋
#     print(sum_score)


# 4344 평균은 넘겠지
# c = int(input())
# for i in range(c):
#     cnt = 0
#     nums = list(map(int, input().split()))
#     n = nums[0]
#     sum_score = sum(nums[1:])
#     avg = sum_score/n
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1
#     rate = cnt/n * 100
#     print(f'{rate:.3f}%')


# 함수
# 15596 정수N개의 합
# def solve(a):
#     ans = 0
#     for i in range(0, len(a)):
#         ans += a[i]
#     return ans


# # 4673 셀프 넘버
# def d(n):  # 생성자 n을 통해 d(n)을 만들어주는 수식
#     n = n + sum(map(int, str(n)))
#     return n
# # 셀프 넘버가 아닌 수들(생성자가 있는 수들)이 들어갈 집합
# no_selfnum = set()
# for i in range(1, 10001):
#     no_selfnum.add(d(i))  # 집합에 넣어줌
# # 셀프넘버 출력하기
# for j in range(1, 10001):
#     if j not in no_selfnum:
#         print(j)


# 1065 한수
# 함수 사용 안함
# n = int(input())
# hansu = 0
# for i in range(1, n+1):
#     if i < 100:
#         hansu += 1
#     else:
#         n = list(map(int, str(i)))
#         if n[0] - n[1] == n[1] - n[2]:
#             hansu += 1
# print(hansu)

# 함수 사용함
# def hansu(n):
#     hansu_cnt = 0
#     for i in range(1, n+1):
#         if i < 100:
#             hansu_cnt += 1
#         else:
#             n = list(map(int, str(i)))
#             if n[0]-n[1] == n[1]-n[2]:
#                 hansu_cnt += 1
#     return hansu_cnt
# n = int(input()) #함수는 입력을 return 후에
# print(hansu(n)) #함수를 출력
