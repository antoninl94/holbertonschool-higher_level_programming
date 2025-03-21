#!/usr/bin/python3
"""
This task is about creating a Python function that
generates personalized invitation files from a template
with placeholders and a list of objects.
"""
from os.path import exists


def generate_invitations(template, attendees):
    """Generate personalized invitations"""

    # checking input types and emptiness
    if not isinstance(template, str):
        raise Exception("template must be a string")
    if not isinstance(attendees, list):
        raise Exception("attendees must be a list")
    if not template:
        raise Exception("Template is empty, no output files generated.")

    # checking type of attendees content
    for attendee in attendees:
        if not isinstance(attendee, dict):
            raise Exception

    # create file for each attendee
    x = 0
    for attendee in attendees:
        # verifying the placeholder existance
        if attendee["name"]:
            name = attendee["name"]
        else:
            name = "N/A"
        if attendee["event_title"]:
            event_title = attendee["event_title"]
        else:
            event_title = "N/A"
        if attendee["event_date"]:
            event_date = attendee["event_date"]
        else:
            event_date = "N/A"
        if attendee["event_location"]:
            event_location = attendee["event_location"]
        else:
            event_location = "N/A"

        # replace placeholder
        new_template = template.replace("{name}", name)\
            .replace("{event_title}", event_title)\
            .replace("{event_date}", event_date)\
            .replace("{event_location}", event_location)

        # create the file
        x += 1
        output = f"output_{x}.txt"
        if not exists(output):
            with open(output, "w") as file:
                file.write(new_template)
        else:
            raise FileExistsError
