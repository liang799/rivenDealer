import discord
from discord import Option, option

from utils.auth import AuthManager
from utils.game import Game
from utils.riven import Riven
from utils.weapon import Weapon
from utils.priceSearch import CollectSample

collect = CollectSample()
collect.setup_method()

async def weapon_searcher(ctx: discord.AutocompleteContext):
    res = Weapon.getWeaponsCol()
    weapons = [x["weapon"] for x in res.data]
    return [weapon for weapon in weapons if weapon.startswith(ctx.value.upper())]


class Roller(discord.Cog):
    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx,
                   riven: Option(str, "Select Riven Mod Type", choices=["Melee", "Rifle", "Pistol"], required=True)):
        if AuthManager.checkRegistered(ctx.author):
            if not Game.getOngoingStatus(ctx.author):
                choice = -1
                if riven == "Rifle":
                    choice = 1
                if riven == "Pistol":
                    choice = 2
                if riven == "Melee":
                    choice = 3
                Riven.startUnveiling(ctx.author, choice)
                await ctx.response.send_message(f"<@{ctx.author.id}> is currently opening a **{riven} Riven Mod**")
            else:
                await ctx.response.send_message("Please wait for the current round to end", ephemeral=True)
        else:
            await ctx.response.send_message("Please use `/register` to register", ephemeral=True)

    @discord.slash_command(name="reveal", description="Reveal unveiled riven")
    @option("name", description="Name of weapon", autocomplete=weapon_searcher)
    async def reveal(self, ctx: discord.ApplicationContext, name: str):
        if AuthManager.checkRegistered(ctx.author):
            if Game.getOngoingStatus(ctx.author):
                embed = discord.Embed(title="List of Speculations", color=discord.Colour.blurple())
                data = Game.getResults(ctx.author)
                if not data:
                    embed = None
                else:
                    table = ""
                    for index in range(len(data)):
                        table += f"<@{data[index]['registration']['user_id']}> " \
                                 f"??? {data[index]['weapon_tiers']['name']}\n"
                    embed.add_field(name="Name ??? Tier", value=table)
                errMsg = Riven.reveal(ctx.author, name)
                if not errMsg:
                    nameInput = Weapon.getWeapon(name)
                    output = ""
                    await ctx.defer()
                    prices = collect.collectDataSample(nameInput.title())
                    
                    for price in prices:
                        output += (price.text + " | ") 
                    msg = f"<@{ctx.author.id}> has opened a/an\n\n"
                    msg += f"**{Weapon.getWeapon(name)}** Riven Mod **({Weapon.getTier(name)} Tier)**\n"
                    msg += "=================================================="
                    msg += f"\n**Reference unroll/trash roll prices:**"
                    msg += "` | " + output + "`\n"

                    await ctx.followup.send(msg, embed=embed)
                    #await ctx.response.send_message(msg, embed=embed)
                else:
                    await ctx.response.send_message(errMsg, ephemeral=True)
            else:
                await ctx.response.send_message("Please use `/open` to open a riven mod", ephemeral=True)
        else:
            await ctx.response.send_message("Please use `/register` to register", ephemeral=True)


def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(Roller(bot))  # add the cog to the bot
