
import csv, datetime, os

FILE = "mood_log.csv"

def mood_to_emoji(m):
    return {"happy":"😊","sad":"😢","neutral":"😐","angry":"😠","excited":"🤩"}.get(m,"")

def add_mood():
    mood = input("Mood today? (happy/sad/neutral/angry/excited): ").lower()
    with open(FILE, 'a', newline='') as f:
        csv.writer(f).writerow([datetime.date.today(), mood])
    print("Mood saved! 😊")

def view_history():
    if not os.path.exists(FILE): return print("No mood data found.")
    print("\n=== Mood History ===")
    for d, m in csv.reader(open(FILE)):
        print(f"{d} - {m.capitalize()} {mood_to_emoji(m)}")

def summary():
    if not os.path.exists(FILE): return print("No mood data to summarize.")
    moods = [m for _, m in csv.reader(open(FILE))]
    print("\n=== Mood Summary ===")
    for m in set(moods):
        print(f"{m.capitalize()}: {moods.count(m)} days {mood_to_emoji(m)}")

while True:
    print("\n==== Daily Mood Tracker ====\n1. Add Mood\n2. View History\n3. Summary\n4. Exit")
    c = input("Choice (1-4): ")
    if c == '1': add_mood()
    elif c == '2': view_history()
    elif c == '3': summary()
    elif c == '4': print("Goodbye! 🌈"); break
    else: print("Invalid choice.")

