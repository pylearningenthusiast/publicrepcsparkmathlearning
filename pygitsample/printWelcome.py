from datetime import datetime

def print_message(message, header_char=''):
    if header_char:
        print(f'{header_char*100}')
    print(f'{datetime.now()}:{message}')
