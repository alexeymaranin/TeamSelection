import json
from typing import NamedTuple, List, Dict

from exceptions import NoUserData


class User(NamedTuple):
    id: int
    players: str
    teams_count: int


def _find_user_saving(user_id: int) -> User:
    try:
        user = read_user_saving(user_id)
    except NoUserData:
        user = _create_user_saving(user_id)
    return user


def _write_saving(user: User):
    file_name = f'users/{user.id}.txt'
    user_json = json.dumps({"id": user.id, "players": user.players, "teams_count": user.teams_count})
    with open(file_name, 'w') as file:
        file.write(user_json)


def _create_user_saving(user_id: int) -> User:
    user = User(id=user_id, players='', teams_count=0)
    _write_saving(user)

    return user


def read_user_saving(user_id: int) -> User:
    file_name = f'users/{user_id}.txt'
    try:
        with open(file_name, 'r') as file:
            from_json = file.read()
    except FileNotFoundError:
        raise NoUserData
    user_data = json.loads(from_json)
    user = User(id=user_data['id'], players=user_data['players'], teams_count=user_data['teams_count'])
    return user


def _update_user_saving(user_id: int, players: str, teams_count: int):
    file_name = f'users/{user_id}.txt'
    user_json = json.dumps({'id': user_id, 'players': players, 'teams_count': teams_count})
    with open(file_name, 'w') as file:
        file.write(user_json)


def save_players(user_id: int, players: str) -> str:
    user = _find_user_saving(user_id)

    new_user = User(id=user.id, players=players, teams_count=user.teams_count)
    _write_saving(new_user)
    return 'Players are added'


def save_teams_count(user_id: int, teams_count: int) -> str:
    user = _find_user_saving(user_id)

    new_user = User(id=user.id, players=user.players, teams_count=teams_count)
    _write_saving(new_user)
    return f'Divide players in {teams_count} teams'


if __name__ == '__main__':
    try:
        usr = read_user_saving(10)
    except NoUserData:
        print('no user data')
