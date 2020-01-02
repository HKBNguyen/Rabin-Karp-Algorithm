#!/usr/bin/python3

def search(text: str, pattern: str, prime=10007) -> int:
    """ Simple implementation of the Rabin-Karp Algorithm to search for a pattern within text. 
    Parameters:
    text: str -- The actual text we're looking through. Assume text has length n.
    pattern: str -- The pattern we're looking for. Assume pattern has length m.
    prime=10007 -- We need a prime number to mod all of our hashes to avoid both integer overflow and hash collisions. Default is 10007, but can be overriden.
    
    Return Value:
    pos: int -- position of the the matching string. Will return -1 if doesn't exist, and a positive integer otherwise.]


    The hash function used works as follows:
    1) Multiply by the ASCII character set. (We're making the assumption that all of the input text characters must be in the ASCII set, change otherwise).
    2) Add to the ASCII of the current character.
    3) Mod by the prime number in order to avoid overflow.

    This is similar to Rabin's Fingerprint.
    """
    charMax = 256
    patternLen = len(pattern)
    textLen = len(text)
    patternHash = 0
    currWindowHash = 0
    divisionFactor = 1
    
    # This is the value used to remove the first character in window we're currently looking at. We need to multiply by charMax to the patternLen - 1 times.
    for index in range(patternLen - 1):
        #print("Division Factor error")
        divisionFactor = (divisionFactor*charMax) % prime

    for letter in range(patternLen):
        print("Calculating hash values...")
        patternHash = (charMax*patternHash + ord(pattern[letter])) % prime
        currWindowHash = (charMax*currWindowHash + ord(text[letter])) % prime

    for index in range(textLen - patternLen + 1):
        if currWindowHash == patternHash:
            print("Potential hash found...Checking if string is correct...")
            if text[index:index+patternLen] == pattern:
                print("Pattern found!")
                return index
        # Find the next window to calculate hash for
        if index < textLen - patternLen:
            # Remove the first character and add the next character in text
            currWindowHash = (charMax*(currWindowHash - ord(text[index])*divisionFactor) + ord(text[index+patternLen])) % prime
            if currWindowHash < 0:
                currWindowHash += prime
    print("No pattern was found...")
    return -1

if __name__ == '__main__':
    text = "ABAAABCDBBABCDDEBCABC"
    pattern = "ABC"
    print(search(text, pattern))

                    





        

        
