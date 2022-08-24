import discord


class RivenSelector(discord.ui.View):
    @discord.ui.select(
        placeholder="Select Riven Mod Type",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(label="Melee", emoji="👊", description="Minimum wager: 35p"),
            discord.SelectOption(label="Rifle", emoji="🏹", description="Minimum wager: 40p"),
            discord.SelectOption(label="Pistol", emoji="🔫", description="Minimum wager: 0p")
        ]
    )
    async def select_callback(self, select, interaction):
        select.disabled = True  # set the status of the select as disabled
        await interaction.response.edit_message(content=f"{select.values[0]} selected!", view=self)
