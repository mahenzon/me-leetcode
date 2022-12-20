class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        seen = {}
        freq = [[] for _ in range(len(words) + 1)]
        for word in words:
            if word in seen:
                seen[word] += 1
            else:
                seen[word] = 1

        for word, count in seen.items():
            freq[count].append(word)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            f_words = freq[i]
            f_words.sort()
            for word in f_words:
                result.append(word)
                if len(result) == k:
                    return result
