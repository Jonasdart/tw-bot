import utils.polls as polls
import unittest


class Test(unittest.TestCase):
    def test_1_create_a_poll(self):
        poll = polls.Poll("Teste")
        assert poll.question == "Teste"

    def test_2_finish_a_poll(self):
        poll = polls.Poll("Teste")
        votes = poll.finish()

        assert poll.isAlive == False
        self.assertRaises(PermissionError, poll.vote_yes)
        assert votes == {"Yes": 0, "No": 0}

    def test_3_voting(self):
        poll = polls.Poll("Teste")
        poll.vote_no("username_teste")
        poll.vote_yes("username_teste2")
        assert poll.votes == {"Yes": 1, "No": 1}

    def test_4_voting_again(self):
        poll = polls.Poll("Teste")
        poll.vote_yes("username_teste")
        poll.vote_no("username_teste")
        assert poll.votes == {"Yes": 1, "No": 0}


