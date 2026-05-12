import numpy as np
#1. Generating the dataset to use, a NumPy array with 3 columns
def generate_weather_data():
    
    np.random.seed(42)  
    
    days=np.arange(1,366) #column 1
    
    min_temps = np.random.randint(-10, 16, size=365) #column2
    
    max_temps = np.random.randint(5, 36, size=365) #column3
    
    weather_data = np.column_stack((days, min_temps, max_temps)) #Stacking the columns.                             
    return weather_data

#2. Function to calculate basic statistics from the dataset.
def basic_statistics(data):
    days = data[:,0]
    min_temps = data[:,1]
    max_temps= data [:,2] 
    #Calculating the average minimum and maximum temperatures,
    #as well as the highest and lowest temperatures along
    # with their corresponding days.
    avg_min = np.mean(min_temps)
    avg_max = np.mean(max_temps)

    max_idx = np.argmax(max_temps)
    highest_temp = max_temps[max_idx]
    highest_day = days[max_idx]

    min_idx = np.argmax(min_temps)
    lowest_temp = min_temps[min_idx]
    lowest_day = days[min_idx]
    
    return avg_min, avg_max,(highest_temp,highest_day), (lowest_temp, lowest_day)

#3. Function to calculate the daily temperature range and identify the day with the largest range.
def daily_temperature_range(data):
    ranges = data[:,2] - data[:,1]   #max-min 
    max_range_idx = np.argmax(ranges)
    days = data[:,0]

    max_idx = np.argmax(ranges)

     
    largest_range_value = ranges[max_range_idx]
    largest_range_day = days[max_range_idx]

    return ranges, (largest_range_day,largest_range_value)

#4. Function to identify heatwaves, defined as periods of at least 
# 3 consecutive days with maximum temperatures above 30 degrees Celsius.
def identify_heatwaves(data):
    # YOUR CODE HERE
    max_temps = data[:, 2]
    days = data [:, 0]

    hot = max_temps >30

    hot_padded = np.concatenate(([0], hot, [0]))
    diff = np.diff(hot_padded)
    
    start_indices = np.where(diff == 1)[0]
    end_indices = np.where(diff == -1)[0] -1
    
    heatwaves = []
    
    for start_idx, end_idx in zip(start_indices, end_indices):
        duration = end_idx - start_idx + 1
        if duration >= 3:
            start_day = days[start_idx]
            end_day = days[end_idx]
            heatwaves.append((int(start_day), int(end_day)))
            
    return len(heatwaves), heatwaves

                        