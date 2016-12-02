eliza
=============

## Overview
A chatbot that emulates a Rogerian psychotherapist, implemented to be a Beep Boop hostable, Python-based Slack bot.

## Assumptions
* You have already signed up with [Beep Boop](https://beepboophq.com) and have a local fork of this project.
* You have sufficient rights in your Slack team to configure a bot and generate/access a Slack API token.

## Usage

### Run locally
Install dependencies ([virtualenv](http://virtualenv.readthedocs.org/en/latest/) is recommended.)

	pip install -r requirements.txt
	export SLACK_TOKEN=<YOUR SLACK TOKEN>; python ./bot/app.py

Things are looking good if the console prints something like:

	Connected <your bot name> to <your slack team> team at https://<your slack team>.slack.com.

If you want change the logging level, prepend `export LOG_LEVEL=<your level>; ` to the `python ./bot/app.py` command.

### Run locally in Docker
	docker build -t starter-python-bot .
	docker run --rm -it -e SLACK_TOKEN=<YOUR SLACK API TOKEN> starter-python-bot

### Run in BeepBoop
If you have linked your local repo with the Beep Boop service (check [here](https://beepboophq.com/0_o/my-projects)), changes pushed to the remote master branch will automatically deploy.

## Credits
The chatbot Eliza was first implemented in 1966 by [Joseph Weizenbaum](https://en.wikipedia.org/wiki/Joseph_Weizenbaum). Much of this project's code was implemented by [Evan Dempsey](https://www.smallsurething.com/implementing-the-famous-eliza-chatbot-in-python/), who again credits [Joe Strout](http://www.jezuk.co.uk/cgi-bin/view/software/eliza) for the original Python implementation.

The [BeepBoop](https://beepboophq.com/docs/article/overview) bot design of this project is heavily inspired by [BeepBoopHQ's Starter Python bot](https://github.com/BeepBoopHQ/starter-python-bot/) (MIT license).

## License
See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
