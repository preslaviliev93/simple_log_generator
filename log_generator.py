import random
import time

"""
        Chose how many logs per second to generate.
        This ensures the proper delay.
"""
logs_per_second = 150
delay = 1.0 / logs_per_second
sample_log_f = "/var/log/sample_log.log"  # Sample file containing actual logs
write_to_file = "/path/to/location/output.log"  # Output file where the logs will be randomly generated


class LogGenerator:
    def __init__(self, sample_log_file):
        self.sample_log_file = sample_log_file

    def print_main_menu(self):
        options = (
            '[1] Generate logs',
            '[2] Exit'
        )

        for item in options:
            print(item)

    def get_user_input(self):
        user_input = input('Enter your choice: ')
        while True:

            if user_input == '1':
                n_lines = int(input('Number of logs [1-10000]:'))
                while n_lines <= 0 or n_lines > 10000:
                    n_lines = int(input('Number of logs [1-10000]:'))
                print(self.generate_logs(n_lines))
                break
            elif user_input == '2':
                break
            else:
                user_input = input('Enter a valid option: ')

    def generate_logs(self, total_logs):
        total_logs_to_write = []
        with open(write_to_file, 'w') as f:
            pass

        with open(self.sample_log_file, 'r') as sample_logs:
            contents = sample_logs.readlines()
            for _ in range(total_logs):
                log = random.choice(contents)
                total_logs_to_write.append(log)
                with open(write_to_file, 'a') as out_file:
                    out_file.write(log)
                    # print(f'Written: {log}')  # Left for debug purposes only
                time.sleep(delay)

        return f'Total logs written {len(total_logs_to_write)}'


if __name__ == '__main__':

    log_generator = LogGenerator(sample_log_f)
    log_generator.print_main_menu()
    log_generator.get_user_input()
