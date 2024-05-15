import telebot
from telebot import types
import main

TOKEN = '5455211214:AAEGQ5mgKHXPEicZfUbtG3H24qsJqbM8yYc'

bot = telebot.TeleBot(TOKEN)
user_state = {}


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'It is a bot to create balanced teams\n' \
           f'You need to load players with ranks and then choose how many teams you want to create\n' \
           f'After you load players and choose teams number press /create_teams button'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    players = types.KeyboardButton('/load_players')
    teams = types.KeyboardButton('/teams_number')
    teams_selection = types.KeyboardButton('/create_teams')
    markup.add(players, teams, teams_selection)

    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['load_players'])
def load_players(message):
    user_state[message.chat.id] = 'players'
    mess = 'Write players and points in format: Name1 89, Name_Surname2 85, Name_Surname3 79'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['teams_number'])
def teams_number(message):
    user_state[message.chat.id] = 'teams'
    mess = 'Write how many teams you want'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['create_teams'])
def create_teams(message):
    mess = main.create_balanced_teams(message.chat.id)
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    load_state = user_state.get(message.chat.id, "")
    mess = main.load_user_data(load_state, message.chat.id, message.text)
    bot.send_message(message.chat.id, mess)


if __name__ == '__main__':
    print('Bot started...')
    bot.polling(none_stop=True)
