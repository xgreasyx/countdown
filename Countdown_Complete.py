# import datetime imports the date functions
import datetime
import time

title = input("Enter Name of Countdown: ")  # ask title of the countdown project
d = datetime.date.today()  # set string todays date to d
print("Today is", d.strftime("%d.%b.%Y"))  # print todays date in the format day month year

# we set x to None then we have a while loop which runs as long as x is none.
# Inside that loop we either set x as a valid date (and so the loop exits)
# or we print a message telling the user what format is required. If it goes to that Except clause,
# x isn't set to anything so it remains None, so the loop will run again
# it just keeps asking the user for a date until they input one in the format we want
x = None

while x is None:
    try:
        c = input("What date do you want to countdown from? DD.MM.YYYY :")
        x = datetime.datetime.strptime(c, "%d.%m.%Y")
    except ValueError:
        print("Please use DD.MM.YYYY format: ")

now = datetime.datetime.now()
dy = x - now
print("There is", dy.days, "days left until", title.upper())
while True:
    n = datetime.datetime.now()
    diff = x - n
    # we need to get the amount of seconds difference so we need to create a total seconds variable
    cd = diff.seconds
    # divmod returns two values - how many times it divides, and what is the remainder.
    # We can set those two values to variables on the one line
    nh, nm = divmod(cd, 3600)
    # same thing, but here we give it the remainder from the above as the amount to be divided
    nm, ns = divmod(nm, 60)
    # we take the total seconds (cd) and divmod them by 3600 that returns two values -
    # how many hours in that amount of seconds, and the seconds left over. All that gives us is the hours.
    # It's like if did divmod $1 on $1.52. it would give us $1 and 52 cents remainder
    # but with time we need to divmod again, to see how many full minutes are in that amount of seconds
    # we do a bit of fancy stuff with the print statement to get it to keep printing on the same line
    print("\r",dy.days, "days", nh, "hours", nm, "minutes", ns, "seconds left", end="")
    time.sleep(1)
