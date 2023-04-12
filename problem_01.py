def get_num_of_years():
    return int(input('Enter the number of years: '))


def get_monthly_rainfall(year):
    print(f"\nFor year {year}")
    monthly_rainfall = []
    for month in range(12):
        monthly_rainfall.append(int(input(f"Enter the rainfall amount for month-{month + 1}: ")))
    return monthly_rainfall


def get_total_and_ave(monthly_rainfall):
    total = 0
    for monthly in monthly_rainfall:
        total += monthly
    average = total / 12
    return total, average


def print_total_and_ave(total, average):
    print("For 12 months")
    print(f"Total rainfall: {total} inches")
    print(f"Average monthly rainfall: {round(average, 2)} inches")


# Main flow
num_of_years = get_num_of_years()
for year in range(num_of_years):
    monthly_rainfall = get_monthly_rainfall(year + 1)
    total, average = get_total_and_ave(monthly_rainfall)
    print_total_and_ave(total, average)
