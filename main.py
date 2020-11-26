import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    global channel
    print(f'> Logged in as: {client.user}')
    print('-----READY----- \n')
    channel = client.get_channel(int(input("> Enter the channel you wish to send messages in: ")))
    await console_input()
    

@client.event
async def console_input():
    global channel
    await client.wait_until_ready()
    msg = input('> Message to send: ')
    await channel.send(msg)
    print('')
    await console_input()


client.run(config.token)
