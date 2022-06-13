from .db import get_db, Query

_polls_db = get_db()

def _persist_polls(function):
    def wrapper(self, *args):
        function_return = function(self, *args)

        poll_query = Query()
        updated_poll = _polls_db.update(
            self.__dict__, poll_query.poll_id == self.poll_id
        )
        if not updated_poll:
            _polls_db.insert(self.__dict__)

        return function_return

    return wrapper