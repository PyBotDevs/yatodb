# Imports
import discord
import json
import time
import os, os.path
import utils.auth
import utils.ping
from random import choice
from discord import ApplicationContext, option
from discord.ext import commands

# Variables
client = discord.Bot()
start_time = round(time.time())
if os.name == "nt":
    with open(f"{os.getcwd()}\\config\\truth.json", 'r') as f: truth_questions = json.load(f)
    with open(f"{os.getcwd()}\\config\\dare.json", 'r') as f: dare_questions = json.load(f)
else:
    with open("config/truth.json", 'r') as f: truth_questions = json.load(f)
    with open("config/dare.json", 'r') as f: dare_questions = json.load(f)
owner_id = utils.auth.get_owner_id()

# Events
@client.event
async def on_ready():
    print(f"[client] Bot client successfully signed into API. ({round(time.time()) - start_time}ms)")
    print(f"[client] Logged in as \"{client.user.name}\".")
    print("[utils/ping] Starting web pinging server...")
    utils.ping.host()

# Functions
@client.slash_command(
    name="help",
    description="View a list of all available commands."
)
async def help(ctx: ApplicationContext):
    localembed = discord.Embed(title="Command Help List", description="The global bot prefix is `/`\n\n**/truth**: Gives you a truth type question\n**/dare**: Gives you a dare type question")
    localembed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.respond(embed=localembed)

@client.slash_command(
    name="truth",
    description="Get a truth-type question."
)
async def truth(ctx: ApplicationContext):
    truth_parsed = list(truth_questions["questions"])
    question = choice(truth_parsed)
    localembed = discord.Embed(
        title=f"Truth question by {ctx.author.display_name}", 
        description=question,
        color=discord.Color.random()
    )
    await ctx.respond(embed=localembed)

@client.slash_command(
    name="dare",
    description="Get a dare-type question."
)
async def dare(ctx: ApplicationContext):
    dare_parsed = list(dare_questions["questions"])
    question = choice(dare_parsed)
    localembed = discord.Embed(
        title=f"Dare question by {ctx.author.display_name}", 
        description=question,
        color=discord.Color.random()
    )
    await ctx.respond(embed=localembed)

@client.slash_command(
    name="suggest",
    description="Suggest a new truth or dare question for the bot."
)
@option(name="mode", description="What mode do you want to suggest this question for?", type=str, choices=["truth", "dare"])
@option(name="question", description="What question do you want to suggest?", type=str)
async def suggest(ctx: ApplicationContext, mode: str, question: str):
    owner_context: discord.User = await client.fetch_user(owner_id)
    embed1 = discord.Embed(
        title="You Have A New Question Suggestion!",
        color=discord.Color.blue()
    )
    embed1.add_field(name="Mode", value=mode, inline=True)
    embed1.add_field(name="Question", value=question, inline=True)
    embed1.add_field(name="Suggested by", value=ctx.author.display_name, inline=True)
    await owner_context.send(embed=embed1)
    await ctx.respond(embed=discord.Embed(description="Your suggestion has been sent!", color=discord.Color.green()), ephemeral=True)

# Client Initialization
client.run(utils.auth.get_token())





# btw i use arch
