import uuid

polls = []

class Poll:
    def __init__(self, question):
        self.poll_id = uuid.uuid4().hex
        self.question = question
        self.votes = {
            "Yes": 0,
            "No": 0
        }
        self.isAlive = True
        self.__persiste_polls()

    def allow_by_status(function):
        def wrapper(self):
            if not self.isAlive:
                raise PermissionError("This poll is now closed.")

            return function(self)
        return wrapper

    def __persiste_polls(self):
        polls.append(self.__dict__)

    @allow_by_status
    def vote_yes(self):
        self.votes["Yes"] += 1

    @allow_by_status
    def vote_no(self):
        self.votes["No"] += 1

    def finish(self) -> dict:
        self.isAlive = False

        return self.votes
