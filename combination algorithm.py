"""
<코드의 동작 원리>

- 종료 조건
1) r이 0이 되면 더 이상 선택할 원소가 없다.
2) 배열이 비었는데 r이 0보다 큰 경우, 더 이상 선택할 원소가 없다.

- 작동
head = arr[0] 첫번째 원소
tail = arr[1:] 나머지 원소들

(ex) arr = ['a', 'b', 'c'], r = 2
첫번째 호출 = [a] + combinations([b,c],1)/combinations([b,c],2)
두번째 호출에서 [b], [c] 획득
결과 합치기로 a,b/a,c 획득

"""
def combinations(arr, r):
    # 종료 조건: r이 0이 되면 더 이상 선택할 필요가 없으므로 빈 리스트를 반환
    if r == 0:
        return [[]]

    # 배열이 비었는데 선택해야 할 원소가 남아 있으면 더 이상 조합을 구할 수 없음
    if len(arr) == 0:
        return []

    # 첫 번째 원소(head)를 포함하는 조합과 포함하지 않는 조합으로 나눠서 재귀 호출
    head = arr[0]  # 첫 번째 원소
    tail = arr[1:]  # 나머지 원소

    # head를 포함한 조합을 구함
    comb_with_head = [[head] + c for c in combinations(tail, r - 1)]

    # head를 포함하지 않은 조합을 구함
    comb_without_head = combinations(tail, r)

    # 두 경우의 결과를 합쳐서 반환
    return comb_with_head + comb_without_head

