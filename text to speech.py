import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty("rate")

engine.setProperty("rate",150)

volume = engine.getProperty("volume")
print("volume is {0}".format(volume))

engine.setProperty("volume",1)

voices = engine.getProperty("voices")

print("male voice : {0}".format(voices[0].id))
print("female voice : {0}".format(voices[1].id))


engine.setProperty("voice",voices[0].id)

engine.say("hi my name is hazard! how are you bro")
print("file is running")

engine.runAndWait()
engine.stop()