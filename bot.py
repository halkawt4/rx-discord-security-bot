import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

''''''

Client = discord.Client()
bot_prefix= "}"
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "[Realm X] - [X Moderation]"

pm_role = '473812644021927946'
helper_role = '453195469309476877'
mod_role = '453195518785486858'
admin_role = '453195993987416064'
manager_role = '453196026547929088'
owner_role = '453194638077984768'
member_role = '453194601247801354'
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
partner_role = '453194705732239360'
muted_role = '453195421611982848'
x_role = '453196094332076045'
error_e = ":octagonal_sign:"
logs = '490437065930965003'
loading_e = '<a:loading:484705261609811979>'
punished_list = []
joined = []

''''''

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    server = client.get_server('452865346081128448')
    punished = discord.utils.get(server.roles, id=muted_role)
    try:
        for i in server.members:
            if punished in i.roles:
                await client.remove_roles(i, punished)
                print("[START UP] Pardoned {}".format(i.id))
    except:
        print("[START UP] Error in pardoning everyone.")
    print("[+][+][+][+][+][+][+][+][+][+][+][+]")
    print("[+] Logged in!")
    print("[+][+][+][+][+][+][+][+][+][+][+][+]")
    print("[+] Name: Moderation")
    print("[+] ID: {}".format(client.user.id))
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel('453193096335720479'))
    t2 = time.perf_counter()
    print("[+] Ping: {}".format(round((t2-t1)*1000)))
    print("[+][+][+][+][+][+][+][+][+][+][+][+]")
    await client.change_presence(game=discord.Game(name="with the ban hammer"))

# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(userName: discord.User):
    joined.append(userName.id)
    server = userName.server
    if userName.id in punished_list:
        try:
            await client.add_roles(server.get_member(userName.id), discord.utils.get(server.roles, id=muted_role))
            await client.send_message(userName, m2)
        except:
            print("")
    a = []
    for i in joined:
        if i == userName.id:
            a.append("+1")
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(a) >= 5:
        await client.http.ban(userName.id, userName.server.id, 0)
        embed.description = "**{}** has been automatically banned.\nReason: Possible raid attempt.".format(userName)
        await client.send_message(client.get_channel('453192466716164137'), embed=embed)
        m = "```diff"
        m += "\n- AUTO BAN -"
        m += "\n+ Target: {} ### {}".format(userName, userName.id)
        m += "\n+ Reason:"
        m += "\nPossible raid attempt."
        m += "\n```"
        await client.send_message(client.get_channel(logs), m)
        async for i in client.logs_from(client.get_channel('453192466716164137'), limit=10):
            if userName.name in str(i.content) or i.author.id == userName.id or userName.id in str(i.content):
                await client.delete_message(i)
        async for i in client.logs_from(client.get_channel('453192385795588096'), limit=10):
            if userName.name in str(i.content):
                await client.delete_message(i)
    if 'gg/' in str(userName.name):
        try:
            await client.kick(userName)
            embed.description = "User with ID **{}** has been automatically kicked.\nReason: Advertising by name.".format(userName.id)
            await client.send_message(client.get_channel('453192466716164137'), embed=embed)
            m = "```diff"
            m += "\n- AUTO KICK -"
            m += "\n+ Target: {} ### {}".format(userName, userName.id)
            m += "\n+ Reason:"
            m += "\nAdvertising by name."
            m += "\n```"
            await client.send_message(client.get_channel(logs), m)
        except:
            print("")
        async for i in client.logs_from(client.get_channel('453192466716164137'), limit=10):
            if userName.name in str(i.content) or i.author.id == userName.id or userName.id in str(i.content):
                await client.delete_message(i)
        async for i in client.logs_from(client.get_channel('453192385795588096'), limit=10):
            if userName.name in str(i.content):
                await client.delete_message(i)


