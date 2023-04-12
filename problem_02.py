def validate_user_input(number, input_type):
    if number < 1:
        print(f"Invalid {input_type}: '{number}'. Must enter positive number only!")


def get_organism_start_count():
    organism_start_count = 0
    while (organism_start_count < 1):
        organism_start_count = int(input("Starting number of organisms: "))
        validate_user_input(organism_start_count, "organism starting number")
    return organism_start_count


def get_daily_increase_pct():
    daily_increase_pct = 0
    while (daily_increase_pct < 1):
        daily_increase_pct = int(input("Average daily percentage increase: "))
        validate_user_input(daily_increase_pct, "average daily percentage increase")
    return daily_increase_pct


def get_num_of_days_data():
    num_of_days_data = 0
    while (num_of_days_data < 1):
        num_of_days_data = int(input("Enter the number of days to display the final data: "))
        validate_user_input(num_of_days_data, "number of days")
    return num_of_days_data


def calc_daily_change(organism_start_count, daily_increase_pct, num_of_days_data):
    daily_organism_count = [organism_start_count]

    for day in range(1, num_of_days_data):
        curr_organism_count = daily_organism_count[day - 1] * (1 + daily_increase_pct / 100)
        daily_organism_count.append(curr_organism_count)

    return daily_organism_count


def print_daily_organism_count(daily_organism_count):
    print("Day Approximate          Population")
    print("__________________________________________________")
    for day in range(len(daily_organism_count)):
        current_day = day + 1
        space_append = ' ' * (25 - len(str(day + 1)))
        current_day_count = daily_organism_count[day]

        print(f"{current_day}{space_append}{current_day_count}")


# Main flow
organism_start_count = get_organism_start_count()
daily_increase_pct = get_daily_increase_pct()
num_of_days_data = get_num_of_days_data()
daily_organism_count = calc_daily_change(organism_start_count, daily_increase_pct, num_of_days_data)
print_daily_organism_count(daily_organism_count)
