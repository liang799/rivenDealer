import discord


class RivenSelector(discord.ui.View):
    def __init__(self, author):
        self.author = author
        super().__init__(timeout=30)

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.message.edit(content="You took too long! Disabled all the components.", view=self)

    @discord.ui.select(
        placeholder="Select Riven Mod Type",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="Melee",
                emoji="👊",
                description="Minimum wager: 35p"
            ),
            discord.SelectOption(
                label="Rifle",
                emoji="🏹",
                description="Minimum wager: 40p"
            ),
            discord.SelectOption(
                label="Pistol",
                emoji="🔫",
                description="Minimum wager: 0p"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if interaction.user.id == self.author.id:
            select.disabled = True  # set the status of the select as disabled
            await interaction.response.edit_message(content=f"{select.values[0]} selected!", view=self)  # edit the message to show the changes
            print(interaction.user)
        else:
            return

