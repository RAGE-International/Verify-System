
        class RoleButton(discord.ui.Button):
            def __init__(self):
                super().__init__(
                    label="Verifiziere dich hier!",  # Text auf dem Button!
                    style=discord.enums.ButtonStyle.green,  # Button-Fabre!
                    custom_id="interaction:RoleButton",
                )

            async def callback(self, interaction: discord.Interaction):
                user = interaction.user

                role = interaction.guild.get_role(Deine_Role_ID)

                if role is None:
                    return

                if role not in user.roles:
                    await user.add_roles(role)
                    await interaction.response.send_message(f"🎉 Du bist nun verifiziert!", ephemeral=True)

                else:
                    await interaction.response.send_message(f"❌ Du bist bereits verifiziert!", ephemeral=True)


        @bot.event
        async def on_ready():
            view = discord.ui.View(timeout=None)
            view.add_item(RoleButton())
            bot.add_view(view)


        @bot.command()
        async def send(ctx: commands.Context):  # Command
            view = discord.ui.View(timeout=None)

            view.add_item(RoleButton())
            verifyem = discord.Embed(
                title="Regelwerk",
                description="👉 Verhalte dich freundlich und respektvoll!"
                            "\r\n👉 Akzeptiere die Meinung anderer User!"
                            "\r\n👉 Niemand wird gemobbt oder Diskriminiert"
                            "\r\n👉 Keine Gehässigen oder Unpassende Usernames und Profilbilder"
                            "\r\n👉 Wer Bugs ausnutz wird gebannt"
                            "\r\n👉 Spam oder andere arten von Belästigung werden nicht toleriert"
                            "\r\n👉 Beachte die allgemeinen RIchlinien von Discord",
                color=0x1f8b4c
            )
            await ctx.message.delete()
            await ctx.send(embed=verifyem, view=view)
