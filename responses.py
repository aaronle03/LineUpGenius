def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'sunset':
        return "Sunset map"
    
    if p_message == 'lotus':
        return "Lotus map"
    
    if p_message == 'pearl':
        return "Pearl map"
    
    if p_message == 'fracture':
        return "Fracture map"
    
    if p_message == 'breeze':
        return "Breeze map"
    
    if p_message == 'icebox':
        return "Icebox map"
    
    if p_message == 'bind':
        return "Bind map"
    
    if p_message == 'haven':
        return "Haven map"
    
    if p_message == 'split':
        return "Split map"
    
    if p_message == 'ascent':
        return "Ascent map"
    
    if p_message == 'help':
        return "`This is a help message!`"
    
    if p_message == 'bad_message':
        return "You didn't enter a valid command. Type !help if you need help!"