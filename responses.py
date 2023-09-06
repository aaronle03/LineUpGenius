from server import *

def handle_map(mapName, characterName) -> str:
    gif_link = get_gif(mapName, characterName)
    gif_strings = list(gif_link)
    if gif_strings:
        return "\n".join(gif_strings)
    else:
        return "No matching items found"

def handle_response(message) -> str:
    p_message = message.lower()
    myList = p_message.split()

    if p_message == 'help':
        return "`!help - Shows all commands\n!mapName characterName - Type a map name then a character name (i.e. !ascent brimstone)`"
    
    if p_message == 'ben':
        return ""

    if(len(myList) == 2):
        if(myList[1] == 'brimstone'):
            word = handle_map(myList[0], myList[1])
            return word
        elif(myList[1] == 'viper'):
            return handle_map(myList[0], myList[1])
        elif(myList[1] == 'killjoy'):
            return handle_map(myList[0], myList[1])
        elif(myList[1] == 'sova'):
            return handle_map(myList[0], myList[1])
        else:
            return "You didn't enter a valid command. Type !help for the list of commands!"

    else:
        if p_message == 'bad_message':
            return "You didn't enter a valid command. Type !help for the list of commands!"