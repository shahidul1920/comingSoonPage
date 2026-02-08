
import os

file_path = r"c:\Users\USER\Documents\GitHub\comingSoonPage\asthacreatives\motion.html"

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Replace the specific corrupted string or patterns
# The read_file showed "15ï¿½60" which suggests the replacement character \ufffd is present
# or literal characters depending on how read_file works.
# Let's try replacing \ufffd first.
new_content = content.replace('\ufffd', '-')

# Also replace literal "ï¿½" just in case it was saved that way
new_content = new_content.replace('ï¿½', '-')

if content != new_content:
    print("Fixed corrupted characters.")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
else:
    print("No corrupted characters found to fix.")
