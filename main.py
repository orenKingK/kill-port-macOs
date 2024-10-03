import subprocess
import re


def send_command(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def clean_output_white_spaces(line_to_clean):
    return re.sub(r"\s+", " ", line_to_clean, flags=re.UNICODE)


def main():
    print('okkkkkkkkkkkkk')

    ports_str = input('Choose a ports with spaces: ')
    ports = ports_str.split(' ')
    for port in ports:
        output_find_process_pid = send_command(f'sudo lsof -i :{port}')
        cmd_output_lines = output_find_process_pid.stdout.readlines()

        if len(cmd_output_lines) < 1:
            print(f"No process at the chosen port {port}!")
            continue

        pid_line = cmd_output_lines[1]
        str_pid_line = pid_line.decode('utf-8')
        str_pid_line = clean_output_white_spaces(str_pid_line)
        pid = str_pid_line.split(' ')[1]

        send_command(f'kill -9 {pid}')

        print("Process at port: ", port, " killed :)")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
