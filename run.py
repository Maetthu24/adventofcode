#!/usr/bin/env python3
import datetime
import json
import shutil
import sys
import traceback
import os
import importlib

if __name__ == "__main__":
    run_everything = False
    if len(sys.argv) >= 2:
        try:
            if sys.argv[1] == "all":
                run_everything = True
                day_number = 1
            else:
                day_number = int(sys.argv[1])
        except Exception:
            print(
                "{} - Runs a given AoC day (or the current day if no arguments are given)".format(sys.argv[0]))
            print("Usage: {} [day]".format(sys.argv[0]))
            sys.exit(1)
    else:
        day_number = datetime.date.today().day

    if day_number <= 0 or day_number > 25:
        print("Day given is out of range 1-25.")
        sys.exit(2)

    if os.path.isfile("common/settings.json"):
        with open("common/settings.json", 'r') as s:
            settings = json.loads("".join(s.readlines()))
    else:
        shutil.copy("common/settings.json.default", "common/settings.json")
        print("Please fill in settings.json first!")
        sys.exit(3)

    session_token = settings['session_token']
    year = settings['year']

    days_to_run = [day_number]
    if run_everything:
        days_to_run = [x+1 for x in range(25)]

    year_dir = f"days/y{year}"

    # Create directory for new year if it does not exist yet
    if not os.path.isdir(year_dir):
        os.mkdir(year_dir)

    init_filename = os.path.join(year_dir, "__init__.py")

    if not os.path.isfile(init_filename):
        template_init = "common/_day_init.py"
        shutil.copy(template_init, init_filename)
    
    # Dynamically try to load the requested day
    exec(f"from days.y{year} import *")
    from common.aocdays import AOCDays
    days: AOCDays = AOCDays.get_instance()

    for d in days_to_run:
        day = days.get_day(d)

        if day:
            for someones_day in day:
                print("Attempting to run AoC day {} from {}...".format(
                    d, someones_day.creator))
                # noinspection PyBroadException
                try:
                    instance = someones_day(year, d, session_token)
                    instance.run()
                except ConnectionError as e:
                    print(e, file=sys.stderr)
                except Exception as e:
                    traceback.print_exc()
        else:
            if d == datetime.date.today().day or (len(sys.argv) >= 3 and sys.argv[2] == "create"):
                # This is today, create it!
                template_filename = "common/_day_template.py"
                newday_filename = f"{year_dir}/day{d}.py"
                shutil.copy(template_filename, newday_filename)
                with open(newday_filename, 'r') as f:
                    lines = f.readlines()
                lines = [x.replace("@day(0)", "@day({})".format(d))
                         for x in lines]
                lines = [x.replace("class DayTemplate(AOCDay):",
                                   "class Day{}(AOCDay):".format(d)) for x in lines]
                with open(newday_filename, 'w') as f:
                    f.writelines(lines)

                print("Files for day {} created! Happy coding and good luck!".format(d))
            else:
                print("Attempting to run AoC day {}...".format(d))
                print("I have nothing to run for day {}".format(d))
