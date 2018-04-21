import multiprocessing
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
