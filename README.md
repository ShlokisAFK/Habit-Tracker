# Habit Tracker CLI

A command-line habit tracking tool built in Python.

## Features
- Log daily habits from the terminal
- Tracks how many times each habit has been completed
- Maintains streak counters with automatic reset on missed days
- Prevents duplicate logging on the same day
- Persistent storage via local JSON file

## Usage
```bash
python tracker.py add <habit>   # log a habit
python tracker.py show          # view all habits
```

## Example
```bash
$ python tracker.py add workout
Logged: workout | count: 3 | streak: 5 days

$ python tracker.py show
workout: 3 times | last done: 2026-03-01 | streak: 5 days
```

## Built With
- Python 3
- JSON for storage
- datetime module for streak calculation
