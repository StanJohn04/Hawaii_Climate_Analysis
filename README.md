# Background
The goal of this challenge is to use Python and SQLAlchemy to perform a climate analysis on Honolulu Hawaii to help with planning a trip to the area. This challenge is broken down into two sections, Analyze/Explore CLimate data and Design a climate app using the Flask python library.

# Part 1: Analyze and Explore Climate Data
  ## Precipitation Analysis
    * Find the most recent date in dataset
    * query precipitation data from the most recent 12 months
    * plot the results
    * print summary statistics
    
![image](https://user-images.githubusercontent.com/121142680/235525788-14a656d1-5032-4be8-861e-6c3b08748659.png)

  ## Exploratory Station Analysis
    * query the total number of stations in the dataset
    * query the most active station
    * query the lowest, hightest, and average temperature for the most active station
    * query the most recent 12 months of temperature data for the most active station
    * create a histogram of the temperature data
    
 ![image](https://user-images.githubusercontent.com/121142680/235526293-61537811-5152-4e6b-b904-3646ff772d8d.png)



# Part 2: Design the CLimate App
  ## Homepage (index route)
    * Start at home
    * List all available routes
 ![image](https://user-images.githubusercontent.com/121142680/235526633-b5ab233f-35ca-4974-88a2-06c4fbb80366.png)

  ## Precipitation
    * Last 12 months of precipitation data
    * returns results to screen
 ![image](https://user-images.githubusercontent.com/121142680/235526915-279d610f-720a-41e8-a238-871deba5b488.png)

  ## Stations
    * return list a station data
![image](https://user-images.githubusercontent.com/121142680/235527084-cc5c44f2-95a2-41ed-93f6-b77e7fcb07b9.png)

  ## Temperature
    * Returns Dates and temperature data from most-active station for previous 12 months
![image](https://user-images.githubusercontent.com/121142680/235527344-c4d54968-2c88-469e-bc54-3e8ad935a02b.png)


  ## Dynamic Routes
    * Two routes that acept either a start date or a start date AND end date and returns
      * reutrns min temp, max temp, and average temp for date range entered
![image](https://user-images.githubusercontent.com/121142680/235527723-70e78f02-ed72-4157-b10f-b1a2704f64a6.png)
