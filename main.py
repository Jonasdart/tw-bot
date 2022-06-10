from twitchio.ext import commands
from utils import Poll
import json

ACCESS_TOKEN = '6it1wdo2f7l7t46rglexcd367tfmuf'


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=ACCESS_TOKEN, prefix='!', initial_channels=['unvett'])
        self.actual_poll = None

    async def create_poll(self, question):
        if self.actual_poll:
            if self.actual_poll.isAlive:
                raise PermissionError("There is already a poll in progress.")
        
        return Poll(question) 

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        #print(message.author)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def poll(self, context: commands.Context):
        poll_question = context.message.content.split("!poll ")[1]

        try:
            self.actual_poll = await self.create_poll(poll_question)
        except PermissionError as e:
            await context.send(str(e))

        await context.send(poll_question)

    @commands.command()
    async def y(self, context: commands.Context):
        try:
            self.actual_poll.vote_yes()
        except PermissionError:
            await context.send("No poll in progress")

    @commands.command()
    async def n(self, context: commands.Context):
        try:
            self.actual_poll.vote_no()
        except PermissionError:
            await context.send("No poll in progress")

    @commands.command()
    async def result(self, context: commands.Context):
        votes = self.actual_poll.finish()

        print(votes)
        print(self.actual_poll.__dict__)
        await context.send(json.dumps(votes))


bot = Bot()
bot.run()