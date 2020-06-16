from multiprocessing import cpu_count

bind = "127.0.0.1:5000"
workers = 2
threads = 2 * cpu_count()
