print("Enter two strings and I'll tell you if they are anagrams: ")

potential_anagram_1 = str(input("Enter the first string: "))
potential_anagram_2 = str(input("Enter the second string: "))
def isAnagram(x,y):
    x = x.replace(" ", " ").lower()
    y = y.replace(" ", " ").lower()
    return sorted(x) == sorted(y)
#potential_anagram_1 = potential_anagram_1.replace(" ", " ").lower()
#potential_anagram_2 = potential_anagram_2.replace(" ", " " ).lower()

print("Are the 2 strings entered anagrams? " +str(isAnagram(potential_anagram_2, potential_anagram_1))+ "!")