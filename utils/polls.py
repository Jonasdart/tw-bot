import uuid
from .db import get_db

__polls_db = get_db()


class Poll:
    def __init__(self, question):
        self.poll_id = uuid.uuid4().hex
        self.question = question
        self.votes = {"Yes": 0, "No": 0}
        self.isAlive = True
        self.__persiste_polls()
        self.voters = []

    def allow_by_status(function):
        def wrapper(self, *args):
            if not self.isAlive:
                raise PermissionError("This poll is now closed.")

            return function(self, *args)

        return wrapper

    def __persiste_polls(self):
        __polls_db.insert(self.__dict__)

    @allow_by_status
    def vote_yes(self, username):
        if username not in self.voters:
            self.votes["Yes"] += 1
            self.voters.append(username)

    @allow_by_status
    def vote_no(self, username):
        if username not in self.voters:
            self.votes["No"] += 1
            self.voters.append(username)

    @allow_by_status
    def finish(self) -> dict:
        self.isAlive = False

        return self.votes
