from datetime import datetime
import pyttsx3 

#dictionary of time and its value
remind_me_string = {
    "07:30": "Breakfast",
	  "12:00": "Lunch",
    "17:00": "Dinner"
}

while (True): #load all the items in remind_me_string
    #format date - timestr to match with the time specified in remind_me_string
    timestr = datetime.now().strftime("%H:%M")
    #get all the items of remind_me_string
    for time,value in remind_me_string.items():
       #identify any match/es
        if time==timestr:
            #if there's a match, a voice will speak the value of remind_me_string 
            speak = pyttsx3.init() 
            voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0" #set female voice -> ZIRA
            speak.setProperty('voice', voice_id)
            speak.setProperty('rate', 180)
            speak.setProperty('volume', 1.0)
            speak.say(y) 
            speak.runAndWait()

#You can exit the program by CTRL + C 
