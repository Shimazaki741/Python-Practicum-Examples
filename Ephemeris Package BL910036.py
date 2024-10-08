import serial
import ephem
import datetime
import math
import time as t

def get_sun_alt_az(lat, lon, date_time):
    # Observer
    obs = ephem.Observer()
    obs.lat = str(lat)
    obs.lon = str(lon)
    obs.date = date_time

    # Sun
    sun = ephem.Sun(obs)
    sun.compute(obs)

    sun_az = round(math.degrees(sun.az), 3)
    sun_alt = round(math.degrees(sun.alt), 3)

    sun_az = (sun_az + 360) % 360

    return sun_alt, sun_az

def get_moon_alt_az(lat, lon, date_time):
    # Observer
    obs = ephem.Observer()
    obs.lat = str(lat)
    obs.lon = str(lon)
    obs.date = date_time

    # Moon
    moon = ephem.Moon(obs)
    moon.compute(obs)

    moon_alt = round(math.degrees(moon.alt), 2)
    moon_az = round(math.degrees(moon.az), 2)

    moon_az = (moon_az + 360) % 360

    return moon_alt, moon_az

# START

import collections
import numpy as np
import matplotlib.pyplot as plt

text = """
<your text>
"""

# Cleaning
words = text.split()
first_letters = [word[0].lower() for word in words if word[0].isalpha()]
letter_counts = collections.Counter(first_letters)

fll_expected = list("taswoihbmcfpdlnerguyvkjqzx")

sorted = {letter: letter_counts[letter] for letter in fll_expected if letter in letter_counts}

# BREAK

def main():
    
    ser = serial.Serial('COM6', 9600)
    
    print()

    for x in text:
            print(x, end='', flush=True)
    if x == ' ':
                t.sleep(0.0001)  
    else:
                t.sleep(0.095)
                
    print()
    print()  
    
    lat = float(input("Current latitude reading in degrees: "))
    lon = float(input("Current longitude reading in degrees: "))
    
    print()
    print()
    print()
    print()
    print()


    current_time = datetime.datetime.utcnow()

    sun_alt, sun_az = get_sun_alt_az(lat, lon, current_time)
    moon_alt, moon_az = get_moon_alt_az(lat, lon, current_time)
    mercury_alt, mercury_az = get_mercury_alt_az(lat, lon, current_time)
    venus_alt, venus_az = get_venus_alt_az(lat, lon, current_time)
    mars_alt, mars_az = get_mars_alt_az(lat, lon, current_time)
    jupiter_alt, jupiter_az = get_jupiter_alt_az(lat, lon, current_time)
    saturn_alt, saturn_az = get_saturn_alt_az(lat, lon, current_time)
    uranus_alt, uranus_az = get_uranus_alt_az(lat, lon, current_time)
    neptune_alt, neptune_az = get_neptune_alt_az(lat, lon, current_time)
    orion_alt, orion_az = get_orion_alt_az(lat, lon, current_time)
    
    print('CELESTIAL OBJECTS COORDINATES (CATALOGUE):')

    print("Sun's altitude:", sun_alt, "degrees")
    print("Sun's azimuth:", ("%.2f" % round(sun_az, 2)), "degrees")
    if sun_alt < 0:
        print('Not Visible')
    else:
        print('Visible')
    
    print()
    print("Moon's altitude:", moon_alt, "degrees")
    print("Moon's azimuth:", ("%.2f" % round(moon_az, 2)), "degrees")
    if moon_alt < 0:
        print('Not Visible')
    elif sun_alt < 90 and sun_alt >= 0:
        print('Faint')
    else:
        print('Visible')

# START

# Benford's Law Check
dataset = [<your numbers>]

fd_set = []

def first_digit(n):
    return int(str(n)[:1])
for d in dataset:
    fd_set.append(first_digit(d))

order = list('123456789')

digit_counts = collections.Counter(fd_set)

counts = [digit_counts[int(digit)] for digit in order]

plt.bar(order, counts)
plt.xlabel('Digit')
plt.ylabel('Count')
plt.title("Benford's Law")
plt.show()

plt.bar(list(sorted.keys()), list(sorted.values()))
plt.xlabel('Letter')
plt.ylabel('Count')
plt.title('First Letter Law')
plt.show()

# END

    count = 0
    while (count < print_count):
        count = count + 1

        fixed_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        current_time = datetime.datetime.utcnow()
        observer.date = current_time

        altitude, azimuth = get_alt_az(selected_planet, observer)
        print("Time:", fixed_time, "- Altitude:", altitude, "degrees, Azimuth:", azimuth, "degrees")
        coordinates = f"{altitude} , {azimuth}"
        coordinates_bytes = coordinates.encode()
        ser.write(coordinates_bytes + b'\n')
        
        t.sleep(interval_seconds)
        
    end_msg = "Tracking Ended."
    coordinates_bytes = end_msg.encode()
    ser.write(coordinates_bytes + b'\n')

    # Print end time
    print("End Time:", datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    
if __name__ == "__main__":
    main()
