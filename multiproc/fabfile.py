import atexit
from functools import partial
import multiprocessing
import signal
import subprocess
import threading

from fabric.api import task, local
from fabric.tasks import execute

@task
def serve_django():
    local('python django_server.py')

@task
def serve_npm():
    local('python npm_server.py')


@task
def serve_thread():
    threads = []
    sub_tasks = [serve_django, serve_npm]
    for sub_task in sub_tasks:
        t = threading.Thread(target=execute, args=(sub_task,))
        threads.append(t)
        t.start()

@task
def serve_proc():
    processes = []
    sub_tasks = [serve_django, serve_npm]
    for sub_task in sub_tasks:
        p = multiprocessing.Process(target=execute, args=(sub_task,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

def term_process(proc):
    try:
        proc.send_signal(signal.SIGTERM)
    except OSError:
        pass

@task
def serve_subproc():
    django_proc = subprocess.Popen(['python', 'django_server.py'])
    npm_proc = subprocess.Popen(['python', 'npm_server.py'])
    django_proc.wait()
    npm_proc.wait()
    atexit.register(partial(term_process, django_proc))
    atexit.register(partial(term_process, npm_proc))
