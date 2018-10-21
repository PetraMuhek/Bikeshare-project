## TODO: import all necessary packages and functions
import csv
import time
import datetime as dt

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

# Global variables
month = 0
day = 0

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function
    if city.lower() == 'chicago':
        city = chicago
    elif city.lower() == 'new york':
        city = new_york_city
    elif city.lower() == 'washington':
        city = washington
    else:
        print('Data for that city is not available. Please choose data for Chicago, New York or Washington')
        return get_city
    return city

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) Filter for time_period
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    if time_period.lower() == 'month':
        time_period = 'month'
    elif time_period.lower() == 'day':
        time_period = 'day'
    elif time_period.lower() == 'none':
        time_period = 'none'
    else:
        print('Please type one of the following: month, day, none.')
        return get_time_period()
    return str(time_period)

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (str) Month specified by user
    '''
    global month
    choose_months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    # TODO: handle raw input and complete function
    if month.lower() in choose_months.keys():
        month = choose_months[month.lower()]
    else:
        get_month()
    return month

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        Month.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        (int) Day specified by user
    '''
    global day
    days = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 0}
    
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function
    for day in days.keys():
        return day

def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    Finds the most popular month for start time.
    Args:
        city_file, time_period
    Returns:
        (str) Name of the most popular month
    '''
    # TODO: complete function
    rides_per_month = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0}
    
    for row in city_file:
        if dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == 1:
            rides_per_month['January'] += 1
        elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == 2:
            rides_per_month['February'] += 1
        elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == 3:
            rides_per_month['March'] += 1
        elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == 4:
            rides_per_month['April'] += 1
        elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == 5:
            rides_per_month['May'] += 1
        elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == 6:
            rides_per_month['June'] += 1
        else:
            print('Error, please try again')
    
    print('The most popular month for start time is: ' + str(max(rides_per_month, key=rides_per_month.get)))

def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    Finds the most popular day of week for start time.
    Args:
        city_file, time_period
    Returns:
        (str) Most popular day of week for start time
    '''
    # TODO: complete function
    rides_per_day = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    
    if time_period == 'none':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 1:
                rides_per_day['Monday'] += 1
            elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 2:
                rides_per_day['Tuesday'] += 1
            elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 3:
                rides_per_day['Wednesday'] += 1
            elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 4:
                rides_per_day['Thursday'] += 1
            elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 5:
                rides_per_day['Friday'] += 1
            elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 6:
                rides_per_day['Saturday'] += 1
            elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 0:
                rides_per_day['Sunday'] += 1
            else:
                print('Error, please try again')
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').month == month:
                if dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 1:
                    rides_per_day['Monday'] += 1
                elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 2:
                    rides_per_day['Tuesday'] += 1
                elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 3:
                    rides_per_day['Wednesday'] += 1
                elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 4:
                    rides_per_day['Thursday'] += 1
                elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 5:
                    rides_per_day['Friday'] += 1
                elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 6:
                    rides_per_day['Saturday'] += 1
                elif dt.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S').weekday() == 0:
                    rides_per_day['Sunday'] += 1
                else:
                    print('Error, please try again')
    
    print('The most popular day for start time is: ' + str(max(rides_per_day, key=rides_per_day.get)))

def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    Finds the most popular hour of the day for start time.
    Args:
        city_file, time_period
    Returns:
        (str) Most popular hour for start time
    '''
    # TODO: complete function
    pop_hours = dict()
    if time_period == 'none':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour not in pop_hours:
                pop_hours[dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] = 1
            else:
                pop_hours[dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour not in pop_hours:
                    pop_hours[dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] = 1
                else:
                    pop_hours[dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday():
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour not in pop_hours:
                    pop_hours[dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] = 1
                else:
                    pop_hours[dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").hour] += 1
    
    print('The most popular hour for start time is: ' + str(max(pop_hours, key=pop_hours.get)))

def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    Finds total and average trip duration (total trip divided by numbers of trips)
    Args:
        city_file, time_period
    Returns:
        (str) Total and average trip duration in seconds.
    '''
    # TODO: complete function
    total_trip_duration = 0
    number_of_trips = 0
    
    if time_period == 'none':
        for row in city_file:
            total_trip_duration += float(row['Trip Duration'])
            number_of_trips += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                total_trip_duration += float(row['Trip Duration'])
                number_of_trips += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday():
                total_trip_duration += float(row['Trip Duration'])
                number_of_trips += 1
    else:
        print('Error, please try again')
    
    print('The total trip duration is: ' + str(total_trip_duration) + ' seconds')
    print('The average trip duration is: ' + str(total_trip_duration / number_of_trips) + ' seconds')

