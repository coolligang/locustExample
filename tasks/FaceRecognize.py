# encoding:utf-8

from locust import TaskSet, task
from restVariable.RestVariable import RestVariable
from entity.Rest import Rest
from tool.RfeLibrary import RfeLibrary


class FaceRecognizeTask(TaskSet):
    @task
    def faceRecognize(self):
        var = RestVariable()
        var_rest = var.faceRecognizeVar()
        rfeLib = RfeLibrary()
        except_rs = '{"faceInfo":[{"fId":"B0001234","uId":"test3000004","userSex":1,"recognizeTime":"20180425140826","rate":0.452894}],"faceNum":1,"status":0,"reqId":"20180425140826728","msg":"Success"}'
        if isinstance(var_rest, Rest):
            if var_rest.getMethod() == "POST":
                with self.locust.client.post(url=var_rest.getUrl(), json=var_rest.getJson(),
                                             catch_response=True) as response:
                    try:
                        rfeLib.assertJson(except_rs, response.content, 0)
                        except_rs2 = '{"faceNum":' + str(len(var_rest.getExcepts())) + ',"status":0,"msg":"Success"}'
                        rfeLib.assertJson(except_rs2, response.content)
                        excepts_userImg = var_rest.getExcepts()
                        actual_userInfo = rfeLib.getValueFromJson(response.content, "$.faceInfo")
                        self.assertRecognize(excepts_userImg, actual_userInfo)
                    except Exception, e:
                        response.failure(repr(e))
                    else:
                        response.success()

    def assertRecognize(self, excepts, actual, rate=0.85):
        error_msg = []
        for i in excepts:
            user_tag = [j for j in actual if j["fId"] == i]
            if len(user_tag) == 0:
                error_msg.append({"type": "lost user", "user": i})
            if user_tag[0]["rate"] > rate:
                if str(user_tag[0]["uId"]).split("_")[0] != str(i).split("_")[0]:
                    error_msg.append({"type": "recognize error", "user": user_tag[0]})
            else:
                if not str(user_tag[0]["uId"]):
                    error_msg.append({"type": "rate error", "user": user_tag[0]})
        if len(error_msg) > 0:
            raise AssertionError("face recognize error:" + str([str(i) for i in error_msg]))
