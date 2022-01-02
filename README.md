# Telegram-Twitter-Bot
A Telegram Bot which listens to tweets from certain Twitter accounts and sends them to a specific Telegram channel in real time.

# Installation
You only need to install `requierements.txt` file in the Terminal

```
pip install -r requirements.txt

```

# Setting Up

Once the installation process has finished, you need to set your own API data. To do so, just go to `config.example.py` and add your credentials. 

You will need Twitter API data from the Twitter developer webpage. More information here: 
[Twitter API ](https://developer.twitter.com/en/products/twitter-api)

Once you have got your API variables, just add them to `config.example.py`. The necessary API Twitter data is:
`API_KEY`
`API_SECRET`
`TOKEN`
`TOKEN_SECRET`

To get a Telegram token, just go to your Telegram app and look for the `BotFather` bot. Follow the instructions to get your `TELEGRAM_BOT_API_KEY`


# Run App
Next, rename `config.example.py` to `config.py` and inspect `main.py` file. 
You will need to add the Twitter accounts you want to listen to and set the Telegram Channel ID receiver. 

Finally, just run `main.py`: 

```
python3 main.py

```
Note: To find out Twitter account IDs, you may use [TweeterID](https://tweeterid.com/)


