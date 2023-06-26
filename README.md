# Yadis

## Rus:
Название Yadis расшифровывается как *Y*et *A*nother *DIS*cord bot<br>

<br><br>

Для запуска данного бота:
```shell
git clone https://github.com/Tumpa-Prizrak/yadis-discord-bot.git
cd yadis-discord-bot
pip3 install -r requirements.txt
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

После этого откройте файл ``src/config/pyconfig.py``
и найдите переменную version
```py
verson = Version(0, 0, 1, True, False)
```
замените четвёртый аттрибут на False
```py
verson = Version(0, 0, 1, False, False)
```

<br><br>

Запустить бота можно при помощи следующей команды:
```shell
python3 -m src
```
Бот тестировался на версии `3.10.8`, но может 
работать и на более ранних или поздних версиях

## Eng
The name Yadis stands for *Y*et *A*nother *DIS*cord bot<br>

<br><br>

To run this bot:
```shell
git clone https://github.com/Tumpa-Prizrak/yadis.git
cd yadis
pip3 install -r requirements.txt
```
Next, create a file called `src/config/bot_info.json` and fill it with the following fields
- token `str` bot token that was received from [this page] (https://discord.com/developers/applications)
- appid `int` application id. Received in the same place
- prefix `str` Symbol from which you will start the commands *(prefix)*.
- debug_channel_id `int` Id of the channel to which the bot sends logs.
- intents `int` intents. On [this website] (https://discord-intents-calculator.vercel.app) you can easily calculate this.

The result file will be something like this
```json
{
    "token": "xxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "appid": 000000000000000000000,
    "prefix": "_",
    "debug_channel_id": 0,
    "intents": 0
}
```

Next, open ``src/config/pyconfig.py``
and search for variable version
```py
verson = Version(0, 0, 1, True, False)
```
Change the fourth attribute to False
```py
verson = Version(0, 0, 1, False, False)
```

<br><br>

With the following command you can run the bot:
```shell
python3 -m src
```
The bot was tested on version ``3.10.8``, but
may work on earlier or later versions
