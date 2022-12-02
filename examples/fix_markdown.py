"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="text-davinci-003",
          temperature=0.5,
          max_tokens=1024
)





# corrected_text = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt=text,
#     temperature=0.5,
#     max_tokens=1024,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )


gpt.add_example(Example('Me no write so good',
                        'I do not know how to write well.'))
gpt.add_example(Example('wHat Is YOUR name',
                        'What is your name?'))
gpt.add_example(Example('Click the button',
                        'Choose the button'))
gpt.add_example(Example('Click OK',
                        'Select OK.'))
gpt.add_example(Example('Next button',
                        '<span style="ssb_orange; white-space: nowrap">Next</span> button'))
         

# Define UI configuration
config = UIConfig(description="Insert Markdown here",
                  button_text="Fix my markdown!",
                  placeholder="Me no write so good")

demo_web_app(gpt, config)
