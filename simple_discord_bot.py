from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!')

@bot.command()
async def dm(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)

@bot.command()
async def dmm(ctx, user: discord.User, num=None, *, message=None):
    num = num or 1
    message = message or "This Message is sent via DM"
    for i in range(0, int(num)):
        await user.send(message)

@bot.command(pass_context=True)
async def chm(ctx, channel: discord.TextChannel, *, message=None):
    message = message or 'This is a message in a channel.'
    await channel.send(message)

@bot.command(pass_context=True)
async def dmrole(ctx, role: discord.Role, *, message=None):
    channel = discord.TextChannel
    message = message or 'This is a message for member whit some role.'

@bot.command(pass_context=True)
async def test(self, ctx, message):
    await ctx.send('test')

bot.run("OTEyNDkzNjU2MTQzOTgyNzAy.YZwv8A.8kTOMIRK_nqCymPOGqRzJYgdM5g")
