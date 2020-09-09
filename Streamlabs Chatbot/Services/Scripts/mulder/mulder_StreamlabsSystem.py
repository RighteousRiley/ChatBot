import random
ScriptName = "Mulder"
Website = "https://www.twitch.tv/righteousriley_"
Description = "First Bot Script GaMeRz"
Creator = "Yuh Boi Riley"
Version = "1.0.0"

def Init():
    return

def Execute(data):
    if data.GetParam(0) != "!alien":
        return
    username = data.UserName
    if is_alien():
        send_message("You are an alien!")
    else:
        send_message("You are not an alien!")
    return

def Tick():
    return

def is_alien():
    alien_probability = 20
    chance_int = Parent.GetRandom(0,100)
    return chance_int <= alien_probability

def send_message(message):
    Parent.SendStreamMessage(message)
    return