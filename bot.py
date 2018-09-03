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
error_e = ':octagonal_sign:'
x_role = '453196094332076045'
loading_e = '<a:loading:484705261609811979>'
limit=10000000000000

''''''
# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("[][][][][][][][][][][][][][]")
    print("[]Logged in!              []")
    print("[][][][][][][][][][][][][][]")
    print("[]Name: X Security        []")
    print("[]ID: 453210219187535887  []")
    print("[][][][][][][][][][][][][][]")
    await client.change_presence(game=discord.Game(name="with the ban hammer"))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("[]Ping: {}".format(round((t2-t1)*1000)))
    print("[][][][][][][][][][][][][][]")
    
''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }ping
@client.command(pass_context=True)
async def ping(ctx, option = None):
    channel = ctx.message.channel
    msg = discord.Embed(colour=0xFF0000, title= "")
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
        msg.description = ":satellite: My ping: `{}ms`.".format(round((t2-t1)*1000))
        await client.say(embed=msg)
    elif option == "c":
        print("")
    elif option == "all":
        msg.description = ":satellite: My ping: `{}ms`.".format(round((t2-t1)*1000))
        await client.say(embed=msg)
    else:
        print("")

# }report <user> <reason>
@client.command(pass_context=True)
async def report(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0xFF0000, title= "")
    msg.set_footer(text=footer_text)
    if user == None or args == None:
        msg.description = "{} Please mention the person you want to report and the reason why you're reporting them.".format(error_e)
    else:
        if len(str(args)) > 1500:
            msg.description = "{} The reason cannot be longer than 1500 characters.".format(error_e)
        else:
            msg.description = ":clipboard: <@{}> reported <@{}>.\nReason:\n{}".format(author.id, user.id, args)
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
    msg = discord.Embed(colour=0xC30000, title= "")
    msg.set_footer(text=footer_text)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        msgs = []
        a = []
        msg.description = "Deleting latest bot messages... {}".format(loading_e)
        await client.say(embed=msg)
        async for i in client.logs_from(ctx.message.channel):
            if len(a) < 50:
                if i.author.bot:
                    msgs.append(i)
                    a.append("+1")
            else:
                break
        try:
            await client.delete_messages(msgs)
            msg.description = "<@{}> removed the latest messages sent by bots.".format(author.id)
            await client.say(embed=msg)
        except:
            for i in msgs:
                try:
                    await client.delete_message(i)
                    msg.description = "<@{}> removed the latest messages sent by bots.".format(author.id)
                    await client.say(embed=msg)
                except:
                    msg.description = "<@{}> removed the latest messages sent by bots.".format(author.id)
                    await client.say(embed=msg)
                    break
    else:
        msg.description = "{} This command can only be used by the staff!".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None or time4 == None:
            msg.description = "{} Not all required arguments were given.".format(error_e)
            await client.say(embed=msg)
        else:
            if punished in user.roles:
                msg.description = "{} That user is already punished.".format(error_e)
                await client.say(embed=msg)
            else:
                if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                    msg.description = "{} Other staff cannot be punished.".format(error_e)
                    await client.say(embed=msg)
                else:
                    try:
                        time = int(time4)
                        if time > 600 or time < 1:
                            msg.description = "{} The time cannot be longer than 600 minutes (10 hours) and lower than 1 minute.".format(error_e)
                            await client.say(embed=msg)
                        else:
                            try:
                                time2 = time * 60
                                msg2 = discord.Embed(colour=0xC30000, title="")
                                msg2.set_footer(text=footer_text)
                                await client.add_roles(user, punished)
                                if args == None:
                                    msg.description = "<@{}> punished <@{}> for {} minute(s).\nNo reason given.".format(author.id, user.id, time4)
                                    await client.say(embed=msg)
                                    m = "```diff"
                                    m += "\n- PUNISH -"
                                    m += "\n+ Author: {} ### {}".format(author, author.id)
                                    m += "\n+ Target: {} ### {}".format(user, user.id)
                                    m += "\n+ Time: {}".format(time4)
                                    m += "\n+ Reason: [No Reason Given]"
                                    m += "\n```"
                                    await client.send_message(client.get_channel('453219479963303936'), m)
                                    await asyncio.sleep(float(time2))
                                    if punished in user.roles:
                                        await client.remove_roles(user, punished)
                                        msg2.description = "<@{}> has been automatically pardoned.".format(user.id)
                                        await client.say(embed=msg2)
                                else:
                                    if len(str(args)) > 1000:
                                        msg.description = "{} The reason cannot be longer than 1000 characters.".format(error_e)
                                    else:
                                        msg.description = "<@{}> punished <@{}> for {} minute(s).\nReason:\n{}".format(author.id, user.id, time4, args)
                                        await client.say(embed=msg)
                                        m = "```diff"
                                        m += "\n- PUNISH -"
                                        m += "\n+ Author: {} ### {}".format(author, author.id)
                                        m += "\n+ Target: {} ### {}".format(user, user.id)
                                        m += "\n+ Time: {}".format(time4)
                                        m += "\n+ Reason:"
                                        m += "\n```"
                                        m += "\n{}".format(args)
                                        await client.send_message(client.get_channel('453219479963303936'), m)
                                        await asyncio.sleep(float(time2))
                                        if punished in user.roles:
                                            await client.remove_roles(user, punished)
                                            msg2.add_field(name=":no_entry_sign: ", value="<@{}> has been automatically pardoned.".format(user.id))
                                            await client.say(embed=msg2)
                            except:
                                msg.description = "{} There has been an error while trying to punish that user.".format(error_e)
                                await client.say(embed=msg)
                    except:
                        msg.description = "{} The time has to be a number.".format(error_e)
                        await client.say(embed=msg)
    else:
        msg.description = "{} This command can only be used by the staff.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.description = "{} Please mention someone you want to pardon.".format(error_e)
        else:
            if punished in user.roles:
                await client.remove_roles(user, punished)
                msg.description = "<@{}> pardoned <@{}>.".format(author.id, user.id)
                m = "```diff"
                m += "\n- PARDON -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n```"
                await client.send_message(client.get_channel('453219479963303936'), m)
            else:
                msg.description = "{} That user isn't punished.".format(error_e)
    else:
        msg.description = "{} This command can only be used by the staff.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None or args == None:
            msg.description = "{} Not all arguments were given.".format(error_e)
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1000:
                msg.description = "{} The reason cannot be longer than 1000 characters.".format(error_e)
                await client.say(embed=msg)
            else:
                msg2 = discord.Embed(colour=0xC30000, title="")
                msg2.set_footer(text=footer_text)
                msg2.description = "You have been warned by <@{}> ( **{}** ).\n`Reason:` {}".format(author.id, author, args)
                try:
                    await client.send_message(user, embed=msg2)
                    msg.description = "<@{}> warned <@{}>.\n`Reason:` {}".format(author.id, user.id, args)
                    await client.say(embed=msg)
                except:
                    msg.description = "<@{}> warned <@{}>.\n`Reason:` {}".format(author.id, user.id, args)
                    await client.say("<@{}>".format(user.id), embed=msg)
                h = await client.send_message(client.get_channel('453218908187394058'), "loading")
                m2 = "{} | {} ### {} | {} ### {} | {}".format(h.id, author, author.id, user, user.id, args)
                await client.edit_message(h, m2)
                m = "```diff"
                m += "\n- WARN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n+ Reason:"
                m += "\n```"
                m += "\n{}".format(args)
                await client.send_message(client.get_channel('453219479963303936'), m)
    else:
        msg.description = "{} This command can only be used by the staff.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.description = "{} Please mention someone you want to run a check on.".format(error_e)
            await client.say(embed=msg)
        else:
            msg2 = discord.Embed(colour=0xC30000, title="")
            msg2.set_footer(text=footer_text)
            msg.description = "Checking warnings for <@{}>... {}".format(user.id, loading_e)
            h = await client.say(embed=msg)
            m = ""
            o = []
            async for i in client.logs_from(client.get_channel('453218908187394058')):
                a = str(i.content)
                if user.id in a:
                    b = i.content.split(' | ')
                    m += "\n**__Warn number: {}__**\n`Warned by:` {}\n`Reason:` {}".format(b[0], b[1], b[3])
                    o.append("+1")
            if len(o) == 0:
                msg.description = "No warnings found for <@{}>.".format(user.id)
                await client.edit_message(h, embed=msg)
            else:
                msg2.add_field(name=":warning: ***__Warning list for {} ### {}__***".format(user, user.id), value=m)
                try:
                    await client.send_message(author, embed=msg2)
                    msg.description = value="<@{}>, please check your DMs!".format(author.id)
                    await client.edit_message(h, embed=msg)
                except:
                    msg.description = "{} I cannot send you DMs. Please try again once you let me slide in your DMs.".format(error_e)
                    await client.edit_message(h, embed=msg)
    else:
        msg.description = "{} This command can only be used by the staff.".format(error_e)
        await client.say(embed=msg)

