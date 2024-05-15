from savings import save_players, save_teams_count, read_user_saving, User
from players import get_balanced_teams
from decoration import html_output_of_teams


def create_balanced_teams(user_id: int) -> str:
    try:
        user = read_user_saving(user_id)
    except:
        return 'You did not load players with ranks and teams number'

    if user.players == '' or user.teams_count == 0:
        return 'Please choose players and teams number'
    else:
        try:
            teams = get_balanced_teams(players_str=user.players, teams_number=user.teams_count)
            teams_html = html_output_of_teams(teams)
            return teams_html
        except:
            return 'Check format of players (no spaces in name of player) or teams number, try to load player names ' \
                   'without spaces. Use format: Name1 89, Name_Surname2 85, Name_Surname3 79 '


def load_user_data(load_state: str, user_id: int, message_text: str) -> str:
    if load_state == 'players':
        players = message_text
        try:
            mess = save_players(user_id=user_id, players=players)
            return mess
        except:
            return 'something went wrong, try again. Load player names without spaces. Use format: Name1 89, ' \
                   'Name_Surname2 85, Name_Surname3 79 '
    elif load_state == 'teams':
        try:
            teams_count = int(message_text)
        except ValueError:
            return 'you need to write a number of teams'
        try:
            mess = save_teams_count(user_id=user_id, teams_count=teams_count)
            return mess
        except:
            return 'Could not save number of players'
    else:
        return 'Choose command /load_players to add players, or /teams_number to add number of teams'
