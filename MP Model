import math
import matplotlib.pyplot as plt

# Bounds
a = 0
b = 1

def mp_rule(n):
  dx = (b - a) / n
  sum = 0
  for i in range (n):
    x_0 = a + (dx * i)
    x_n = a + (dx * (i+1))
    x = (x_0 * x_n) ** 0.5

# Break
            print("\t\t|Directions|Altitude|")
            print(f"\t\t|   {hours}:{minutes}   | {altitude} |")
            starting_time=datetime.datetime.now()
            starting_time=starting_time.strftime("%H:%M:%S")
            for i in range(y):
                t.sleep(interval)
                observer.date = ephem.now()
                body.compute(observer)
                azimuth2 = math.degrees(body.az)
                altitude2 = round(math.degrees(body.alt),3)
                #altitude2=round(altitude2)
                #azimuth2=round(azimuth2)
                #clock_system
                azimuth2=azimuth2/30
                hours2=int(azimuth2)
                minutes2=round((azimuth2-hours2)*60)
                if azimuth2==azimuth:
                    #az2 changes #minutes 2 changes
                    continue
                else:
                    print(f"\t\t|   {hours2}:{minutes2}   | {altitude2} |")
                    azimuth=azimuth2
                    altitude=altitude2
                    hours=hours2
                    minutes=minutes2
            ending_time=datetime.datetime.now()
            ending_time=ending_time.strftime("%H:%M:%S")
            print(f'''Starting time= {starting_time}
                ending_time={ending_time}"
                Total Time Tracked={ending_time-starting_time}''')  
            print("Exited")
        elif x=="3":
            sunset()
        elif x=="4":
            sunrise()
        elif x=="5":
            chart()
        elif x=="7":
            print("Exited")
            exit()
        elif x=="6":
            calculate_twilight()
        elif x=='0':
            guided()
        else:
            print("Value Error")
except Exception as e:
    print("Please replace 'your_longitude' with your actual longitudes and 'your_latitude' with your actual latitude")
# Continue
    # Function
    fn = math.exp(x ** 2)
    sum += fn
  final = dx * sum
  return final

values = range(4, 13)
results = [mp_rule(n) for n in values]

plt.plot(values, results)
plt.xlabel("n")
plt.ylabel("Values")
plt.title("Midpoint Rule Approximation")
plt.show()
