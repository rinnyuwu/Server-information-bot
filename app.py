import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Boosty developer: https://boosty.to/mao-mao")
    print("GitHub: https://github.com/rinnyuwu")
    print("Donation Alerts: https://www.donationalerts.com/r/rinnyuwu")

@bot.slash_command(name="server", description="Get information about the server")
async def server(interaction: disnake.ApplicationCommandInteraction):
    guild = interaction.guild
    owner = guild.owner.mention if guild.owner else "Unknown"
    created_at = int(guild.created_at.timestamp())

    text_channels = len([channel for channel in guild.channels if isinstance(channel, disnake.TextChannel)])
    voice_channels = len([channel for channel in guild.channels if isinstance(channel, disnake.VoiceChannel)])
    stage_channels = len([channel for channel in guild.channels if isinstance(channel, disnake.StageChannel)])
    forum_channels = len([channel for channel in guild.channels if isinstance(channel, disnake.ForumChannel)])

    media_channels = len([channel for channel in guild.channels if isinstance(channel, disnake.TextChannel) and channel.is_news()])

    active_threads = len([channel for channel in guild.threads if isinstance(channel, disnake.Thread) and not channel.archived])

    bot_count = len([m for m in guild.members if m.bot])
    user_count = guild.member_count - bot_count

    if bot_count == 1:
        member_text = f"Members: **{guild.member_count}** (**{user_count} user** and **{bot_count} bot**) "
    elif bot_count > 1:
        member_text = f"Members: **{guild.member_count}** (**{user_count} users** and **{bot_count} bots**) "
    else:
        member_text = f"Members: **{guild.member_count}** (**{user_count} users**) "

    embed = disnake.Embed(title="Server information", color=disnake.Color.blue())
    embed.set_thumbnail(url=guild.icon.url)

    embed.description = (
        f" - Name: **{guild.name}**\n"
        f" - Server ID: **{guild.id}**\n"
        f" - Owner: **{owner}**\n"
        f" - Created On: <t:{created_at}:f>\n"
        f" - {member_text}\n"
        f" - Boosts: **{guild.premium_subscription_count}**\n"
        f" - Roles: **{len(guild.roles)}**\n"
        f" - Channels: **{len(guild.channels)}**\n"
        f"  - Text Channels: **{text_channels}**\n"
        f"  - Voice Channels: **{voice_channels}**\n"
        f"  - Stage Channels: **{stage_channels}**\n"
        f"  - Active Threads: **{active_threads}**\n"
        f"  - Forum Channels: **{forum_channels}**\n"
        f"  - Media Channels: **{media_channels}**"
    )

    await interaction.send(embed=embed)

bot.run("INSERT-TOKEN") # To run the bot, you'll need a token which you get by creating an application in the Discord Developer Portal (https://discord.com/developers/)
                        # Replace INSERT-TOKEN with your token here
                        # Make sure the token remains confidential and is not published in public sources