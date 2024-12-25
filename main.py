#print"請輸入測驗日期(yyyy/mm/dd eg.2024.01.01請輸入2024/01/01)"
#print"請輸入受測者出生日期(yyyy/mm/dd eg.2021.01.01請輸入2021/01/01)"

#月齡=測驗日期-出生日期

    #if 月齡<24個月(即<2歲)
    #print"請輸入受測者出生週數(ww/d eg.34週+5天請輸入34/5)"

        #if出生週數<38週
        #print"請輸入受測者預產期(yyyy/mm/dd eg.2021.01.01請輸入2021/01/01)"
        #使用矯正年齡計算 月齡=測驗日期-預產期

#print"月齡:(y/mm)" (顯示_歲__月，若"dd"相減>=15則"月"進位一個月，若否則捨去)
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from datetime import datetime, timedelta

def calculate_months(test_date, birth_date, due_date=None):
    if due_date:
        corrected_birth_date = due_date
    else:
        corrected_birth_date = birth_date

    # Calculate the difference in days
    delta = test_date - corrected_birth_date
    total_months = delta.days // 30
    extra_days = delta.days % 30

    years = total_months // 12
    months = total_months % 12

    if extra_days >= 15:
        months += 1
        if months == 12:
            years += 1
            months = 0

    return years, months

def main():
    test_date_input = input("測驗日期(eg.2024.01.01請輸入2024/01/01):")
    test_date = datetime.strptime(test_date_input, "%Y/%m/%d")

    birth_date_input = input("受測者出生日期(eg.2021.01.01請輸入2021/01/01):")
    birth_date = datetime.strptime(birth_date_input, "%Y/%m/%d")

    # Calculate initial months
    years, months = calculate_months(test_date, birth_date)

    if years <2 :
        birth_weeks_input = input("受測者出生週數(ww/d eg.34週+0天請輸入34/0):")
        birth_weeks, birth_days = map(int, birth_weeks_input.split("/"))

        if birth_weeks < 38:
            due_date_input = input("預產期(eg.2021.01.01請輸入2021/01/01):")
            due_date = datetime.strptime(due_date_input, "%Y/%m/%d")

            years, months = calculate_months(test_date, birth_date, due_date)

    print(f"測驗月齡(早產兒未滿2歲顯示矯正年齡): {years}歲{months}月")

if __name__ == "__main__":
    main()
