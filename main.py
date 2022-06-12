from config import ACCESS_TOKEN, COMMANDS_PREFIX, CHANNELS_NAME
from twitchio.ext import commands
from utils.polls import Poll
import json


class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(
            token=ACCESS_TOKEN, prefix=COMMANDS_PREFIX, initial_channels=CHANNELS_NAME
        )
        self.actual_poll = None
        self.result_text = ""

    async def create_poll(self, question):
        if self.actual_poll:
            if self.actual_poll.isAlive:
                raise PermissionError("There is already a poll in progress.")

        return Poll(question)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        await self.handle_commands(message)

    @commands.command()
    async def poll(self, context: commands.Context):
        poll_question = context.message.content.split(f"{COMMANDS_PREFIX}poll ")[1]

        try:
            self.actual_poll = await self.create_poll(poll_question)
        except PermissionError as e:
            await context.send(str(e))

        await context.send(poll_question)

    @commands.command()
    async def y(self, context: commands.Context):
        try:
            self.actual_poll.vote_yes(context.message.author)
        except PermissionError:
            await context.send("No poll in progress")

    @commands.command()
    async def n(self, context: commands.Context):
        try:
            self.actual_poll.vote_no(context.message.author)
        except PermissionError:
            await context.send("No poll in progress")

    @commands.command()
    async def result(self, context: commands.Context):
        try:
            votes = self.actual_poll.finish()

            total_votes = votes["Yes"] + votes["No"]
            yes_percent = (votes["Yes"] * 100) / total_votes
            no_percent = (votes["No"] * 100) / total_votes

            self.result_text = f"No: {no_percent}% | Yes: {yes_percent}%"
            if yes_percent >= no_percent:
                self.result_text = f"Yes: {yes_percent}% | No: {no_percent}%"
        except PermissionError as e:
            print(e)

        await context.send(json.dumps(self.result_text))


if __name__ == "__main__":
    bot = Bot()
    bot.run()
