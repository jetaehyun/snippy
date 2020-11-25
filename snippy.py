from discord.ext import commands
import discord
import profanity


bot = commands.Bot(command_prefix='!')
TOKEN = open("TOKEN.txt", "r").readline()

@bot.command(pass_context=True)
async def test(ctx, arg):
    if ctx.message.author.top_role.permissions.administrator:
        print("UP")
    await ctx.send(arg)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    channel = bot.get_channel(781236679272824925)
    await channel.send('Snippy just woke up...')

@bot.event
async def on_message(message):
    print(message)
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('hello')

    await bot.process_commands(message)

def main():
    test = profanity.filterManager('banned_words.txt')
    bot.run(TOKEN)

if __name__=='__main__':
    main()
