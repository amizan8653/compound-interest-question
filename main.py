import math


def calculate_principal(p, r, n, t):
    base = 1 + r / n
    exponent = n * t
    return p * math.pow(base, exponent)


def calculate_principal_for_x_a_day_for_t_years(r, n, amount_per_day, years):
    summation = 0
    for year in range(int(years)):

        if year % 4 == 0:
            # this is a leap year
            end_day_range = 366
        else:
            # this is not a leap year
            end_day_range = 365

        for day in range(end_day_range):
            summation += calculate_principal(amount_per_day, r, n, year + day / end_day_range)
    return summation


def run_calculations():
    r = .30  # 30 % per year
    n = 1    # interest compounds 1 time per year
    years = 30.0

    print()
    print("this is the amount of money you'd have if you invested just $5 on day 1 and waited {} years"
          .format(years))
    invest_only_5_on_day_1 = calculate_principal(5, r, n, years)
    print(invest_only_5_on_day_1)
    print()

    print("this is the amount of money you'd have if you invested just $5 on day 2 and waited 29 years and 364 days")
    invest_only_5_on_day_2 = calculate_principal(5, r, n, 29.0 + 364.0/365.0)
    print(invest_only_5_on_day_2)
    print()

    print("this is the amount of money you'd have if you invested just $5 on day 1 and 2 and waited {} years"
          .format(years))
    principal_after_2_days = calculate_principal(5, r, n, 1.0/365.0) + 5
    invest_only_5_on_day_1_and_2 = calculate_principal(principal_after_2_days, r, n, 29.0 + 364.0/365.0)
    print(invest_only_5_on_day_1_and_2)
    print()

    print("this is the difference between investing on day 1 and 2 VS sum of 2 accounts, investing on separate days")
    difference = invest_only_5_on_day_1_and_2 - (invest_only_5_on_day_1 + invest_only_5_on_day_2)
    print("{} - ({} + {}) = {}"
          .format(invest_only_5_on_day_1_and_2, invest_only_5_on_day_1, invest_only_5_on_day_2, difference))
    print()

    print("since this result is 0, it implies that a series summation is a sufficient for calculations. ")
    print()

    print("amount of money you'd have after investing $5 a day for {} years, "
          "{}% compound interest compounding yearly (ignoring the extra leap day in leap year):"
          .format(years, r * 100))
    summation_one = calculate_principal_for_x_a_day_for_t_years(r, n, 5, years)
    print(summation_one)
    print()

    print("amount of money you'd have after investing into 5 accounts, each at $1 a day for {} years, "
          "{}% compound interest compounding yearly (ignoring the extra leap day in leap year):"
          .format(years, r * 100))
    summation_two = 5 * calculate_principal_for_x_a_day_for_t_years(r, n, 1, years)
    print(summation_two)
    print()

    print("here's the difference between the 2 previous summations (there might be some floating point error)")
    print(summation_two - summation_one)
    print()


if __name__ == '__main__':
    run_calculations()
