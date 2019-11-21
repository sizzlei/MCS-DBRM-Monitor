import telegram
from datetime import datetime, timedelta

class botTelegram:
    _strtime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    _chat_id = ""
    _bot = ""

    def __init__(self, _token, _chatid):
        self._bot = telegram.Bot(token=_token)
        self._chat_id = _chatid

    def Send(self, _msg):
        _alert_form = 'STR : <b>%s</b> End : <b>%s</b> Message : <b>%s</b>'
        _end_time = datetime.today().strftime("%H:%M:%S")
        _alert_msg = _alert_form % (self._strtime, _end_time, _msg)

        try:
            self._bot.sendMessage(chat_id=self._chat_id, text=_alert_msg, parse_mode=telegram.ParseMode.HTML)
        except Exception as Chat_err:
            print(Chat_err)