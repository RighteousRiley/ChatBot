import csv
ScriptName = "join_command"
Website = "https://www.twitch.tv/righteousriley_"
Description = "Join command for ThatGuy7"
Creator = "Riley Simpson"
Version = "1.0.0"

def Init():
    return

def Execute(data):
    if data.GetParam(0) != "!join":
        return
    csv_file = make_csv()
    add_users(csv_file,data)
    send_message(str(data.UserName) + " has joined The Cool Kids Club")
    return

def Tick():
    return

def send_message(message):
    Parent.SendStreamMessage(message)
    return

def is_user_present(data):
    username = data.UserName
    file = open("party_users.csv", "r")
    for row in file.readlines().split(","):
        if row[0] == username:
            return True
    return False

def make_csv():
    csv_file = open("party_users.csv", "a")
    return csv_file

def add_users(file, data):
    csv_writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([data.UserName, 0])
    file.close()
    return
