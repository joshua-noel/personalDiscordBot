from calendar import c
from socket import timeout
import sys
sys.dont_write_bytecode = True #Prevents creation of .pyc files
import random
import discord
from discord.ext import commands
import asyncio

class Connect4():
    def __init__(self):
        self.blankBoard = [["⠀:white_circle:⠀" for col in range(7)] for row in range(6)]
        self.emotes = ["1⃣", "2⃣", "3⃣", "4⃣", "5⃣", "6⃣", "7⃣"]

    class CheckWin():
        def __init__(self, board):
            self.board = board

        async def vertical(self, board, row, col, color):
            pass

        async def horizontal(self, board, row, col, color):
            pass

        async def diagonal(self, board, row, col, color):
            pass

    async def printBoard(self, board, turn = None):
        if turn == "red":
            boardEmbed = discord.Embed(title="Connect 4", description="Current turn is reflected in the embed color", color=0xD2042D)

        elif turn == "blue":
            boardEmbed = discord.Embed(title="Connect 4", description="Current turn is reflected in the embed color", color=0x4F9CC9)
        
        else:
            boardEmbed = discord.Embed(title="Connect 4", description="Current turn is reflected in the embed color", color=0xFAFAFA)

        for row in range(6):
            rowContent = ""
            for col in range(7):
                rowContent += board[row][col] + " "
            boardEmbed.add_field(name="⠀", value=rowContent, inline=False)
            
        return boardEmbed

    async def win(self, board):
        pass

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="connect4", aliases=["c4"])
    async def connect4(self, ctx, opponent: discord.Member):
        #initialize game
        board = Connect4().blankBoard #current board (2d list)
        turn = random.choice(["red", "blue"]) #randomly choose who goes first
        winner = ""

        game = await Connect4.printBoard(self, board, turn) #game embed
        game.add_field(name="⠀:red_circle:", value=f"⠀{ctx.author.name}") #adds red player
        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
        game.set_footer(text="Turn will yield after 20 seconds")
        msg = await ctx.send(embed=game)

        for emote in Connect4().emotes:
            await msg.add_reaction(f"{emote}")

        #game loop
        while True:
            #check for reactions
            if turn == "red":
                try:
                    react = await self.bot.wait_for("reaction_add", timeout=20.0, check=lambda reaction, user: user == ctx.author and str(reaction.emoji) in Connect4().emotes)

                    if str(react[0].emoji) == "1⃣":
                        row = 5
                        col = 0

                        while True:
                            if board[row][col] == "⠀:white_circle:⠀":
                                try:
                                    board[row][col] = "⠀:red_circle:⠀"

                                except IndexError:
                                    break

                                break

                            else:
                                row -= 1

                        turn = "blue"
                        await msg.clear_reactions()

                        for emote in Connect4().emotes:
                            await msg.add_reaction(f"{emote}")

                        game = await Connect4.printBoard(self, board, turn)
                        game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                        game.set_footer(text="Turn will yield after 20 seconds")
                        await msg.edit(embed=game)

                    elif str(react[0].emoji) == "2⃣":
                        row = 5
                        col = 1

                        while True:
                            if board[row][col] == "⠀:white_circle:⠀":
                                try:
                                    board[row][col] = "⠀:red_circle:⠀"

                                except IndexError:
                                    break

                                break

                            else:
                                row -= 1

                        turn = "blue"
                        await msg.clear_reactions()

                        for emote in Connect4().emotes:
                            await msg.add_reaction(f"{emote}")

                        game = await Connect4.printBoard(self, board, turn)
                        game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                        game.set_footer(text="Turn will yield after 20 seconds")
                        await msg.edit(embed=game)

                    elif str(react[0].emoji) == "3⃣":
                        row = 5
                        col = 2

                        while True:
                            if board[row][col] == "⠀:white_circle:⠀":
                                try:
                                    board[row][col] = "⠀:red_circle:⠀"

                                except IndexError:
                                    break

                                break

                            else:
                                row -= 1

                        turn = "blue"
                        await msg.clear_reactions()

                        for emote in Connect4().emotes:
                            await msg.add_reaction(f"{emote}")

                        game = await Connect4.printBoard(self, board, turn)
                        game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                        game.set_footer(text="Turn will yield after 20 seconds")
                        await msg.edit(embed=game)

                    elif str(react[0].emoji) == "4⃣":
                        row = 5
                        col = 3

                        while True:
                            if board[row][col] == "⠀:white_circle:⠀":
                                try:
                                    board[row][col] = "⠀:red_circle:⠀"

                                except IndexError:
                                    break

                                break

                            else:
                                row -= 1

                        turn = "blue"
                        await msg.clear_reactions()

                        for emote in Connect4().emotes:
                            await msg.add_reaction(f"{emote}")

                        game = await Connect4.printBoard(self, board, turn)
                        game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                        game.set_footer(text="Turn will yield after 20 seconds")
                        await msg.edit(embed=game)

                    elif str(react[0].emoji) == "5⃣":
                        row = 5
                        col = 4

                        while True:
                            if board[row][col] == "⠀:white_circle:⠀":
                                try:
                                    board[row][col] = "⠀:red_circle:⠀"

                                except IndexError:
                                    break

                                break

                            else:
                                row -= 1

                        turn = "blue"
                        await msg.clear_reactions()

                        for emote in Connect4().emotes:
                            await msg.add_reaction(f"{emote}")

                        game = await Connect4.printBoard(self, board, turn)
                        game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                        game.set_footer(text="Turn will yield after 20 seconds")
                        await msg.edit(embed=game)

                    elif str(react[0].emoji) == "6⃣":
                        row = 5
                        col = 5
                        
                        while True:
                            if board[row][col] == "⠀:white_circle:⠀":
                                try:
                                    board[row][col] = "⠀:red_circle:⠀"

                                except IndexError:
                                    break

                                break

                            else:
                                row -= 1

                        turn = "blue"
                        await msg.clear_reactions()

                        for emote in Connect4().emotes:
                            await msg.add_reaction(f"{emote}")

                        game = await Connect4.printBoard(self, board, turn)
                        game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                        game.set_footer(text="Turn will yield after 20 seconds")
                        await msg.edit(embed=game)

                    elif str(react[0].emoji) == "7⃣":
                        row = 5
                        col = 6
                        
                        while True:
                            if board[row][col] == "⠀:white_circle:⠀":
                                try:
                                    board[row][col] = "⠀:red_circle:⠀"

                                except IndexError:
                                    break

                                break

                            else:
                                row -= 1

                        turn = "blue"
                        await msg.clear_reactions()

                        for emote in Connect4().emotes:
                            await msg.add_reaction(f"{emote}")

                        game = await Connect4.printBoard(self, board, turn)
                        game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                        game.set_footer(text="Turn will yield after 20 seconds")
                        await msg.edit(embed=game)

                except asyncio.TimeoutError:
                    turn = "blue"
                    await msg.clear_reactions()

                    for emote in Connect4().emotes:
                        await msg.add_reaction(f"{emote}")

                    game = await Connect4.printBoard(self, board, turn)
                    game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                    game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                    game.set_footer(text="Turn will yield after 20 seconds")
                    await msg.edit(embed=await Connect4.printBoard(self, board, turn))
                    break #temp remove when workinf

            elif turn == "blue":
                turn = "red"
                await msg.clear_reactions()

                for emote in Connect4().emotes:
                    await msg.add_reaction(f"{emote}")

                game = await Connect4.printBoard(self, board, turn)
                game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
                game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
                game.set_footer(text="Turn will yield after 20 seconds")
                await msg.edit(embed=game)

        game = await Connect4.printBoard(self, board)
        game.add_field(name="⠀:red_circle:", value=f"{ctx.author.name}") #adds red player
        game.add_field(name=":blue_circle:", value=f"{opponent.name}") #adds blue player
        await ctx.send(f"{winner} wins!")

def setup(bot):
    bot.add_cog(Games(bot))