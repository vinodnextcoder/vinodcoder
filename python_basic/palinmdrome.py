def is_palindrome(s) :
    if s[::-1] == s:
        return True
    return False

S = raw_input("String: ")
if is_palindrome(S):
    print("Results:\n   " +S + " is a palindrome string.")
else:
    print("Results:\n   " + S + " is not a palindrome string.")
