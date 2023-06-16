# Yadik

## Rus:
Название Yadik расшифровывается как *Y*et *A*nother *DI*s*K*ord bot<br>

Для запуска данного бота:
```shell
git clone git@github.com:Tumpa-Prizrak/yadis.git
cd yadis # Клонирование репозитория и переход в корневую директорию
pip3 install -r requirements.txt # Установка зависимостей
```
Далее создайте файл `src/config/bot_info.json` и внесите в него следующие поля:
- token `str` токен бота получаемый с [этого сайта](https://discord.com/developers/applications)
- appid `int` id приложения. Получается там же и равен id бота
- prefix `str` символ с которого начинаются команды *(префикс)*
- debug_channel_id `int` id канала, в который бот будет отправалять логи
- intents `int` интенты. Можно легко посчитать на [этом сайте](https://discord-intents-calculator.vercel.app)

Готовый файл будет выглядеть примерно так:
```json
{
    "token": "xxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "appid": 0000000000000000000,
    "prefix": "_",
    "debug_channel_id": 0,
    "intents": 0
}
```

Запустить бота можно при помощи следующей команды:
```shell
python3 -m src
```
Бот тестировался на версии `3.10.8`, но может 
работать и на более ранних или поздних версиях
