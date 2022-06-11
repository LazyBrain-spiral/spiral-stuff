import discord
from discord.ext import commands
import random
import math

spi=commands.Bot(command_prefix="?")
spi.remove_command("help")

@spi.event
async def on_ready():
    print("hello world")


@spi.command(aliases=["8ball"])
async def _8ball(ctx,*,ques):
    embul=discord.Embed(title=":8ball: 8ball",color=discord.Color.blurple())
    
    response=["It is certain.",
              "It is decidedly so.",
              "Without a doubt.",
              "Yes - definitely.",
              "You may rely on it.",
              "As I see it, yes.",
              "Most likely.",
              "Outlook good.",
              "Yes.",
              "Signs point to yes.",
              "Reply hazy, try again.",
              "Ask again later.",
              "Better not tell you now.",
              "Cannot predict now.",
              "Concentrate and ask again.",
              "Don't count on it.",
              "My reply is no.",
              "My sources say no.",
              "Outlook not so good.",
              "Very doubtful."]
    embul.add_field(name=f"the question is: {ques} \nThe answer is: {random.choice(response)}",value="This is a random response.")
    await ctx.channel.send(embed=embul)

def pi(x:str,y:int):
    return x*y

@spi.command()
async def ping(ctx,x:str,y:int):
    pong=pi(x,y)
    await ctx.send(pong)



def addition(x:float , y:float):
    return x+y

def subtract(x:float , y:float):
    return x-y

def multiplication(x:float , y:float):
    return x*y

def divison(x:float , y:float):
    return x/y

@spi.command()
async def add(ctx,x:float,y:float):
    embud=discord.Embed(title="Addition",color=discord.Color.blurple())
    lol=addition(x, y)
    embud.add_field(name=f"Your answer is: {lol}!",value="You can thank me later")
    await ctx.channel.send(embed=embud)

@spi.command()
async def sub(ctx,x:float,y:float):
    embud=discord.Embed(title="Subtraction",color=discord.Color.blurple())
    bong=subtract(x,y)
    embud.add_field(name=f"Your answer is: {bong}!",value="You can thank me later")
    await ctx.channel.send(embed=embud)

@spi.command()
async def mul(ctx,x:float,y:float):
    embud=discord.Embed(title="Multiplication",color=discord.Color.blurple())
    bing=multiplication(x,y)
    embud.add_field(name=f"Your answer is: {bing}!",value="You can thank me later")
    await ctx.channel.send(embed=embud)


@spi.command()
async def div(ctx,x:float,y:float):
    
    embud=discord.Embed(title="Division",color=discord.Color.blurple())
    bleep=divison(x, y)
    embud.add_field(name=f"Your answer is: {bleep}!",value="You can thank me later")
    await ctx.channel.send(embed=embud)




@spi.command()
async def help(ctx):
    helper=discord.Embed(
        title="help",
        color=discord.Color.blurple())

    helper.set_footer(text="Every command for the bot.")
    
    helper.add_field(name="?ping <member> <value>",
    value="This is basically gonna ping the member by the number of times u entered.It only goes for certain amount.",inline=False)
    
    helper.add_field(name="?8ball <question>",value="Ask the 8ball.",inline=True)
    helper.add_field(name="?snipe",value="retrives the message which was deleted by a user before",inline=False)
    helper.add_field(name="?add <value1> <value2>",value="adds the given arguement",inline=True)
    helper.add_field(name="?sub <value1> <value2>",value="subtracts the given arguement",inline=False)
    helper.add_field(name="?mul <value1> <value2>",value="multiplies the given arguement",inline=True)
    helper.add_field(name="?div <value1> <value2>",value="divides the given arguement",inline=False)
    await ctx.channel.send(embed=helper)


spi.run("Token here")