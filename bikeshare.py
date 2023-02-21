import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("enter city name: ").lower()
    while city not in ('chicago', 'washington', 'new york city'):
        print("this city data not available")
        city = input("enter city name: ").lower()
    filter = input("do you want to filter by month, day or all: ")
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input("enter month name: ").lower()

    while month not in ('january','february','march','april','may','june','all'):
        print("invalid data")
        month = input("enter month name: ").lower()
    
    day = input("enter the day: ").lower()
    while day not in ('saturday','sunday','monday','tuesday','wednesday','thursday','friday', 'all'):
        print("invalid data")
        day = input("enter the day: ").lower()
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
#load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])
#convert the start time to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
#extract day and month from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
# filter by month 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

 # filter by month to create the new dataframe
        df = df[df['month'] == month]

 # filter by day 
    if day != 'all':
       
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    
    print("the most common month: ", most_common_month)
    
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]

    print("the most common day of week: ", most_common_day)
    # TO DO: display the most com   
    df['hour'] = df['Start Time'].dt.hour
    
    most_hr = df['hour'].mode()[0] 
    print("most common hour is: ", most_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("most common start station is: ", common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("most common end station is: ", common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + df['End Station']
    most_common_trip = df['trip'].max()
    print("most common trip is: ", most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time: ", total_travel_time)
    
   

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time: ", mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print ('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    
    print(user_types_count)
    
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("counts of gender is: ", gender_count)
            
    except KeyError:
        print("There's no column called 'Gender']")
    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        most_common_year = df['Birth Year'].mode()[0]
        print("most common birth year is: ", most_common_year)
    except KeyError:
        print("There's no column called 'Birth Year']")
        
    try:
        youngest_users = df['Birth Year'].max()
        print("the youngest user birth year is: ", youngest_users)
    except:
        print("There's no column called 'Birth Year']")

    try:
        oldest_users = df['Birth Year'].min()
        print("the youngest user birth year is: ", oldest_users)
    except:
        print("There's no column called 'Birth Year']")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    L = 5 
    while "true":
        rawa_data = df.head(L)
        L += 5
        print(rawa_data)
        restart = input('\nWould you like to type more data? Enter yes or no.\n')
        if restart == 'no':
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        
        trip_duration_stats(df)
        
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
