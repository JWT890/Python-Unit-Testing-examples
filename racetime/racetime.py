def conv_secs_time(seconds):
    hrs = int(seconds/3600)
    rem_secs = seconds%3600
    mins = int(rem_secs/60)
    secs = rem_secs%60
    print("Final time: ",hrs,':',mins,':',secs)



def run_finish_time(hr,mn):
    start_time = hr*3600+mn*60
    easy_pace_time = 2*(8*60+15)
    tempo_pace_time = 3*(7*60+12)
    finish_time = start_time+easy_pace_time+tempo_pace_time
    print("Finish time in seconds",finish_time)
    conv_secs_time(finish_time)

start_hr = int(input("Enter the starting hours: "))
start_min = int(input("Enter the starting minutes: "))
run_finish_time(start_hr,start_min)

conv_secs_time(5678)
