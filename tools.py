import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        call_time = datetime.datetime.now()
        time_format = call_time.strftime('%d/%m/%Y, %H:%M:%S')
        name_func = old_function.__name__
        arguments = f'{args}, {kwargs}'
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as log_file:
            write = f'Дата и время вызова функции: {time_format}\n ' \
                    f'Функция: {name_func}\n Аргументы: {arguments}\n Возвращаемое значение: {result}\n\n'
            log_file.writelines(write)
        return result
    return new_function

def logger_path(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            call_time = datetime.datetime.now()
            time_format = call_time.strftime('%d/%m/%Y, %H:%M:%S')
            name_func = old_function.__name__
            arguments = f'{args}, {kwargs}'
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as log_file:
                write = f'Дата и время вызова функции: {time_format}\n ' \
                        f'Функция: {name_func}\n Аргументы: {arguments}\n Возвращаемое значение: {result}\n\n'
                log_file.writelines(write)
            return result
        return new_function
    return __logger
