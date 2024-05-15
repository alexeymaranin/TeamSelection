from players import Team, List, get_balanced_teams


def html_output_of_teams(teams: List[Team]) -> str:
    html_message = ''
    for team in teams:
        players_str = ''
        for player in team.players:
            players_str += f'<u>{player.name}</u> <i>({player.rating})</i>\n'
        html_message += f'<b>Team {teams.index(team)+1}:</b> <i>(Total rating: {team.total_rating})</i>\n' + players_str + '\n'
    return html_message


# players_string: str = 'Кирилл 74, Азамат 68, Валера 74, Аргентина 81, Игорь 85, Алексей 85, Шота 89, ' \
#                       'Эдик 81, Ваня 86, Овик 79, Вася 72, Дима 76, Миша 95, Евгений 91, Вадим 90'
# teams_test = get_balanced_teams(players_string, 3)
# print(html_output_of_teams(teams_test))

