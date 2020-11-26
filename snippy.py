from discord.ext import commands
import discord
import profanity


bot = commands.Bot(command_prefix='!')
TOKEN = open("TOKEN.txt", "r").readline()
bot_filter = profanity.filterManager('banned_words.txt')

@bot.command(pass_context=True)
@commands.has_guild_permissions(administrator=True)
async def snip(ctx, *arg):
    if len(arg) == 2:
        if arg[0] == 'filter' and bot_filter.addWord(arg[1]):
            await ctx.send('The word **{}** has been added to the banlist...'.format(arg[1]))
        else:
            await ctx.send('The word **{}** is already in the banlist...'.format(arg[1]))

@bot.command(pass_context = True)
@commands.has_guild_permissions(administrator=True)
async def alert(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    channel = bot.get_channel(781236679272824925)
    await channel.send('@everyone Snippy just woke up...')

@bot.event
async def on_message(message):
    print(message)
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('hello')

    await bot.process_commands(message)

def main():
    bot.run(TOKEN)

if __name__=='__main__':
    main()
