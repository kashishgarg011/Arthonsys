#12. Check if a string is a pangram (contains all letters of the alphabet).
def ispangram(str):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
string='pack my box with five dozen liquor jugs'
if (ispangram(string)==True):
    print('Yes')
else:
    print('No')