import os
import re
import emoji

def extract_emojis(s):
  return ''.join(c for c in s if c in emoji.UNICODE_EMOJI['en'])

os.environ['REPLICATE_API_TOKEN'] = "r8_GpHFP7FZY6kxNX5L3tZeVrQqbnHWBwW4CsSvw"

import replicate

pre_prompt = "You are an expert narrator who only uses emojis to respond to text. You need to transform the entire text below sent to you into emojis."

print("Please enter your text:")
prompt_input = input()

output = replicate.run('lucataco/llama-2-13b-chat:18f253bfce9f33fe67ba4f659232c509fbdfb5025e5dbe6027f72eeb91c8624b',
    input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ",
    "temperature":0.1, "top_p":0.9, "max_length":256})

full_response = ""

for item in output:
    full_response += item

extracted_emojis = extract_emojis(full_response)

print(extracted_emojis)
