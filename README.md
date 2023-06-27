## WhatsAppBot-AdminChecker

WhatsAppBot-AdminChecker is a versatile and resilient WhatsApp bot implemented in Python, designed to simplify group chat administration. It offers a range of functionalities that can be easily integrated into your projects. The bot operates without relying on Selenium, ensuring compatibility even if WhatsApp undergoes code changes.

## Features

- [x] Listen to new messages
- [x] Mute participants
- [x] Unmute participants
- [x] Ask ChatGPT
- [x] Send a message

## Requirements

To use WhatsAppBot-AdminChecker, ensure you have the following dependencies installed:

- Python 3.x
- pyautogui
- pyperclip
- re
- time
- threading
- sys

## Usage

1. Import the necessary libraries.

```python
from pyautogui import moveTo, click, rightClick, write, keyDown, keyUp, hotkey, scroll
import pyautogui
import pyperclip
import re
import time
from threading import Thread, Event
import sys
```

2. Define the required functions for bot functionalities such as `send`, `searchimagine`, `checkuserperms`, `unmute`, `mute`, `ask`, and `runspccmd`.

```python
# Define functions for bot functionalities

def send(message1):
    # Implementation for sending a message
    # ...

def searchimagine(ce):
    # Implementation for searching an image
    # ...

def checkuserperms():
    # Implementation for checking user permissions
    # ...

def unmute(time34=1, name1="test"):
    # Implementation for unmuting a participant
    # ...

def mute(name, time2, reason="None"):
    # Implementation for muting a participant
    # ...

def ask(what):
    # Implementation for asking a question
    # ...

def runspccmd(lastmessage):
    # Implementation for running special commands
    # ...
```

3. Customize the bot's behavior and settings according to your project requirements.

4. Run the bot.

```python
while True:
    # Bot main loop
    # ...
```

## Customization

Feel free to modify the provided code to suit your specific project needs. You can comment out or remove any unnecessary functionalities. Additionally, you can integrate this code into your existing projects by incorporating the required functions and methods.

## Contributions

Contributions to WhatsAppBot-AdminChecker are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Start using WhatsAppBot-AdminChecker today to streamline your group chat administration and leverage the power of Python automation!
