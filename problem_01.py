def get_num_of_years():
    return int(input('Enter the number of years: '))


def get_monthly_rainfall(num_of_years):
    monthly_rainfall_per_year = []
    for year in range(0, num_of_years):
        print(f"\nFor year {year + 1}")
        monthly_rainfall_per_year.append([])
        for month in range(0, 12):
            monthly_rainfall_per_year[year].append(int(input(f"Enter the rainfall amount for month-{month + 1}: ")))
    return monthly_rainfall_per_year


def get_yearly_total_and_ave(monthly_rainfall_each_year):
    yearly_total_and_ave = []

    for yearly in monthly_rainfall_each_year:
        total = 0
        for monthly in yearly:
            total += monthly
        average = total / 12
        yearly_total_and_ave.append([total, average])

    return yearly_total_and_ave


def print_yearly_total_and_ave(yearly_total_and_ave):
    for year in range(0, len(yearly_total_and_ave)):
        print(f"\nFor year {year + 1}")
        print("For 12 months")
        print(f"Total rainfall: {yearly_total_and_ave[year][0]} inches")
        print(f"Average monthly rainfall: {round(yearly_total_and_ave[year][1], 2)} inches")


# Main flow
num_of_years = get_num_of_years()
monthly_rainfall_per_year = get_monthly_rainfall(num_of_years)
yearly_total_and_ave = get_yearly_total_and_ave(monthly_rainfall_per_year)
print_yearly_total_and_ave(yearly_total_and_ave)
