import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os
import time

''''''

Client = discord.Client()
bot_prefix = ["xm!", "}"]
client = commands.Bot(command_prefix=bot_prefix)
footer_text = "[Realm X] - [X Moderation]"
limit = 1000000000000

warns_chnl = '506089510292029450'
warns = []

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
splitter = "**`====================`**"
punished_list = []
joined = []

''''''

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    async for i in client.logs_from(client.get_channel(warns_chnl), limit=limit):
        a = i.content.split(' | ')
        warns.append(a[0])
        print("[START UP] Warning Added: {}".format(len(warns)))
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
    await client.change_presence(game=discord.Game(name="}help | }invite"))

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
        embed.description = "<:auto:506092657932500993> **{}** has been automatically banned.\nReason: Possible raid attempt.".format(userName)
        await client.send_message(client.get_channel('453192466716164137'), embed=embed)
        m = "{}".format(splitter)
        m += "\n<:log:506091764415725579> **__Auto Ban__** <:auto:506092657932500993>"
        m += "\n`Target:` {} ### {}".format(userName, userName.id)
        m += "\n`Reason:`"
        m += "\nPossible raid attempt."
        await client.send_message(client.get_channel(logs), m)
        async for i in client.logs_from(client.get_channel('453192466716164137'), limit=25):
            if userName.name in str(i.content) or i.author.id == userName.id or userName.id in str(i.content):
                await client.delete_message(i)
        async for i in client.logs_from(client.get_channel('453192385795588096'), limit=25):
            if userName.name in str(i.content):
                await client.delete_message(i)
    if 'gg/' in str(userName.name):
        try:
            await client.kick(userName)
            embed.description = "<:auto:506092657932500993> User with ID **{}** has been automatically kicked.\nReason: Advertising by name.".format(userName.id)
            await client.send_message(client.get_channel('453192466716164137'), embed=embed)
            m = "{}".format(splitter)
            m += "\n<:log:506091764415725579> **__Auto Kick__** <:auto:506092657932500993>"
            m += "\n`Target:` {} ### {}".format(userName, userName.id)
            m += "\n`Reason:`"
            m += "\nAdvertising by name."
            await client.send_message(client.get_channel(logs), m)
        except:
            print("")
        async for i in client.logs_from(client.get_channel('453192466716164137'), limit=25):
            if userName.name in str(i.content) or i.author.id == userName.id or userName.id in str(i.content):
                await client.delete_message(i)
        async for i in client.logs_from(client.get_channel('453192385795588096'), limit=25):
            if userName.name in str(i.content):
                await client.delete_message(i)


