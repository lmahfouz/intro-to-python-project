import csv

print("Welcome to your weekly planner!")


def weekly_planner():
    with open("planner.csv", "w") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        x = 1
        day = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        while x < 8:
            day_of_week = day[x - 1]
            activity = input(
                "This is the entry for " + day[x - 1] + ". What are your plans?"
            )
            time = input("What time will you be doing this? ")
            notes = input("Are there any extra notes you need for your plans? (y/n) ")
            if notes == "y":
                notes1 = input("Cool! Please note the things you need to remember: ")
            elif notes == "n":
                print("No worries.")
                notes1 = "Nothing to note."
            else:
                print("I'll take that as a no.")
                notes1 = "Nothing to note."

            w.writerow([day_of_week, activity, time, notes1])
            x += 1


weekly_planner()

print("Looks like you have a busy week ahead! Good thing you've got your planner.")
