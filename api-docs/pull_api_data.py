# Note: Some of these imports require you install them using pip.
import requests
import json

def save(data):
    """Save data in json file locally."""
    print(0)

def get_request(url):
    """Connects to API and pulls the relevant data, without parsing."""
    return 0  # change this to relevant method body

def parse_data(data):
    """Parses json data for ready use in a pandas dataframe."""
    save(data) # change this to relevant method body

def main():
    data = get_request("www.example.com/api")
    parse_data(data)

if __name__ == "__main__":
    main()