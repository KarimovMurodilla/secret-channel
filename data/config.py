from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

# Telegram Bot
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов


# Mailjet Api (Send mail)
API_KEY = env.str("API_KEY")
API_SECRET = env.str("API_SECRET")