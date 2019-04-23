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
    await bot.change_presence(activity=Game(name="Guarding Earth"))


#----------------------------------------------#
@bot.command(name='hook',
            descripton='Answers the gang.',
            aliases=['Hook'])
async def hook(ctx):

    await ctx.send("***GANG GAWD***")
#----------------------------------------------#

@bot.command(name='lilgreen',
            aliases=['LilGreen', 'Lilgreen'])
async def lilgreen(ctx):

    await ctx.send("My name is **Dende**")

#----------------------------------------------#
@bot.command(name='addrole',
            aliases=['add', 'addRole', 'AddRole', 'Add'])
async def addrole(ctx):
    if ctx.channel.name != 'role-requests':
        return

    valid_roles = ['Sync\'d with Nail', 'Ma Junior',
                    'NA', 'EU', 'Steam', 'PS4', 'Xbone']
    msg = ctx.message
    entered_role = ctx.message.content.split(' ', 1)[1]
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name=entered_role)

    if role == None or role.name not in valid_roles:
        bot_msg = await ctx.send("Invalid Role {0.message.author.mention}, roles you are able to add are: \n`\"Ma Junior\", \"Sync\'d with Nail\", \"NA\", \"EU\", \"Steam\", \"PS4\", \"Xbone\"`".format(ctx))
    else:
        await member.add_roles(role)
        bot_msg = await ctx.send('I\'ve given {0.message.author.mention} the role **{1.name}**'.format(ctx, role))

    await asyncio.sleep(10)
    await msg.delete()
    await bot_msg.delete()
#--------------------------------------------------#

@bot.command(name='removerole',
            aliases=['Removerole', 'RemoveRole', 'removeRole','Rm', 'rm', 'rM', 'remove'])
async def removerole(ctx):
    if ctx.channel.name != 'role-requests':
        return

    msg = ctx.message
    entered_role = ctx.message.content.split(' ', 1)[1]
    member = ctx.author
    role = discord.utils.get(ctx.guild.roles, name=entered_role)

    if role == None:
        bot_msg = await ctx.send("Invalid Role {0.message.author.mention}, roles avaiable to remove are: \n`\"Ma Junior\" \"Sync\'d with Nail\", \"NA\", \"EU\", \"Steam\", \"PS4\", \"Xbone\"`".format(ctx))
    elif role not in ctx.author.roles:
        bot_msg = await ctx.send("{0.message.author.mention} You do not have this role.".format(ctx))
    else:
        await member.remove_roles(role)
        bot_msg = await ctx.send('I\'ve removed the role **{0.name}** from {1.message.author.mention} '.format(role, ctx))

    await asyncio.sleep(10)
    await msg.delete()
    await bot_msg.delete()

#----------------------------------------------#
# Kill command for the bot.
@bot.command(name='stop')
async def stop(ctx):

    role = discord.utils.get(ctx.guild.roles, name="Fused With Kami")
    if m.guild_permissions.administrator or role in ctx.author.roles:
        await bot.close()
    else:
        return
#---------------------------------------------#

@bot.command(name='uptime',
            description='Gives the current uptime of the bot as Hour/Min/Sec',
            brief='Curent uptime of Dende',
            aliases=['up', 'Uptime', 'Up'])
async def uptime(ctx):

    current_time = time.time()
    uptime = int(round(current_time - start_time))
    await ctx.send("Uptime: {}".format(str(datetime.timedelta(seconds=uptime))))

#-------------------------------------------------------------#

@bot.command(name='source',
            description='Source code for Dende',
            brief='Source code for Dende',
            aliases=['sc', 'sourcecode'])
async def source(ctx):

    await ctx.send("You want to see my source code? Anything for you Gohan :wink: https://github.com/crewsz96/Dende_Bot")

#-------------------------------------------------------------#

bot.run(TOKEN)
