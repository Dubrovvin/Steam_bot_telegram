from config_data import config
#Модуль для работы с внешними API Steam



def steam_id_url(name):
    url = f'{config.STEAM_API_URL}/ISteamUser/ResolveVanityURL/v0001/?key={config.STEAM_API_KEY}&vanityurl={name}'
    print(url)
    return url

def steam_info_url(id):
    url = (f'{config.STEAM_API_URL}/IPlayerService/GetOwnedGames/v1/?key={config.STEAM_API_KEY}&'
           f'steamid={id}&include_appinfo=true&include_played_free_games=true&l=ru&format=json')
    return url

