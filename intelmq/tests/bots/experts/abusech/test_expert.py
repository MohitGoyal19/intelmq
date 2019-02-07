# -*- coding: utf-8 -*-
import unittest

import intelmq.lib.test as test
from intelmq.bots.experts.abusech.expert_urlhaus import AbusechURLhausExpertBot

EXAMPLE_INPUT = {"__type": "Event",
                 "extra.tags": "elf,mirai",
                 "extra.urlhaus.threat_type": "malware_download",
                 "extra.urlhaus_link": "https://urlhaus.abuse.ch/url/116575/",
                 "feed.provider": "abuse.ch",
                 "feed.url": "https://urlhaus.abuse.ch/downloads/csv/",
                 "source.url": "http://209.97.182.204/bins/frosty.mpsl",
                 "status": "online",
                 "time.observation": "2019-02-04T07:05:58+00:00",
                 "time.source": "2019-02-04T07:03:22+00:00"
                 }
EXAMPLE_OUTPUT = {"__type": "Event",
                  "extra.tags": "elf,mirai",
                  "extra.urlhaus.threat_type": "malware_download",
                  "extra.urlhaus_link": "https://urlhaus.abuse.ch/url/116575/",
                  "feed.provider": "abuse.ch",
                  "feed.url": "https://urlhaus.abuse.ch/downloads/csv/",
                  "source.url": "http://209.97.182.204/bins/frosty.mpsl",
                  "status": "online",
                  "time.observation": "2019-02-04T07:05:58+00:00",
                  "time.source": "2019-02-04T07:03:22+00:00",
                  "malware.hash.sha256": "7846fd95d0885658945dd665d5699b040af30236b30d06f2ddd0b160018e4419"
                  }


class TestAbusechURLhausExpertBot(test.BotTestCase, unittest.TestCase):

    @classmethod
    def set_bot(cls):
        cls.bot_reference = AbusechURLhausExpertBot

    def test_event(self):
        self.input_message = EXAMPLE_INPUT
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_OUTPUT)


if __name__ == '__main__':
    unittest.main
