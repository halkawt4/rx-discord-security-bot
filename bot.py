import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS

''''''

Client = discord.Client()
bot_prefix= "}"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='414089074870321153')
footer_text = "[Realm X] - [X Security]"

member_role = '453194601247801354'
bot1_role = '453194562379186176'
bot2_role = '453195460346380288'
owner_role = '453194638077984768'
partner_role = '453194705732239360'
lvl2_role = '453194792457732096'
lvl5_role = '453195170662449152'
lvl10_role = '453195184327491594'
lvl15_role = '453195194607861761'
lvl20_role = '453195205416321034'
lvl25_role = '453195220192854027'
lvl35_role = '453195231517474826'
lvl40_role = '453195258675855361'
lvl50_role = '453195292376825856'
vip_role = '453195303403913227'
legend_role = '453195358575656986'
punished_role = '453195421611982848'
helper_role = '453195469309476877'
mod_role = '453195518785486858'
admin_role = '453195993987416064'
manager_role = '453196026547929088'
hell_role = '453247719067090944'
nsfw_role = '453247786637590570'
partner2_role = '453247829855567872'
lvl0_role = '453653105696047105'
error_img = ':octagonal_sign:'
x_role = '453196094332076045'

''''''
# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("============================================================")
    print("X - SECURITY")
    print("============================================================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("============================================================")
    await client.change_presence(game=discord.Game(name='with the ban hammer.'))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("Ping: {}".format(round((t2-t1)*1000)))
    print("============================================================")
    
''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }ping
@client.command(pass_context=True)
async def ping(ctx, option = None):
    channel = ctx.message.channel
    msg = discord.Embed(colour=0xFF0000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    if option == None:
        print("")
    elif option == "g":
        print("")
    elif option == "f":
        print("")
    elif option == "s":
        msg.add_field(name=":satellite: ", value="My ping: `{}ms`.".format(round((t2-t1)*1000)))
        await client.say(embed=msg)
    elif option == "all":
        msg.add_field(name=":satellite: ", value="My ping: `{}ms`.".format(round((t2-t1)*1000)))
        await client.say(embed=msg)
    else:
        print("")

# }report <user> <reason>
@client.command(pass_context=True)
async def report(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xFF0000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None or args == None:
        msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `}report @Minx Bullying me.`.")
    else:
        if len(str(args)) > 1500:
            msg,add_field(name=error_img, value="The reason cannot be longer than 1500 characters.")
        else:
            msg.add_field(name=":clipboard: ", value="<@{}> reported <@{}>.\nReason:\n{}".format(author.id, user.id, args))
            chnl = client.get_channel('453193084591931405')
            m = "```diff"
            m += "\n- REPORT -"
            m += "\n+ Author: {} ### {}".format(author, author.id)
            m += "\n+ Target: {} ### {}".format(user, user.id)
            m += "\n+ Reason:"
            m += "\n```"
            m += "\n{}".format(args)
            await client.send_message(chnl, m)
    await client.say(embed=msg)

''' COMMANDS FOR HELPERS '''
# }cb
@client.command(pass_context=True)
async def cb(ctx):
    author = ctx.message.author
    chnl = ctx.message.channel
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    a = []
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        async for i in client.logs_from(chnl):
            if len(a) < 50:
                if i.author.bot:
                    await client.delete_message(i)
                    a.append("+1")
                else:
                    print("")
            else:
                break
        msg.add_field(name=":robot: :gun: Bot Killer", value="<@{}> removed the latest messages sent by bots.".format(author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff!")
    await client.say(embed=msg)
    
# }punish <user> <time> [reason]
@client.command(pass_context=True)
async def punish(ctx, user: discord.Member = None, time4 = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None or time4 == None:
            msg.add_field(name=error_img, value="Not all required arguments were given.\nExamples:\n`}punish @Nilzzu 15 Spamming.`.\n`}punish @Nilzzu 15`.")
            await client.say(embed=msg)
        else:
            if punished in user.roles:
                msg.add_field(name=error_img, value="That user is already punished.")
                await client.say(embed=msg)
            else:
                if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                    msg.add_field(name=error_img, value="Other staff cannot be punished.")
                    await client.say(embed=msg)
                else:
                    try:
                        time = int(time4)
                        if time > 600:
                            msg.add_field(name=error_img, value="The time cannot be longer than 600 minutes (10 hours).")
                            await client.say(embed=msg)
                        else:
                            testtime = time * 0
                            try:
                                await asyncio.sleep(float(testtime))
                                time2 = time * 60
                                chnl = client.get_channel('453219479963303936')
                                msg2 = discord.Embed(colour=0xC30000, description= "")
                                msg2.title = ""
                                msg2.set_footer(text=footer_text)
                                await client.add_roles(user, punished)
                                if args == None:
                                    msg.add_field(name=":no_entry_sign: ", value="<@{}> punished <@{}> for {} minute(s).\nNo reason given.".format(author.id, user.id, time4))
                                    await client.say(embed=msg)
                                    m = "```diff"
                                    m += "\n- PUNISH -"
                                    m += "\n+ Author: {} ### {}".format(author, author.id)
                                    m += "\n+ Target: {} ### {}".format(user, user.id)
                                    m += "\n+ Time: {}".format(time4)
                                    m += "\n+ Reason: [No Reason Given]"
                                    m += "\n```"
                                    await client.send_message(chnl, m)
                                    await asyncio.sleep(float(time2))
                                    await client.remove_roles(user, punished)
                                    msg2.add_field(name=":no_entry_sign: ", value="<@{}> has been automatically pardoned.".format(user.id))
                                    await client.say(embed=msg2)
                                else:
                                    if len(str(args)) > 1000:
                                        msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                                    else:
                                        msg.add_field(name=":no_entry_sign: ", value="<@{}> punished <@{}> for {} minute(s).\nReason:\n{}".format(author.id, user.id, time4, args))
                                        await client.say(embed=msg)
                                        m = "```diff"
                                        m += "\n- PUNISH -"
                                        m += "\n+ Author: {} ### {}".format(author, author.id)
                                        m += "\n+ Target: {} ### {}".format(user, user.id)
                                        m += "\n+ Time: {}".format(time4)
                                        m += "\n+ Reason:"
                                        m += "\n```"
                                        m += "\n{}".format(args)
                                        await client.send_message(chnl, m)
                                        await asyncio.sleep(float(time2))
                                        await client.remove_roles(user, punished)
                                        msg2.add_field(name=":no_entry_sign: ", value="<@{}> has been automatically pardoned.".format(user.id))
                                        await client.say(embed=msg2)
                            except:
                                msg.add_field(name=error_img, value="There has been an error while trying to punish that user.")
                                await client.say(embed=msg)
                    except:
                        msg.add_field(name=error_img, value="The time has to be a number.\nExample: `}punish @Sarah 10` will mute Sarah for 10 minutes.")
                        await client.say(embed=msg)
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
        await client.say(embed=msg)

# }pardon <user>
@client.command(pass_context=True)
async def pardon(ctx, user: discord.Member = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to pardon.\nExample: `}pardon @Celery`.")
        else:
            if punished in user.roles:
                await client.remove_roles(user, punished)
                msg.add_field(name=":o: ", value="<@{}> pardoned <@{}>.".format(author.id, user.id))
                chnl = client.get_channel('453219479963303936')
                m = "```diff"
                m += "\n- PARDON -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n```"
                await client.send_message(chnl, m)
            else:
                msg.add_field(name=error_img, value="That user isn't punished.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
    await client.say(embed=msg)

# }warn <user> <reason>
@client.command(pass_context=True)
async def warn(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `}warn @Ster Watching hentai at 3 AM.`.")
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1000:
                msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                await client.say(embed=msg)
            else:
                msg2 = discord.Embed(colour=0xC30000, description= "")
                msg2.title = ""
                msg2.set_footer(text=footer_text)
                msg2.add_field(name=":warning: ", value="Hello, <@{}>.\nYou have been warned by <@{}> ( **{}** ).\nReason:\n{}".format(user.id, author.id, author, args))
                try:
                    await client.send_message(user, embed=msg2)
                    msg.add_field(name=":warning: ", value="<@{}> warned <@{}>.\nReason:\n{}".format(author.id, user.id, args))
                    await client.say(embed=msg)
                except:
                    msg.add_field(name=":warning: ", value="<@{}> warned <@{}>.\nReason:\n{}".format(author.id, user.id, args))
                    await client.say("<@{}>".format(user.id), embed=msg)
                chnl = client.get_channel('453219479963303936')
                chnl2 = client.get_channel('453218908187394058')
                m2 = "**__~~= = = = = = = = = =~~__**"
                m2 += "\n`Target:` <@{}>".format(user.id)
                m2 += "\n`Warned by:` <@{}>".format(author.id)
                m2 += "\n`Reason:`"
                m2 += "\n{}".format(args)
                await client.send_message(chnl2, m2)
                m = "```diff"
                m += "\n- WARN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n+ Reason:"
                m += "\n```"
                m += "\n{}".format(args)
                await client.send_message(chnl, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
        await client.say(embed=msg)

# }check <user>
@client.command(pass_context=True)
async def check(ctx, user: discord.Member = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to run a check on.")
            await client.say(embed=msg)
        else:
            msg2 = discord.Embed(colour=0xC30000, description= "")
            msg2.title = ""
            msg2.set_footer(text=footer_text)
            chnl = client.get_channel('453218908187394058')
            b = []
            await client.send_typing(ctx.message.channel)
            async for i in client.logs_from(chnl):
                a = str(i.content)
                if user.id in a:
                    b.append("+1")
                    msg2.add_field(name=":warning: Warning number {}".format(len(b)), value="{}".format(i.content))
                else:
                    print("")
            try:
                await client.send_message(author, embed=msg2)
                msg.add_field(name=":mag: Warnings Check", value="<@{}>, please check your DMs!".format(author.id), inline=True)
                await client.say(embed=msg)
            except:
                msg.add_field(name=error_img, value="I cannot send you DMs. Please try again once you let me slide in your DMs.")
                await client.say(embed=msg)
                    
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
        await client.say(embed=msg)

# }clear <user>
@client.command(pass_context=True)
async def clear(ctx, user: discord.Member = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to clear the warnings from.")
        else:
            chnl = client.get_channel('453218908187394058')
            chnl2 = client.get_channel('453219479963303936')
            b = []
            await client.send_typing(ctx.message.channel)
            async for i in client.logs_from(chnl):
                a = str(i.content)
                if user.id in a:
                    await client.delete_message(i)
                    b.append("+1")
                else:
                    print("")
            msg.add_field(name=":scissors: ", value="<@{}> cleared `{}` warnings from <@{}>!".format(author.id, len(b), user.id))
            m = "```diff"
            m += "\n- CLEAR WARNINGS -"
            m += "\n+ Author: {} ### {}".format(author, author.id)
            m += "\n+ Target: {} ### {}".format(user, user.id)
            m += "\n+ Cleared: {}".format(len(b))
            m += "\n```"
            await client.send_message(chnl2, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
    await client.say(embed=msg)

# }purge <number>
@client.command(pass_context=True)
async def purge(ctx, number = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if number == None:
            msg.add_field(name=error_img, value="Please specify the number of messages you want to delete.")
        else:
            try:
                testnumber = int(number)
                number2 = testnumber * 0
                await asyncio.sleep(float(number2))
                try:
                    deleted = await client.purge_from(ctx.message.channel, limit=testnumber)
                    if len(deleted) < testnumber:
                        msg.add_field(name=":wastebasket: ", value="<@{}> tried to delete {} messages.\n{} messages were deleted.".format(author.id, number, len(deleted)))
                    else:
                        msg.add_field(name=":wastebasket: ", value="<@{}> deleted {} messages.".format(author.id, len(deleted)))
                    chnl = client.get_channel('453219479963303936')
                    m = "```diff"
                    m += "\n- PURGE -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ In: {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                    m += "\n+ Number: {}".format(number)
                    m += "\n+ Deleted: {}".format(len(deleted))
                    m += "\n```"
                    await client.send_message(chnl, m)
                except:
                    msg.add_field(name=error_img, value="There has been an error while trying to purge messages.")
            except:
                msg.add_field(name=error_img, value="The number has to be a number. Come on, guys, this is simple stuff.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
    await client.say(embed=msg)

# }nick <user> [nickname]
@client.command(pass_context=True)
async def nick(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to nickname.\nExamples:\n`}nick @Shy Trap Lord - Lord Of All Traps`.\n`}nick @Shy`.")
        else:
            if len(str(args)) > 32:
                msg.add_field(name=error_img, value="The nickname cannot be longer than 32 characters.")
            else:
                nickname = args
                try:
                    await client.change_nickname(user, nickname)
                    if args == None:
                        msg.add_field(name=":label: ", value="<@{}> removed <@{}>'s nickname.".format(author.id, user.id))
                    else:
                        msg.add_field(name=":label: ", value="<@{}> changed <@{}>'s nickname to `{}`.".format(author.id, user.id, nickname))
                except:
                    msg.add_field(name=error_img, value="<@{}> tried to edit <@{}>'s nickname, but failed.".format(author.id, user.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
    await client.say(embed=msg)

''' COMMANDS FOR MODERATORS '''
# }ban <user> [reason]
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="No target given.\nExamples:\n`}ban @Jimmy Stealing the soap.`.\n`}ban @Jimmy`.")
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                msg.add_field(name=error_img, value="You cannot ban other staff.\nStaff can only be banned manualy.")
            else:
                chnl = client.get_channel('453219479963303936')
                m = "```diff"
                m += "\n- BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                if args == None:
                    m += "\n+ Reason: [No Reason Given]"
                    m += "\n```"
                    msg.add_field(name=":hammer: Ban Hammer", value="<@{}> banned **{}**!\nNo reason given.".format(author.id, user))
                    await client.ban(user)
                    await client.send_message(chnl, m)
                else:
                    if len(str(args)) > 1000:
                        msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                    else:
                        m += "\n+ Reason:"
                        m += "\n```"
                        m += "\n{}".format(args)
                        msg.add_field(name=":hammer: Ban Hammer", value="<@{}> banned **{}**!\nReason:\n{}".format(author.id, user, args))
                        await client.ban(user)
                        await client.send_message(chnl, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Managers and Owners.")
    await client.say(embed=msg)

# }tempban <user> <time> [reason]
@client.command(pass_context=True)
async def tempban(ctx, user: discord.User = None, time4 = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0xC30000, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None or time4 == None:
            msg.add_field(name=error_img, value="Not all required arguments were given.\nExamples:\n`}tempban @Jimmy 120 Stealing the soap, again!`.\n`}tempban @Jimmy 120`.")
            await client.say(embed=msg)
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                msg.add_field(name=error_img, value="You cannot ban other staff.\nStaff can only be banned manualy.")
                await client.say(embed=msg)
            else:
                try:
                    time = int(time4)
                    if time > 600:
                        msg.add_field(name=error_img, value="The time cannot be longer than 600 minutes (10 hours).")
                        await client.say(embed=msg)
                    else:
                        testtime = time * 0
                        try:
                            await asyncio.sleep(float(testtime))
                            time2 = time * 60
                            userid = user.id
                            username = "{}#{}".format(user.name, user.discriminator)
                            chnl = client.get_channel('453219479963303936')
                            m = "```diff"
                            m += "\n- TEMPBAN -"
                            m += "\n+ Author: {} ### {}".format(author, author.id)
                            m += "\n+ Target: {} ### {}".format(user, user.id)
                            if args == None:
                                m += "\n+ Reason: [No Reason Given]"
                                m += "\n```"
                                msg.add_field(name=":hammer: Ban Hammer", value="<@{}> banned **{}** for `{}` minute(s).\nNo reason given.".format(author.id, user, time))
                                await client.say(embed=msg)
                                await client.ban(user)
                                await client.send_message(chnl, m)
                                await asyncio.sleep(float(time2))
                                banned_users = await client.get_bans(ctx.message.server)
                                user2 = discord.utils.get(banned_users,id=userid)
                                await client.unban(ctx.message.server, user2)
                                msg2.add_field(name=":tools: ", value="**{}** was automatically unbanned.".format(username))
                                await client.say(embed=msg2)
                            else:
                                if len(str(args)) > 1000:
                                    msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                                else:
                                    m += "\n+ Reason:"
                                    m += "\n```"
                                    m += "\n{}".format(args)
                                    msg.add_field(name=":hammer: Ban Hammer", value="<@{}> banned **{}** for `{}` minute(s).\nReason:\n{}".format(author.id, user, time, args))
                                    await client.say(embed=msg)
                                    await client.ban(user)
                                    await client.send_message(chnl, m)
                                    await asyncio.sleep(float(time2))
                                    banned_users = await client.get_bans(ctx.message.server)
                                    user2 = discord.utils.get(banned_users,id=userid)
                                    await client.unban(ctx.message.server, user2)
                                    msg2.add_field(name=":tools: ", value="**{}** was automatically unbanned.".format(username))
                                    await client.say(embed=msg2)
                        except:
                            msg.add_field(name=error_img, value="There has been an error while trying to tempban that user.")
                            await client.say(embed=msg)
                except:
                    msg.add_field(name=error_img, value="The time has to be a number.\nExample: `}tempban @Bob 10` will ban Bob for 10 minutes.")
                    await client.say(embed=msg)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Managers and Owners.")
        await client.say(embed=msg)

# }kick <user> [reason]
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="No target given.\nExamples:\n`}kick @Cookie Eating my cookies.`.\n`}kick @Cookie`.")
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                msg.add_field(name=error_img, value="You cannot kick other staff.\nStaff can only be kicked manualy.")
            else:
                chnl = client.get_channel('453219479963303936')
                m = "```diff"
                m += "\n- KICK -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                if args == None:
                    m += "\n+ Reason: [No Reason Given]"
                    m += "\n```"
                    msg.add_field(name=":boot: Kicking Boot", value="<@{}> kicked **{}**!\nNo reason given.".format(author.id, user))
                    await client.kick(user)
                    await client.send_message(chnl, m)
                else:
                    if len(str(args)) > 1000:
                        msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                    else:
                        m += "\n+ Reason:"
                        m += "\n```"
                        m += "\n{}".format(args)
                        msg.add_field(name=":boot: Kicking Boot", value="<@{}> kicked **{}**!\nReason:\n{}".format(author.id, user, args))
                        await client.kick(user)
                        await client.send_message(chnl, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Managers and Owners.")
    await client.say(embed=msg)

# }unban <user id>
@client.command(pass_context=True)
async def unban(ctx, userID = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if userID == None:
            msg.add_field(name=error_img, value="No user ID given.\nExample: `}unban 421820402076221442`.")
        else:
            banned_users = await client.get_bans(ctx.message.server)
            try:
                user = discord.utils.get(banned_users,id=userID)
                await client.unban(ctx.message.server, user)
                msg.add_field(name=":tools: ", value="<@{}> unbanned **{}** ( `{}` ).".format(author.id, user, userID))
                m = "```diff"
                m += "\n- UNBAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n```"
                chnl = client.get_channel('453219479963303936')
                await client.send_message(chnl, m)
            except:
                msg.add_field(name=error_img, value="There was an error while trying to unban that ID.\nEither the ID you specified doesn't exist or it isn't banned.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Managers and Owners.")
    await client.say(embed=msg)

''' COMMANDS FOR ADMININISTRATORS '''
# }embed <title> <description> <field name> <field value> <footer>
@client.command(pass_context=True)
async def embed(ctx, *, args = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `}embed Embed Title | Embed Description | Embed Field Name | Embed Field Value/Text | Embed Footer`.")
            await client.say(embed=msg)
        else:
            a = str(args)
            if '|' in a:
                b = a.split('|')
                try:
                    color = discord.Color(random.randint(0x000000, 0xFFFFFF))
                    msg2 = discord.Embed(colour=color, description="{}".format(b[1]))
                    msg2.title = "{}".format(b[0])
                    msg2.set_footer(text=b[4])
                    msg2.add_field(name="{}".format(b[2]), value="{}".format(b[3]))
                    await client.say(embed=msg2)
                except:
                    msg.add_field(name=error_img, value="The command was used incorrectly.\nExample: `}embed Embed Title | Embed Description | Embed Field Name | Embed Field Value/Text | Embed Footer`.")
                    await client.say(embed=msg)
            else:
                msg.add_field(name=error_img, value="The command was used incorrectly.\nExample: `}embed Embed Title | Embed Description | Embed Field Name | Embed Field Value/Text | Embed Footer`.")
                await client.say(embed=msg)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Administrators, Managers and Owners.")
        await client.say(embed=msg)

# }takerole <user> <role>
@client.command(pass_context=True)
async def takerole(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `}takerole @Aer Introvert (Level 10)`.")
        else:
            try:
                rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
                if author.top_role == rolename2 or author.top_role < rolename2:
                    msg.add_field(name=error_img, value="You cannot remove a role that is the same or higher than your top role.")
                else:
                    try:
                        await client.remove_roles(user, rolename2)
                        msg.add_field(name=":outbox_tray: ", value="<@{}> removed `{}` from <@{}>.".format(author.id, args, user.id))
                    except:
                        msg.add_field(name=error_img, value="Either I can't edit that user's role or the role you specified is higher than Manager.")
            except:
                msg.add_field(name=error_img, value="The specified role was not found.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Administrators, Managers and Owners.")
    await client.say(embed=msg)

# }giverole <user> <role>
@client.command(pass_context=True)
async def giverole(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `}giverole @Galaxygirl Introvert (Level 10)`.")
        else:
            try:
                rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
                if author.top_role == rolename2 or author.top_role < rolename2:
                    msg.add_field(name=error_img, value="You cannot add a role that is the same or higher than your top role.")
                else:
                    try:
                        await client.add_roles(user, rolename2)
                        msg.add_field(name=":inbox_tray: ", value="<@{}> added `{}` to <@{}>.".format(author.id, args, user.id))
                    except:
                        msg.add_field(name=error_img, value="Either I can't edit that user's role or the role you specified is higher than Manager.")
            except:
                msg.add_field(name=error_img, value="The specified role was not found.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Administrators, Managers and Owners.")
    await client.say(embed=msg)

''' COMMANDS FOR MANAGERS '''
# }idban <id> <reason>
@client.command(pass_context=True)
async def idban(ctx, target = None, *, args = None):
    author = ctx.message.author
    server = ctx.message.server
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    msg = discord.Embed(colour=0xC30000, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or manager in author.roles:
        if target == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `}idban @Zero Stealing chocolate.`.")
        else:
            try:
                a = await client.get_user_info(target)
                await client.http.ban(target, server.id, 0)
                msg.add_field(name=":hammer_pick: ", value="<@{}> ID banned **{}**.\nReason:\n{}".format(author.id, a, args))
                m = "```diff"
                m += "\n- ID BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(a, a.id)
                m += "\n+ Reason:"
                m += "\n```"
                m += "\n{}".format(args)
                chnl = client.get_channel('453219479963303936')
                await client.send_message(chnl, m)
            except:
                msg.add_field(name=error_img, value="There was an error while trying to ID ban that user.\nEither the user cannot be banned or the ID you specified doesn't exist.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Managers and Owners.")
    await client.say(embed=msg)
    
#######################
client.run(os.environ['BOT_TOKEN'])
