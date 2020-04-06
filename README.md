# Todoist One-per-Day

This project is a simple Python 3 script that updates your Todoist tasks so that
one of your tasks labelled as @one-per-day gets randomly scheduled to "today"
and the rest get unscheduled. This might be helpful if you have a lot of
low-priority tasks that you want to get done at some point but don't want to
forget about. Simply label those tasks as @one-per-day and then run this script
every morning to have a random @one-per-day task show up as due today.


## Usage

```
pipenv install
pipenv run python3 oneperday.py
```


## Configuration

To run this script you'll need your Todoist API token. You'll find this in
Settings > Integrations > API Token. Put the value in the "API Token" field into
a `config.ini` file that looks like this:

```
[Todoist]
token = 1234567890abcdef1234567890abcdef12345678
```


<!-- vim: set textwidth=80: -->
