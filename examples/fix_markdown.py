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
#Examples of inclusive language
gpt.add_example(Example('Click yes',
                        'Choose **Yes**'))
gpt.add_example(Example('Click OK',
                        'Select OK.'))
#Define button styles
gpt.add_example(Example('Next button',
                        '<span style="ssb_orange; white-space: nowrap">Next</span> button'))
#Standardize headings for tasks and subtasks
gpt.add_example(Example('## View the live streaming workflow',
                        '## Task 1: View the live stream'))
gpt.add_example(Example('### Watch The Live Stream',
                        '### Task 1.1: Watch the live stream'))
gpt.add_example(Example('### Create a Topic and Subscription in Amazon SNS',
                        '### Task 2.1: Create a topic and subscription in Amazon SNS'))
#Examples of tabs placed inside ** **
gpt.add_example(Example('Click the Destinations tab',
                        'Select the **Destinations** tab'))
gpt.add_example(Example('Open the Networking tab',
                        'Open the **Networking** tab'))
#Examples of using the search bar
gpt.add_example(Example('Go to the **Simple Notification Service** console.',
                        'At the top of the AWS Management Console, in the search bar, search for and choose `Simple Notification Service`.'))
gpt.add_example(Example('Open the **EC2** console.',
                        'At the top of the AWS Management Console, in the search bar, search for and choose `EC2`.'))
gpt.add_example(Example('In the search box to the right of <i class="fas fa-th"></i> **Services**, search for and choose **IAM** to open the IAM console.',
                        'At the top of the AWS Management Console, in the search bar, search for and choose `IAM`.'))
#Examples of using correct names for services
gpt.add_example(Example('Cloudfront is a global content delivery network',
                        '**Amazon Cloudfront** is a global content delivery network'))
gpt.add_example(Example('Cloudwatch is a managed monitoring service for resources and applications in the cloud',
                        '**Amazon Cloudwatch** is a managed monitoring service for resources and applications in the cloud'))
gpt.add_example(Example('DynamoDB is a managed NoSQL database',
                        '**Amazon DynamoDB** is a managed NoSQL database'))


# Define UI configuration
config = UIConfig(description="Insert Markdown here",
                  button_text="Fix my markdown!",
                  placeholder="Me no write so good")

demo_web_app(gpt, config)
