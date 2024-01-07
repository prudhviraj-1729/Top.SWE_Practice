# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

from collections import Counter

def maxConsecutiveAnswers(answerKey, k):
    max_freq = i = 0
    char_count = Counter()

    for j in range(len(answerKey)):

        char_count[answerKey[j]] += 1
        max_freq = max(max_freq, char_count[answerKey[j]])

        if j - i + 1 > max_freq + k:
            char_count[answerKey[i]] -= 1
            i += 1

    return len(answerKey) - i