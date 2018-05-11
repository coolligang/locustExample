# encoding:utf-8
from locust import TaskSet, task
from entity.Rest import Rest
from restVariable.RestVariable import RestVariable
from tool.RfeLibrary import RfeLibrary


class SingleRegist(TaskSet):
    @task
    def singleRegister(self):
        rest = RestVariable()
        var_rest = rest.batchRegist()
        rfeLib = RfeLibrary()
        if isinstance(var_rest, Rest):
            if var_rest.getMethod() == "POST":
                reqId = var_rest.getExcepts()
                excepts = '{"reqId": "20180511092955098", "status": 0, "msg": "Success"}'
                with self.locust.client.post(url=var_rest.getUrl(), json=var_rest.getJson(),
                                             catch_response=True) as response:
                    try:
                        rfeLib.assertJson(excepts, response.content, 0)
                        excepts2 = '{"status": 0, "msg": "Success"}'
                        rfeLib.assertJson(excepts2, response.content)
                    except Exception, e:
                        response.failure(repr(e))
                    else:
                        response.success()


class BatchRegist(TaskSet):
    @task
    def batchRegister(self):
        rest = RestVariable()
        var_rest = rest.batchRegist()
        rfeLib = RfeLibrary()
        if isinstance(var_rest, Rest):
            if var_rest.getMethod() == "POST":
                reqId = var_rest.getExcepts()
                excepts = '{"apiId":null,"timestamp":null,"sign":null,"reqId":"' + reqId + '","status":0,"msg":"Success","result":[]}'
                with self.locust.client.post(url=var_rest.getUrl(), json=var_rest.getJson(),
                                             catch_response=True) as response:
                    try:
                        rfeLib.assertJson(excepts, response.content)
                    except Exception, e:
                        response.failure(repr(e))
                    else:
                        response.success()