# }clear <warn number>
@client.command(pass_context=True)
async def clear(ctx, number = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, id=x_role)
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if number == None:
            msg.description = "{} Please specify which warning you want to remove using its number.".format(error_e)
            await client.say(embed=msg)
        else:
            msg.description = "Looking for warning... {}".format(loading_e)
            h = await client.say(embed=msg)
            o = []
            async for i in client.logs_from(client.get_channel('453218908187394058'), limit=limit):
                a = i.content.split(' | ')
                if a[0] == number:
                    await client.delete_message(i)
                    msg.description = "<@{}> cleared a warning from **{}**.".format(author.id, a[2])
                    await client.edit_message(h, embed=msg)
                    m = "```diff"
                    m += "\n- CLEAR WARNING -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ Target: {}".format(a[2])
                    m += "\n```"
                    await client.send_message(client.get_channel('453219479963303936'), m)
                    o.append("+1")
                    break
            if len(o) == 0:
                msg.description = "{} Warning not found.".format(error_e)
                await client.edit_message(h, embed=msg)
    else:
        msg.description = "{}This command can only be used by the staff.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if number == None:
            msg.description = "{} Please specify the number of messages you want to delete.".format(error_e)
            await client.say(embed=msg)
        else:
            try:
                testnumber = int(number)
                try:
                    deleted = await client.purge_from(ctx.message.channel, limit=testnumber)
                    if len(deleted) < testnumber:
                        msg.description = "<@{}> tried to delete {} messages.\n{} messages were deleted.".format(author.id, number, len(deleted))
                    else:
                        msg.description = "<@{}> deleted {} messages.".format(author.id, len(deleted))
                    await client.say(embed=msg)
                    m = "```diff"
                    m += "\n- PURGE -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ In: {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                    m += "\n+ Number: {}".format(number)
                    m += "\n+ Deleted: {}".format(len(deleted))
                    m += "\n```"
                    await client.send_message(client.get_channel('453219479963303936'), m)
                except:
                    msg.description = "{} There has been an error while trying to purge messages.".format(error_e)
            except:
                msg.description = "{} The number has to be a number. Come on, guys, this is simple stuff.".format(error_e)
    else:
        msg.description = "{} This command can only be used by the staff.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.description = "{} Please mention someone you want to nickname.".format(error_e)
            await client.say(embed=msg)
        else:
            if len(str(args)) > 32:
                msg.description = "{} The nickname cannot be longer than 32 characters.".format(error_e)
                await client.say(embed=msg)
            else:
                nickname = args
                try:
                    await client.change_nickname(user, nickname)
                    if args == None:
                        msg.description = "<@{}> removed **{}**'s nickname.".format(author.id, user.name)
                    else:
                        msg.description = "<@{}> changed **{}**'s nickname to `{}`.".format(author.id, user.name, nickname)
                    await client.say(embed=msg)
                except:
                    msg.description = "<@{}> tried to edit <@{}>'s nickname, but failed.".format(author.id, user.id)
                    await client.say(embed=msg)
    else:
        msg.description = "{} This command can only be used by the staff.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None:
            msg.description = "{} No target given.".format(error_e)
            await client.say(embed=msg)
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                msg.description = "{} You cannot ban other staff. Staff can only be banned manualy.".format(error_e)
                await client.say(embed=msg)
            else:
                m = "```diff"
                m += "\n- BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                if args == None:
                    m += "\n+ Reason: [No Reason Given]"
                    m += "\n```"
                    msg.description = "<@{}> banned **{}**!\nNo reason given.".format(author.id, user)
                    await client.say(embed=msg)
                    await client.ban(user)
                    await client.send_message(client.get_channel('453219479963303936'), m)
                else:
                    if len(str(args)) > 1000:
                        msg.description = "{} The reason cannot be longer than 1000 characters.".format(error_e)
                    else:
                        m += "\n+ Reason:"
                        m += "\n```"
                        m += "\n{}".format(args)
                        msg.description = "<@{}> banned **{}**!\nReason:\n{}".format(author.id, user, args)
                        await client.say(embed=msg)
                        await client.ban(user)
                        await client.send_message(client.get_channel('453219479963303936'), m)
    else:
        msg.description = "{} This command can only be used by Moderators, Administrators, Managers and Owners.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if userID == None:
            msg.description = "{} No user ID given.".format(error_e)
            await client.say(embed=msg)
        else:
            try:
                user = await client.get_user_info(userID)
                await client.unban(ctx.message.server, user)
                msg.description = "<@{}> unbanned **{}** ( `{}` ).".format(author.id, user, userID)
                await client.say(embed=msg)
                m = "```diff"
                m += "\n- UNBAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n```"
                await client.send_message(client.get_channel('453219479963303936'), m)
            except:
                msg.description = "{} There was an error while trying to unban that ID.\nEither the ID you specified doesn't exist or it isn't banned.".format(error_e)
                await client.say(embed=msg)
    else:
        msg.description = "{} This command can only be used by Moderators, Administrators, Managers and Owners.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0xC30000, title="")
    msg2.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None or time4 == None:
            msg.description = "{} Not all required arguments were given.".format(error_e)
            await client.say(embed=msg)
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                msg.description = "{} You cannot ban other staff.\nStaff can only be banned manualy.".format(error_e)
                await client.say(embed=msg)
            else:
                try:
                    time = int(time4)
                    if time > 600:
                        msg.description = "{} The time cannot be longer than 600 minutes (10 hours).".format(error_e)
                        await client.say(embed=msg)
                    else:
                        try:
                            time2 = time * 60
                            m = "```diff"
                            m += "\n- TEMPBAN -"
                            m += "\n+ Author: {} ### {}".format(author, author.id)
                            m += "\n+ Target: {} ### {}".format(user, user.id)
                            if args == None:
                                m += "\n+ Reason: [No Reason Given]"
                                m += "\n```"
                                msg.description = "<@{}> banned **{}** for `{}` minute(s).\nNo reason given.".format(author.id, user, time)
                                await client.say(embed=msg)
                                await client.ban(user)
                                await client.send_message(client.get_channel('453219479963303936'), m)
                                await asyncio.sleep(float(time2))
                                try:
                                    await client.unban(ctx.message.server, user)
                                    msg2.description = "**{} ### {}** was automatically unbanned.".format(user, user.id)
                                    await client.say(embed=msg2)
                                except:
                                    print("")
                            else:
                                if len(str(args)) > 1000:
                                    msg.description = "{} The reason cannot be longer than 1000 characters.".format(error_e)
                                else:
                                    m += "\n+ Reason:"
                                    m += "\n```"
                                    m += "\n{}".format(args)
                                    msg.description = "<@{}> banned **{}** for `{}` minute(s).\nReason:\n{}".format(author.id, user, time, args)
                                    await client.say(embed=msg)
                                    await client.ban(user)
                                    await client.send_message(client.get_channel('453219479963303936'), m)
                                    await asyncio.sleep(float(time2))
                                    try:
                                        await client.unban(ctx.message.server, user)
                                        msg2.description = "**{} ### {}** was automatically unbanned.".format(user, user.id)
                                        await client.say(embed=msg2)
                                    except:
                                        print("")
                        except:
                            msg.description = "{} There has been an error while trying to tempban that user.".format(error_e)
                            await client.say(embed=msg)
                except:
                    msg.description = "{} The time has to be a number.".format(error_e)
                    await client.say(embed=msg)
    else:
        msg.description = "{] This command can only be used by Moderators, Administrators, Managers and Owners.".format(error_e)
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
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None:
            msg.description = "{} No target given.".format(error_e)
            await client.say(embed=msg)
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                msg.description = "You cannot kick other staff.\nStaff can only be kicked manualy.".format(error_e)
                await client.say(embed=msg)
            else:
                m = "```diff"
                m += "\n- KICK -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                if args == None:
                    m += "\n+ Reason: [No Reason Given]"
                    m += "\n```"
                    msg.description = "<@{}> kicked **{}**!\nNo reason given.".format(author.id, user)
                    await client.say(embed=msg)
                    await client.kick(user)
                    await client.send_message(client.get_channel('453219479963303936'), m)
                else:
                    if len(str(args)) > 1000:
                        msg.description = "{} The reason cannot be longer than 1000 characters.".format(error_e)
                        await client.say(embed=msg)
                    else:
                        m += "\n+ Reason:"
                        m += "\n```"
                        m += "\n{}".format(args)
                        msg.description = "<@{}> kicked **{}**!\nReason:\n{}".format(author.id, user, args)
                        await client.say(embed=msg)
                        await client.kick(user)
                        await client.send_message(client.get_channel('453219479963303936'), m)
    else:
        msg.description = "{} This command can only be used by Moderators, Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=msg)

