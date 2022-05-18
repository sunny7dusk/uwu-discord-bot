import discord
import os # default module
from dotenv import load_dotenv
from uwu import uwufied

load_dotenv() # load all the variables from the env file

bot = discord.Bot(debug_guilds=[int(os.getenv('GUILD'))])

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(name="uwu", description="UwU translater; for stuterring, use 0.0-1.0", alias=["uwufied"])
async def uwu(ctx, sentence: discord.Option(str), stuttering=0.2):
    print("To convert: " + sentence)
    embed = discord.Embed(
        color=discord.Colour.fuchsia(), # Pycord provides a class with default colors you can choose from
    )

    converted = uwufied(sentence, float(stuttering))

    embed.add_field(name="\u200b",value=converted)
    await ctx.respond(embed=embed)

bot.run(os.getenv('TOKEN'))