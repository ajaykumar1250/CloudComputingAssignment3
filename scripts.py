import os
from collections import Counter
import socket
import re

# Define file paths
file1_path = "/home/data/IF.txt"
file2_path = "/home/data/AlwaysRememberUsThisWay.txt"
output_file = "result.txt"

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# 1. Count the total number of words in each file
def word_count(text):
    return len(text.split())

# 2. Calculate grand total words across both files
def grand_total(count1, count2):
    return count1 + count2

# 3. Find top 3 most frequent words in IF.txt
def top_words(text, top_n=3):
    words = text.split()
    counter = Counter(words)
    return counter.most_common(top_n)

# 4. Handle contractions and split them into individual words
def handle_contractions(text):
    contractions = {
        "I'm": "I am", "can't": "cannot", "don't": "do not", 
        "you're": "you are", "they're": "they are", "it's": "it is",
        "isn't": "is not", "aren't": "are not", "won't": "will not",
        "didn't": "did not", "I'll": "I will", "we're": "we are",
        "you've": "you have", "he's": "he is", "she's": "she is",
        "wasn't": "was not", "weren't": "were not", "that's": "that is"
    }
    
    # Use regex to replace contractions with expanded forms
    pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in contractions.keys()) + r')\b')
    expanded_text = pattern.sub(lambda x: contractions[x.group(0)], text)
    
    return expanded_text

# 5. Get machine's IP address
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Main logic
if __name__ == "__main__":

    # Ensure the output directory exists
    output_dir = "/home/data/output"
    os.makedirs(output_dir, exist_ok=True)

    # Read files
    text1 = read_file(file1_path)
    text2 = read_file(file2_path)

    # Word counts
    count1 = word_count(text1)
    count2 = word_count(text2)
    grand_count = grand_total(count1, count2)

    # Top words in IF.txt
    top_if_words = top_words(text1)

    # Handle contractions in AlwaysRememberUsThisWay.txt
    text2_with_contractions = handle_contractions(text2)

    # Top words in AlwaysRememberUsThisWay.txt after handling contractions
    top_always_words = top_words(text2_with_contractions)

    # IP address
    ip_address = get_ip_address()

    # Write results to file
    with open(output_file, 'w') as output:
        output.write(f"Total words in IF.txt: {count1}\n")
        output.write(f"Total words in AlwaysRememberUsThisWay.txt: {count2}\n")
        output.write(f"Grand total words: {grand_count}\n")
        output.write(f"Top 3 words in IF.txt: {top_if_words}\n")
        output.write(f"Top 3 words in AlwaysRememberUsThisWay.txt after handling contractions: {top_always_words}\n")
        output.write(f"Container IP Address: {ip_address}\n")

    # Print result file content to console
    with open(output_file, 'r') as result:
        print(result.read())
