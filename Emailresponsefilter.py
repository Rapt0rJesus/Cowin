
def getAllCenters(response):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        for session in center["sessions"]:
            if session["available_capacity"]!=0:
                if session["date"] in dateCenterdict:
                    dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"],session["min_age_limit"],center['fee_type']])
                else:
                    dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"],session["min_age_limit"],center['fee_type']]]
    return(dateCenterdict)

def getAgeBasedCenters(response,age):
    response=response.json()
    listofCenters=[]
    centers=response["centers"]
    dateCenterdict={}
    for center in centers:
        for session in center["sessions"]:
            if session["min_age_limit"]==age and session["available_capacity"]!=0:
                if session["date"] in dateCenterdict:
                    dateCenterdict[session["date"]].append([center["name"],session["vaccine"],session["available_capacity"],center['fee_type']])
                else:
                    dateCenterdict[session["date"]]=[[center["name"],session["vaccine"],session["available_capacity"],center['fee_type']]]
    return(dateCenterdict)