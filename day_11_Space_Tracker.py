import requests 

def get_space_data():
print("Connecting to the ISS API...") 

### 1. Fetching the current location of the International Space Station

iss_url = "http://api.open-notify.org/iss-now.json" 

### 2. Fetching the list of astronauts currently in space

people_url = "http://api.open-notify.org/astros.json" 

try: 

### Get ISS Location

iss_response = requests.get(iss_url, timeout=10)
iss_response.raise_for_status() # Raises an error if the website is down
iss_data = iss_response.json() 

### Extract specific data from the JSON dictionary

position = iss_data["iss_position"]
latitude = position["latitude"]
longitude = position["longitude"] 

### Get Astronaut Names

people_response = requests.get(people_url, timeout=10)
people_response.raise_for_status()
people_data = people_response.json() 

### Print the final results cleanly

print("\n=== SUCCESS: LIVE DATA FETCHED ===")
print(f"ISS Current Location: Latitude {latitude}, Longitude {longitude}")
print(f"Total People in Space Right Now: {people_data['number']}")
print("Astronaut Names:") 

# Using a Day 3 For Loop to loop through the list of astronauts

for person in people_data["people"]:
print(f" - {person['name']} (onboard the {person['craft']})")

except requests.exceptions.ConnectionError:
print("\n❌ Error: Could not connect to the internet. Please check your connection.")
except requests.exceptions.Timeout:
print("\n❌ Error: The server took too long to respond. Try again later.")
except Exception as e:
print(f"\n❌ An unexpected error occurred: {e}") 

### Run the function

if **name** == "**main**":
get_space_data()