''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }ping <option>
@client.command(pass_context=True)
async def ping(ctx, option = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if option == None:
        print("")
    elif option == "all" or option == "m":
        t1 = time.perf_counter()
        await client.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        embed.description = "My ping is `{}`ms.".format(round((t2-t1)*1000))
        await client.say(embed=embed)

# }report <user> <reason>
@client.command(pass_context=True)
async def report(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if user == None or args == None:
        embed.description = "{} Please mention the user you want to report and add the reason why you are reporting them.".format(error_e)
        await client.say(embed=embed)
    elif len(str(args)) > 1500:
        embed.description = "{} The reason cannot be longer than 1500 characters.".format(error_e)
        await client.say(embed=embed)
    else:
        m = "```md\n# =============== #\n```"
        m += "\n***__REPORT:__***"
        m += "\n`Author:` <@{}> ### {}".format(ctx.message.author.id, ctx.message.author.id)
        m += "\n`Target:` <@{}> ### {}".format(user.id, user.id)
        m += "\n`Reason:`"
        m += "\n{}".format(args)
        await client.send_message(client.get_channel('453193084591931405'), m)
        embed.description = "<@{}> reported <@{}> to the staff.".format(ctx.message.author.id, user.id)
        await client.say(embed=embed)

''' COMMANDS FOR HELPERS '''

# }cb
@client.command(pass_context=True)
async def cb(ctx):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        embed.description = "Deleting latest messages sent by bots... {}".format(loading_e)
        h = await client.say(embed=embed)
        a = []
        msgs = []
        async for i in client.logs_from(ctx.message.channel):
            if len(a) < 50:
                if i.author.bot and i.id != h.id:
                    msgs.append(i)
                    a.append("+1")
            else:
                break
        try:
            await client.delete_messages(msgs)
            embed.description = "<@{}> removed the latest messages sent by bots.".format(author.id)
            await client.edit_message(h, embed=embed)
        except:
            for i in msgs:
                await client.delete_message(i)
            embed.description = "<@{}> removed the latest messages sent by bots.".format(author.id)
            await client.edit_message(h, embed=embed)
    else:
        embed.description = "{} This command can only be used by staff.".format(error_e)
        await client.say(embed=embed)

# }punish <user> <minutes> [reason]
@client.command(pass_context=True)
async def punish(ctx, user: discord.Member = None, time = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=muted_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or time == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <minutes> [reason]`.".format(error_e)
            await client.say(embed=embed)
        elif helper in user.roles or mod in user.roles or admin in user.roles or manager in user.roles or owner in user.roles or user.bot:
            embed.description = "{} Other staff and bots cannot be punished.".format(error_e)
            await client.say(embed=embed)
        elif punished in user.roles:
            embed.description = "{} That user is already punished.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250 and args != None:
            embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                time2 = int(time)
                if time2 > 600 or time2 < 1:
                    embed.description = "{} You cannot punish someone for longer than 600 minutes and shorter than 1 minute.".format(error_e)
                    await client.say(embed=embed)
                else:
                    await client.add_roles(user, punished)
                    punished_list.append(user.id)
                    minutes = time2 * 60
                    if args == None:
                        reason = "?"
                    else:
                        reason = args
                    embed.description = "<@{}> punished <@{}> for `{}` minute(s).\nReason: {}".format(author.id, user.id, time, reason)
                    await client.say(embed=embed)
                    m = "```diff"
                    m += "\n- PUNISH -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ Target: {} ### {}".format(user, user.id)
                    m += "\n+ Time: {} minute(s)".format(time)
                    m += "\n+ Reason:"
                    m += "\n{}".format(reason)
                    m += "\n```"
                    await client.send_message(client.get_channel(logs), m)
                    await asyncio.sleep(float(minutes))
                    try:
                        try:
                            punished_list.remove(user.id)
                        except:
                            print("")
                        if punished in user.roles:
                            await client.remove_roles(user, punished)
                            embed.description = "<@{}> was automatically pardoned.".format(user.id)
                            await client.say(embed=embed)
                    except:
                        print("")
            except:
                embed.description = "{} The minutes have to be a number.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by staff.".format(error_e)
        await client.say(embed=embed)

# }pardon <user>
@client.command(pass_context=True)
async def pardon(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    punished = discord.utils.get(ctx.message.server.roles, id=muted_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None:
            embed.description = "{} Please mention the user you want to pardon.".format(error_e)
            await client.say(embed=embed)
        elif punished in user.roles:
            try:
                punished_list.remove(user.id)
            except:
                print("")
            await client.remove_roles(user, punished)
            embed.description = "<@{}> pardoned <@{}>.".format(author.id, user.id)
            await client.say(embed=embed)
            m = "```diff"
            m += "\n- PARDON -"
            m += "\n+ Author: {} ### {}".format(author, author.id)
            m += "\n+ Target: {} ### {}".format(user, user.id)
            m += "\n```"
            await client.send_message(client.get_channel(logs), m)
        else:
            embed.description = "{} That user is not punished.".format(error_e)
            await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by staff.".format(error_e)
        await client.say(embed=embed)

# }warn <user> <reason>
@client.command(pass_context=True)
async def warn(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or args == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <reason>`.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250:
            embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                embed.description = "You have been warned in **Realm ✘**.\nReason: {}".format(args)
                await client.send_message(user, embed=embed)
                embed.description = "<@{}> warned <@{}>.\nReason: {}".format(author.id, user.id, args)
                await client.say(embed=embed)
            except:
                embed.description = "<@{}> warned <@{}>.\nReason: {}".format(author.id, user.id, args)
                await client.say("<@{}>".format(user.id), embed=embed)
            h = await client.send_message(client.get_channel('453218908187394058'), "new warn data incoming")
            await client.edit_message(h, "{} | {} | {} | {}".format(user.id, author.id, args, h.id))
            m = "```diff"
            m += "\n- WARN -"
            m += "\n+ Author: {} ### {}".format(author, author.id)
            m += "\n+ Target: {} ### {}".format(user, user.id)
            m += "\n+ Reason:"
            m += "\n{}".format(args)
            m += "\n```"
            await client.send_message(client.get_channel(logs), m)
    else:
        embed.description = "{} This command can only be used by staff.".format(error_e)
        await client.say(embed=embed)

# }check <user>
@client.command(pass_context=True)
async def check(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None:
            embed.description = "{} Please mention the user you want to check.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "Checking warnings... {}".format(loading_e)
            h = await client.say(embed=embed)
            o = []
            p = []
            async for i in client.logs_from(client.get_channel('453218908187394058'), limit=10000000):
                a = i.content.split(' | ')
                p.append("+1")
                if a[0] == user.id:
                    m = "`WARN NUMBER: {}`".format(a[3])
                    m += "\n-----`Warned by:` <@{}> ### {}".format(a[1], a[1])
                    m += "\n-----`Reason:` {}".format(a[2])
                    try:
                        await client.send_message(author, m)
                        o.append("+1")
                    except:
                        embed.description = "{} Please give me permissions to DM you and try again.".format(error_e)
                        await client.edit_message(h, embed=embed)
                        break
            if len(p) == 0:
                embed.description = "No warnings found for <@{}>.".format(user.id)
                await client.edit_message(h, embed=embed)
            elif len(o) != 0:
                embed.description = "The warning data for <@{}> has been sent to <@{}>'s DMs.".format(user.id, author.id)
                await client.edit_message(h, embed=embed)
    else:
        embed.description = "{} This command can only be used by staff.".format(error_e)
        await client.say(embed=embed)

# }clear <user> <warn number/all>
@client.command(pass_context=True)
async def clear(ctx, user: discord.Member = None, target = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or target == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <warn number/all>`.".format(error_e)
            await client.say(embed=embed)
        elif target == "all":
            embed.description = "Checking warnings... {}".format(loading_e)
            h = await client.say(embed=embed)
            o = []
            async for i in client.logs_from(client.get_channel('453218908187394058'), limit=10000000):
                a = i.content.split(' | ')
                if a[0] == user.id:
                    await client.delete_message(i)
                    o.append("+1")
            if len(o) == 0:
                embed.description = "No warnings found for <@{}>.".format(user.id)
            else:
                embed.description = "<@{}> cleared `{}` warning(s) for <@{}>.".format(author.id, len(o), user.id)
            await client.edit_message(h, embed=embed)
            m = "```diff"
            m += "\n- CLEAR WARNINGS -"
            m += "\n+ Author: {} ### {}".format(author, author.id)
            m += "\n+ Target: {} ### {}".format(user, user.id)
            m += "\n+ Number: {}".format(len(o))
            m += "\n```"
            await client.send_message(client.get_channel(logs), m)
        else:
            embed.description = "Checking warnings... {}".format(loading_e)
            h = await client.say(embed=embed)
            o = []
            async for i in client.logs_from(client.get_channel('453218908187394058'), limit=10000000):
                a = i.content.split(' | ')
                if a[0] == user.id and a[3] == target:
                    await client.delete_message(i)
                    o.append("+1")
                    break
            if len(o) == 0:
                embed.description = "{} A warning with that number hasn't been found.".format(error_e)
            else:
                embed.description = "<@{}> cleared `1` warning for <@{}>.".format(author.id, user.id)
            await client.edit_message(h, embed=embed)
            m = "```diff"
            m += "\n- CLEAR WARNINGS -"
            m += "\n+ Author: {} ### {}".format(author, author.id)
            m += "\n+ Target: {} ### {}".format(user, user.id)
            m += "\n+ Number: {}".format(len(o))
            m += "\n```"
            await client.send_message(client.get_channel(logs), m)
    else:
        embed.description = "{} This command can only be used by staff.".format(error_e)
        await client.say(embed=embed)

# }purge <number>
@client.command(pass_context=True)
async def purge(ctx, number = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if number == None:
            embed.description = "{} Please give the number of messages you want to delete.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                amount = int(number)
                try:
                    deleted = await client.purge_from(ctx.message.channel, limit=amount)
                    embed.description = "<@{}> deleted `{}` messages.".format(author.id, len(deleted))
                    await client.say(embed=embed)
                    m = "```diff"
                    m += "\n- PURGE -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ Channel: {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                    m += "\n+ Number: {}/{}".format(len(deleted), number)
                    m += "\n```"
                    await client.send_message(client.get_channel(logs), m)
                except:
                    deleted = []
                    async for i in client.logs_from(ctx.message.channel, limit=amount):
                        await client.delete_message(i)
                        deleted.append("+1")
                        await asyncio.sleep(float(1.5))
                    embed.description = "<@{}> deleted `{}` messages.".format(author.id, len(deleted))
                    await client.say(embed=embed)
                    m = "```diff"
                    m += "\n- PURGE -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ Channel: {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                    m += "\n+ Number: {}/{}".format(len(deleted), number)
                    m += "\n```"
                    await client.send_message(client.get_channel(logs), m)
            except:
                embed.description = "{} Do you know what a number is?".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by staff.".format(error_e)
        await client.say(embed=embed)

# }nick <user> [nickname]
@client.command(pass_context=True)
async def nick(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [nickname]`.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 32 and args != None:
            embed.description = "{} The nickname cannot be longer than 32 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                await client.change_nickname(user, args)
                if args == None:
                    embed.description = "<@{}> removed <@{}>'s nickname.".format(author.id, user.id)
                else:
                    embed.description = "<@{}> changed **{}**'s nickname to `{}`.".format(author.id, user.name, args)
                    m = "```diff"
                    m += "\n- NICK -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ Target: {} ### {}".format(user, user.id)
                    m += "\n+ Nickname: {}".format(args)
                    m += "\n```"
                    await client.send_message(client.get_channel(logs), m)
                await client.say(embed=embed)
            except:
                embed.description = "{} I was unable to edit <@{}>'s nickname.".format(error_e, user.id)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by staff.".format(error_e)
        await client.say(embed=embed)

''' COMMANDS FOR MODS '''

# }ban <user> [reason]
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [reason]`.".format(error_e)
            await client.say(embed=embed)
        elif helper in user.roles or mod in user.roles or admin in user.roles or manager in user.roles or owner in user.roles:
            embed.description = "{} Other staff can only be banned manually.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                await client.ban(user)
                if args == None:
                    reason = "?"
                else:
                    reason = args
                embed.description = "<@{}> banned **{}**.\nReason: {}".format(author.id, user, reason)
                await client.say(embed=embed)
                m = "```diff"
                m += "\n- BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n+ Reason:"
                m += "\n{}".format(reason)
                m += "\n```"
                await client.send_message(client.get_channel(logs), m)
            except:
                embed.description = "{} I am unable to ban that user.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Moderators, Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=embed)

# }unban <user id>
@client.command(pass_context=True)
async def unban(ctx, ID = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if ID == None:
            embed.description = "{} Please give the user ID you want to unban.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                user = await client.get_user_info(ID)
                try:
                    await client.unban(ctx.message.server, user)
                    embed.description = "<@{}> unbanned **{}**.".format(author.id, user)
                    await client.say(embed=embed)
                    m = "```diff"
                    m += "\n- UNBAN -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ Target: {} ### {}".format(user, user.id)
                    m += "\n```"
                    await client.send_message(client.get_channel(logs), m)
                except:
                    embed.description = "{} The user with that ID is not banned.".format(error_e)
                    await client.say(embed=embed)
            except:
                embed.description = "{} A user with that ID was not found.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Moderators, Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=embed)

# }tempban <user> <minutes> [reason]
@client.command(pass_context=True)
async def tempban(ctx, user: discord.Member = None, time = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or time == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <minutes> [reason]`.".format(error_e)
            await client.say(embed=embed)
        elif helper in user.roles or mod in user.roles or admin in user.roles or manager in user.roles or owner in user.roles:
            embed.description = "{} Other staff can only be banned manually.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250 and args != None:
            embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                time2 = int(time)
                if time2 > 600 or time2 < 1:
                    embed.description = "{} You cannot tempban someone for longer than 600 minutes and shorter than 1 minute.".format(error_e)
                    await client.say(embed=embed)
                else:
                    try:
                        await client.ban(user)
                        if args == None:
                            reason = "?"
                        else:
                            reason = args
                        embed.description = "<@{}> tempbanned **{}** for `{}` minute(s).\nReason: {}".format(author.id, user, time, reason)
                        await client.say(embed=embed)
                        m = "```diff"
                        m += "\n- TEMPBAN -"
                        m += "\n+ Author: {} ### {}".format(author, author.id)
                        m += "\n+ Target: {} ### {}".format(user, user.id)
                        m += "\n+ Time: {} minute(s)".format(time)
                        m += "\n+ Reason:"
                        m += "\n{}".format(reason)
                        m += "\n```"
                        await client.send_message(client.get_channel(logs), m)
                        minutes = time2 * 60
                        await asyncio.sleep(float(minutes))
                        try:
                            await client.unban(ctx.message.server, user)
                            embed.description = "**{}** was automatically unbanned.".format(user)
                            await client.say(embed=embed)
                        except:
                            print("")
                    except:
                        embed.description = "{} I am unable to ban that user.".format(error_e)
                        await client.say(embed=embed)
            except:
                embed.description = "{} The minutes have to be a number.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Moderators, Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=embed)

# }kick <user> [reason]
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
    helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
    if mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [reason]`.".format(error_e)
            await client.say(embed=embed)
        elif helper in user.roles or mod in user.roles or admin in user.roles or manager in user.roles or owner in user.roles:
            embed.description = "{} Other staff can only be kicked manually.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                await client.kick(user)
                if args == None:
                    reason = "?"
                else:
                    reason = args
                embed.description = "<@{}> kicked **{}**.\nReason: {}".format(author.id, user, reason)
                await client.say(embed=embed)
                m = "```diff"
                m += "\n- KICK -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n+ Reason:"
                m += "\n{}".format(reason)
                m += "\n```"
                await client.send_message(client.get_channel(logs), m)
            except:
                embed.description = "{} I am unable to kick that user.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Moderators, Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=embed)

''' COMMANDS FOR ADMINS '''
# }takerole <user> <role name>
@client.command(pass_context=True)
async def takerole(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or args == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [role name]`.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                role = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
                if author.top_role <= role:
                    embed.description = "{} You cannot remove a role that is the same or higher than your top role.".format(error_e)
                    await client.say(embed=embed)
                else:
                    try:
                        await client.remove_roles(user, role)
                        embed.description = "<@{}> removed `{}` from <@{}>'s roles.".format(author.id, args, user.id)
                        await client.say(embed=embed)
                        m = "```diff"
                        m += "\n- TAKE ROLE -"
                        m += "\n+ Author: {} ### {}".format(author, author.id)
                        m += "\n+ Target: {} ### {}".format(user, user.id)
                        m += "\n+ Role: {}".format(args)
                        m += "\n```"
                        await client.send_message(client.get_channel(logs), m)
                    except:
                        embed.description = "{} There was an error while trying to edit that user's roles.".format(error_e)
                        await client.say(embed=embed)
            except:
                embed.description = "{} A role with that name was not found.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=embed)

# }giverole <user> <role name>
@client.command(pass_context=True)
async def giverole(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or args == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [role name]`.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                role = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
                if author.top_role <= role:
                    embed.description = "{} You cannot give a role that is the same or higher than your top role.".format(error_e)
                    await client.say(embed=embed)
                else:
                    try:
                        await client.add_roles(user, role)
                        embed.description = "<@{}> added `{}` to <@{}>'s roles.".format(author.id, args, user.id)
                        await client.say(embed=embed)
                        m = "```diff"
                        m += "\n- GIVE ROLE -"
                        m += "\n+ Author: {} ### {}".format(author, author.id)
                        m += "\n+ Target: {} ### {}".format(user, user.id)
                        m += "\n+ Role: {}".format(args)
                        m += "\n```"
                        await client.send_message(client.get_channel(logs), m)
                    except:
                        embed.description = "{} There was an error while trying to edit that user's roles.".format(error_e)
                        await client.say(embed=embed)
            except:
                embed.description = "{} A role with that name was not found.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Administrators, Managers and Owners.".format(error_e)
        await client.say(embed=embed)

''' COMMANDS FOR MANAGERS '''
# }idban <user id> <reason>
@client.command(pass_context=True)
async def idban(ctx, target = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    if manager in author.roles or owner in author.roles:
        if target == None or args == None:
            embed.description = "{} The command was used incorrectly.\nProper usage: `<user ID> <reason>`.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250:
            embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            try:
                user = await client.get_user_info(target)
                await client.http.ban(target, ctx.message.server.id, 0)
                embed.description = "<@{}> ID banned **{}**.\nReason: {}".format(author.id, user, args)
                await client.say(embed=embed)
                m = "```diff"
                m += "\n- ID BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n+ Reason:"
                m += "\n{}".format(args)
                m += "\n```"
                await client.send_message(client.get_channel(logs), m)
            except:
                embed.description = "{} Either I cannot ban the user with that ID or that user ID does not exist.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Managers and Owners.".format(error_e)
        await client.say(embed=embed)


#######################
client.run(os.environ['BOT_TOKEN'])
