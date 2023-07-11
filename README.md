# Yadis

## Rus:
Название Yadis расшифровывается как *Y*et *A*nother *DIS*cord bot<br>

Для запуска данного бота:
```shell
git clone https://github.com/Tumpa-Prizrak/yadis-discord-bot.git
cd yadis-discord-bot\src
pip3 install -r requirements.txt
```
Далее создайте файл `src\models\config\bot_info.json` и внесите в него следующие поля:
- token `str` токен. Можно получить на [этом сайте](https://discord.com/developers/applications/)
- prefix `str` префикс.
- intents `int` интенты. Можно легко посчитать на [этом сайте](https://discord-intents-calculator.vercel.app)

Готовый файл будет выглядеть примерно так:
```json
{
    "token": "xxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "prefix": "_",
    "intents": 0
}
```

<br><br>

Перед запуском убедитесь, что вы находитесь в дирекотрии yadis-discord-bot\src <br>
Запустить бота можно при помощи следующей команды:
```shell
python3 main.py
```
Бот тестировался на версии `3.10.8`, но может 
работать и на более ранних или поздних версиях

## Eng
The name Yadis is decoded as *Y*et *A*nother *DIS*cord bot<br>

To run this bot:
```shell
git clone https://github.com/Tumpa-Prizrak/yadis-discord-bot.git
cd yadis-discord-bot\src
pip3 install -r requirements.txt
```
Then create the file ``src\models\config\bot_info.json`` and enter the following fields into it:
- token ``str`` token. Can be obtained on [this site](https://discord.com/developers/applications/)
- prefix ``str`` prefix.
- intents ``int`` intents. Can be easily calculated on [this site](https://discord-intents-calculator.vercel.app)

The finished file will look something like this:
```json
{
    "token": "xxxxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "prefix": "_",
    "intents": 0 
}
```
Before starting, make sure you are in the yadis-discord-bot\src directory<br>
You can start the bot using the following command:
```
python3 main.py
```
The bot was tested on version `3.10.8`, but maywork on earlier or later versions