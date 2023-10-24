def convert(time_str):
    
    try:
        hours, minutes = map(int, time_str.split(":"))
        return hours + minutes / 60.0
    except ValueError:
        print("please use a valid time formate hh:mm")
        exit()

def main():
    
    user_time_str = input("Please enter the time in 24-hour format (e.g., 08:30): ")
    
    
    user_time = convert(user_time_str)

    
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 19.0
    dinner_end = 20.0

   
    if breakfast_start <= user_time <= breakfast_end:
        print("breakfast time")
    elif lunch_start <= user_time <= lunch_end:
        print("lunch time")
    elif dinner_start <= user_time <= dinner_end:
        print("dinner time")
    

if __name__ == "__main__":
    main()
