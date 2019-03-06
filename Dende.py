import discord
import json
from discord import Game
from discord.ext import commands
import random
import asyncio
import datetime, time

with open('config.json') as f:
    data = json.load(f)

TOKEN = data["token"]
BOT_PREFIX = data["prefix"]

bot = commands.Bot(command_prefix=BOT_PREFIX)
start_time = time.time()

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
    if context.message.channel.name != 'role-requests':
        return

    valid_roles = ['Sync\'d with Nail', 'Ma Junior',
                    'NA', 'EU', 'Steam', 'PS4', 'Xbone']
    entered_role = context.message.content.split(' ', 1)[1]
    member = context.message.author
    role = discord.utils.get(context.message.server.roles, name=entered_role)

    if role == None or role.name not in valid_roles:
        msg = await bot.send_message(context.message.channel, "Invalid Role {0.message.author.mention}, roles you are able to add are: \n`\"Ma Junior\", \"Sync\'d with Nail\", \"NA\", \"EU\", \"Steam\", \"PS4\", \"Xbone\"`".format(context))
    else:
        await bot.add_roles(member, role)
        msg = await bot.send_message(context.message.channel, 'I\'ve given {0.message.author.mention} the role **{1.name}**'.format(context, role))

    await asyncio.sleep(10)
    await bot.delete_message(msg)
    await bot.delete_message(context.message)
#--------------------------------------------------#

@bot.command(name='removerole',
            aliases=['Removerole', 'RemoveRole', 'removeRole','Rm', 'rm', 'rM', 'remove'],
            pass_context=True)
async def removerole(context):
    if context.message.channel.name != 'role-requests':
        return

    entered_role = context.message.content.split(' ', 1)[1]
    member = context.message.author
    role = discord.utils.get(context.message.server.roles, name=entered_role)

    if role == None:
        msg = await bot.send_message(context.message.channel, "Invalid Role {0.message.author.mention}, roles avaiable to remove are: \n'\"Ma Junior\" \"Sync\'d with Nail\", \"NA\", \"EU\", \"Steam\", \"PS4\", \"Xbone\"'".format(context))
    elif role not in context.message.author.roles:
        msg = await bot.send_message(context.message.channel, "{0.message.author.mention} You do not have this role.".format(context))
    else:
        await bot.remove_roles(member, role)
        msg = await bot.send_message(context.message.channel, 'I\'ve removed the role **{0.name}** from {1.message.author.mention} '.format(role, context))

    await asyncio.sleep(10)
    await bot.delete_message(msg)
    await bot.delete_message(context.message)

#----------------------------------------------#
# Kill command for the bot.
@bot.command(name='stop',
            pass_context=True)
async def stop(context):

    m = context.message.author
    if m.server_permissions.administrator or "Fused With Kami" in m.roles:
        await bot.close()
    else:
        return
#---------------------------------------------#

@bot.command(name='uptime',
            description='Gives the current uptime of the bot as Hour/Min/Sec',
            brief='Curent uptime of Dende',
            aliases=['up', 'Uptime', 'Up'])
async def uptime():
    current_time = time.time()
    uptime = int(round(current_time - start_time))
    await bot.say("Uptime: {}".format(str(datetime.timedelta(seconds=uptime))))

#-------------------------------------------------------------#

@bot.command(name='source',
            description='Source code for Dende',
            brief='Source code for Dende',
            aliases=['sc', 'sourcecode'])
async def source():

    await bot.say("You want to see my source code? Anything for you Gohan :wink: https://github.com/crewsz96/Dende_Bot")

#-------------------------------------------------------------#

bot.run(TOKEN)
