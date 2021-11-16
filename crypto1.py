######################################################
#   Intro to Cybersecurity
#   Crypto Lab 1,  crypto1.py
#
#   Praneetha Kishore Kumar
#
#   This is a brute force against a caeser cipher
#   all upper and lower case letter are shifted
#   26 times in a loop, decremeting each time.
#   The output is sent to the screen as well as written
#   to a file.
#
#######################################################

def decrypt(cipher):
    #
    #   Your solution goes here
    #

    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher=cipher.upper()
    
    
    for k in range(len(alphabets)):
        cracker=""
        for _ in cipher:
            if _ in alphabets: 
                i = (alphabets.find(_)-k) % len(alphabets)

                cracker = cracker + alphabets[i]
                
            else:
                cracker = cracker+_
        print(k)
        print(cracker)


    
        with open("cryptans.txt","a") as file:
            file.write(cracker)
    return cracker

def main():
    
    with open("cyrpto1.txt", "r") as file2:
        cipher = file2.read()

    decrypt(cipher)

    print ("\nScroll through the results, it's easy to the correct cipher\n")
    print ("These results have been saved to 'Crypto1-solution.txt'\n")

if __name__ == '__main__':
    main()
