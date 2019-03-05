import discord
import json
from discord import Game
from discord.ext import commands
import random
import asyncio

with open('config.json') as f:
    data = json.load(f)

TOKEN = data["token"]
BOT_PREFIX = data["prefix"]

bot = commands.Bot(command_prefix=BOT_PREFIX)

#-----------------------------------------------#
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')
    await bot.change_presence(game=Game(name="Guarding Earth"))


#----------------------------------------------#
@bot.command(name='hook',
            descripton='Answers the gang.',
            aliases=['Hook'],
            pass_context=True)
async def hook(context):


    await bot.say("***GANG GAWD***")
#----------------------------------------------#

@bot.command(name='lilgreen',
            aliases=['LilGreen', 'Lilgreen'],
            pass_context=True)
async def lilgreen(context):


    await bot.say("My name is **Dende**")

#----------------------------------------------#
@bot.command(name='addrole',
            aliases=['add', 'addRole', 'AddRole', 'Add'],
            pass_context=True)
async def addrole(context):
    if context.message.channel.name != 'role-request':
        return

    valid_roles = ['Sync\'d with Nail', 'Ma Junior',
                    'NA', 'EU', 'Steam', 'PS4', 'Xbone']
    entered_role = context.message.content.split(' ', 1)[1]
    member = context.message.author
    role = discord.utils.get(context.message.server.roles, name=entered_role)

    if role == None or role.name not in valid_roles:
        await bot.say("Invalid Role, roles you are able to add are: \"Ma Junior\", \"Sync\'d with Nail\", \"NA\", \"EU\", \"Steam\", \"PS4\", \"Xbone\"")
        return

    await bot.add_roles(member, role)

    msg = 'I\'ve given {0.message.author.mention} the role **{1.name}**'.format(context, role)
    msg = await bot.say(msg)

    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(context.message)
#--------------------------------------------------#

@bot.command(name='removerole',
            aliases=['Removerole', 'RemoveRole', 'removeRole','Rm', 'rm', 'rM', 'remove'],
            pass_context=True)
async def removerole(context):
    if context.message.channel.name != 'role-request':
        return

    entered_role = context.message.content.split(' ', 1)[1]
    member = context.message.author
    role = discord.utils.get(context.message.server.roles, name=entered_role)

    if role == None:
        await bot.say("Invalid Role, roles avaiable to remove are: \"Ma Junior\" \"Sync\'d with Nail\", \"NA\", \"EU\", \"Steam\", \"PS4\", \"Xbone\"")
        return

    if role not in context.message.author.roles:
        await bot.say("You do not have this role.")
        return

    await bot.remove_roles(member, role)

    msg = 'I\'ve removed the role **{0.name}** from {1.message.author.mention} '.format(role, context)
    msg = await bot.say(msg)

    await asyncio.sleep(3)
    await bot.delete_message(msg)
    await bot.delete_message(context.message)

#--------------------------------------------------#




#--------------------------------------------------#

bot.run(TOKEN)
