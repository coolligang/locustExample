# encoding:utf-8

from restVariable.RestVariable import RestVariable
from entity.Rest import Rest
from tool.RfeLibrary import RfeLibrary
import json


class Test():
    def testFace(self):
        var = RestVariable()
        var_rest = var.faceRecognizeVar()
        rfeLib = RfeLibrary()
        except_rs = '{"faceInfo":[{"fId":"B0001234","uId":"test3000004","userSex":1,"recognizeTime":"20180425140826","rate":0.452894}],"faceNum":1,"status":0,"reqId":"20180425140826728","msg":"Success"}'
        if isinstance(var_rest, Rest):
            if var_rest.getMethod() == "POST":
                url = "http://172.16.31.36:9090" + var_rest.getUrl()
                rs = rfeLib.reqByJson(var_rest.getMethod(), url,
                                      json=var_rest.getJson())
                try:
                    rfeLib.assertJson(except_rs, rs.content, 0)
                    except_rs2 = '{"faceNum":' + str(len(var_rest.getExcepts())) + ',"status":0,"msg":"Success"}'
                    rfeLib.assertJson(except_rs2, rs.content)
                    excepts_userImg = var_rest.getExcepts()
                    print excepts_userImg
                    print rs.content
                    actual_userInfo = rfeLib.getValueFromJson(rs.content, "$.faceInfo")
                    print actual_userInfo
                    self.assertFace(excepts_userImg, actual_userInfo)
                except Exception, e:
                    raise AssertionError(repr(e))

    def assertFace(self, excepts, actual):
        error_msg = []
        for i in excepts:
            user_tag = [j for j in actual if j["fId"] == i]
            if len(user_tag) == 0:
                print "用户没有正常识别"
                error_msg.append({"type": "lost user", "user": i})
            if user_tag[0]["rate"] > 0.85:
                if str(user_tag[0]["uId"]).split("_")[0] != str(i).split("_")[0]:
                    print "用户识别错误"
                    error_msg.append({"type": "recognize error", "user": user_tag[0]})
            else:
                if not str(user_tag[0]["uId"]):
                    print "分数错误"
                    error_msg.append({"type": "rate error", "user": user_tag[0]})
        if len(error_msg) > 0:
            raise AssertionError("face recognize error:" + str([str(i) for i in error_msg]))
        else:
            print "断言正确"

    def betchRegist(self):
        rest = RestVariable()
        var_rest = rest.batchRegist()
        rfeLib = RfeLibrary()
        if isinstance(var_rest, Rest):
            if var_rest.getMethod() == "POST":
                reqId = var_rest.getExcepts()
                excepts = '{"apiId":null,"timestamp":null,"sign":null,"reqId":"' + reqId + '","status":0,"msg":"Success","result":[]}'
                print excepts
                url="http://172.16.31.36:9090" + var_rest.getUrl()
                rs = rfeLib.reqByJson(method=var_rest.getMethod(), url=url, json=var_rest.getJson())
                print rs.content


if __name__ == "__main__":
    test = Test()
    test.betchRegist()
