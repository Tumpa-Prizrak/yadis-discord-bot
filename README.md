# Yadis

## Rus:
Название Yadis расшифровывается как *Y*et *A*nother *DIS*cord bot<br>

Для запуска данного бота:
```shell
git clone https://github.com/Tumpa-Prizrak/yadis.git
cd yadis # Клонирование репозитория и переход в корневую директорию
pip3 install -r requirements.txt # Установка зависимостей
```
Далее создайте файл `src/config/bot_info.json` и внесите в него следующие поля:
- token `str` токен бота получаемый с [этого сайта](https://discord.com/developers/applications)
- appid `int` id приложения. Получается там же
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

## Eng
The name Yadis stands for *Y*et *A*nother *DIS*cord bot bot<br>

To run this bot:
```shell
git clone https://github.com/Tumpa-Prizrak/yadis.git
cd yadis # Clone the repository and jump to the root directory
pip3 install -r requirements.txt # Install dependencies
```
Next, create a file `src/config/bot_info.json` and enter the following fields into it:
- token `str` bot token received from [this site](https://discord.com/developers/applications)
- appid `int` application id. Obtained in the same place
- prefix `str` symbol from which you start commands *(prefix)*
- debug_channel_id `int` id of the channel to which the bot will send logs
- intents `int` intents. You can easily calculate on [this website](https://discord-intents-calculator.vercel.app)

The resulting file will look something like this:
```json
{
    "token": "xxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "appid": 000000000000000000000,
    "prefix": "_",
    "debug_channel_id": 0,
    "intents": 0
}
```

You can run the bot with the following command:
```shell
python3 -m src
```
The bot has been tested on version ``3.10.8``, but may 
may work on earlier or later versions
