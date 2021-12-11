def solution(n, d):
    if d <= 0:
        return []
    elif d >= len(str(n)):
        return [int(i) for i in str(n)]

    else:
        return [int(i) for i in str(n)][-d:]
