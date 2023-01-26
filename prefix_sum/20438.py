import sys
import heapq
input = sys.stdin.readline
###########################################
# 입력데이터 정보 받아오기
n, k, q, m = map(int, input().split())

# 자는 학생 저장하기
# n+2까지 숫자가 index로 들어가야 하므로 길이는 n+3
sleep = [False for _ in range(n+3)]
for i in map(int, input().split()):
    sleep[i] = True

# 출석부르는 학생들 작은 수 부터 부르기 위한 heappush
call = []
for i in map(int, input().split()):
    heapq.heappush(call, i)

# 출석을 불렀는지 저장하는 리스트
check_call = [[False for _ in range(n+3)]]

# 출석이 불려서 자신의 배수인 학생을 호출 했는지 저장하는 리스트
call_list = [False for _ in range(n+3)]

# 더이상 불러야할 학생이 없을 때까지 반복
while call:
    # 불러야하는 학생중 가장 작은번호를 호출 시작함
    call_num = heapq.pop(call)

    # 이미 호출해서 다른사람을 부른 사람이면 안함
    if call_list[call_num]:
        continue







