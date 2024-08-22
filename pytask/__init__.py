from icalendar import Calendar
from taskw_ng import TaskWarrior
import re
import requests

hvl = requests.get("https://cloud.timeedit.net/hvl/web/studbergen/ri6795Q03k22u1QZQtQn39CQZQ8QY96dZ6328Z0y66809wtZ485ZF29A20ABB0EA8CBF6000A415E04F.ics")
hvl = hvl.text
uib = requests.get("https://mitt.uib.no/feeds/calendars/user_urR0om7uZCMG1dcgcIpFOg1hx926MEjktxJQTPwA.ics")
uib = uib.text

print("\n------------ UiB -------------\n")

calendar = Calendar.from_ical(uib)

for event in calendar.walk('VEVENT')[:5]:
    # print('UID:', event.get('UID'))
    print('DTSTART:', event.get('DTSTART'))
    print('DTEND:', event.get('DTEND'))
    print('DTSTAMP:', event.get('DTSTAMP'))
    # print('CLASS:', event.get('CLASS'))
    # print('LOCATION:', event.get('LOCATION'))

    # Retrieving Location from Description using string manipulation
    # location = event.get('DESCRIPTION')
    # start = location.find('[')
    # end = location.find(']', start)
    # location = location[start:end+1][1:-1]
    # print('LOCATION:', location)

    # Retrieving Location from Description using regular expression
    pattern = r'\[.*?\]'
    locations = re.findall(pattern, event.get('DESCRIPTION'))
    cleaned_locations = ""
    i = 1
    for location in locations:
        cleaned_locations += location[1:-1]
        if i == 2:
            break
        cleaned_locations += ", "
        i += 1
    print('LOCATION:', cleaned_locations)

    # print('SEQUENCE:', event.get('SEQUENCE'))
    print('SUMMARY:', event.get('SUMMARY'))
    # print('URL:', event.get('URL'))
    # print('DESCRIPTION:', event.get('DESCRIPTION'))
    # print('X-ALT-DESC:', event.get('X-ALT-DESC'))
    print("\n----------------------------\n")


calendar = Calendar.from_ical(hvl)

print("\n------------ HVL -------------\n")

for event in calendar.walk('VEVENT')[:5]:
    print("DTSTART:", event.get("DTSTART"))
    print("DTEND:", event.get("DTEND"))
    # print("UID:", event.get("UID"))
    print("DTSTAMP:", event.get("DTSTAMP"))
    # print("LAST-MODIFIED:", event.get("LAST-MODIFIED"))
    print("SUMMARY:", event.get("SUMMARY"))
    print("LOCATION:", event.get("LOCATION"))
    # print("DESCRIPTION:", event.get("DESCRIPTION"))

    print("\n----------------------------\n")

