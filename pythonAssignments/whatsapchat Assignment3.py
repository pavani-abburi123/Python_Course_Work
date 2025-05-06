
#Assignment 3#


n = int(input("Enter number of chat entries: "))
conversations = {}

for _ in range(n):
    sender, message = input().split(":", 1)
    sender = sender.strip()
    message = message.strip()
    if sender in conversations:
        conversations[sender].append(message)
    else:
        conversations[sender] = [message]

print(conversations)
print(conversations.keys())


def show_menu():
    options = [
        "Exit","Count total number of messages","Identify unique participants","Count total words in messages",
        "Calculate average words per message","Find the longest message sent","Find the most active participant",
        "Get message count for a participant","Find the most frequent word by a participant", "Retrieve first and last messages from a participant",
        "Check if a participant exists","Find repeated words in chat","Participant with longest average message length",
        "Count messages that mention a specific participant","Remove repeated messages","Sort messages alphabetically",
        "Extract all questions", "Calculate reply ratio between two participants","Check for deleted messages"
    ]
    for i in range(len(options)):
        print(f"{i}. {options[i]}")


def total_messages(conv):
    total = 0
    for user in conv:
        total += len(conv[user])
    return total


def unique_participants(conv):
    unique_set = set()
    for user in conv:
        unique_set.add(user)
    return f"{len(unique_set)}\n{unique_set}"


def total_words(conv):
    all_text = ""
    for user in conv:
        for msg in conv[user]:
            all_text += msg + " "
    return len(all_text.split())


def average_words(conv):
    total_msg = 0
    all_text = ""
    for user in conv:
        for msg in conv[user]:
            total_msg += 1
            all_text += msg + " "
    if total_msg == 0:
        return 0
    return len(all_text.split()) / total_msg


def get_longest_message(conv):
    longest = ""
    for user in conv:
        for msg in conv[user]:
            if len(msg) > len(longest):
                longest = msg
    return longest


def top_sender(conv):
    max_count = 0
    max_user = ""
    for user in conv:
        if len(conv[user]) > max_count:
            max_count = len(conv[user])
            max_user = user
    return max_user


def message_count(conv):
    user = input("Enter participant name: ")
    if user in conv:
        return len(conv[user])
    return 0


def most_used_word(conv):
    user = input("Enter participant name: ")
    word_count = {}
    if user in conv:
        for msg in conv[user]:
            words = msg.split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    max_word = ""
    max_count = 0
    for word in word_count:
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word
    return max_word


def first_and_last(conv):
    user = input("Enter participant name: ")
    if user in conv:
        return f"First: {conv[user][0]}\nLast: {conv[user][-1]}"
    return "User not found"


def check_participant(conv):
    user = input("Enter participant name: ")
    if user in conv:
        return "Found"
    return "Not found"


def repeated_words(conv):
    word_count = {}
    for user in conv:
        for msg in conv[user]:
            words = msg.split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    repeated = []
    for word in word_count:
        if word_count[word] > 1:
            repeated.append(word)
    return repeated


def longest_avg_msg(conv):
    max_avg = 0
    top_user = ""
    for user in conv:
        total_words = 0
        total_msgs = len(conv[user])
        for msg in conv[user]:
            total_words += len(msg.split())
        avg = total_words / total_msgs if total_msgs > 0 else 0
        if avg > max_avg:
            max_avg = avg
            top_user = user
    return f"{top_user} with avg length {max_avg}"


def mention_count(conv):
    user = input("Enter participant name to check mentions: ")
    count = 0
    for sender in conv:
        for msg in conv[sender]:
            if user in msg:
                count += 1
    return count


def clean_duplicates(conv):
    for user in conv:
        seen = set()
        unique_msgs = []
        for msg in conv[user]:
            if msg not in seen:
                seen.add(msg)
                unique_msgs.append(msg)
        conv[user] = unique_msgs
    return conv


def alphabetical_msgs(conv):
    all_msgs = []
    for user in conv:
        for msg in conv[user]:
            all_msgs.append(msg)
    all_msgs.sort()
    return all_msgs


def question_messages(conv):
    questions = []
    for user in conv:
        for msg in conv[user]:
            if "?" in msg:
                questions.append(msg)
    return questions


def reply_ratio(conv):
    p1, p2 = input("Enter two names (A and B): ").split(" and ")
    p1 = p1.strip()
    p2 = p2.strip()
    count = 0
    if p2 in conv:
        for msg in conv[p2]:
            if p1 in msg:
                count += 1
    return f"Replies from {p2} to {p1}: {count}"


def check_deleted(conv):
    deleted_count = 0
    for user in conv:
        for msg in conv[user]:
            if "deleted" in msg.lower():
                deleted_count += 1
    return deleted_count


while True:
    print("===" * 15)
    print("Menu:")
    show_menu()
    print("===" * 15)
    option = int(input("Enter your choice: "))
    if option == 0:
        break
    elif option == 1:
        print("Total messages:", total_messages(conversations))
    elif option == 2:
        print("Unique participants:", unique_participants(conversations))
    elif option == 3:
        print("Total words:", total_words(conversations))
    elif option == 4:
        print("Average words per message:", average_words(conversations))
    elif option == 5:
        print("Longest message:", get_longest_message(conversations))
    elif option == 6:
        print("Most active participant:", top_sender(conversations))
    elif option == 7:
        print("Message count:", message_count(conversations))
    elif option == 8:
        print("Most frequent word:", most_used_word(conversations))
    elif option == 9:
        print(first_and_last(conversations))
    elif option == 10:
        print(check_participant(conversations))
    elif option == 11:
        print("Repeated words:", repeated_words(conversations))
    elif option == 12:
        print(longest_avg_msg(conversations))
    elif option == 13:
        print("Mentions:", mention_count(conversations))
    elif option == 14:
        print("Duplicates removed.")
        print(clean_duplicates(conversations))
    elif option == 15:
        print("Sorted messages:", alphabetical_msgs(conversations))
    elif option == 16:
        print("Questions found:", question_messages(conversations))
    elif option == 17:
        print(reply_ratio(conversations))
    elif option == 18:
        print("Deleted messages count:", check_deleted(conversations))
    else:
        print("Invalid choice")
