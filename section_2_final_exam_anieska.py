'''Section 2:
2.1 a Coding Questions [24 points] Answer'''
def count_unique_consonants(string):
    vowels = "aeiou"
    consonants = set()
    for char in string.lower():
        if char.isalpha() and char not in vowels:
            consonants.add(char)
    return len(consonants)


print(count_unique_consonants("cat"))
print(count_unique_consonants("cataract"))


'''2.B Answer

**Time Complexity: O(n), where n is the length of the string 
(because we go through each character once).
Space Complexity: O(c), where c is the number of unique consonants (the size of the set).'''

'''2.2 Non-recursive solution:'''

def count_squares(x):
    return sum(i**2 for i in range(1, x + 1))


print(count_squares(2))
print(count_squares(3))

''' recursive solution'''
def count_squares_recursive(x):
    if x == 1:
        return 1
    return x**2 + count_squares_recursive(x - 1)

print(count_squares_recursive(2))
print(count_squares_recursive(3))

'''Section 3: Theory Challenge - answer '''
'''3.1'''
def hash_function(key, size):
    return sum(ord(char) for char in key) % size

''' 3.2 answer
For a hash table of size 10:
***Input: "cat"
***ASCII sum: c=99, a=97, t=116 → Total = 312
***Hash: 312 % 10 = 2
*** The value is stored at index 2.'''

'''3.3 answer
For a hash table of size 10:
***Input 1: "bat" → Hash = 2
***Input 2: "cat" → Hash = 2
***B oth values are stored at index 2 using chaining (e.g., in a list).'''