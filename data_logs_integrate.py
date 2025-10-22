from datetime import datetime
import calendar

class LogProcess():
    def __init__(self, logs: str, month: int, date: int):
        self.logs = logs
        self.month = month
        self.date = date

        try:
            self.month_num = int(self.month)
            self.month_abbr = calendar.month_abbr[self.month_num]
        except(ValueError, IndexError):
            raise ValueError("Month must be integer between 1 and 12.")
        
        self.date_str = str(self.date).strip()
        self.logs_locaton = f"/var/log/{self.logs}"

    def data_syslog(self):
        raw_logs = []
        finish_logs = []

        try:
            with open(self.logs_locaton, mode='r', encoding='utf-8') as file:
                read_lines = file.readlines()
                for data in read_lines:
                    data_process = data.strip("\n").split()

                    if len(data_process) < 2:
                        continue

                    if data_process[0] == self.month_abbr and data_process[1] == self.date_str:
                        raw_logs.append(data_process)
                
                finish_logs = [' '.join(line) for line in raw_logs]

                return finish_logs
        except FileNotFoundError:
            print(f"Error: Log file not found at {self.logs_location}. Check file path and permissions.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def data_auth():
        pass


if __name__ == '__main__':
    syslog = LogProcess("syslog", 10, 22)
    print(syslog.data_syslog())