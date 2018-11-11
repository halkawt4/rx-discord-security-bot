print("Starting...")
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
version = "2.0"

warns_chnl = '506089510292029450'
warns = []
muted_list = []
joined = []

loading_e = '<a:loading:484705261609811979>'
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
reload_e = "<:reload:510828383765135360>"
worked_e = "<:worked:511106249895444490>"

help1 = "```diff"
help1 += "\n--- COMMANDS FOR EVERYONE ---"
help1 += "\nxm!ping"
help1 += "\n-    Pings the bot. Used to check if the bot is lagging."
help1 += "\n"
help1 += "\n--- COMMANDS FOR SERVER STAFF ---"
help1 += "\nxm!cb"
help1 += "\n-    Removes the latest messages sent by bots."
help1 += "\nxm!mute <user> <minutes> [reason]"
help1 += "\n-    Mutes the mentioned user for the specified amount of minutes."
help1 += "\nxm!unmute <user>"
help1 += "\n-    Unmutes the mentioned user."
help1 += "\nxm!warn <user> <reason>"
help1 += "\n-    Warns the mentioned user."
help1 += "\nxm!check <user>"
help1 += "\n-    Gives you a list of warnings for the mentioned user."
help1 += "\nxm!clear <user> <warn number/all>"
help1 += "\n-    Clears all or a specified warning for the mentioned user."
help1 += "\nxm!purge <number>"
help1 += "\n-    Deletes the given amount of messages."
help1 += "\nxm!nick <user> [nickname]"
help1 += "\n-    Changes the nickname of the mentioned user or removes it if no nickname is given."
help1 += "\nxm!ban <user> <reason>"
help1 += "\n-    Bans the mentioned user."
help1 += "\nxm!unban <user ID>"
help1 += "\n-    Unbans the user with the matching ID as the one given."
help1 += "\nxm!kick <user> <reason>"
help1 += "\n-    Kicks the mentioned user."
help1 += "\n"
help1 += "\n--- COMMANDS FOR OWNERS ---"
help1 += "\nxm!takerole <user> <role name>"
help1 += "\n-    Removes a role from the mentioned user."
help1 += "\nxm!giverole <user> <role name>"
help1 += "\n-    Adds a role to the mentioned user."
help1 += "\nxm!idban <user ID> <reason>"
help1 += "\n-    Bans the user with the matching ID as the one given, their IP and all their alts that aren't already in the server. Works even if the user isn't in the server."
help1 += "\n```"

owners_role = "510748756858109953"
xbots_role = "510749122257485835"
staff_role = "510748890883031050"
support_role = "510749024114966528"
members_role = "510749251777855488"
announcement_role = "510752070522109952"
partners_role = "510787027051085834"
muted_role = "510753281945894923"
splitter = "**~~`====================`~~**"
log_chnl = "510765922152218637"

''''''

# START UP SYSTEM
started = []
@client.event
async def on_ready():
    async for i in client.logs_from(client.get_channel(warns_chnl), limit=limit):
        a = i.content.split(' | ')
        warns.append(a[0])
    print("[START UP] Loaded warnings.")
    server = client.get_server('452865346081128448')
    mute = discord.utils.get(server.roles, id=muted_role)
    try:
        for i in server.members:
            if mute in i.roles:
                await client.remove_roles(i, mute)
                print("[START UP] Unmuted {}".format(i.id))
    except:
        print("[START UP] Error in unmuting everyone.")
    started.append("+1")
    print("[START UP] Finished.")
    await client.change_presence(game=discord.Game(name="}help | }invite"))
    m = splitter
    m += "\n{} **__Bot Restart__** {} `-` Version: {}".format(log_e, reload_e, version)
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel('510765922152218637'))
    t2 = time.perf_counter()
    m += "\n{} Ping: `{}ms`".format(pingok_e, round((t2-t1)*1000))
    m += "\n{} Warnings: `{}`".format(warn_e, len(warns))
    await client.send_message(client.get_channel(log_chnl), m)

