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

error_e = "<:error:507167378765774858>"
log_e = "<:log:507167379520880640>"
auto_e = "<:auto:507167379344588800>"
pinggood_e = "<:pinggood:507167379533332500>"
pingok_e = "<:pingok:507167378891735041>"
pingbad_e = "<:pingbad:507167378975490076>"
clearbots_e = "<:clearbots:507167378853855233>"
muted_e = "<:muted:507167379227279370>"
unmuted_e = "<:unmuted:507167379349045248>"
warn_e = "<:warn:507167379370016768>"
checking_e = "<:checking:507167378728026136>"
clear_e = "<:clear:507167379072221204>"
purge_e = "<:purge:507167379533332480>"
nick_e = "<:nick:507167378925420546>"
ban_e = "<:ban:507167378417909761>"
unban_e = "<:unban:507167379520749588>"
tempban_e = "<:tempban:507167379365822464>"
kick_e = "<:kick:507167379101450240>"
takerole_e = "<:takerole:507167379201982465>"
giverole_e = "<:giverole:507167378866700315>"
idban_e = "<:idban:507167379109838868>"
promote_e = "<:promote:509729142434955287>"
demote_e = "<:demote:509729142145548309>"

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
        embed.description = "{} **{}** has been automatically banned.\nReason: Possible raid attempt.".format(auto_e, userName)
        await client.send_message(client.get_channel('453192466716164137'), embed=embed)
        m = "{}".format(splitter)
        m += "\n{} **__Auto Ban__** {}".format(log_e, auto_e)
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
            embed.description = "{} User with ID **{}** has been automatically kicked.\nReason: Advertising by name.".format(auto_e, userName.id)
            await client.send_message(client.get_channel('453192466716164137'), embed=embed)
            m = "{}".format(splitter)
            m += "\n{} **__Auto Kick__** {}".format(log_e, auto_e)
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
        m = "{} The bot is lagging.".format(pingbad_e)
    elif ping > 200:
        m = "{} The bot might be lagging.".format(pingok_e)
    else:
        m = "{} The bot isn't lagging.".format(pinggood_e)
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
        embed.description = "{} Deleting latest messages sent by bots... {}".format(clearbots_e, loading_e)
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
            embed.description = "{} <@{}> removed the latest messages sent by bots.".format(clearbots_e, author.id)
            await client.edit_message(h, embed=embed)
        except:
            for i in msgs:
                await client.delete_message(i)
            embed.description = "{} <@{}> removed the latest messages sent by bots.".format(clearbots_e, author.id)
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
                    embed.description = "{} <@{}> punished <@{}> for `{}` minute(s).\nReason: {}".format(muted_e, author.id, user.id, time, reason)
                    await client.say(embed=embed)
                    m = "{}".format(splitter)
                    m += "\n{} **__Punish__** {}".format(log_e, muted_e)
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
                            embed.description = "{} <@{}> was automatically pardoned.".format(unmuted_e, user.id)
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
            embed.description = "{} <@{}> pardoned <@{}>.".format(unmuted_e, author.id, user.id)
            await client.say(embed=embed)
            m = "{}".format(splitter)
            m += "\n{} **__Pardon__** {}".format(log_e, unmuted_e)
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
                embed.description = "{} **{}** has been automatically banned.\nReason: Reached max warnings.".format(auto_e, user)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n{} **__Auto Ban__** {}".format(log_e, auto_e)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Reason:`"
                m += "\nReached max warnings."
                await client.send_message(client.get_channel(logs), m)
            else:
                try:
                    embed.description = "{} You have been warned in **Realm ✘**.\nReason: {}".format(warn_e, args)
                    await client.send_message(user, embed=embed)
                    embed.description = "{} <@{}> warned <@{}>.\nReason: {}".format(warn_e, author.id, user.id, args)
                    await client.say(embed=embed)
                except:
                    embed.description = "{} <@{}> warned <@{}>.\nReason: {}".format(warn_e, author.id, user.id, args)
                    await client.say("<@{}>".format(user.id), embed=embed)
                warns.append(user.id)
                await client.send_message(client.get_channel(warns_chnl), "{} | {} ### {} | {}".format(user.id, author, author.id, args))
                m = "{}".format(splitter)
                m += "\n{} **__Warning__** {}".format(log_e, warn_e)
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
            embed.description = "{} Checking warnings... {}".format(checking_e, loading_e)
            h = await client.say(embed=embed)
            p = []
            embed2 = discord.Embed(colour=0x7F1100)
            embed2.set_footer(text=footer_text)
            embed2.description = "{} Warning data for **{}** ( `{}` ):".format(checking_e, user, user.id)
            async for i in client.logs_from(client.get_channel(warns_chnl), limit=10000000):
                a = i.content.split(' | ')
                p.append("+1")
                if a[0] == user.id:
                    embed2.add_field(name="{} **__Warning Number:__** `{}`".format(warn_e, i.id), value="`Warned by:` {}\n`Reason:` {}".format(a[1], a[2]))
            if len(p) == 0:
                embed.description = "{} No warnings found for <@{}>.".format(checking_e, user.id)
                await client.edit_message(h, embed=embed)
            else:
                try:
                    await client.send_message(author, embed=embed2)
                    embed.description = "{} The warning data for <@{}> has been sent to <@{}>'s DMs.".format(checking_e, user.id, author.id)
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
            embed.description = "{} Checking warnings... {}".format(clear_e, loading_e)
            h = await client.say(embed=embed)
            o = []
            async for i in client.logs_from(client.get_channel(warns_chnl), limit=10000000):
                a = i.content.split(' | ')
                if a[0] == user.id:
                    await client.delete_message(i)
                    o.append("+1")
            if len(o) == 0:
                embed.description = "{} No warnings found for <@{}>.".format(clear_e, user.id)
            else:
                embed.description = "<@{}> cleared `{}` warning(s) for <@{}>.".format(author.id, len(o), user.id)
                m = "{}".format(splitter)
                m += "\n{} **__Clear Warnings__** {}".format(log_e, clear_e)
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Number:` {} (all)".format(len(o))
                await client.send_message(client.get_channel(logs), m)
            await client.edit_message(h, embed=embed)
        else:
            embed.description = "{} Checking warnings... {}".format(clear_e, loading_e)
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
                embed.description = "{} <@{}> cleared `1` warning for <@{}>.".format(clear_e, author.id, user.id)
                m = "{}".format(splitter)
                m += "\n{} **__Clear Warnings__** {}".format(log_e, clear_e)
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
                    embed.description = "{} <@{}> deleted `{}` messages.".format(purge_e, author.id, len(deleted))
                    await client.say(embed=embed)
                    m = "{}".format(splitter)
                    m += "\n{} **__Purge__** {}".format(log_e, purge_e)
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
                    embed.description = "{} <@{}> deleted `{}` messages.".format(purge_e, author.id, len(deleted))
                    await client.say(embed=embed)
                    m = "{}".format(splitter)
                    m += "\n{} **__Purge__** {}".format(log_e, purge_e)
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
                    embed.description = "{} <@{}> removed <@{}>'s nickname.".format(nick_e, author.id, user.id)
                else:
                    embed.description = "{} <@{}> changed **{}**'s nickname to `{}`.".format(nick_e, author.id, user.name, args)
                    m = "{}".format(splitter)
                    m += "\n{} **__Nickname__** {}".format(log_e, nick_e)
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
                embed.description = "{} <@{}> banned **{}**.\nReason: {}".format(ban_e, author.id, user, reason)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n{} **__Ban__** {}".format(log_e, ban_e)
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
                    embed.description = "{} <@{}> unbanned **{}**.".format(unban_e, author.id, user)
                    await client.say(embed=embed)
                    m = "{}".format(splitter)
                    m += "\n{} **__Unban__** {}".format(log_e, unban_e)
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
                        embed.description = "{} <@{}> tempbanned **{}** for `{}` minute(s).\nReason: {}".format(tempban_e, author.id, user, time, reason)
                        await client.say(embed=embed)
                        m = "{}".format(splitter)
                        m += "\n{} **__Tempban__** {}".format(tempban_e)
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
                            embed.description = "{} **{}** was automatically unbanned.".format(unban_e, user)
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
                embed.description = "{} <@{}> kicked **{}**.\nReason: {}".format(kick_e, author.id, user, reason)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n{} **__Kick__** {}".format(log_e, kick_e)
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
                            embed.description = "{} <@{}> removed `{}` from <@{}>'s roles.".format(takerole_e, author.id, i.name, user.id)
                            await client.say(embed=embed)
                            m = "{}".format(splitter)
                            m += "\n{} **__Take Role__** {}".format(log_e, takerole_e)
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
                            embed.description = "{} <@{}> added `{}` to <@{}>'s roles.".format(giverole_e, author.id, i.name, user.id)
                            await client.say(embed=embed)
                            m = "{}".format(splitter)
                            m += "\n{} **__Give Role__** {}".format(log_e, giverole_e)
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

''' COMMANDS FOR MANAGERS '''
# }promote <user> <reason>
@client.command(pass_context=True)
async def promote(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    if manager in author.roles or owner in author.roles:
        if user == None or args == None:
            embed.description = "{} Not all arguments were given.\nProper usage: `<user> <reason>`.".format(error_e)
            await client.say(embed=embed)
        elif user.bot:
            embed.description = "{} Bots cannot be promoted.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 500:
            embed.description = "{} The reason cannot be longer than 500 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "{} Loading...".format(loading_e)
            h = await client.say(embed=embed)
            staff = discord.utils.get(ctx.message.server.roles, id='469224793359646730')
            admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
            mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
            helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
            channel = client.get_channel('505745631386796032')
            roles = {helper : mod,
                     mod: admin,
                     admin: manager}
            o = []
            if helper not in user.roles and mod not in user.roles and admin not in user.roles and manager not in user.roles and owner not in user.roles:
                await client.add_roles(user, staff)
                await asyncio.sleep(1.25)
                await client.add_roles(user, helper)
                embed.description = "{} <@{}> has been promoted to <@&{}> by <@{}>.\n`Reason:` {}".format(promote_e, user.id, helper.id, author.id, args)
                await client.send_message(channel, embed=embed)
                embed.description = "{} <@{}> promoted <@{}> to <@&{}>.".format(promote_e, author.id, user.id, helper.id)
                await client.edit_message(h, embed=embed)
                log = "{}".format(splitter)
                log += "\n{} **__Promote__** {}".format(log_e, promote_e)
                log += "\n`Author:` {} ### {}".format(author, author.id)
                log += "\n`Target:` {} ### {}".format(user, user.id)
                log += "\n`Role:` {}".format(helper.name)
                log += "\n`Reason:` {}".format(args)
                await client.send_message(client.get_channel(logs), log)
            else:
                for i in roles:
                    if i in user.roles:
                        if roles[i] in author.roles:
                            embed.description = "{} You cannot promote users with to the same role as you.".format(error_e)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                        else:
                            await client.remove_roles(user, i)
                            await asyncio.sleep(1.25)
                            await client.add_roles(user, roles[i])
                            embed.description = "{} <@{}> has been promoted to <@&{}> by <@{}>.\n`Reason:` {}".format(promote_e, user.id, roles[i].id, author.id, args)
                            await client.send_message(channel, embed=embed)
                            embed.description = "{} <@{}> promoted <@{}> to <@&{}>.".format(promote_e, author.id, user.id, roles[i].id)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            log = "{}".format(splitter)
                            log += "\n{} **__Promote__** {}".format(log_e, promote_e)
                            log += "\n`Author:` {} ### {}".format(author, author.id)
                            log += "\n`Target:` {} ### {}".format(user, user.id)
                            log += "\n`Role:` {}".format(roles[i].name)
                            log += "\n`Reason:` {}".format(args)
                            await client.send_message(client.get_channel(logs), log)
                            break
                if len(o) == 0:
                    embed.description = "{} There was an error while trying to demote that user.".format(error_e)
                    await client.edit_message(h, embed=embed)
    else:
        embed.description = "{} This command can only be used by Managers and Owners.".format(error_e)
        await client.say(embed=embed)

# }demote <user> <reason>
@client.command(pass_context=True)
async def demote(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, id=owner_role)
    admin = discord.utils.get(ctx.message.server.roles, id=admin_role)
    manager = discord.utils.get(ctx.message.server.roles, id=manager_role)
    if manager in author.roles or owner in author.roles:
        if user == None or args == None:
            embed.description = "{} Not all arguments were given.\nProper usages:\n`<user> <reason>`\n`<user> -all <reason>`.".format(error_e)
            await client.say(embed=embed)
        elif user.bot:
            embed.description = "{} Bots cannot be demoted.".format(error_e)
            await client.say(embed=embed)
        elif len(str(args)) > 500:
            embed.description = "{} The reason cannot be longer than 500 characters.".format(error_e)
            await client.say(embed=embed)
        else:
            embed.description = "{} Loading...".format(loading_e)
            h = await client.say(embed=embed)
            member = discord.utils.get(ctx.message.server.roles, id='453194601247801354')
            staff = discord.utils.get(ctx.message.server.roles, id='469224793359646730')
            mod = discord.utils.get(ctx.message.server.roles, id=mod_role)
            helper = discord.utils.get(ctx.message.server.roles, id=helper_role)
            roles = {helper : member,
                     mod : helper,
                     admin : mod,
                     manager : admin}
            o = []
            channel = client.get_channel('505745631386796032')
            if helper not in user.roles and mod not in user.roles and admin not in user.roles and manager not in user.roles and owner not in user.roles:
                embed.description = "{} That user is not a staff member.".format(error_e)
                await client.edit_message(h, embed=embed)
            else:
                for i in roles:
                    if i in user.roles:
                        if i in author.roles:
                            embed.description = "{} You cannot demote people with the same role as you.".format(error_e)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            break
                        elif '-all' in str(args):
                            await client.remove_roles(user, staff)
                            await asyncio.sleep(1.25)
                            await client.remove_roles(user, i)
                            m = args.replace("-all", "")
                            embed.description = "{} <@{}> has been demoted to <@&{}> by <@{}>.\n`Reason:` {}".format(demote_e, user.id, member.id, author.id, m)
                            await client.send_message(channel, embed=embed)
                            embed.description = "{} <@{}> demoted <@{}> to <@&{}>.".format(demote_e, author.id, user.id, member.id)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            log = "{}".format(splitter)
                            log += "\n{} **__Demote__** {}".format(log_e, demote_e)
                            log += "\n`Author:` {} ### {}".format(author, author.id)
                            log += "\n`Target:` {} ### {}".format(user, user.id)
                            log += "\n`Role:` {}".format(member.name)
                            log += "\n`Reason:` {}".format(m)
                            await client.send_message(client.get_channel(logs), log)
                            break
                        else:
                            await client.remove_roles(user, i)
                            await asyncio.sleep(1.25)
                            await client.add_roles(user, roles[i])
                            if i == helper:
                                await asyncio.sleep(1.25)
                                await client.remove_roles(user, staff)
                            embed.description = "{} <@{}> has been demoted to <@&{}> by <@{}>.\n`Reason:` {}".format(demote_e, user.id, roles[i].id, author.id, args)
                            await client.send_message(channel, embed=embed)
                            embed.description = "{} <@{}> demoted <@{}> to <@&{}>.".format(demote_e, author.id, user.id, roles[i].id)
                            await client.edit_message(h, embed=embed)
                            o.append("+1")
                            log = "{}".format(splitter)
                            log += "\n{} **__Demote__** {}".format(log_e, demote_e)
                            log += "\n`Author:` {} ### {}".format(author, author.id)
                            log += "\n`Target:` {} ### {}".format(user, user.id)
                            log += "\n`Role:` {}".format(roles[i].name)
                            log += "\n`Reason:` {}".format(args)
                            await client.send_message(client.get_channel(logs), log)
                            break
                if len(o) == 0:
                    embed.description = "{} There was an error while trying to demote that user.".format(error_e)
                    await client.edit_message(h, embed=embed)
    else:
        embed.description = "{} This command can only be used by Managers and Owners.".format(error_e)
        await client.say(embed=embed)
        
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
                embed.description = "{} <@{}> ID banned **{}**.\nReason: {}".format(idban_e, author.id, user, args)
                await client.say(embed=embed)
                m = "{}".format(splitter)
                m += "\n{} **__ID Ban__** {}".format(log_e, idban_e)
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
