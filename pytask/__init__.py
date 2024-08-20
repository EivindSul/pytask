from icalendar import Calendar
from taskw_ng import TaskWarrior
from pathlib import Path


"""
Expected output:
    task add INF264 - Kræsjkurs i Python frivillig - Aktivt rom 2+3
    task add DAT351 - Forelesning - B313

I want the tasks to only include location, topic, and time.
It should also have a tag, like ics, so that they can all be removed on
each update to prevent duplicates.
"""

print("\n------------ HVL -------------\n")

ics_path = Path("ics/hvl-canvas.ics")

with ics_path.open() as f:
    calendar = Calendar.from_ical(f.read())

for event in calendar.walk('VEVENT'):
    print("DTSTART:", event.get("DTSTART"))
    print("DTEND:", event.get("DTEND"))
    # print("UID:", event.get("UID"))
    print("DTSTAMP:", event.get("DTSTAMP"))
    # print("LAST-MODIFIED:", event.get("LAST-MODIFIED"))
    print("SUMMARY:", event.get("SUMMARY"))
    print("LOCATION:", event.get("LOCATION"))
    # print("DESCRIPTION:", event.get("DESCRIPTION"))
    break

print("\n------------ UiB -------------\n")


ics_path = Path("ics/mittuib.ics")

with ics_path.open() as f:
    calendar = Calendar.from_ical(f.read())

for event in calendar.walk('VEVENT'):
    # print('UID:', event.get('UID'))
    print('DTSTART:', event.get('DTSTART'))
    print('DTEND:', event.get('DTEND'))
    print('DTSTAMP:', event.get('DTSTAMP'))
    # print('CLASS:', event.get('CLASS'))
    # print('LOCATION:', event.get('LOCATION'))
    # print('SEQUENCE:', event.get('SEQUENCE'))
    print('SUMMARY:', event.get('SUMMARY'))
    # print('URL:', event.get('URL'))
    # print('DESCRIPTION:', event.get('DESCRIPTION'))
    # print('X-ALT-DESC:', event.get('X-ALT-DESC'))
    break

# TODO: 
# Extract position from description or x-alt-desc in UiB entries.
# This can maybe be hard-coded.

