# 4. Create two lists to store cities and locations by accepting values from user. Display 1st city and 1st location then 2nd city and 2nd location
cities = [i for i in input("Enter Cities: ").split(" ")]
locations = [i for i in input("Enter Locations: ").split(" ")]
for n1,n2 in zip(cities, locations):
  print(f"{n1} --> {n2}")