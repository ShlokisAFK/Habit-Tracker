import sys
import json
import os
from datetime import date

today = date.today()
FILE = "habits.json"

def load_habits():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_habits(habits):
    with open(FILE, "w") as f:
        json.dump(habits, f)

def main():
    habits = load_habits()

    if len(sys.argv) < 2:
        print("Commands: add <habit> | show")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error\nCommands: add <habit> | show")
            return

        habit = sys.argv[2]
        count = habits.get(habit, {}).get("count", 0) + 1
        stored = habits.get(habit, {})
        last_done = stored.get("last_done", None)
        streak = stored.get("streak", 0)

        if last_done:
            diff = (today - date.fromisoformat(last_done)).days
            if diff == 1:
                streak += 1
            elif diff == 0:
                print("Already logged today!")
                return
            else:
                streak = 1
        else:
            streak = 1

        habits[habit] = {"count": count, "last_done": str(today), "streak": streak}
        save_habits(habits)
        print(f"Logged: {habit} | count: {count} | streak: {streak} days")

    elif command == "show":
        if not habits:
            print("No habits tracked yet.")
        else:
            for habit, data in habits.items():
                print(f"{habit}: {data['count']} times | last done: {data['last_done']} | streak: {data['streak']} days")

main()