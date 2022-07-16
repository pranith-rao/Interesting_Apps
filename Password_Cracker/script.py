import random, pyautogui
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$"           #characters used to compose a password
chars_list = list(chars)                                     #converted to list so that each letter can be used to compare

password = pyautogui.password("Enter a password: ")          #pops up a window to enter the password  to be guessed
guess_password = ""                                          

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))    #chooses the letters from chars_list to form a password of the same length as the one entered by you
    print("<----------"+str(guess_password)+"---------->")          #prints all the automatically guessed input 
    if(guess_password == list(password)):
        print("Your password is :"+ "".join(guess_password))        #if matches the guessed correct password is printed
        break