# -*- coding: utf-8 -*-
"""
Add current time in extra fields
"""

from json import loads, dumps
from collections.abc import Mapping
from datetime import datetime as dt

from intelmq.lib.bot import Bot


class AddTimeExpertBot(Bot):

    def init(self):
        self.field_name = getattr(self.parameters,
                                    'time_field_name', 'es_time')


    def process(self):
        event = self.receive_message()
        now_time = dt.utcnow().isoformat()
        if 'extra' in event:
            extra = event['extra']
            if isinstance(extra, str):
                    try:
                        extra = loads(extra)
                    except:
                        pass
            if isinstance(extra, Mapping):
                event.add('extra.{}'.format(self.field_name), now_time)
            # oddity existing extra value is string and we dont know the key
            # how do we handle this?
            else:
                extra = {
                            "extra": extra,
                            self.field_name: now_time
                        }
                event.change('extra',extra)

        else: # no extra add extra
            event.add('extra',{self.field_name: now_time})


        self.send_message(event)
        self.acknowledge_message()


BOT = AddTimeExpertBot
