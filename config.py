#-----------------------------------------------------------#
#  Конфигурация для аутентификации бота на серверах Twitch  #
#-----------------------------------------------------------#

# Хост и порт для входа на сервера Twitch. Не изменять ни в коем случае, иначе работать не будет!
HOST = "irc.twitch.tv"
PORT = 6667

# Настройки бота: Никнейм бота, токен бота, префикс команд и режим бета-тестирования.
BOTNAME = "xrpsxbot" # Писать нижними буквами!
OAUTHTOKEN = "TOKEN HERE" # Токен аутентификации можно взять на https://twitchapps.com/tmi/
PREFIX = "+" # Можно поменять на любые символы или даже слово :D
BOTFOLDER = "C:/xrpsxBot" # Укажите папку, где находится бот. Нужен для команд "+pasta" и "+art"

# На какой канал заходить?
CHANNELJOIN = "xrpsxbot" # Можно ввести только 1 канал, в будущем будет версия с мультиканалами :)
CHANNELJOIN = CHANNELJOIN.lower() # Поменять все буквы на нижний регистр.
IRCCHANNELJOIN = "#" + CHANNELJOIN # Для отправки данных Twitch.

modList = ['ilotterytea', 'МожноДобавитьЕщёПользователя', 'Somebody'] # Эти пользователи имеют доступ к командам, которые могут спамить: +pasta
blackList = ['BadUser', 'VeryBadUser'] # Эти пользователи не смогут никак взаимодействовать с ботом ;(.