import sys

def solve(teamA, teamB):
    global result
    if len(teamA) == n // 2:
        stat_teamA = 0
        stat_teamB = 0
        for i in range(n // 2):
            for j in range(n // 2):
                stat_teamA += stat[teamA[i]][teamA[j]]
                stat_teamB += stat[teamB[i]][teamB[j]]
        result = min(result, abs(stat_teamA - stat_teamB))
        return

    last_member = teamA[-1] + 1 if teamA else 0
    for i in range(last_member, n):
        solve(teamA + [i], teamB)
        solve(teamA, teamB + [i])

n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
result = sys.maxsize

solve([], [])
print(result)

