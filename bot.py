print("Starting X Moderation...")
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
version = "3.0"
splitter = "**~~`====================`~~**"


warns = []
muted_list = []
owner_roles = []
manager_roles = []
admin_roles = []
mod_roles = []
helper_roles = []
muted_roles = []
logs = []

warns_chnl = '506089510292029450'
owner_roles_chnl = '517357850264338433'
manager_roles_chnl = '517357867397808128'
admin_roles_chnl = '517357880672911360'
mod_roles_chnl = '517357889602584596'
helper_roles_chnl = '517357900142870565'
muted_roles_chnl = '517357914009370685'
logs_chnl = '517358120561803279'
log_chnl = '516595345476681758'

loading_e = '<a:loading:484705261609811979>'
error_e = "<:error:517356130968666132>"
log_e = "<:log:517356131115597824>"
auto_e = "<:auto:517356130557755396>"
pinggood_e = "<:pinggood:517356130855550977>"
pingok_e = "<:pingok:517356130918203394>"
pingbad_e = "<:pingbad:517356131086106624>"
clearbots_e = "<:clearbots:517356130855419934>"
muted_e = "<:muted:517356135972470794>"
unmuted_e = "<:unmuted:517356137964765193>"
warn_e = "<:warn:517356131467657226>"
checking_e = "<:checking:517356130608087051>"
clear_e = "<:clear:517356137054601216>"
purge_e = "<:purge:517356131320987649>"
nick_e = "<:nick:517356137499328513>"
ban_e = "<:ban:517356130549366784>"
unban_e = "<:unban:517356131279044628>"
tempban_e = "<:tempban:517356131245359126>"
kick_e = "<:kick:517356131895607326>"
takerole_e = "<:takerole:517356131450880000>"
giverole_e = "<:giverole:517356130880454656>"
idban_e = "<:idban:517356137310453760>"
promote_e = "<:promote:517356131379707907>"
demote_e = "<:demote:517356137310584843>"
reload_e = "<:reload:517356130939306020>"
worked_e = "<:worked:517356137817964545>"
roles_e = "<:roles:517356131379707905>"

help1 = "```diff"
help1 += "\n--- COMMANDS FOR EVERYONE ---"
help1 += "\nxm!ping"
help1 += "\n-    Pings the bot. Used to check if the bot is lagging."
help1 += "\n"
help1 += "\n--- COMMANDS FOR HELPERS ---"
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
help1 += "\n"
help1 += "\n--- COMMANDS FOR MODERATORS ---"
help1 += "\nxm!ban <user> <reason>"
help1 += "\n-    Bans the mentioned user."
help1 += "\nxm!unban <user ID>"
help1 += "\n-    Unbans the user with the matching ID as the one given."
help1 += "\nxm!kick <user> <reason>"
help1 += "\n-    Kicks the mentioned user."
help1 += "\n"
help1 += "\n--- COMMANDS FOR ADMINISTRATORS ---"
help1 += "\nxm!takerole <user> <role name>"
help1 += "\n-    Removes a role from the mentioned user."
help1 += "\nxm!giverole <user> <role name>"
help1 += "\n-    Adds a role to the mentioned user."
help1 += "\n"
help1 += "\n--- COMMANDS FOR MANAGERS ---"
help1 += "\nxm!idban <user ID> <reason>"
help1 += "\n-    Bans the user with the matching ID as the one given, their IP and all their alts that aren't already in the server. Works even if the user isn't in the server."
help1 += "\n"
help1 += "\n--- COMMANDS FOR OWNERS ---"
help1 += "\nxm!setrole <option> <role name>"
help1 += "\n-    Used to manage roles in the bot's database."
help1 += "\nxg!log <channel name>"
help1 += "\n-    Sets the logs channel."
help1 += "\n```"

''''''

