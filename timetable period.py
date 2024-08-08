days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
periods_per_day = 8
period_duration = 50

start_time = 8 * 60 

for day in days:
    print(f"\n{day}:")
    current_time = start_time
    for period in range(1, periods_per_day + 1):
        start_hours = current_time // 60
        start_minutes = current_time % 60
        current_time += period_duration
        end_hours = current_time // 60
        end_minutes = current_time % 60
        print(f"  Period {period}: {start_hours:02}:{start_minutes:02} - {end_hours:02}:{end_minutes:02}")
