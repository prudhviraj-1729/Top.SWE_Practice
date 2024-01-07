# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from bisect import bisect_left

def jobScheduling(startTime, endTime, profit):

    jobs = sorted(list(zip(startTime, endTime, profit)))
    startTime = [i[0] for i in jobs]
    n = len(jobs)
    dp = [0] * (n + 1)
    for k in range(n-1,-1,-1):
        temp = bisect_left(startTime, jobs[k][1])
        dp[k] = max(jobs[k][2] + dp[temp], dp[k+1])
    return dp[0]
