  def calculate_twilight():
        city = ephem.Observer()
        city.lon =121.13347
        city.lat =14.63747
        city.date = ephem.now()
        city.horizon="-18"
        sun=ephem.Sun()
        sun.compute(city)
        astro=ephem.localtime(city.next_setting(sun))
        astro=(astro.strftime("%H'o clock at %M Minutes"))
        city.horizon="-12"
        nautical=ephem.localtime(city.next_setting(sun))
        nautical=(nautical.strftime("%H'o clock at %M Minutes"))
        city.horizon="-6"
        civil=ephem.localtime(city.next_setting(sun))
        civil=(civil.strftime("%H'o clock at %M Minutes"))
        print(f'''Civil Twilight at {civil}
    Nautical Twilight at {nautical}
    Astronomical Twilight at {astro} ''')
    xz=0
    sam=0
    if sam==0:  
        introduction()   # COMMENTIZE ME TO SKIP INTRODUCTION
        sam+=1          
        t.sleep(2)
        print("# COMMENTIZE Introduction() in the code to SKIP introduction everytime")
        t.sleep(4)
    menu()
    while True:
        if xz==0:
            xz=1
        else:
            menu2()
        x=input("RESPONSE: ")
        if x=="1":

            observer = ephem.Observer()
            observer.lon =121.13347
            observer.lat =14.63747

            observer.date =ephem.now()

            x=input("Enter a Celestial Body name:")
            if x.title() == "Moon":
                body=ephem.Moon()
            elif x.title() == "Sun":
                body=ephem.Sun()
            elif x.title() == "Mercury":
                body=ephem.Mercury()
            elif x.title() == "Venus":
                body=ephem.Venus()
            elif x.title() == "Mars":
                body=ephem.Mars()
            elif x.title() == "Jupiter":   
                body=ephem.Jupiter()
            elif x.title() == "Saturn":
                body=ephem.Saturn()
            elif x.title() == "Uranus":
                body=ephem.Uranus()
            elif x.title() == "Neptune":
                body=ephem.Neptune()
            elif x.title() == "Pluto":
                body=ephem.Pluto()
            else:
                print("please enter a valid obbject")
                exit()
            #Calculation
            body.compute(observer)
            azimuth = math.degrees(body.az)
            altitude = math.degrees(body.alt)
            altitude=round(altitude)
            azimuth=round(azimuth)
            #clock_system
            azimuth=azimuth/30
            hours=int(azimuth)
            minutes=round((azimuth-hours)*60)
            print("Calculating.")
            t.sleep(1)
            print("Calculating..")
            t.sleep(1)
            print("Calculating...")
            t.sleep(1)
            print("Look at",hours,"o'clock and",minutes,"minutes",end=' ')
            print("At",altitude,"Degrees")
        elif x=="2":
            try:
                y=int(input("For how much time do you want to track the position? (In minutes):"))
                interval=float(input("Enter the interval inbetween the tracking reports(seconds):"))
            except ValueError:
                print("Please enter a valid number")
                exit()
            observer = ephem.Observer()
# START
import matplotlib.pyplot as plt

my_file = open("your_data.txt")
data = my_file.read()
numbers = data.replace('\n', ' ').replace(',','').split()
my_file.close()

prime = []
composite = []

for i in range (int(len(numbers))):
    num = int(numbers[i])
    if num == 0 or num == 1:
        composite.append(numbers[i])
    elif num>1:
        is_prime = True
        for m in range(2, num):
            if num % m == 0:
                composite.append(numbers[i])
                is_prime = False
                break
        if is_prime:
            prime.append(numbers[i])

print(prime)
print(composite)

plt.bar(['Primes', 'Composites'], [len(prime), len(composite)], alpha=0.5)
plt.title('Number of Primes vs. Composites')
plt.ylabel('Count')
plt.show()
# END
