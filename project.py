'''The start time in hr:Min:Sc   and duration in hr:Min:sc  of  a particular event is given, Write class Time that includes necessary data members. Use add time() that adds the corresponidng units of time. Create two objects that represent two different events. 
Ex: start time : 2:45:07   and duration is  1:20:60  than total time is   4:06:07
'''
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_time(self, duration):
        # Adding seconds and handling overflow
        total_seconds = self.seconds + duration.seconds
        carry_minutes = total_seconds // 60  # Calculate carry for minutes Using. Instead of round ensures we correctly get the integer carry-over value.
        self.seconds = total_seconds % 60

        # Adding minutes and handling overflow
        total_minutes = self.minutes + duration.minutes + carry_minutes
        carry_hours = total_minutes // 60  # Calculate carry for hours
        self.minutes = total_minutes % 60

        # Adding hours
        self.hours += duration.hours + carry_hours

    def display(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Creating two Time objects for start time and duration
start_time = Time(2, 45, 7)
duration = Time(1, 20, 60)

# Adding the duration to the start time
start_time.add_time(duration)

# Displaying the total time
print("Total time:", start_time.display())