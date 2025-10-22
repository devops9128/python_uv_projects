from datetime import datetime
import calendar

today_date = datetime.today().strftime("%b")

def data_syslog(month: int, date: int):

    raw_logs = []
    finish_logs = []

    month_num = int(month)
    month_abbr = calendar.month_abbr[month_num]

    date_str = str(date)

    with open('/var/log/syslog', mode='r', encoding='utf-8') as file:
        read_lines = file.readlines()
        for data in read_lines:
            data_process = data.strip("\n").split(' ')
            if data_process[0] == month_abbr and data_process[1] == date_str:
                raw_logs.append(data_process)
        
        joined_logs = [' '.join(line) for line in raw_logs]
        for i in joined_logs:
            finish_logs.append(i)

        return finish_logs

def date_auth(month: int, date: int):

    raw_logs = []
    finish_logs = []

    month_num = int(month)
    month_abbr = calendar.month_abbr[month_num]

    date_str = str(date)

    with open('/var/log/auth.log', mode='r', encoding='utf-8') as file:
        read_lines = file.readlines()
        for data in read_lines:
            data_process = data.strip("\n").split(' ')
            if data_process[0] == month_abbr and data_process[1] == date_str:
                raw_logs.append(data_process)

        joined_logs = [' '.join(line) for line in raw_logs]
        for i in joined_logs:
            finish_logs.append(i)
        
        return finish_logs




def data_boot():
    pass

def data_lastlog():
    pass

def failog():
    pass

if __name__ == '__main__':
    for i in data_syslog(10, 20):
        print(i)
    print()
    for i in date_auth(10, 22):
        print(i)
