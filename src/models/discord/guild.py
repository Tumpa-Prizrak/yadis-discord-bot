import typing

from discord import Guild as dGuild
from discord import VoiceChannel


class Guild:
    """
    Класс, представляющий гильдию Discord.
    
    Атрибуты:
    custom_voice_entry (typing.Optional[VoiceChannel]): Кастомный голосовой канал для гильдии.
    is_blacklisted (bool): Флаг, указывающий, занесена ли гильдия в черный список.
    guild (dGuild): Объект гильдии Discord.
    
    Методы:
    __init__(guild: dGuild, is_blacklisted: bool | int, custom_voice_entry: typing.Optional[VoiceChannel] = None) -> None: 
    Инициализирует гильдию.
    
        Параметры:
        guild (dGuild): Объект гильдии Discord.
        is_blacklisted (bool | int): Флаг, указывающий, занесена ли гильдия в черный список.
        custom_voice_entry (typing.Optional[VoiceChannel], optional): Кастомный голосовой канал для гильдии.
        
        Действия:
        - Сохраняет параметры в атрибуты класса.
        - Преобразует is_blacklisted в bool.
    
    """
    custom_voice_entry: typing.Optional[VoiceChannel]
    is_blacklisted: bool
    guild: dGuild

    def __init__(
        self,
        guild: dGuild,
        is_blacklisted: bool | int,
        custom_voice_entry: typing.Optional[VoiceChannel] = None,
    ) -> None:
        self.guild = guild
        self.is_blacklisted = bool(is_blacklisted)
        self.custom_voice_entry = custom_voice_entry
