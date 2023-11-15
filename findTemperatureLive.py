import requests

def findTemperatureLive():  
    """Print the current temperature in Wenham using data from localconditions.com.
  
    This function depends on knowledge of the page structure - if they change
    the page structure, the program will not work!
    """

    # Get the weather page
    weather = requests.get("https://www.localconditions.com/weather-boston-massachusetts/01984/").text

    # The temperature can be found near the top of the page after the word "Wenham" and
    # immediately before the HTML code &deg; (the degree symbol)
    curLoc = weather.find("Wenham")
    if curLoc != -1:
        # Now, find the degree symbol ("&deg;") following the temperature
        degLoc = weather.find("&deg;", curLoc)
        # The temperature number is preceded by a pipe
        tempLoc = weather.rfind("|", 0, degLoc)
        # Temperature value is everything between the pipe (and space) and the degree symbol
        print("Current temperature in Wenham is",weather[tempLoc+2:degLoc], "degrees")
        return "Current temperature in Wenham is " + weather[tempLoc+2:degLoc] + " degrees"
    else:
        print("Page format has changed; cannot find the temperature")
    
if __name__ == "__main__":
    findTemperatureLive()
