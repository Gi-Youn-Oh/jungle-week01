# import sys

# N = int(input()) #도시의 수

# start, next, value, visited

# min_value

# route_list = [list(map(int,input().split)) for i in range(N)] # 리스트를 만드는데 도시의 수 만큼 받는다.
# route = route_list[루트리스트중 인덱스 하나 는 도시]
# # if route_list[][] != 0 : #루트 리스트 안의 이동비용이 0이 아니면
#     #루트 총비용을 최소값과 비교해서 작은 것을 최소값으로 돌려준다.

    

# def dfs_backtracking(start, next, value, visited): #시작도시번호,다음도시번호,비용,방문 도시
#     global min_value

#     if len(visited) == N: #만약 방문한 도시가 입력받은 도시의 개수라면
#         if travel_cost[next][start] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
#             min_value = min(min_value, value + travel_cost[next][start]) #더한 값을 저장되어있는 최소값과 비교해서 대입
#         return
#     for i in range(N): #도시의 개수 만큼 반복문을 돈다.
#         #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
#         if travel_cost[next][i] != 0 and i not in visited and value < min_value: 
#             visited.append(i) #그 도시를 방문목록에 추가
#             dfs_backtracking(start, i, value + travel_cost[next][i], visited) #그 도시를 방문한다.
#             visited.pop() #방문을 완료했다면 방문목록 해제