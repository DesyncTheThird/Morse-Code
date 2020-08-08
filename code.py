import string
import random
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
flag=True
while flag==True:
    letter=random.choice(string.ascii_lowercase+".,?:/z\"\';")
    print(letter)
    code=input(">>> ")
    if code==morse[letter][0]:
        print("Correct!")
    else:
        print("Incorrect. Code is; ["+morse[letter][0]+"]")
        print("Mnemonic; "+morse[letter][1])
    if code=="stop":
        flag=False
