import string
from string import punctuation
import numbers
import os
import ssl
import random
import discord
from dotenv import load_dotenv

try:
    msg = await client.wait_for_message(timeout= 30, author=message.author, check=check)
    