from datetime import datetime
import calendar

# 获取当前月份，转换成英文缩写 Oct, Nov, Dec
today_date = datetime.today().strftime("%b")

# 定义处理syslog日志
def data_syslog(month: int, date: int):

    # 定义空列表，用于保存筛选出要用的数据
    raw_logs = []

    # 定义空列表，用于保存已经处理好的数据
    finish_logs = []

    # 将传入的参数值，转换成整数
    month_num = int(month)

    # 将整数的值，转换成英文月份缩写 Oct Nov Dec
    month_abbr = calendar.month_abbr[month_num]

    # 将传入的参数值，转换成字符
    date_str = str(date)

    # 打开syslog日志，使用只读模式，使用utf-8编码，然后创建别名 file
    with open('/var/log/syslog', mode='r', encoding='utf-8') as file:

        # 日志每一行数据，然后使用列表形式返回数据
        read_lines = file.readlines()

        # 遍历 read_lines 列表中所有数据
        for data in read_lines:
            
            # 
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
