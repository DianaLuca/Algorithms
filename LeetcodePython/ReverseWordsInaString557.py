# Given a string, you need to reverse the order of characters in each word within a sentence
#  while still preserving whitespace and initial word order.

def reverseWords(s):
    words = s.split(" ")
    result = ""

    for el in words:
        el = el[::-1]
        result += el + " "
    return result[:len(result)-1]  # subtract the ending white space

