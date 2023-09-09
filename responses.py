from server import *

def handle_map(mapName, characterName) -> list:
    gif_links = get_gif(mapName, characterName)
    return gif_links

def handle_response(message) -> list:
    p_message = message.lower()
    myList = p_message.split()

    if p_message == 'help':
        return "`!help - Shows all commands\n!mapName characterName - Type a map name then a character name (i.e. !ascent brimstone)`"
    
    if p_message == 'ben':
        return "https://www.youtube.com/watch?v=1hGcAUVfVZ8"

    if len(myList) == 2:
        if myList[1] in ['brimstone', 'viper', 'killjoy', 'sova']:
            return handle_map(myList[0], myList[1])
        else:
            return ["You didn't enter a valid command. Type !help for the list of commands!"]

    else:
        if p_message == 'bad_message':
            return "You didn't enter a valid command. Type !help for the list of commands!"