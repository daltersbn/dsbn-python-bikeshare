import pandas as pd
from datetime import datetime

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

def get_filters():
    print("Hello! Let's explore some US bikeshare data!")

    while True:
        city = input("Choose a city (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        print("Invalid city.")

    while True:
        month = input("Choose a month (all, january, february, march, april, may, june): ").lower()
        if month in ["all", "january", "february", "march", "april", "may", "june"]:
            break
        print("Invalid month.")

    while True:
        day = input("Choose a day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()
        if day in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            break
        print("Invalid day.")

    print("-" * 40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name().str.lower()

    if month != "all":
        month_num = [
            "january", "february", "march", "april", "may", "june"
        ].index(month) + 1
        df = df[df["month"] == month_num]

    if day != "all":
        df = df[df["day_of_week"] == day]

    return df


def time_stats(df):
    print("Calculating The Most Frequent Times of Travel...")

    popular_month = df["month"].mode()[0]
    popular_day = df["day_of_week"].mode()[0]
    popular_hour = df["Start Time"].dt.hour.mode()[0]

    print(f"Most common month: {popular_month}")
    print(f"Most common day: {popular_day}")
    print(f"Most common hour: {popular_hour}")
    print("-" * 40)


def station_stats(df):
    print("Calculating The Most Popular Stations and Trip...")

    start_station = df["Start Station"].mode()[0]
    end_station = df["End Station"].mode()[0]
    trip = (df["Start Station"] + " → " + df["End Station"]).mode()[0]

    print(f"Most common start station: {start_station}")
    print(f"Most common end station: {end_station}")
    print(f"Most common trip: {trip}")
    print("-" * 40)


def trip_duration_stats(df):
    print("Calculating Trip Duration...")

    total_time = df["Trip Duration"].sum()
    mean_time = df["Trip Duration"].mean()

    print(f"Total travel time: {total_time}")
    print(f"Average travel time: {mean_time}")
    print("-" * 40)


def user_stats(df):
    print("Calculating User Stats...")

    if "User Type" in df.columns:
        print(df["User Type"].value_counts())

    if "Gender" in df.columns:
        print(df["Gender"].value_counts())

    if "Birth Year" in df.columns:
        print(f"Earliest birth year: {int(df['Birth Year'].min())}")
        print(f"Most recent birth year: {int(df['Birth Year'].max())}")
        print(f"Most common birth year: {int(df['Birth Year'].mode()[0])}")

    print("-" * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("Would you like to restart? (yes/no): ").lower()
        if restart != "yes":
            break


if __name__ == "__main__":
    main()
