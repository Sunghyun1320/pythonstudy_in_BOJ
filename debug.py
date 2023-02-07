import sys
input_ = sys.stdin.readline
S = int(input_())
tops = list(map(int,input_().split()))  # 탑들 받는 거
stack = []                              # 스택을 이용할 건데 먼저 제일 오른쪽 탑의 높이를 넣는다
stack_num = []                          # 그리고 탑들의 위치를 기록해놓은 stack_num
top = -1                                # 스택 제일 위쪽에 있는 탑의 위치(현재는 없으니 -1)
line = [0]*(S)                          # 결과를 담을 리스트 default는 0
for i in range(S-1,-1,-1):              # 제일 왼쪽 것은 담았기 때문에 하나 줄여서 시작
    # if tops[i] > stack[top]:
        while top >= 0:                 # 그리고 스택의 높이가 0이상일때
            if tops[i] > stack[top]:    # 스택을 하나씩 제거 해가면서 i번째 탑의 높이가 stack 제일 위에 있는 탑의 높이보다 클 경우
                stack.pop()             #하나씩 빼고
                a = stack_num.pop()     #또 그 전에 있던 탑의 위치 빼고
                line[a] = i+1           #그 위치에다가 i+1 을 저장
                top -= 1                #그리고 스택의 높이도 하나 빼고
            else:
                break
        stack.append(tops[i])           #위의 while문이 끝나면 i번째 탑과 탑위 위치를 각각 저장, 그리고 스택의 높이도 +1
        stack_num.append(i)
        top += 1
    # else:
    #     stack.append(tops[i])
    #     stack_num.append(i)
    #     top += 1
for i in range(S-1):
    print(line[i], end = " ")
print(line[S-1])