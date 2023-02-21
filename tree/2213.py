import sys
input = sys.stdin.readline
##################################################
n = int(input())

input_data = [list(input().split()) for _ in range(n)]

ant_tunnel = [{} for _ in range(n)]

