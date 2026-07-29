'''
Variable sliding window Problems:
Array based:
209. Minimum Size Subarray Sum
713. Subarray product less than K
904. Fruit Into Baskets

Longest substring based:
3. Longest Substring Without Repeating Characters
424. Longest Repeating Character Replacement
'''
from typing import List
def totalFruit(fruits: List[int]) -> int:
    left,ans = 0,0
    freq = {}
    for right in range(len(fruits)):
        freq[fruits[right]] = freq.get(fruits[right],0) + 1
        while len(freq) > 2:
            freq[fruits[left]] -= 1
            if freq[fruits[left]] == 0:
                del freq[fruits[left]]
            left += 1
        ans = max(ans,right-left+1)
    return ans
fruits = [1,2,3,2,2]
print(totalFruit(fruits))

def lengthOfLongestSubstring(s: str) -> int:
    left,ans = 0,0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        ans = max(ans,right - left + 1)
    return ans

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("abcabcbb"))