''' COMMANDS FOR ADMININISTRATORS '''
# }takerole <user> <role>
@client.command(pass_context=True)
async def takerole(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or args == None:
            msg.description = "{} Not all arguments were given.".format(error_e)
            await client.say(embed=msg)
        else:
            try:
                rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
                if author.top_role <= rolename2:
                    msg.description = "{} You cannot remove a role that is the same or higher than your top role.".format(error_e)
                    await client.say(embed=msg)
                else:
                    try:
                        await client.remove_roles(user, rolename2)
                        msg.description = "<@{}> removed `{}` from <@{}>.".format(author.id, args, user.id)
                        await client.say(embed=msg)
                    except:
                        msg.description = "{} Either I can't edit that user's roles or the role you specified is higher than mine.".format(error_e)
                        await client.say(embed=msg)
            except:
                msg.description = "{} The specified role was not found.".format(error_e)
                await client.say(embed=msg)
    else:
        msg.description = "{} This command can only be used by Administrators, Managers and Owners.".format(error_e)
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
            msg.description = "{} Not all arguments were given.".format(error_e)
            await client.say(embed=msg)
        else:
            try:
                rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
                if author.top_role <= rolename2:
                    msg.description = "{} You cannot add a role that is the same or higher than your top role.".format(error_e)
                    await client.say(embed=msg)
                else:
                    try:
                        await client.add_roles(user, rolename2)
                        msg.description = "<@{}> added `{}` to <@{}>.".format(author.id, args, user.id)
                        await client.say(embed=msg)
                    except:
                        msg.description = "{} Either I can't edit that user's roles or the role you specified is higher than mine.".format(error_e)
                        await client.say(embed=msg)
            except:
                msg.description = "{} The specified role was not found.".format(error_e)
                await client.say(embed=msg)
    else:
        msg.description = "{} This command can only be used by Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=msg)

''' COMMANDS FOR MANAGERS '''
# }idban <id> <reason>
@client.command(pass_context=True)
async def idban(ctx, target = None, *, args = None):
    author = ctx.message.author
    server = ctx.message.server
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    msg = discord.Embed(colour=0xC30000, title="")
    msg.set_footer(text=footer_text)
    if owner in author.roles or manager in author.roles:
        if target == None or args == None:
            msg.description = "{} Not all arguments were given.".format(error_e)
            await client.say(embed=msg)
        else:
            try:
                a = await client.get_user_info(target)
                await client.http.ban(target, server.id, 0)
                msg.description = "<@{}> ID banned **{}**.\nReason:\n{}".format(author.id, a, args)
                await client.say(embed=msg)
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
                msg.description = "{} There was an error while trying to ID ban that user.\nEither the user cannot be banned or the ID you specified doesn't exist.".format(error_e)
                await client.say(embed=msg)
    else:
        msg.description = "{} This command can only be used by Managers and Owners.".format(error_e)
        await client.say(embed=msg)
    
#######################
client.run(os.environ['BOT_TOKEN'])
