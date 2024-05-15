import random
import copy
from typing import NamedTuple, List


class Player(NamedTuple):
    name: str
    rating: int


class Team(NamedTuple):
    players: List[Player]
    total_rating: int


def _parse_players_from_str_to_list(players_str: str) -> List[Player]:
    players_list = [tuple(player.split(sep=' ')) for player in players_str.split(sep=', ')]
    players: List[Player] = [Player(player[0], int(player[1])) for player in players_list]
    return players


def _create_teams(players: List[Player], teams_number: int) -> List[Team]:
    players_per_team: int = int(len(players) / teams_number)
    teams = []

    for i in range(teams_number):
        selection_team = []
        for j in range(players_per_team):
            selection_team.append(players.pop(random.randint(0, len(players) - 1)))
        rating = sum([player.rating for player in selection_team])

        teams.append(Team(players=selection_team, total_rating=rating))

    return teams


def _teams_are_balanced(teams: List[Team], accuracy: int) -> bool:
    average = sum([team.total_rating for team in teams]) / len(teams)
    balanced = True
    for team in teams:
        if abs(team.total_rating - average) > accuracy:
            balanced = False
    return balanced


def get_balanced_teams(players_str: str, teams_number: int) -> List[Team]:
    players = _parse_players_from_str_to_list(players_str)
    accuracy = 1
    counter = 0
    while True:
        counter += 1
        players_copy = copy.deepcopy(players)
        teams = _create_teams(players_copy, teams_number)

        if _teams_are_balanced(teams, accuracy):
            break

        if counter > 30:
            accuracy += 1
            counter = 0

    return teams

