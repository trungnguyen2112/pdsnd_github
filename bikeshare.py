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
    city = ""
    while True:
        cityInput = input("Enter a city name : ").strip().lower()
        if cityInput in ['chicago', 'new york city', 'washington']:
            city = cityInput
            break
        else:
            print("Invalid input. Please enter one of the provided city names.")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while True:
        monthInput = input("Enter a month: ").strip().lower()
        if monthInput in ["all","january","february","march","april","may","june"]:
            month = monthInput
            break
        else:
            print("Enter month invalid!")
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while True:
        dayInput = input("Enter a day of week: ").strip().lower()
        if dayInput in ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
            day = dayInput
            break
        else:
            print("Enter day invalid!")


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
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    most_month = df['month'].mode()[0]
    most_day = df['day_of_week'].mode()[0]
    df['start_hour'] = df['Start Time'].dt.hour
    most_start_hour = df['start_hour'].mode()[0]

    # TO DO: display the most common month
    print('The most common month: ', most_month, '\n')

    # TO DO: display the most common day of week
    print('The most common day:', most_day, '\n')

    # TO DO: display the most common start hour
    print('The most common start hour:', most_start_hour, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', most_start_station, '\n')

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:', most_end_station, '\n')


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + '_' + df['End Station']
    most_combination = df['Combination'].mode()[0]
    print('The most frequent combination of start station and end station trip:', most_combination, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    total_travel_time = df['Travel Time'].sum()
    print('The total travel time:', total_travel_time, '\n')

    # TO DO: display mean travel time
    total_mean_time = df['Travel Time'].mean() 
    print('The mean travel time:', total_mean_time, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('The counts of user types:', user_type_counts, '\n')

    # TO DO: Display counts of gender
    gender_list = None
    try:
        if df.get('Gender') is not None:
            gender_counts = df['Gender'].value_counts()
            print('The counts of gender:', gender_counts, '\n')
        else:
            print('The property Gender does not exist in the DataFrame.')
    except Exception as e:
        print("An error occurred:", e)
 

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        if df.get('Birth Year') is not None:
            earliest_year = int(df['Birth Year'].min())
            print('The earliest year of birth:', earliest_year, '\n')

            most_recent_year = int(df['Birth Year'].max())
            print('The most recent year of birth:', most_recent_year, '\n')

            most_common_year = int(df['Birth Year'].mode()[0])
            print('The most common year of birth:', most_common_year, '\n')
        else:
            print('The property Birth Year does not exist in the DataFrame.')
    except Exception as e:
        print("An error occurred:", e)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_raw_data(df):
    """ Display raw data """
    i = 0
    raw = input("Do you want to display raw data? ").lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df) # TO DO: appropriately subset/slice your data frame to display next five rows
            raw = input("Do you want to display raw data again? ").lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
