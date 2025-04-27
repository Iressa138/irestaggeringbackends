import requests
import random
import json
from flask import Flask, jsonify, request
# give me fucking credits bro.
app = Flask(__name__)
def GameInfo():
TitleID: mew = ""
PlayFabKey: mew = ""
erm = ""
BanURL = f"https://titleid.playfabapi.com/Admin/BanUsers" # the reason why i put erm because you maybe won't get this so if you get this you don't no what erm means HAHA, find something else to skid.
@app.route('/')
@app.route("/CheckForMOTD")
def CheckForMOTD():
return jsonify({"MOTD":"<color=yellow>WELCOME TO IRES TAG!</color>\n\n<color=blue>YOUR PLAYER ID IS: " + currentPlayerId + "</color>\n\n<color=magenta>CURRENT UPDATE: SUMMER 2022!</color>\n\n<color=cyan>.JOIN THE DISCORD FOR A COOKIE!</color>\n\n<color=red>CREDITS: IRES, MICHAEL</color>"})

@app.route("/", methods = ["POST", "GET"])
def main():
    return "ires made this shit"

def auth():
    return {"content-type": "application/json","X-SecretKey": PlayFabKey}

def ermShitSigma():
@app.route('/api/PlayFabAuthentication', methods=['POST'])
def PlayFabAuthentication():
    data = request.get_json()

    print(data)

    CustomId: str = data.get("CustomId", "Null")
    Nonce: str = data.get("Nonce", "Null")
    OculusId: str = data.get("OculusId", "Null")
    Platform: str = data.get("Platform", "Null")

    erm = requests.post(
        url=
f"https://{title}.playfabapi.com/Server/LoginWithServerCustomId",
        json={
            "ServerCustomId": CustomId,
            "CreateAccount": True
        },
        headers={
            "content-type": "application/json",
            "x-secretkey": secretkey
        })
    if BLAH.status_code == 200: 
        print("successful login chat!")
        jsontypeshi = BLAH.json()
        goodjson = jsontypeshi.get("data")
        PlayFabId = goodjson.get("PlayFabId")
        SessionTicket = goodjson.get("SessionTicket")
        Entity = goodjson.get("EntityToken")
        EntityToken = Entity["EntityToken"]
        EntityId = Entity["Entity"]["Id"]
        EntityType = Entity["Entity"]["Type"]

        data = [
            PlayFabId,
            SessionTicket,
            Entity,
            EntityToken,
            EntityId,
            Nonce,
            OculusId,
            Platform
        ]

        EASports = requests.post(
            url=f"https://{title}.playfabapi.com/Client/LinkCustomID",
            json={
                "CustomID": CustomId,
                "ForceLink": True
            },
            headers={
                "content-type": "application/json",
                "x-authorization": SessionTicket
            })
        if EASports.status_code == 200:
            print("erm")
            return jsonify({
                "PlayFabId": PlayFabId,
                "SessionTicket": SessionTicket,
                "EntityToken": EntityToken,
                "EntityId": EntityId,
                "EntityType": EntityType
            }), 200
        else:
            return jsonify({"Message": "Failed"}), 400
    else:
        return jsonify({"Message": "More likely banned"}), 403

@app.route("/api/CachePlayFabId", methods=["POST"])
def cpi():
    getjson = request.get_json()
    coems[getjson.get("PlayFabId")] = getjson
    return jsonify({"Message": "worked!!"}), 200

@app.route("/api/titledata", methods=["POST", "GET"])
def TitLeData():
    ts = f"https://{TitleID}.playfabapi.com/Server/GetTitleData"
    mew = {"X-SecretKey": PlayFabKey, "Content-Type": "application/json"}
    e = requests.post(url=ts, headers=mew)
    StopAu = e.json().get("data", "").get("Data", "")

    return jsonify(StopAu)
# i think you know what to put it's for every fucking backends
@app.route("/CheckForAntiCheat", methods= ["POST", "GET"])
def CheckForAntiCheat():
getjson = request.get_json()
UserId = getjson.get("UserId")
CustomID = getjson.get("CustomId")
if CustomID == "OCULUS0"
ban_response = requests.post(
BanUrl,
headers={"X-SecretKey": PlayFabKey},
json={
"Bans": [{"PlayFabId": UserId, "DurationInHours": "672", "Reason": "CHEATING."}]
}
@app.route("/CheckForBadName", methods=["POST","GET"])
def cfbn():
    name = request.args.get('name')
    BadNames = [
        "KKK", "PENIS", "NIGG", "NEG", "NIGA", "MONKEYSLAVE", "SLAVE", "FAG", 
        "NAGGI", "TRANNY", "QUEER", "KYS", "DICK", "PUSSY", "VAGINA", "BIGBLACKCOCK", 
        "DILDO", "HITLER", "KKX", "XKK", "NIGA", "NIGE", "NIG", "NI6", "PORN", 
        "JEW", "JAXX", "TTTPIG", "SEX", "COCK", "CUM", "FUCK", "PENIS", "DICK", 
        "ELLIOT", "JMAN", "K9", "NIGGA", "TTTPIG", "NICKER", "NICKA", 
        "REEL", "NII", "@here", "!", " ", "JMAN", "PPPTIG", "CLEANINGBOT", "JANITOR", "K9", 
        "H4PKY", "MOSA", "NIGGER", "NIGGA", "IHATENIGGERS", "@everyone", "TTT", "GOODDICK"
    ];
    if name not in BadNames:result = 0
    else: result = 2
    return jsonify({"Message":"the name thingy worked!","Name":name,"Result":result})
     
    @app.route("/photon", methods=["POST", "GET"])
    def PhotonAuthBruh():
    getjson = request.get_json()
    ticket = getjson.get("Ticket")
    nonce = getjson.get("Nonce")
    titleid = getjson.get("AppId")
    platform = getjson.get("Platform")
    user_id = getjson.get("UserId")
    appversion = getjson.get("AppVersion")
    token = getjson.get("Token")
    username = getjson.get("username")
    if nonce is None:return jsonify({'Error': 'Bad request', 'Message': 'scaruy auther'}), 304
    if titleid != 'titleidhere':return jsonify({'Error': 'Bad request', 'Message': 'Invalid titleid!'}), 403
    if platform != 'Quest':return jsonify({'Error': 'Bad request', 'Message': 'cheeyaj'}), 403
    return jsonify({"ResultCode":1, "StatusCode":200, "Message":"gfrthbtrhteh", "Result": 0, "UserId": user_id, "AppId":titleid, "AppVersion":appversion, "Ticket":ticket, "Token":token, "Nonce":nonce, "Platform":platform, "Username":username}), 200

    @app.route("/pepebut", methods=["POST", "GET"])
    def pepebut():
    getjson = request.get_json()["FunctionResult"]
    return jsonify(getjson)

    @app.route("/api/GetAcceptedAgreements", methods = ["POST", "GET"])
    def getacceptedagreements():
    rjson = request.get_json()["FunctionResult"]

    return jsonify(rjson)

   @app.route("/api/SubmitAcceptedAgreements", methods = ["POST", "GET"])
    def submitacceptedagreements():
    rjson = request.get_json()["FunctionResult"]

    return jsonify(rjson)

    def NonceValid(nonce: str, OculusID: str):
    req = requests.post(
        url=f'https://graph.oculus.com/user_nonce_validate?nonce=' + nonce +
        '&user_id=' + OculusID + '&access_token=' + settings.ApiKey,
        headers={"content-type": "application/json"})
    return req.json().get("is_valid")


  if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)



