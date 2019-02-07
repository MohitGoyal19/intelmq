# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs

from intelmq.lib.bot import Bot
from intelmq.lib import utils


class AbusechURLhausExpertBot(Bot):

    def process(self):
        event = self.receive_message()
        url = event.get("extra.urlhaus_link")
        url = requests.get(url).text
        soup = bs(url, 'html.parser')
        soup = soup.find_all('table')
        if len(soup) > 1:
            soup = soup[1]
            soup = soup.find_all('tr')
            for i in range(1, len(soup)):
                data = soup[i].find_all('td')[3].text
                event.add('malware.hash.sha256', data, overwrite=True)
                self.send_message(event)
        self.acknowledge_message()


BOT = AbusechURLhausExpertBot