# ANTI MUTE BYPASS / ANTI JOIN-LEAVE RAID / ANTI ADVERTISE SYSTEMS
@client.async_event
async def on_member_join(userName: discord.User):
    joined.append(userName.id)
    server = userName.server
    if userName.id in muted_role:
        try:
            await client.add_roles(server.get_member(userName.id), discord.utils.get(server.roles, id=muted_role))
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
        await client.send_message(client.get_channel('510747587071180801'), embed=embed)
        m = splitter
        m += "\n{} **__Auto Ban__** {}".format(log_e, auto_e)
        m += "\n`Target:` {} ### {}".format(userName, userName.id)
        m += "\n`Reason:` Possible raid attempt."
        await client.send_message(client.get_channel(log_chnl), m)
        async for i in client.logs_from(client.get_channel('510747587071180801'), limit=25):
            if userName.name in str(i.content) or i.author.id == userName.id or userName.id in str(i.content):
                await client.delete_message(i)
        async for i in client.logs_from(client.get_channel('510747536823418880'), limit=25):
            if userName.name in str(i.content):
                await client.delete_message(i)
    if 'gg/' in str(userName.name):
        try:
            await client.kick(userName)
            embed.description = "{} User with ID **{}** has been automatically kicked.\nReason: Advertising by name.".format(auto_e, userName.id)
            await client.send_message(client.get_channel('510747587071180801'), embed=embed)
            m = "{}".format(splitter)
            m += "\n{} **__Auto Kick__** {}".format(log_e, auto_e)
            m += "\n`Target:` {} ### {}".format(userName, userName.id)
            m += "\n`Reason:` Advertising by name."
            await client.send_message(client.get_channel(logs), m)
        except:
            print("")
        async for i in client.logs_from(client.get_channel('510747587071180801'), limit=25):
            if userName.name in str(i.content) or i.author.id == userName.id or userName.id in str(i.content):
                await client.delete_message(i)
        async for i in client.logs_from(client.get_channel('510747536823418880'), limit=25):
            if userName.name in str(i.content):
                await client.delete_message(i)


''' COMMANDS FOR EVERYONE '''
client.remove_command('help')

# }ping <option>
@client.command(pass_context=True)
async def ping(ctx, option = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
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
            
# }help
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        if 'xm!' in str(ctx.message.content):
            try:
                await client.send_message(ctx.message.author, help1)
                embed.description = "{} A list of commands has been sent to your DMs.".format(worked_e)
                await client.say(embed=embed)
            except:
                embed.description = "{} I was unable to DM you my list of commands.".format(error_e)
                await client.say(embed=embed)

''' COMMANDS FOR STAFF '''

# }cb
@client.command(pass_context=True)
async def cb(ctx):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if owner in author.roles or staff in author.roles:
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
                embed.description = "{} **{}** removed the latest messages sent by bots.".format(clearbots_e, author.name)
                await client.edit_message(h, embed=embed)
            except:
                for i in msgs:
                    await client.delete_message(i)
                embed.description = "{} **{}** removed the latest messages sent by bots.".format(clearbots_e, author.name)
                await client.edit_message(h, embed=embed)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }mute <user> <minutes> [reason]
