# OBJECTIVES:
#
# 1) make sure that we can initialize / instantiate our Team class
#
# 2) make sure that the Team class' .full_name property behaves as desired
#

import unittest

from app.team import Team

class TestTeams(unittest.TestCase):

    def test_full_name(self):
        team = Team("New York", "Giants", [])
        self.assertEqual(team.full_name, "New York Giants")

if __name__ == "__main__": # only run if this script is invoked from the command-line:
    unittest.main()
