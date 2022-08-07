import string
import random
import winsound

morse={
    "a":(".-","a-PART"),
    "b":("-...","BOOT to the head"),
    "c":("-.-.","CO-ca CO-la"),
    "d":("-..","DAN-ger-ous"),
    "e":(".","eh"),
    "f":("..-.","fen-e-STRA-tion"),
    "g":("--.","GOOD GRA-vy"),
    "h":("....","hip-pi-ty hop"),
    "i":("..","aye-aye"),
    "j":(".---","let's JUMP JUMP JUMP"),
    "k":("-.-","KAN-a-ROO"),
    "l":(".-..","to 'ELL with it"),
    "m":("--","MMMM-MMMM"),
    "n":("-.","NA-vy"),
    "o":("---","ONE OF US"),
    "p":(".--.","a PIZ-ZA pie"),
    "q":("--.-","GOD SAVE the QUEEN"),
    "r":(".-.","ro-TA-tion"),
    "s":("...","si si si"),
    "t":("-","TALL"),
    "u":("..-","un-der WHERE?"),
    "v":("...-","beet-ho-ven's FIFTH"),
    "w":(".--","a WHITE WHALE"),
    "x":("-..-","X marks the SPOT"),
    "y":("-.--","YEL-low YO-YO"),
    "z":("--..","ZINC ZOO-keep-er"),
    ".":(".-.-.-","a STOP, a STOP, a STOP"),
    ",":("--..--","COM-MA, it's a COM-MA"),
    "?":("..--..", "it's a QUES-TION, is it?"),
    ":":("---...","HA-WA-II stan-dard time"),
    "/":("-..-.","SHAVE and a HAIR-cut"),
    "\"":(".-..-.","six-TY-six nine-TY-nine"),
    "\'":(".----.","and THIS STUFF GOES TO me!"),
    ";":("-.-.-.","A-list; B-list; C-list"),
}


while True:
    print("===============")
    print("Modes:")
    print("[0] Sending")
    print("[1] Receiving (Text)")
    print("[2] Receiving (Sound)")
    mode=input(">>> ")
    if mode=="0":
        print("Enter \"menu\" to return to mode selection menu.")
        while True:
            letter=random.choice(string.ascii_lowercase+".,?:/z\"\';")
            print(letter)
            code=input(">>> ")
            if code=="menu":
                break
            if code==morse[letter][0]:
                print("Correct!")
            else:
                print("Incorrect. Code is; ["+morse[letter][0]+"]")
                print("Mnemonic; "+morse[letter][1])
    if mode=="1":
        print("Enter \"menu\" to return to mode selection menu.")
        while True:
            letter=random.choice(string.ascii_lowercase+".,?:/z\"\';")
            print(str(morse[letter][0]))
            code=input(">>> ")
            if code=="menu":
                break
            if code==letter:
                print("Correct!")
            else:
                print("Incorrect. Letter is; ["+letter+"]")
                print("Mnemonic; "+morse[letter][1])
    if mode=="2":
        frequency=750
        while True:
            print("===============")
            print("Speed Settings:")
            print("[0] Slow")
            print("[1] Moderate")
            print("[2] Fast")
            print("[3] Hyper")
            speed=input(">>> ")
            if speed=="0":
                dit=200
                dah=400
                break
            if speed=="1":
                dit=150
                dah=300
                break
            if speed=="2":
                dit=100
                dah=200
                break
            if speed=="3":
                dit=60
                dah=120
                break
            else:
                print("\nPlease enter 0, 1, 2, or 3.\n")
                continue
        print("Enter \"menu\" to return to mode selection menu.")
        print("Enter \"repeat\" to replay sound.")
        print("Enter \"hint\" to display sound as text.")
        flag=True
        while flag==True:
            letter=random.choice(string.ascii_lowercase+".,?:/z\"\';")
            for char in morse[letter][0]:
                if char==".":
                    winsound.Beep(frequency, dit)
                if char=="-":
                    winsound.Beep(frequency, dah)
            while flag==True:
                code=input(">>> ")
                if code=="repeat":
                    for char in morse[letter][0]:
                        if char==".":
                            winsound.Beep(frequency, dit)
                        if char=="-":
                            winsound.Beep(frequency, dah)
                    continue
                if code=="hint":
                    print("Code is; ["+morse[letter][0]+"]")
                    continue
                if code=="menu":
                    flag=False
                if code==letter:
                    print("Correct!")
                    break
                else:
                    print("Incorrect. Code is; ["+morse[letter][0]+"]")
                    print("Letter is; ["+letter+"]")
                    print("Mnemonic; "+morse[letter][1])
                    break
    else:
        print("\nPlease enter 0, 1, or 2.\n")
        continue