# encoding:utf-8

from tool.RfeLibrary import RfeLibrary
from tool.RfeLibTool import RfeLibTool
from entity.Rest import Rest


class RestVariable:
    apiId = "BOxALFZsYGw0GNzebQck1xKs"
    apiKey = "1285384ddfb057814bad78127bc789be"

    def __init__(self):
        self.rfeLibrary = RfeLibrary()
        self.rfeRfeTool = RfeLibTool()

    def faceRecognizeVar(self):
        url = "/api/v1/face/facerecognize"
        rest = Rest("post", url)
        timestamp = str(self.rfeLibrary.getTimestamp())
        pre_sign = "api/v1/facerecognize" + self.apiKey + str(timestamp)
        sign = self.rfeLibrary.toMD5(pre_sign)

        userNum = self.rfeRfeTool.getRandInt(1, 5)
        faceInfos = []
        excepts_msg = []
        for i in range(userNum):
            userImg = self.rfeRfeTool.listRandFileName("feature/")
            with open("feature/" + userImg[0] + "/0.txt", "r") as fin:
                feature = fin.read()
            fId = userImg[0] + "_" + timestamp + "_" + self.rfeRfeTool.getRandStr()
            excepts_msg.append(fId)
            user = {"fId": fId, "feature": feature[:-1]}
            faceInfos.append(user)
        rest.setExcepts(excepts_msg)
        body = {"apiId": self.apiId, "timestamp": timestamp, "cameraId": "Auto_camer_001", "sign": sign,
                "cameraIp": "10.23.25.44",
                "faceInfos": faceInfos}
        rest.setJson(body)
        return rest

    def singleRegist(self):
        url = "/api/v1/face/singleregist"
        rest = Rest("post", url)
        timestamp = str(self.rfeLibrary.getTimestamp())
        pre_sign = "api/v1/face/singleregist" + self.apiKey + str(timestamp)
        sign = self.rfeLibrary.toMD5(pre_sign)
        path = "imgs/gallery_f/"
        userImgs = self.rfeRfeTool.listRandFileName(path)
        userImg = self.rfeRfeTool.toBase64(path + userImgs[0])
        userRegion = "Auto_Region_" + timestamp
        userSex = 1
        uId = userImgs[0] + timestamp + self.rfeRfeTool.getRandStr()
        obj_json = {"apiId": self.apiId, "timestamp": timestamp, "userImg": userImg, "sign": sign, "uId": uId,
                    "userSex": userSex, "userRegion": userRegion}
        rest.setJson(obj_json)
        rest.setExcepts(userImgs[0])
        return rest

    def batchRegist(self):
        url = "/api/v1/face/batchregist"
        rest = Rest("post", url)
        timestamp = str(self.rfeLibrary.getTimestamp())
        pre_sign = "api/v1/face/batchregist" + self.apiKey + str(timestamp)
        sign = self.rfeLibrary.toMD5(pre_sign)
        reqId = self.rfeRfeTool.listUUID()[0]

        registInfo = []
        userNum = self.rfeRfeTool.getRandInt(1, 100)
        for i in range(userNum):
            path = "imgs/gallery_f/"
            userImgs = self.rfeRfeTool.listRandFileName(path)
            userImg = self.rfeRfeTool.toBase64(path + userImgs[0])
            userRegion = "Auto_Region_" + timestamp
            userSex = 1
            uId = userImgs[0] + timestamp + self.rfeRfeTool.getRandStr()
            user = {"uId": uId, "userSex": userSex, "userRegion": userRegion, "userImg": userImg}
            registInfo.append(user)
        obj_json = {"apiId": self.apiId, "timestamp": timestamp, "sign": sign, "reqId": reqId, "registInfo": registInfo}
        rest.setJson(obj_json)
        rest.setExcepts(reqId)
        return rest


if __name__ == "__main__":
    test = RestVariable()
    rest = test.singleRegist()
    if isinstance(rest, Rest):
        print rest.getMethod()
        print rest.getUrl()
        print rest.getJson()
