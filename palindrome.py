import sys
import math
def pal(text):
    return text == text[::-1]
if __name__ == "__main__":
    if len(sys.argv)==2:
       
        text = sys.argv[1]
    else:
       
        text = "madam"
        print(f"Palindrome: {pal(text)}")
