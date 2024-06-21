print("Welcome to p1anez's ATIS Maker v1.0.0")

airportAtis = input("Enter the ICAO of your airport: ")
atisTag = input("Enter the tag of your ATIS: ")
controllerCallsign = input("Enter your position callsign: ")

maxTaxi = input("Default taxi speed is 30, would you like to change this? (yes/no) | ")

if maxTaxi == "yes":
    maxTaxi = input("What would you like it to be (in knots, number only) | ")
else:
    maxTaxi = "30"

if airportAtis in ["IRFD", "IPPH", "ITKO", "IZOL", "IIAB", "ILAR"]:
    maxACFT = "N/A"
elif airportAtis in ["IMLR", "IGRV", "IPAP"]:
    maxACFT = "B787/A350/MD11/AN22"
elif airportAtis == "ISCM":
    maxACFT = "B767/A350/MD11 (no B747)"
elif airportAtis == "ISAU":
    maxACFT = "A320/B737/MD90"
elif airportAtis in ["IBTH", "IJAF", "IGAR"]:
    maxACFT = "CRJ7/Q400/ATR72"
elif airportAtis == "ILKL":
    maxACFT = "LJ45/DHC6"
elif airportAtis in ["IDCS", "IBAR", "IHEN", "IBLT", "ISKP"]:
    maxACFT = "SF50/DHC6"
else:
    maxACFT = "C172"

depRwy = input("Enter your departure runway: ")
arrRwy = input("Enter your arrival runway: ")
pres = input("Enter pressure: ")

notams = []
print("Enter your NOTAMS, Press ENTER on an empty line to finish.")

while True:
    notam = input()
    if notam == "":
        break
    notams.append(notam)

chartAuth = input("Enter your chart pack author (leave empty if not using charts): ")
chartLink = input("Enter your chart pack link (leave empty if not using): ")

print("Here's your finished ATIS:")
print()
print(airportAtis, "ATIS Information", atisTag)
print("――――――――――――――――――――――")
print("**Controller Callsign:**", controllerCallsign)
print("――――――――――――――――――――――")
print("**Aerodrome:**")
print("Max Taxi Speed:", maxTaxi)
print("Max ACFT Size:", maxACFT)
print("Arrival Runway(s):", arrRwy)
print("Departure Runway(s):", depRwy)
print()
print("**NOTAMS:**")

for notam in notams:
    print(notam)

print()

print("**Charts:**")
print("Chart Pack Author:", chartAuth)
print("Chart Pack Link:", chartLink)
print("――――――――――――――――――――――")
print("**End of ATIS Information**", atisTag)
