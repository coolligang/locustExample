# encoding:utf-8

from locust import HttpLocust
from gevent import monkey
from tasks.FaceRecognize import FaceRecognizeTask
from tasks.Regist import SingleRegist
from tasks.Regist import BatchRegist
from tasks.LangChao import LangChao

monkey.patch_all()


class Lancher(HttpLocust):
    # task_set = FaceRecognizeTask
    # task_set = SingleRegist
    # task_set = BatchRegist
    task_set = LangChao
    host = "http://172.16.31.36:9090"
    min_wait = 0
    max_wait = 5000
