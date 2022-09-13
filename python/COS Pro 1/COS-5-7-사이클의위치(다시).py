def find(parent, u):
	if u == parent[u]:
		return u
	parent[u] = find(parent, parent[u])
	return parent[u]

def merge(parent, u, v):
	u = find(parent, u)
	v = find(parent, v)
	if u == v:
		return True
	parent[u] = v
	return False

def solution(n, connections):
    answer = 0
    parent = [i for i in range(n+1)]
    for i, connection in enumerate(connections):
        if merge(parent, connection[0], connection[1]):
            answer = i + 1
            break
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 3
connections = [[1, 2], [1, 3], [2, 3]]
ret = solution(n, connections)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")