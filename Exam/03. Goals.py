def best_sequence(goals):
    dp = [1] * len(goals)
    previous = [-1] * len(goals)

    for i in range(1, len(goals)):
        for j in range(i):
            if goals[j] < goals[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                previous[i] = j
            elif goals[j] == goals[i] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1
                previous[i] = j

    max_length = max(dp)
    index = dp.index(max_length)

    sequence = []
    while index != -1:
        sequence.append(goals[index])
        index = previous[index]

    sequence.reverse()
    print(*sequence, sep=' ')


goals = [int(x) for x in input().split(', ')]

best_sequence(goals)