''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }ping <option>
@client.command(pass_context=True)
async def ping(ctx, option = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    t1 = time.perf_counter()
    await client.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    ping = round((t2-t1)*1000)
    if ping > 300:
        m = "<:pingbad:506094169379569666> The bot is lagging."
    elif ping > 200:
        m = "<:pingok:506094170050658307> The bot might be lagging."
    else:
        m = "<:pinggood:506094169840812032> The bot isn't lagging."
    if '}' in str(ctx.message.content):
        if option == "all" or option == "m":
            embed.description = "My ping is `{}`ms.\n{}".format(ping, m)
            await client.say(embed=embed)
    else:
        embed.description = "My ping is `{}`ms.\n{}".format(ping, m)
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
        embed.description = "<:clearbots:506096652231114753> Deleting latest messages sent by bots... {}".format(loading_e)
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
            embed.description = "<:clearbots:506096652231114753> <@{}> removed the latest messages sent by bots.".format(author.id)
            await client.edit_message(h, embed=embed)
        except:
            for i in msgs:
                await client.delete_message(i)
            embed.description = "<:clearbots:506096652231114753> <@{}> removed the latest messages sent by bots.".format(author.id)
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
                    embed.description = "<:muted:506097765156126724> <@{}> punished <@{}> for `{}` minute(s).\nReason: {}".format(author.id, user.id, time, reason)
                    await client.say(embed=embed)
                    m = "{}".format(splitter)
                    m += "\n<:log:506091764415725579> **__Punish__** <:muted:506097765156126724>"
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
                    m += "\n`Time:` {} minute(s)".format(time)
                    m += "\n`Reason:`"
                    m += "\n{}".format(reason)
                    await client.send_message(client.get_channel(logs), m)
                    await asyncio.sleep(float(minutes))
                    try:
                        try:
                            punished_list.remove(user.id)
                        except:
                            print("")
                        if punished in user.roles:
                            await client.remove_roles(user, punished)
                            embed.description = "<:unmuted:506098845088743441> <@{}> was automatically pardoned.".format(user.id)
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
            embed.description = "<:unmuted:506098845088743441> <@{}> pardoned <@{}>.".format(author.id, user.id)
            await client.say(embed=embed)
            m = "{}".format(splitter)
            m += "\n<:log:506091764415725579> **__Pardon__** <:unmuted:506098845088743441>"
            m += "\n`Author:` {} ### {}".format(author, author.id)
            m += "\n`Target:` {} ### {}".format(user, user.id)
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
        elif helper in user.roles or mod in user.roles or admin in user.roles or manager in user.roles or owner in user.roles:
            embed.description = "{} Other staff cannot be warned.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 250:
            embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            a = []
            for i in warns:
                if i == user.id:
                    a.append("+1")
            if len(a) >= 5:
                await client.ban(user)
                embed.description = "<:auto:506092657932500993> **{}** has been automatically banned.\nReason: Reached max warnings.".format(user)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n<:log:506091764415725579> **__Auto Ban__** <:auto:506092657932500993>"
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Reason:`"
                m += "\nReached max warnings."
                await client.send_message(client.get_channel(logs), m)
            else:
                try:
                    embed.description = "<:warn:506101565841735680> You have been warned in **Realm ✘**.\nReason: {}".format(args)
                    await client.send_message(user, embed=embed)
                    embed.description = "<:warn:506101565841735680> <@{}> warned <@{}>.\nReason: {}".format(author.id, user.id, args)
                    await client.say(embed=embed)
                except:
                    embed.description = "<:warn:506101565841735680> <@{}> warned <@{}>.\nReason: {}".format(author.id, user.id, args)
                    await client.say("<@{}>".format(user.id), embed=embed)
                warns.append(user.id)
                await client.send_message(client.get_channel(warns_chnl), "{} | {} ### {} | {}".format(user.id, author, author.id, args))
                m = "{}".format(splitter)
                m += "\n<:log:506091764415725579> **__Warning__** <:warn:506101565841735680>"
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Reason:`"
                m += "\n{}".format(args)
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
            embed.description = "<:checking:506104792070881311> Checking warnings... {}".format(loading_e)
            h = await client.say(embed=embed)
            p = []
            embed2 = discord.Embed(colour=0x7F1100)
            embed2.set_footer(text=footer_text)
            embed2.description = "<:checking:506104792070881311> Warning data for **{}** ( `{}` ):".format(user, user.id)
            async for i in client.logs_from(client.get_channel(warns_chnl), limit=10000000):
                a = i.content.split(' | ')
                p.append("+1")
                if a[0] == user.id:
                    embed2.add_field(name="<:warn:506101565841735680> **__Warning Number:__** `{}`".format(i.id), value="`Warned by:` {}\n`Reason:` {}".format(a[1], a[2]))
            if len(p) == 0:
                embed.description = "<:checking:506104792070881311> No warnings found for <@{}>.".format(user.id)
                await client.edit_message(h, embed=embed)
            else:
                try:
                    await client.send_message(author, embed=embed2)
                    embed.description = "<:checking:506104792070881311> The warning data for <@{}> has been sent to <@{}>'s DMs.".format(user.id, author.id)
                    await client.edit_message(h, embed=embed)
                except:
                    embed.description = "{} Please give me permissions to DM you and try again.".format(error_e)
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
            embed.description = "<:clear:506108172562333696> Checking warnings... {}".format(loading_e)
            h = await client.say(embed=embed)
            o = []
            async for i in client.logs_from(client.get_channel(warns_chnl), limit=10000000):
                a = i.content.split(' | ')
                if a[0] == user.id:
                    await client.delete_message(i)
                    o.append("+1")
            if len(o) == 0:
                embed.description = "<:clear:506108172562333696> No warnings found for <@{}>.".format(user.id)
            else:
                embed.description = "<@{}> cleared `{}` warning(s) for <@{}>.".format(author.id, len(o), user.id)
                m = "{}".format(splitter)
                m += "\n<:log:506091764415725579> **__Clear Warnings__** <:clear:506108172562333696>"
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Number:` {} (all)".format(len(o))
                await client.send_message(client.get_channel(logs), m)
            await client.edit_message(h, embed=embed)
        else:
            embed.description = "<:clear:506108172562333696> Checking warnings... {}".format(loading_e)
            h = await client.say(embed=embed)
            o = []
            async for i in client.logs_from(client.get_channel(warns_chnl), limit=10000000):
                a = i.content.split(' | ')
                if a[0] == user.id and i.id == target:
                    await client.delete_message(i)
                    o.append("+1")
                    break
            if len(o) == 0:
                embed.description = "{} A warning with that number hasn't been found.".format(error_e)
            else:
                embed.description = "<:clear:506108172562333696> <@{}> cleared `1` warning for <@{}>.".format(author.id, user.id)
                m = "{}".format(splitter)
                m += "\n<:log:506091764415725579> **__Clear Warnings__** <:clear:506108172562333696>"
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Number:` {}".format(len(o))
                await client.send_message(client.get_channel(logs), m)
            await client.edit_message(h, embed=embed)
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
                    embed.description = "<:purge:506113200094314520> <@{}> deleted `{}` messages.".format(author.id, len(deleted))
                    await client.say(embed=embed)
                    m = "{}".format(splitter)
                    m += "\n<:log:506091764415725579> **__Purge__** <:purge:506113200094314520>"
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Channel:` {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                    m += "\n`Number:` {}/{}".format(len(deleted), number)
                    await client.send_message(client.get_channel(logs), m)
                except:
                    deleted = []
                    async for i in client.logs_from(ctx.message.channel, limit=amount):
                        await client.delete_message(i)
                        deleted.append("+1")
                        await asyncio.sleep(float(1.5))
                    embed.description = "<:purge:506113200094314520> <@{}> deleted `{}` messages.".format(author.id, len(deleted))
                    await client.say(embed=embed)
                    m = "{}".format(splitter)
                    m += "\n<:log:506091764415725579> **__Purge__** <:purge:506113200094314520>"
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Channel:` {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                    m += "\n`Number:` {}/{}".format(len(deleted), number)
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
                    embed.description = "<:nick:506115462170542120> <@{}> removed <@{}>'s nickname.".format(author.id, user.id)
                else:
                    embed.description = "<:nick:506115462170542120> <@{}> changed **{}**'s nickname to `{}`.".format(author.id, user.name, args)
                    m = "{}".format(splitter)
                    m += "\n<:log:506091764415725579> **__Nickname__** <:nick:506115462170542120>"
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
                    m += "\n`Nickname:` {}".format(args)
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
                embed.description = "<:ban:506116355318087681> <@{}> banned **{}**.\nReason: {}".format(author.id, user, reason)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n<:log:506091764415725579> **__Ban__** <:ban:506116355318087681>"
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Reason:`"
                m += "\n{}".format(reason)
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
                    embed.description = "<:unban:506116834760720395> <@{}> unbanned **{}**.".format(author.id, user)
                    await client.say(embed=embed)
                    m = "{}".format(splitter)
                    m += "\n<:log:506091764415725579> **__Unban__** <:unban:506116834760720395>"
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
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
                        embed.description = "<:tempban:506117641149087766> <@{}> tempbanned **{}** for `{}` minute(s).\nReason: {}".format(author.id, user, time, reason)
                        await client.say(embed=embed)
                        m = "{}".format(splitter)
                        m += "\n<:log:506091764415725579> **__Tempban__** <:tempban:506117641149087766>"
                        m += "\n`Author:` {} ### {}".format(author, author.id)
                        m += "\n`Target:` {} ### {}".format(user, user.id)
                        m += "\n`Time:` {} minute(s)".format(time)
                        m += "\n`Reason:`"
                        m += "\n{}".format(reason)
                        await client.send_message(client.get_channel(logs), m)
                        minutes = time2 * 60
                        await asyncio.sleep(float(minutes))
                        try:
                            await client.unban(ctx.message.server, user)
                            embed.description = "<:unban:506116834760720395> **{}** was automatically unbanned.".format(user)
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
                embed.description = "<:kick:506118557050863651> <@{}> kicked **{}**.\nReason: {}".format(author.id, user, reason)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n<:log:506091764415725579> **__Kick__** <:kick:506118557050863651>"
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Reason:`"
                m += "\n{}".format(reason)
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
            a = []
            for i in ctx.message.server.roles:
                if args.lower() in str(i.name.lower()):
                    a.append("+1")
                    if author.top_role <= i:
                        embed.description = "{} You cannot remove a role that is the same or higher than your top role.".format(error_e)
                        await client.say(embed=embed)
                        break
                    else:
                        try:
                            await client.remove_roles(user, i)
                            embed.description = "<:takerole:506119899064827905> <@{}> removed `{}` from <@{}>'s roles.".format(author.id, i.name, user.id)
                            await client.say(embed=embed)
                            m = "{}".format(splitter)
                            m += "\n<:log:506091764415725579> **__Take Role__** <:takerole:506119899064827905>"
                            m += "\n`Author:` {} ### {}".format(author, author.id)
                            m += "\n`Target:` {} ### {}".format(user, user.id)
                            m += "\n`Role:` {}".format(i.name)
                            await client.send_message(client.get_channel(logs), m)
                        except:
                            embed.description = "{} There was an error while trying to edit that user's roles.".format(error_e)
                            await client.say(embed=embed)
                        break
            if len(a) == 0:
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
            a = []
            for i in ctx.message.server.roles:
                if args.lower() in str(i.name.lower()):
                    a.append("+1")
                    if author.top_role <= i:
                        embed.description = "{} You cannot give a role that is the same or higher than your top role.".format(error_e)
                        await client.say(embed=embed)
                        break
                    else:
                        try:
                            await client.add_roles(user, i)
                            embed.description = "<:giverole:506119899014496266> <@{}> added `{}` to <@{}>'s roles.".format(author.id, i.name, user.id)
                            await client.say(embed=embed)
                            m = "{}".format(splitter)
                            m += "\n<:log:506091764415725579> **__Give Role__** <:giverole:506119899014496266>"
                            m += "\n`Author:` {} ### {}".format(author, author.id)
                            m += "\n`Target:` {} ### {}".format(user, user.id)
                            m += "\n`Role:` {}".format(i.name)
                            m += "\n```"
                            await client.send_message(client.get_channel(logs), m)
                        except:
                            embed.description = "{} There was an error while trying to edit that user's roles.".format(error_e)
                            await client.say(embed=embed)
                        break
            if len(a) == 0:
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
                await client.http.ban(target, server.id, 0)
                embed.description = "<:idban:506124539277737985> <@{}> ID banned **{}**.\nReason: {}".format(author.id, user, args)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n<:log:506091764415725579> **__ID Ban__** <:idban:506124539277737985>"
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Reason:`"
                m += "\n{}".format(args)
                await client.send_message(client.get_channel(logs), m)
            except:
                embed.description = "{} Either I cannot ban the user with that ID or that user ID does not exist.".format(error_e)
                await client.say(embed=embed)
    else:
        embed.description = "{} This command can only be used by Managers and Owners.".format(error_e)
        await client.say(embed=embed)


#######################
client.run(os.environ['BOT_TOKEN'])
