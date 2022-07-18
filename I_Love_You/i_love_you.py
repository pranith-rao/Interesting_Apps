import pyttsx3

girlfriend = pyttsx3.init()
voices = girlfriend.getProperty('voices')
girlfriend.setProperty('voice',voices[1].id)
girlfriend.say('I love you')
girlfriend.runAndWait()

