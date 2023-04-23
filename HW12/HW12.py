
def my_function():
    import datetime
    def log_call_time(func):
        def wrapper(*args, **kwargs):
            function_name = func.__name__
            current_time = datetime.datetime.now()
            print(f"Функція '{function_name}' була викликана {current_time}")
            return func(*args, **kwargs)
        return wrapper