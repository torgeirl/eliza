import json
import logging
import re

logger = logging.getLogger(__name__)


class RtmEventHandler(object):
    def __init__(self, slack_clients, msg_writer):
        self.clients = slack_clients
        self.msg_writer = msg_writer

    def handle(self, event):
        if 'type' in event:
            self._handle_by_type(event['type'], event)

    def _handle_by_type(self, event_type, event):
        # See https://api.slack.com/rtm for a full list of events
        if event_type == 'error':
            # error
            self.msg_writer.write_error(event['channel'], json.dumps(event))
        elif event_type == 'message':
            # message was sent to channel
            self._handle_message(event)
        elif event_type == 'channel_joined':
            # you joined a channel
            self.msg_writer.write_starter(event['channel'])
        elif event_type == 'group_joined':
            # you joined a private group
            self.msg_writer.write_starter(event['channel'])
        else:
            pass

    def _handle_message(self, event):
        # Filter out messages from the bot itself, and from non-users (eg. webhooks)
        if ('user' in event) and (not self.clients.is_message_from_me(event['user'])):

            msg_txt = event['text']

            if self.clients.is_bot_mention(msg_txt) or self._is_direct_message(event['channel']):
                if re.search('hi|hello', msg_txt):
                    self.msg_writer.write_greeting(event['channel'], event['user'])
                elif re.search('goodbye', msg_txt):
                    self.msg_writer.write_goodbye(event['channel'], event['user'])
                else:
                    self.msg_writer.write_psychobabble(event['channel'], msg_txt)
            else:
                self.msg_writer.write_psychobabble(event['channel'], msg_txt)

    def _is_direct_message(self, channel):
         return channel.startswith('D')
