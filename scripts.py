import string
from collections import Counter
import socket
import os

# Ensure output directory exists
if not os.path.exists('/home/data/output'):
    os.makedirs('/home/data/output')

# Function to clean text and remove punctuation, while preserving standalone words
def clean_text(text):
    # Remove punctuation and lower the case
    return text.translate(str.maketrans('', '', string.punctuation)).lower()

# Count the number of words in a file
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()  # Read the file as-is
        cleaned_text = clean_text(text)  # Clean the text
    return len(cleaned_text.split())

# Get the top 3 most frequent words in a file
def top_3_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()  # Read the file as-is
        cleaned_words = clean_text(text).split()  # Clean and split into words
    word_count = Counter(cleaned_words)
    return word_count.most_common(3)

# Handle contractions
def handle_contractions(text):
    contractions = {
        "I'm": "I am", "It's": "It is", "I'll": "I will",
        "you're": "you are", "You're": "You are", "can't": "can not",
        "couldn't": "could not", "don't": "do not", "won't": "will not",
        "that's": "that is", "don’t": "do not", "that’s": "that is",
        "build ’em": "build them", "you’ve": "you have", "you’ll": "you will"
    }
    for contraction, full_form in contractions.items():
        text = text.replace(contraction, full_form)
    return text

# Count words in a file with contractions handled
def count_words_with_contractions(file_path):
    with open(file_path, 'r') as file:
        text = file.read()  # Read the file as-is
        text = handle_contractions(text)  # Handle contractions
        cleaned_text = clean_text(text)  # Clean the text
    return len(cleaned_text.split())

# Get the top 3 words in a file after handling contractions
def top_3_contractions(file_path):
    with open(file_path, 'r') as file:
        text = file.read()  # Read the text as-is
        text = handle_contractions(text)  # Handle contractions
        cleaned_words = clean_text(text).split()  # Clean and split into words
    word_count = Counter(cleaned_words)
    return word_count.most_common(3)

# Get the container's IP address
def get_ip():
    return socket.gethostbyname(socket.gethostname())

# Count words in both files without contractions
total_words_if = count_words('/home/data/IF.txt')
total_words_always = count_words('/home/data/AlwaysRememberUsThisWay.txt')
grand_total = total_words_if + total_words_always

# Count words in both files with contractions handled
total_words_if_with_contractions = count_words_with_contractions('/home/data/IF.txt')
total_words_always_with_contractions = count_words_with_contractions('/home/data/AlwaysRememberUsThisWay.txt')
grand_total_with_contractions = total_words_if_with_contractions + total_words_always_with_contractions

# Top 3 words in IF.txt without contractions
top_if = top_3_words('/home/data/IF.txt')
# Top 3 words in AlwaysRememberUsThisWay.txt without contractions
top_always = top_3_words('/home/data/AlwaysRememberUsThisWay.txt')

# Top 3 words in IF.txt with contractions
top_if_with_contractions = top_3_contractions('/home/data/IF.txt')
# Top 3 words in AlwaysRememberUsThisWay.txt with contractions
top_always_with_contractions = top_3_contractions('/home/data/AlwaysRememberUsThisWay.txt')

# Get container's IP address
ip_address = get_ip()

# Write results to /home/data/output/result.txt
with open('/home/data/output/result.txt', 'w') as result_file:
    result_file.write(f"Results without contractions:")
    result_file.write(f"Total words in IF.txt without the contractions: {total_words_if}\n")
    result_file.write(f"Total words in AlwaysRememberUsThisWay.txt without the contractions: {total_words_always}\n")
    result_file.write(f"Grand total of words without the contractions: {grand_total}\n")
    result_file.write(f"Top 3 words in IF.txt without the contractions: {top_if}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt without the contractions: {top_always}\n")
    
    result_file.write(f"Results with contractions:")
    result_file.write(f"\nTotal words in IF.txt with contractions: {total_words_if_with_contractions}\n")
    result_file.write(f"Total words in AlwaysRememberUsThisWay.txt with contractions: {total_words_always_with_contractions}\n")
    result_file.write(f"Grand total of words with contractions: {grand_total_with_contractions}\n")
    result_file.write(f"Top 3 words in IF.txt with contractions: {top_if_with_contractions}\n")
    result_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt with contractions: {top_always_with_contractions}\n")
    
    result_file.write(f"IP Address: {ip_address}\n")

# Print the result before exiting
with open('/home/data/output/result.txt', 'r') as result_file:
    print(result_file.read())
