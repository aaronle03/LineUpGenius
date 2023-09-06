import discord
import responses
from credentials import *

intents = discord.Intents.all()
intents.typing = False
intents.messages = True

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = TOKEN_KEY
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        brim = 0
        viper = 0
        sova = 0
        killjoy = 0

        print(f"{username} said '{user_message}' ({channel})")

        if user_message and user_message[0] == '?':
            user_message = user_message[1:]
            #print("Sending private message")
            await send_message(message, user_message, is_private=True)
        elif user_message and user_message[0] == '!':
            user_message = user_message[1:]
            #print("Sending public message2")
            await send_message(message, user_message, is_private=False)
        else:
            user_message = "bad_message"
            #print("Bad Message")
            await send_message(message, user_message, is_private=False)
    
    client.run(TOKEN)