def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    Finds the most popular start station and most poopular end station.
    Args:
        city_file, time_period
    Returns:
        (str) Name of the most popular stations
    '''
    # TODO: complete function
    pop_start = dict()
    pop_end = dict()

    if time_period == 'none':
        for row in city_file:
            if row['Start Station'] not in pop_start:
                pop_start[row['Start Station']] = 1
            else:
                pop_start[row['Start Station']] += 1
            if row['End Station'] not in pop_end:
                pop_end[row['End Station']] = 1
            else:
                pop_end[row['End Station']] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if row['Start Station'] not in pop_start:
                    pop_start[row['Start Station']] = 1
                else:
                    pop_start[row['Start Station']] += 1
                if row['End Station'] not in pop_end:
                    pop_end[row['End Station']] = 1
                else:
                    pop_end[row['End Station']] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday():
                if row['Start Station'] not in pop_start:
                    pop_start[row['Start Station']] = 1
                else:
                    pop_start[row['Start Station']] += 1
                if row['End Station'] not in pop_end:
                    pop_end[row['End Station']] = 1
                else:
                    pop_end[row['End Station']] += 1
    
    print('The most popular start station is: ' + str(max(pop_start, key=pop_start.get)))
    print('The most popular end station is: ' + str(max(pop_end, key=pop_end.get)))

def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    Finds the most popular trip (pair of start and end station).
    Args:
        city_file, time_period
    Returns:
        (str) Name of the most popular trip.
    '''
    # TODO: complete function
    pop_trips = dict()
    if time_period == 'none':
        for row in city_file:
            trip = str(row['Start Station']) + \
            ' to: ' + str(row['End Station'])
            if trip not in pop_trips:
                pop_trips[trip] = 1
            else:
                pop_trips[trip] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                trip = str(row['Start Station']) + \
                    ' to: ' + str(row['End Station'])
                if trip not in pop_trips:
                    pop_trips[trip] = 1
                else:
                    pop_trips[trip] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday():
                trip = str(row['Start Station']) + \
                    ' to: ' + str(row['End Station'])
                if trip not in pop_trips:
                    pop_trips[trip] = 1
                else:
                    pop_trips[trip] += 1
    print('The most popular trip is: ' + str(max(pop_trips, key=pop_trips.get)))

def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    Finds the number of each user.
    Args:
        city_file, time_period
    Returns:
        (str) Count of each user
    '''
    # TODO: complete function
    user_type = dict()
    if time_period == 'none':
        for row in city_file:
            if row['User Type'] not in user_type:
                user_type[row['User Type']] = 1
            else:
                user_type[row['User Type']] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if row['User Type'] not in user_type:
                    user_type[row['User Type']] = 1
                else:
                    user_type[row['User Type']] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday():
                if row['User Type'] not in user_type:
                    user_type[row['User Type']] = 1
                else:
                    user_type[row['User Type']] += 1
    for k, v in user_type.items():
        print(str(k) + ': ' + str(v))

def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    Finds the number of each gender.
    Args:
        city_file, time_period
    Returns:
        (str) Count of each gender
    '''
    # TODO: complete function
    genders = dict()
    if time_period == 'none':
        for row in city_file:
            if row['Gender'] not in genders:
                genders[row['Gender']] = 1
            else:
                genders[row['Gender']] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if row['Gender'] not in genders:
                    genders[row['Gender']] = 1
                else:
                    genders[row['Gender']] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday():
                if row['Gender'] not in genders:
                    genders[row['Gender']] = 1
                else:
                    genders[row['Gender']] += 1
    for k, v in genders.items():
        if k == '':
            print(' N/A: ' + str(v))
        else:
            print(str(k) + ': ' + str(v))

def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Finds the oldest users, the youngest users, and the most popular birth years.
    Args:
        city_file, time_period
    Returns:
        (Int) Years (oldest, youngest, most popular)
    '''
    # TODO: complete function
    birth_years = dict()
    
    if time_period == 'none':
        for row in city_file:
            if row['Birth Year'] == '':
                pass
            else:
                birth_y = row['Birth Year'].replace('.0', "")
                if int(birth_y) not in birth_years:
                    birth_years[int(birth_y)] = 1
                else:
                    birth_years[int(birth_y)] += 1
    elif time_period == 'month':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                if row['Birth Year'] == '':
                    pass
                else:
                    birth_y = row['Birth Year'].replace('.0', "")
                    if int(birth_y) not in birth_years:
                        birth_years[int(birth_y)] = 1
                    else:
                        birth_years[int(birth_y)] += 1
    elif time_period == 'day':
        for row in city_file:
            if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday():
                if row['Birth Year'] == '':
                    pass
                else:
                    birth_y = row['Birth Year'].replace('.0', "")
                    if int(birth_y) not in birth_years:
                        birth_years[int(birth_y)] = 1
                    else:
                        birth_years[int(birth_y)] += 1

    print('Birth year of the oldest user is: ' + str(sorted(birth_years)[0]))
    print('Birth year of the youngest user is: ' + str(sorted(birth_years)[-1]))
    print('The most popular birth year is: ' + str(max(birth_years, key=birth_years.get)))

def display_data(city_file, time_period):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        city_file, time_period.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        Five lines of data
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    
    if display == 'yes':
        city_file_filtered = list()
        if time_period == 'none':
            city_file_filtered = city_file
        elif time_period == 'month':
            for row in city_file:
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").month == month:
                    city_file_filtered.append(row)
        elif time_period == 'day':
            for row in city_file:
                if dt.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S").weekday():
                    city_file_filtered.append(row)
       
        start = 0
        end = 5
        while display == 'yes':
            for x in range(start, end):
                print(city_file_filtered[x])
                start += 5
                end += 5
            display = input('\nMore? (yes or no)\n')
    elif display == 'no':
        pass
    else:
        print('Sorry, please try again.\n')
        display_data(city_file, time_period)
            
def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    global month
    month = 0
    global day
    day = 0
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    
    with open(city) as csv_file:
        city_file = [{k: v for k, v in row.items()}
                     for row in csv.DictReader(csv_file, skipinitialspace=True)]
        
    # Filter by time period (month, day, none)
    time_period = get_time_period()

    if time_period == 'month':
        month = get_month()
    elif time_period == 'day':
        get_day()
    else:
        time_period = 'none'

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        popular_month(city_file, time_period)
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        popular_day(city_file, time_period)
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city_file, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    
    if city == chicago or city == new_york_city:
        print("Calculating the next statistic...")
        start_time = time.time()
        gender(city_file, time_period)
        print("That took %s seconds." % (time.time() - start_time))
    # TODO: call gender function and print the results
    
        print("Calculating the next statistic...")
        start_time = time.time()
        birth_years(city_file, time_period)
        print("That took %s seconds." % (time.time() - start_time))

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file, time_period)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    statistics()