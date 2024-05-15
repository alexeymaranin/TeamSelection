class CantGetTeamNumber(Exception):
    """ Did not get correct teams number """


class NoUserData(Exception):
    """ User did not load players and teams number """


class CantGetBalancedTeams(Exception):
    """ User did not load players and teams number """


class CantSavePlayers(Exception):
    """ Failed to save players to user data """


class CantSaveTeamsNumber(Exception):
    """ Failed to save teams number to user data """