# START UP SYSTEM
started = []
@client.event
async def on_ready():
    async for i in client.logs_from(client.get_channel(owner_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        owner_roles.append(role)
    print("[START UP] Loaded owner roles.")
    async for i in client.logs_from(client.get_channel(manager_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        manager_roles.append(role)
    print("[START UP] Loaded manager roles.")
    async for i in client.logs_from(client.get_channel(admin_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        admin_roles.append(role)
    print("[START UP] Loaded administrator roles.")
    async for i in client.logs_from(client.get_channel(mod_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        mod_roles.append(role)
    print("[START UP] Loaded moderator roles.")
    async for i in client.logs_from(client.get_channel(helper_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        helper_roles.append(role)
    print("[START UP] Loaded helper roles.")
    async for i in client.logs_from(client.get_channel(muted_roles_chnl), limit=limit):
        a = i.content.split(' | ')
        server = client.get_server(a[0])
        role = discord.utils.get(server.roles, id=a[1])
        muted_roles.append(role)
    print("[START UP] Loaded muted roles.")
    async for i in client.logs_from(client.get_channel(logs_chnl), limit=limit):
        logs.append(i.content)
    print("[START UP] Loaded logs channels.")
    async for i in client.logs_from(client.get_channel(warns_chnl), limit=limit):
        a = i.content.split(' | ')
        warns.append(a[1])
    print("[START UP] Loaded warnings.")
    started.append("+1")
    print("[START UP] Finished.")
    await client.change_presence(game=discord.Game(name="}help | }invite"))
    m = splitter
    m += "\n{} **__Bot Restart__** {} `-` Version: {}".format(log_e, reload_e, version)
    t1 = time.perf_counter()
    await client.send_typing(client.get_channel(log_chnl))
    t2 = time.perf_counter()
    m += "\n{} Ping: `{}ms`".format(pingok_e, round((t2-t1)*1000))
    await client.send_message(client.get_channel(log_chnl), m)

# ANTI MUTE BYPASS
@client.async_event
async def on_member_join(user: discord.User):
    for i in muted_list:
        a = i.split(' | ')
        if a[1] == user.id:
            for u in user.server.roles:
                if u in muted_roles:
                    try:
                        await client.add_roles(user.server.get_member(user.id), u)
                    except:
                        print("[ANTI MUTE BYPASS] Error.")

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
        if '}' in str(ctx.message.content):
            if option == "all" or option == "m":
                t1 = time.perf_counter()
                await client.send_typing(ctx.message.channel)
                t2 = time.perf_counter()
                ping = round((t2-t1)*1000)
                if ping > 300:
                    m = "{} The bot is lagging.\nAttempting to fix the bot's ping. This should take about a minute to finish.".format(pingbad_e)
                elif ping > 200:
                    m = "{} The bot might be lagging.".format(pingok_e)
                else:
                    m = "{} The bot isn't lagging.".format(pinggood_e)
                embed.description = "My ping is `{}`ms.\n{}".format(ping, m)
                await client.say(embed=embed)
        else:
            t1 = time.perf_counter()
            await client.send_typing(ctx.message.channel)
            t2 = time.perf_counter()
            ping = round((t2-t1)*1000)
            if ping > 300:
                m = "{} The bot is lagging.\nAttempting to fix the bot's ping. This should take about a minute to finish.".format(pingbad_e)
            elif ping > 200:
                m = "{} The bot might be lagging.".format(pingok_e)
            else:
                m = "{} The bot isn't lagging.".format(pinggood_e)
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

''' COMMANDS FOR HELPERS '''
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    embed.description = "{} Deleting latest messages sent by bots... {}".format(clearbots_e, loading_e)
                    h = await client.say(embed=embed)
                    msgs = []
                    async for o in client.logs_from(ctx.message.channel, limit=100, before=ctx.message):
                        if o.author.bot and o.id != h.id:
                            msgs.append(o)
                try:
                    await client.delete_messages(msgs)
                    embed.description = "{} **{}** removed the latest messages sent by bots.".format(clearbots_e, author.name)
                    await client.edit_message(h, embed=embed)
                except:
                    for o in msgs:
                        await client.delete_message(o)
                    embed.description = "{} **{}** removed the latest messages sent by bots.".format(clearbots_e, author.name)
                    await client.edit_message(h, embed=embed)
                a.append("+1")
                break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by staff.".format(error_e)
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
        muted = []
        for i in muted_roles:
            if i in ctx.message.server.roles:
                muted.append(i)
                break
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if len(muted) != 0:
                        if user == None or time == None:
                            embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <minutes> [reason]`.".format(error_e)
                            await client.say(embed=embed)
                        elif muted[0] in user.roles:
                            embed.description = "{} That user is already muted.".format(error_e)
                            await client.say(embed=embed)
                        else:
                            b = []
                            for o in roles:
                                for r in o:
                                    if r in ctx.message.server.roles and r in user.roles:
                                        embed.description = "{} Other server staff cannot be muted.".format(error_e)
                                        await client.say(embed=embed)
                                        b.append("+1")
                                        break
                                if len(b) != 0:
                                    break
                            if len(b) == 0:
                                if len(str(args)) > 250 and args != None:
                                    embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
                                    await client.say(embed=embed)
                                else:
                                    try:
                                        time2 = int(time)
                                        if time2 > 600 or time2 < 1:
                                            embed.description = "{} You cannot mute someone for longer than 600 minutes and shorter than 1 minute.".format(error_e)
                                            await client.say(embed=embed)
                                        else:
                                            await client.add_roles(user, muted[0])
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
                                            for o in logs:
                                                b = o.split(' | ')
                                                if b[0] == ctx.message.server.id:
                                                    c = client.get_channel(b[1])
                                                    await client.send_message(c, m)
                                                    break
                                            await asyncio.sleep(float(minutes))
                                            try:
                                                try:
                                                    muted_list.remove(user.id)
                                                except:
                                                    print("[AUTO UNMUTE] Unable to remove user from muted list.")
                                                if muted[0] in user.roles:
                                                    await client.remove_roles(user, muted[0])
                                                    embed.description = "{} **{}** was automatically unmuted.".format(unmuted_e, user.name)
                                                    await client.say(embed=embed)
                                            except:
                                                print("[AUTO UNMUTE] Unable to remove role from user.")
                                    except:
                                        embed.description = "{} The minutes have to be a number.".format(error_e)
                                        await client.say(embed=embed)
                    else:
                        embed.description = "{} No muted role found.".format(error_e)
                        await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by staff.".format(error_e)
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
        muted = []
        for i in muted_roles:
            if i in ctx.message.server.roles:
                muted.append(i)
                break
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if len(muted) != 0:
                        if user == None:
                            embed.description = "{} Please mention the user you want to unmute.".format(error_e)
                            await client.say(embed=embed)
                        elif muted[0] in user.roles:
                            try:
                                muted_list.remove(user.id)
                            except:
                                print("[UNMUTE] Unable to remove user from muted list.")
                            await client.remove_roles(user, muted[0])
                            embed.description = "{} **{}** unmuted **{}**.".format(unmuted_e, author.name, user.name)
                            await client.say(embed=embed)
                            m = splitter
                            m += "\n{} **__Unmute__** {}".format(log_e, unmuted_e)
                            m += "\n`Author:` {} ### {}".format(author, author.id)
                            m += "\n`Target:` {} ### {}".format(user, user.id)
                            for o in logs:
                                b = o.split(' | ')
                                if b[0] == ctx.message.server.id:
                                    c = client.get_channel(b[1])
                                    await client.send_message(c, m)
                                    break
                        else:
                            embed.description = "{} That user is not muted.".format(error_e)
                            await client.say(embed=embed)
                    else:
                        embed.description = "{} No muted role found.".format(error_e)
                        await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by staff.".format(error_e)
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if user == None or args == None:
                        embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <reason>`.".format(error_e)
                        await client.say(embed=embed)
                    else:
                        b = []
                        for o in roles:
                            for r in o:
                                if r in ctx.message.server.roles and r in user.roles:
                                    embed.description = "{} Other server staff and bots cannot be warned.".format(error_e)
                                    await client.say(embed=embed)
                                    b.append("+1")
                                    break
                            if len(b) != 0:
                                break
                        if len(b) == 0:
                            if len(str(args)) > 250:
                                embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
                                await client.say(embed=embed)
                            elif warns.count(user.id) >= 5:
                                await client.ban(user)
                                embed.description = "{} **{}** has been automatically banned.\nReason: Reached max warnings.".format(auto_e, user)
                                await client.say(embed=embed)
                                m = splitter
                                m += "\n{} **__Auto Ban__** {}".format(log_e, auto_e)
                                m += "\n`Target:` {} ### {}".format(user, user.id)
                                m += "\n`Reason:` Reached max warnings."
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
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
                                await client.send_message(client.get_channel(warns_chnl), "{} | {} | {} | {}".format(ctx.message.server.name, user.id, author.id, args))
                                m = splitter
                                m += "\n{} **__Warning__** {}".format(log_e, warn_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Target:` {} ### {}".format(user, user.id)
                                m += "\n`Reason:` {}".format(args)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by staff.".format(error_e)
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
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
                            embed.description = "{} Warning data for **{}** ( `{}` ):".format(checking_e, user, user.id)
                            async for o in client.logs_from(client.get_channel(warns_chnl), limit=limit):
                                b = o.content.split(' | ')
                                if b[1] == user.id:
                                    r = await client.get_user_info(b[2])
                                    embed.add_field(name="{} **__Warning Number:__** `{}`".format(warn_e, o.id), value="`Warned by:` {} ### {}\n`Reason:` {}\n`Warned in:` {}".format(r, r.id, b[3], b[0]))
                            await client.edit_message(h, embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by staff.".format(error_e)
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if user == None or target == None:
                        embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <warn number/all>`.".format(error_e)
                        await client.say(embed=embed)
                    elif warns.count(user.id) == 0:
                        embed.description = "{} No warnings found for **{}**.".format(clear_e, user.name)
                        await client.say(embed=embed)
                    elif target == "all":
                        embed.description = "{} Clearing warnings... {}".format(clear_e, loading_e)
                        h = await client.say(embed=embed)
                        p = []
                        async for o in client.logs_from(client.get_channel(warns_chnl), limit=limit):
                            b = o.content.split(' | ')
                            if b[1] == user.id:
                                await client.delete_message(o)
                                p.append("+1")
                        embed.description = "{} **{}** cleared `{}` warning(s) for **{}**.".format(clear_e, author.name, len(p), user.name)
                        await client.edit_message(h, embed=embed)
                        m = splitter
                        m += "\n{} **__Clear Warnings__** {}".format(log_e, clear_e)
                        m += "\n`Author:` {} ### {}".format(author, author.id)
                        m += "\n`Target:` {} ### {}".format(user, user.id)
                        m += "\n`Number:` {} (all)".format(len(p))
                        for o in logs:
                            b = o.split(' | ')
                            if b[0] == ctx.message.server.id:
                                c = client.get_channel(b[1])
                                await client.send_message(c, m)
                                break
                    else:
                        embed.description = "{} Clearing warning... {}".format(clear_e, loading_e)
                        h = await client.say(embed=embed)
                        p = []
                        async for o in client.logs_from(client.get_channel(warns_chnl), limit=limit):
                            b = o.content.split(' | ')
                            if b[1] == user.id and o.id == target:
                                await client.delete_message(o)
                                warns.remove(user.id)
                                p.append("+1")
                                break
                        if len(p) == 0:
                            embed.description = "{} A warning with that number was not found.".format(error_e)
                            await client.edit_message(h, embed=embed)
                        else:
                            embed.description = "{} **{}** cleared `1` warning for **{}**.".format(clear_e, author.name, user.name)
                            await client.edit_message(h, embed=embed)
                            m = splitter
                            m += "\n{} **__Clear Warnings__** {}".format(log_e, clear_e)
                            m += "\n`Author:` {} ### {}".format(author, author.id)
                            m += "\n`Target:` {} ### {}".format(user, user.id)
                            m += "\n`Number:` {}".format(len(p))
                            for o in logs:
                                b = o.split(' | ')
                                if b[0] == ctx.message.server.id:
                                    c = client.get_channel(b[1])
                                    await client.send_message(c, m)
                                    break
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by staff.".format(error_e)
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
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
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
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
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                        except:
                            embed.description = "{} Invalid number given.".format(error_e)
                            await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles, helper_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
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
                                await client.say(embed=embed)
                                m = splitter
                                m += "\n{} **__Nickname__** {}".format(log_e, nick_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Target:` {} ### {}".format(user, user.id)
                                m += "\n`Nickname:` 'cleared'"
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                            else:
                                embed.description = "{} **{}** changed **{}**'s nickname to `{}`.".format(nick_e, author.name, user.name, args)
                                await client.say(embed=embed)
                                m = splitter
                                m += "\n{} **__Nickname__** {}".format(log_e, nick_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Target:` {} ### {}".format(user, user.id)
                                m += "\n`Nickname:` {}".format(args)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                        except:
                            embed.description = "{} Unable to edit **{}**'s nickname.".format(error_e, user.name)
                            await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by staff.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR MODERATORS '''
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if user == None or args == None:
                        embed.description = "{} The command was used incorrectly.\nProper usage: `<user> <reason>`.".format(error_e)
                        await client.say(embed=embed)
                    else:
                        b = []
                        for o in roles:
                            for r in o:
                                if r in ctx.message.server.roles and r in user.roles:
                                    embed.description = "{} Other staff can only be banned manually.".format(error_e)
                                    await client.say(embed=embed)
                                    b.append("+1")
                                    break
                            if len(b) != 0:
                                break
                        if len(b) == 0:
                            if len(str(args)) > 250:
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
                                    for o in logs:
                                        b = o.split(' | ')
                                        if b[0] == ctx.message.server.id:
                                            c = client.get_channel(b[1])
                                            await client.send_message(c, m)
                                            break
                                except:
                                    embed.description = "{} I am unable to ban that user.".format(error_e)
                                    await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by moderators, administrators, managers and owners.".format(error_e)
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
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
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                            except:
                                embed.description = "{} The user with that ID is not banned.".format(error_e)
                                await client.say(embed=embed)
                        except:
                            embed.description = "{} A user with that ID was not found.".format(error_e)
                            await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by moderators, administrators, managers and owners.".format(error_e)
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
        roles = [owner_roles, manager_roles, admin_roles, mod_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if user == None or args == None:
                        embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [reason]`.".format(error_e)
                        await client.say(embed=embed)
                    else:
                        b = []
                        for o in roles:
                            for r in o:
                                if r in ctx.message.server.roles and r in user.roles:
                                    embed.description = "{} Other staff can only be banned manually.".format(error_e)
                                    await client.say(embed=embed)
                                    b.append("+1")
                                    break
                            if len(b) != 0:
                                break
                        if len(b) == 0:
                            if len(str(args)) > 250:
                                embed.description = "{} The reason cannot be longer than 250 characters.".format(error_e)
                                await client.say(embed=embed)
                            else:
                                try:
                                    await client.kick(user)
                                    embed.description = "{} **{}** kicked **{}**.\nReason: {}".format(kick_e, author.name, user, args)
                                    await client.say(embed=embed)
                                    m = splitter
                                    m += "\n{} **__Kick__** {}".format(log_e, kick_e)
                                    m += "\n`Author:` {} ### {}".format(author, author.id)
                                    m += "\n`Target:` {} ### {}".format(user, user.id)
                                    m += "\n`Reason:` {}".format(args)
                                    for o in logs:
                                        b = o.split(' | ')
                                        if b[0] == ctx.message.server.id:
                                            c = client.get_channel(b[1])
                                            await client.send_message(c, m)
                                            break
                                except:
                                    embed.description = "{} I am unable to kick that user.".format(error_e)
                                    await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by moderators, administrators, managers and owners.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR ADMINISTRATORS '''
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
        roles = [owner_roles, manager_roles, admin_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if user == None or args == None:
                        embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [role name]`.".format(error_e)
                        await client.say(embed=embed)
                    else:
                        b = []
                        for o in ctx.message.server.roles:
                            if args.lower() in str(o.name.lower()):
                                b.append("+1")
                                if author.top_role <= o:
                                    embed.description = "{} You cannot remove a role that is the same or higher than your top role.".format(error_e)
                                    await client.say(embed=embed)
                                    break
                                else:
                                    try:
                                        await client.remove_roles(user, o)
                                        embed.description = "{} **{}** removed `{}` from **{}**'s roles.".format(takerole_e, author.name, o.name, user.name)
                                        await client.say(embed=embed)
                                        m = splitter
                                        m += "\n{} **__Take Role__** {}".format(log_e, takerole_e)
                                        m += "\n`Author:` {} ### {}".format(author, author.id)
                                        m += "\n`Target:` {} ### {}".format(user, user.id)
                                        m += "\n`Role:` {}".format(o.name)
                                        for o in logs:
                                            b = o.split(' | ')
                                            if b[0] == ctx.message.server.id:
                                                c = client.get_channel(b[1])
                                                await client.send_message(c, m)
                                                break
                                    except:
                                        embed.description = "{} There was an error while trying to edit that user's roles.".format(error_e)
                                        await client.say(embed=embed)
                                    break
                        if len(b) == 0:
                            embed.description = "{} A role with that name was not found.".format(error_e)
                            await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by administrators, managers and owners.".format(error_e)
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
        roles = [owner_roles, manager_roles, admin_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
                    if user == None or args == None:
                        embed.description = "{} The command was used incorrectly.\nProper usage: `<user> [role name]`.".format(error_e)
                        await client.say(embed=embed)
                    else:
                        b = []
                        for o in ctx.message.server.roles:
                            if args.lower() in str(o.name.lower()):
                                b.append("+1")
                                if author.top_role <= o:
                                    embed.description = "{} You cannot give a role that is the same or higher than your top role.".format(error_e)
                                    await client.say(embed=embed)
                                    break
                                else:
                                    try:
                                        await client.add_roles(user, o)
                                        embed.description = "{} **{}** added `{}` to **{}**'s roles.".format(giverole_e, author.name, o.name, user.name)
                                        await client.say(embed=embed)
                                        m = splitter
                                        m += "\n{} **__Give Role__** {}".format(log_e, giverole_e)
                                        m += "\n`Author:` {} ### {}".format(author, author.id)
                                        m += "\n`Target:` {} ### {}".format(user, user.id)
                                        m += "\n`Role:` {}".format(o.name)
                                        for o in logs:
                                            b = o.split(' | ')
                                            if b[0] == ctx.message.server.id:
                                                c = client.get_channel(b[1])
                                                await client.send_message(c, m)
                                                break
                                    except:
                                        embed.description = "{} There was an error while trying to edit that user's roles.".format(error_e)
                                        await client.say(embed=embed)
                                    break
                        if len(b) == 0:
                            embed.description = "{} A role with that name was not found.".format(error_e)
                            await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by administrators, managers and owners.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR MANAGERS '''
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
        roles = [owner_roles, manager_roles]
        a = []
        for i in roles:
            for u in i:
                if u in ctx.message.server.roles and u in ctx.message.author.roles:
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
                            for o in logs:
                                b = o.split(' | ')
                                if b[0] == ctx.message.server.id:
                                    c = client.get_channel(b[1])
                                    await client.send_message(c, m)
                                    break
                        except:
                            embed.description = "{} Either I cannot ban the user with that ID or that user ID does not exist.".format(error_e)
                            await client.say(embed=embed)
                    a.append("+1")
                    break
            if len(a) != 0:
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by managers and owners.".format(error_e)
            await client.say(embed=embed)

''' COMMANDS FOR OWNERS '''
# }setrole <option> <role name>
@client.command(pass_context=True)
async def setrole(ctx, option = None, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        a = []
        for i in owner_roles:
            if i in ctx.message.server.roles and i in ctx.message.author.roles:
                options = ["owner", "manager", "admin", "mod", "helper", "muted"]
                if option == None or args == None:
                    embed.description = "{} Not all arguments were given.\nOptions: `owner`, `manager`, `admin`, `mod`, `helper`, `muted`.\nTo remove a role from the database write the role's name like this: `<role name> | none`.".format(error_e)
                    await client.say(embed=embed)
                elif option.lower() not in options:
                    embed.description = "{} Invalid option.\nOptions: `owner`, `manager`, `admin`, `mod`, `helper`, `muted`.\nTo remove a role from the database write the role's name like this: `<role name> | none`.".format(error_e)
                    await client.say(embed=embed)
                else:
                    t = {"owner" : owner_roles_chnl,
                         "manger" : manager_roles_chnl,
                         "admin" : admin_roles_chnl,
                         "mod" : mod_roles_chnl,
                         "helper" : helper_roles_chnl,
                         "muted" : muted_roles_chnl}
                    k = {"owner" : owner_roles,
                         "manger" : manager_roles,
                         "admin" : admin_roles,
                         "mod" : mod_roles,
                         "helper" : helper_roles,
                         "muted" : muted_roles}
                    embed.description = "{} Editing roles database... {}".format(roles_e, loading_e)
                    h = await client.say(embed=embed)
                    p = []
                    r = []
                    for u in ctx.message.server.roles:
                        if ' | ' in args:
                            y = args.split(' | ')
                            args = y[0]
                            r.append(y[1])
                        if args.lower() in str(u.name.lower()):
                            p.append("+1")
                            if " | none" in r:
                                async for o in client.logs_from(client.get_channel(t[option]), limit=limit):
                                    b = o.content.split(' | ')
                                    if b[0] == ctx.message.server.id and b[1] == u.id:
                                        await client.delete_message(o)
                                        k[option].remove(u)
                                        break
                                embed.description = "{} **{}** removed `{}` from the `{}` roles database.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Removed role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Role type:` {}".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                                break
                            elif option.lower() != "member":
                                async for o in client.logs_from(client.get_channel(t[option]), limit=limit):
                                    b = o.content.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        k[option].remove(discord.utils.get(ctx.message.server.roles, id=b[1]))
                                        await client.delete_message(o)
                                        break
                                await client.send_message(client.get_channel(t[option]), "{} | {}".format(ctx.message.server.id, u.id))
                                k[option].append(u)
                                embed.description = "{} **{}** set the `{}` role as `{}`.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Set role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Set as:` {}".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                                break
                            else:
                                await client.send_message(client.get_channel(t[option]), "{} | {}".format(ctx.message.server.id, u.id))
                                k[option].append(u)
                                embed.description = "{} **{}** set the `{}` role as `{}`/`auto role`.".format(roles_e, author.name, u.name, option)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Set Role__** {}".format(log_e, roles_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`Set role:` {} ### {}".format(u.name, u.id)
                                m += "\n`Set as:` {}/auto role".format(option)
                                for o in logs:
                                    b = o.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        c = client.get_channel(b[1])
                                        await client.send_message(c, m)
                                        break
                                break
                    if len(p) == 0:
                        embed.description = "{} Role not found.".format(error_e)
                        await client.edit_message(h, embed=embed)
                a.append("+1")
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)
            
# }log <channel name>
@client.command(pass_context=True)
async def log(ctx, *, args = None):
    embed = discord.Embed(colour=0x7F1100)
    embed.set_footer(text=footer_text)
    if len(started) == 0:
        embed.description = "{} The bot is restarting. Please try again in a few seconds.".format(reload_e)
        await client.say(embed=embed)
    else:
        author = ctx.message.author
        a = []
        for i in owner_roles:
            if i in ctx.message.server.roles and i in ctx.message.author.roles:
                if args == None:
                    embed.description = "{} No channel name given.".format(error_e)
                    await client.say(embed=embed)
                else:
                    embed.description = "{} Editing log channels database... {}".format(roles_e, loading_e)
                    h = await client.say(embed=embed)
                    p = []
                    for u in ctx.message.server.channels:
                        if args.lower() in str(u.name.lower()):
                            p.append("+1")
                            try:
                                k = await client.send_message(u, "test log message")
                                async for i in client.logs_from(client.get_channel(logs_chnl), limit=limit):
                                    b = i.content.split(' | ')
                                    if b[0] == ctx.message.server.id:
                                        logs.remove(i.content)
                                        await client.delete_message(i)
                                        break
                                await client.send_message(client.get_channel(logs_chnl), "{} | {}".format(ctx.message.server.id, u.id))
                                logs.append("{} | {}".format(ctx.message.server.id, u.id))
                                embed.description = "{} **{}** set `{}` as the new logs channel.".format(log_e, author.name, u.name)
                                await client.edit_message(h, embed=embed)
                                m = splitter
                                m += "\n{} **__Log Channel__** {}".format(log_e, log_e)
                                m += "\n`Author:` {} ### {}".format(author, author.id)
                                m += "\n`New channel:` {} ### {}".format(u.name, u.id)
                                await client.edit_message(k, m)
                                break
                            except:
                                embed.description = "{} Unable to send logs in that channel ( `{}` ).".format(error_e, u.name)
                                await client.edit_message(h, embed=embed)
                                break
                    if len(p) == 0:
                        embed.description = "{} Channel not found.".format(error_e)
                        await client.edit_message(h, embed=embed)
                a.append("+1")
                break
        if len(a) == 0:
            embed.description = "{} This command can only be used by owners.".format(error_e)
            await client.say(embed=embed)


#######################
client.run(os.environ['Dk3.XrCKlg.Dqlk3pxNihXZXB1IRLmLyxq93jI'])
