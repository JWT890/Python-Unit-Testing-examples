import unittest
from voting import voter_id

class ValidatingVoterId(unittest.TestCase):
    def validate_voter_id(voter_id):
        return voter_id in voter_id

    def validate_vote(vote):
        return vote [1,2]