@client.command(pass_context=True)
async def mute(ctx, user: discord.Member = None, time = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        muted = discord.utils.get(ctx.message.server.roles, id=muted_role)
        if owner in author.roles or staff in author.roles:
            if user == None or time == None:
                embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <minutes> [reason]`.".format(error_e)
                await client.say(embed=embed)
            elif owner in user.roles or staff in user.roles:
                embed.description = "{} Other server staff cannot be muted.".format(error_e)
                await client.say(embed=embed)
            elif muted in user.roles:
                embed.description = "{} That user is already muted.".format(error_e)
                await client.say(embed=embed)
            elif len(str(args)) > 250 and args != None:
                embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    time2 = int(time)
                    if time2 > 600 or time2 < 1:
                        embed.description = "{} You cannot mute someone for longer than 600 minutes and shorter than 1 minute.".format(error_e)
                        await client.say(embed=embed)
                    else:
                        await client.add_roles(user, muted)
                        muted_list.append(user.id)
                        minutes = time2 * 60
                        if args == None:
                            reason = "?"
                        else:
                            reason = args
                        embed.description = "{} **{}** muted **{}** for `{}` minute(s).\nReason: {}".format(muted_e, author.name, user.name, time, reason)
                        await client.say(embed=embed)
                        m = splitter
                        m += "\n{} **__Mute__** {}".format(log_e, muted_e)
                        m += "\n`Author:` {} ### {}".format(author, author.id)
                        m += "\n`Target:` {} ### {}".format(user, user.id)
                        m += "\n`Time:` {} minute(s)".format(time)
                        m += "\n`Reason:` {}".format(reason)
                        await client.send_message(client.get_channel(log_chnl), m)
                        await asyncio.sleep(float(minutes))
                        try:
                            try:
                                muted_list.remove(user.id)
                            except:
                                print("")
                            if muted in user.roles:
                                await client.remove_roles(user, muted)
                                embed.description = "{} **{}** was automatically unmuted.".format(unmuted_e, user.name)
                                await client.say(embed=embed)
                        except:
                            print("")
                except:
                    embed.description = "{} The minutes have to be a number.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }unmute <user>
@client.command(pass_context=True)
async def unmute(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        muted = discord.utils.get(ctx.message.server.roles, id=muted_role)
        if owner in author.roles or staff in author.roles:
            if user == None:
                embed.description = "{} Please mention the user you want to unmute.".format(error_e)
                await client.say(embed=embed)
            elif muted in user.roles:
                try:
                    punished_list.remove(user.id)
                except:
                    print("")
                await client.remove_roles(user, muted)
                embed.description = "{} **{}** unmuted **{}**.".format(unmuted_e, author.name, user.name)
                await client.say(embed=embed)
                m = splitter
                m += "\n{} **__Unmute__** {}".format(log_e, unmuted_e)
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                await client.send_message(client.get_channel(log_chnl), m)
            else:
                embed.description = "{} That user is not muted.".format(error_e)
                await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }warn <user> <reason>
@client.command(pass_context=True)
async def warn(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if staff in author.roles or owner in author.roles:
            if user == None or args == None:
                embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <reason>`.".format(error_e)
                await client.say(embed=embed)
            elif staff in user.roles or owner in user.roles or user.bot:
                embed.description = "{} Other server staff and bots cannot be warned.".format(error_e)
                await client.say(embed=embed)
            elif len(str(args)) > 250:
                embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
                await client.say(embed=embed)
            else:
                if warns.count(user.id) >= 5:
                    await client.ban(user)
                    embed.description = "{} **{}** has been automatically banned.\nReason: Reached max warnings.".format(auto_e, user)
                    await client.say(embed=embed)
                    m = splitter
                    m += "\n{} **__Auto Ban__** {}".format(log_e, auto_e)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
                    m += "\n`Reason:` Reached max warnings."
                    await client.send_message(client.get_channel(log_chnl), m)
                else:
                    try:
                        embed.description = "{} You have been warned in **Realm ✘**.\nReason: {}".format(warn_e, args)
                        await client.send_message(user, embed=embed)
                        embed.description = "{} **{}** warned **{}**.\nReason: {}".format(warn_e, author.name, user.name, args)
                        await client.say(embed=embed)
                    except:
                        embed.description = "{} **{}** warned **{}**.\nReason: {}".format(warn_e, author.name, user.name, args)
                        await client.say("<@{}>".format(user.id), embed=embed)
                    warns.append(user.id)
                    await client.send_message(client.get_channel(warns_chnl), "{} | {} ### {} | {}".format(user.id, author, author.id, args))
                    m = splitter
                    m += "\n{} **__Warning__** {}".format(log_e, warn_e)
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
                    m += "\n`Reason:` {}".format(args)
                    await client.send_message(client.get_channel(log_chnl), m)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }check <user>
@client.command(pass_context=True)
async def check(ctx, user: discord.Member = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if staff in author.roles or owner in author.roles:
            if user == None:
                embed.description = "{} Please mention the user you want to check.".format(error_e)
                await client.say(embed=embed)
            else:
                if warns.count(user.id) == 0:
                    embed.description = "{} No warnings found for **{}**.".format(checking_e, user.name)
                    await client.say(embed=embed)
                else:
                    embed.description = "{} Checking warnings... {}".format(checking_e, loading_e)
                    h = await client.say(embed=embed)
                    p = []
                    embed2 = discord.Embed(colour=0x7F1100)
                    embed2.set_footer(text=footer_text)
                    embed2.description = "{} Warning data for **{}** ( `{}` ):".format(checking_e, user, user.id)
                    async for i in client.logs_from(client.get_channel(warns_chnl), limit=limit):
                        a = i.content.split(' | ')
                        p.append("+1")
                        if a[0] == user.id:
                            embed2.add_field(name="{} **__Warning Number:__** `{}`".format(warn_e, i.id), value="`Warned by:` {}\n`Reason:` {}".format(a[1], a[2]))
                    try:
                        await client.send_message(author, embed=embed2)
                        embed.description = "{} The warning data for **{}** has been sent to **{}**'s DMs.".format(checking_e, user.name, author.name)
                        await client.edit_message(h, embed=embed)
                    except:
                        await client.edit_message(h, embed=embed2)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }clear <user> <warn number/all>
