# Metrodex
A Discord bot created for TransitTime!
Given a picture and facts, guess NYC subway stations to add them to your collection!


Watch the project in action [here](https://youtu.be/xB0gkqSXjIo), or clone the repo and host it yourself!
Remember to change the guild ID & channel ID when hosting your own instance of the bot.

## Notice to HCTG Reviewers
Thank you so much for reviewing my project! The reason why my demo link is a video as opposed to a playable or experience link is that I lack the hosting credits to host the bot on a larger scale + it's a bit finicky to have a playable link for a Discord bot? Hopefully the video will be sufficient instead. If you have any questions for me about the project or the demo, please let me know! Thank you so much!

## Instructions to set up your own instance
1. Clone the repo
2. Empty the collections.json file, and replace it with an empty set of curly braces: `{}`
3. Create a Discord bot on the Discord Developer Portal and obtain its token. Remember to enable the "read messages" scope in the Bot tab of the portal, as the bot may request to use it. It will be functional without it, so you can disable it within the Python code to use it without the scope.
4. Create a file called `.env` inside the cloned repo folder, and place `DISCORD_TOKEN="<YOUR_TOKEN_HERE>"` in it, replacing `<YOUR_TOKEN_HERE>` with your Discord bot's token.
5. Replace the server ID in this line `server = discord.Object(id=1081625448385085440)` with the guild ID of the server you intend to run this bot with.
6. Replace the channel ID in this line `channel = bot.get_channel(1477473312291553453)` with the channel ID of the channel you want the bot to spawn stations in.
7. (Optional) Run your bot by running the Python script (in a command line or an IDE), and immediately turn it off.
8. (Optional) Replace the long string of numbers (application command ID) all instances of `</guess:1477481130507763754>` with a command ID that your bot will generate the first time it is run. See [here](https://stackoverflow.com/a/73988996) on how to get the ID of a command.
9. Replace the User ID in this line `if interaction.user.id != 700061928243986512:` with your own ID, if you'd like to enable debugging / viewing all user data with a command.
10. Run your bot and enjoy!
