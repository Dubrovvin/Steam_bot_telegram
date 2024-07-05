from config_data import config


def steam_id_url(name: str) -> str:
    """
    Генерирует URL для запроса Steam API для разрешения vanity URL пользователя.

    :param name: (str) Vanity URL или пользовательское имя в Steam.
    :return: (str) Сформированный URL для запроса к Steam API.
    """
    url = f'{config.STEAM_API_URL}/ISteamUser/ResolveVanityURL/v0001/?key={config.STEAM_API_KEY}&vanityurl={name}'
    print(url)
    return url


def steam_info_url(id: str) -> str:
    """
    Генерирует URL для запроса Steam API для получения информации о играх пользователя.

    :param id: (str) Steam ID пользователя.
    :return: (str) Сформированный URL для запроса к Steam API.
    """
    url = (f'{config.STEAM_API_URL}/IPlayerService/GetOwnedGames/v1/?key={config.STEAM_API_KEY}&'
           f'steamid={id}&include_appinfo=true&include_played_free_games=true&l=ru&format=json')
    return url