@client.command(pass_context=True)
async def clear(ctx, user: discord.Member = None, target = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if staff in author.roles or owner in author.roles:
            if user == None or target == None:
                embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <warn number/all>`.".format(error_e)
                await client.say(embed=embed)
            elif warns.count(user.id) == 0:
                embed.description = "{} No warnings found for **{}**.".format(clear_e, user.name)
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
                embed.description = "{} **{}** cleared `{}` warning(s) for **{}**.".format(clear_e, author.name, len(o), user.name)
                await client.edit_message(h, embed=embed)
                m = splitter
                m += "\n{} **__Clear Warnings__** {}".format(log_e, clear_e)
                m += "\n`Author:` {} ### {}".format(author, author.id)
                m += "\n`Target:` {} ### {}".format(user, user.id)
                m += "\n`Number:` {} (all)".format(len(o))
                await client.send_message(client.get_channel(log_chnl), m)
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
                    embed.description = "{} A warning with that number was not found.".format(error_e)
                    await client.edit_message(h, embed=embed)
                else:
                    embed.description = "{} **{}** cleared `1` warning for **{}**.".format(clear_e, author.name, user.name)
                    await client.edit_message(h, embed=embed)
                    m = splitter
                    m += "\n{} **__Clear Warnings__** {}".format(log_e, clear_e)
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
                    m += "\n`Number:` {}".format(len(o))
                    await client.send_message(client.get_channel(log_chnl), m)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }purge <number>
@client.command(pass_context=True)
async def purge(ctx, number = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if staff in author.roles or owner in author.roles:
            if number == None:
                embed.description = "{} Please give the number of messages you want to delete.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    amount = int(number)
                    try:
                        await client.delete_message(ctx.message)
                        deleted = await client.purge_from(ctx.message.channel, limit=amount)
                        embed.description = "{} **{}** deleted `{}` messages.".format(purge_e, author.name, len(deleted))
                        await client.say(embed=embed)
                        m = splitter
                        m += "\n{} **__Purge__** {}".format(log_e, purge_e)
                        m += "\n`Author:` {} ### {}".format(author, author.id)
                        m += "\n`Channel:` {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                        m += "\n`Number:` {}/{}".format(len(deleted), number)
                        await client.send_message(client.get_channel(log_chnl), m)
                    except:
                        deleted = []
                        await client.delete_message(ctx.message)
                        async for i in client.logs_from(ctx.message.channel, limit=amount):
                            await client.delete_message(i)
                            deleted.append("+1")
                            await asyncio.sleep(float(1.25))
                        embed.description = "{} **{}** deleted `{}` messages.".format(purge_e, author.name, len(deleted))
                        await client.say(embed=embed)
                        m = splitter
                        m += "\n{} **__Purge__** {}".format(log_e, purge_e)
                        m += "\n`Author:` {} ### {}".format(author, author.id)
                        m += "\n`Channel:` {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                        m += "\n`Number:` {}/{}".format(len(deleted), number)
                        await client.send_message(client.get_channel(log_chnl), m)
                except:
                    embed.description = "{} That is not a valid number.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by staff.".format(error_e)
            await client.say(embed=embed)

# }nick <user> [nickname]
@client.command(pass_context=True)
async def nick(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if staff in author.roles or owner in author.roles:
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
                        embed.description = "{} **{}** removed **{}**'s nickname.".format(nick_e, author.name, user.name)
                    else:
                        embed.description = "{} **{}** changed **{}**'s nickname to `{}`.".format(nick_e, author.name, user.name, args)
                        m = splitter
                        m += "\n{} **__Nickname__** {}".format(log_e, nick_e)
                        m += "\n`Author:` {} ### {}".format(author, author.id)
                        m += "\n`Target:` {} ### {}".format(user, user.id)
                        m += "\n`Nickname:` {}".format(args)
                        await client.send_message(client.get_channel(log_chnl), m)
                    await client.say(embed=embed)
                except:
                    embed.description = "{} I was unable to edit **{}**'s nickname.".format(error_e, user.name)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }ban <user> <reason>
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if staff in author.roles or owner in author.roles:
            if user == None or args == None:
                embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <reason>`.".format(error_e)
                await client.say(embed=embed)
            elif staff in user.roles or owner in user.roles:
                embed.description = "{} Other staff can only be banned manually.".format(error_e)
                await client.say(embed=embed)
            elif len(str(args)) > 250:
                embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    await client.ban(user)
                    embed.description = "{} **{}** banned **{}**.\nReason: {}".format(ban_e, author.name, user, args)
                    await client.say(embed=embed)
                    m = splitter
                    m += "\n{} **__Ban__** {}".format(log_e, ban_e)
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
                    m += "\n`Reason:` {}".format(args)
                    await client.send_message(client.get_channel(logs), m)
                except:
                    embed.description = "{} I am unable to ban that user.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }unban <user id>
@client.command(pass_context=True)
async def unban(ctx, ID = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if staff in author.roles or owner in author.roles:
            if ID == None:
                embed.description = "{} Please give the user ID you want to unban.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    user = await client.get_user_info(ID)
                    try:
                        await client.unban(ctx.message.server, user)
                        embed.description = "{} **{}** unbanned **{}**.".format(unban_e, author.name, user)
                        await client.say(embed=embed)
                        m = splitter
                        m += "\n{} **__Unban__** {}".format(log_e, unban_e)
                        m += "\n`Author:` {} ### {}".format(author, author.id)
                        m += "\n`Target:` {} ### {}".format(user, user.id)
                        await client.send_message(client.get_channel(log_chnl), m)
                    except:
                        embed.description = "{} The user with that ID is not banned.".format(error_e)
                        await client.say(embed=embed)
                except:
                    embed.description = "{} A user with that ID was not found.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

# }kick <user> <reason>
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if staff in author.roles or owner in author.roles:
            if user == None or args == None:
                embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [reason]`.".format(error_e)
                await client.say(embed=embed)
            elif staff in user.roles or owner in user.roles:
                embed.description = "{} Other staff can only be kicked manually.".format(error_e)
                await client.say(embed=embed)
            elif len(str(args)) > 250:
                embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
                await client.say(embed=embed)
            else:
                try:
                    await client.kick(user)
                    embed.description = "{} **{}** kicked **{}**.\nReason: {}".format(kick_e, author.name, user, reason)
                    await client.say(embed=embed)
                    m = splitter
                    m += "\n{} **__Kick__** {}".format(log_e, kick_e)
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
                    m += "\n`Reason:` {}".format(args)
                    await client.send_message(client.get_channel(log_chnl), m)
                except:
                    embed.description = "{} I am unable to kick that user.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by the server staff.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR OWNERS '''

# }takerole <user> <role name>
@client.command(pass_context=True)
async def takerole(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        if owner in author.roles:
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
                                embed.description = "{} **{}** removed `{}` from **{}**'s roles.".format(takerole_e, author.id, i.name, user.name)
                                await client.say(embed=embed)
                                m = splitter
                                m += "\n{} **__Take Role__** {}".format(log_e, takerole_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Target:` {} ### {}".format(user, user.id)
                                m += "\n`Role:` {}".format(i.name)
                                await client.send_message(client.get_channel(log_chnl), m)
                            except:
                                embed.description = "{} There was an error while trying to edit that user's roles.".format(error_e)
                                await client.say(embed=embed)
                            break
                if len(a) == 0:
                    embed.description = "{} A role with that name was not found.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)

# }giverole <user> <role name>
@client.command(pass_context=True)
async def giverole(ctx, user: discord.Member = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        if owner in author.roles:
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
                                embed.description = "{} **{}** added `{}` to **{}**'s roles.".format(giverole_e, author.name, i.name, user.name)
                                await client.say(embed=embed)
                                m = splitter
                                m += "\n{} **__Give Role__** {}".format(log_e, giverole_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Target:` {} ### {}".format(user, user.id)
                                m += "\n`Role:` {}".format(i.name)
                                await client.send_message(client.get_channel(log_chnl), m)
                            except:
                                embed.description = "{} There was an error while trying to edit that user's roles.".format(error_e)
                                await client.say(embed=embed)
                            break
                if len(a) == 0:
                    embed.description = "{} A role with that name was not found.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)
        
# }idban <user id> <reason>
@client.command(pass_context=True)
async def idban(ctx, target = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        owner = discord.utils.get(ctx.message.server.roles, id=owners_role)
        staff = discord.utils.get(ctx.message.server.roles, id=staff_role)
        if owner in author.roles:
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
                    embed.description = "{} **{}** ID banned **{}**.\nReason: {}".format(idban_e, author.name, user, args)
                    await client.say(embed=embed)
                    m = splitter
                    m += "\n{} **__ID Ban__** {}".format(log_e, idban_e)
                    m += "\n`Author:` {} ### {}".format(author, author.id)
                    m += "\n`Target:` {} ### {}".format(user, user.id)
                    m += "\n`Reason:`".format(args)
                    await client.send_message(client.get_channel(log_chnl), m)
                except:
                    embed.description = "{} Either I cannot ban the user with that ID or that user ID does not exist.".format(error_e)
                    await client.say(embed=embed)
        else:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)


#######################
client.run(os.environ['BOT_TOKEN'])
