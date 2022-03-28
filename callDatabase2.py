import sqlite3 as sql
# import csv

global connection
global cursor

connection = sql.connect('aircraftDB', check_same_thread=False)
cursor = connection.cursor()

# class Aircraft():
#     def __init__(self, evID, aircraftKey, regisNo, ntsbNo, aircraftMissing, farPart, flightPlanFilled, flightPlanActive, damage, aircraftFire, aircraftExpl, make, model, series, serialNo, certMaxGrWt, category, acftRegCls, homebuilt	, fcSeats, ccSeats, paxSeats, totalSeats, numEng, fixedRetractable, typeLastInsp, dateLastInsp, afmHrsLastInsp, afmHrs, eltInstall, eltOper, eltAidedLocEv, eltType, ownerAircraft, ownerStreet, ownerCity, ownerState, ownerCountry, ownerZip, operIndividualName, operName, operSame, operDba, operAddrSame, operStreet, operCity, operState, operCountry, operZip, operCode, certsHeld, oprtngCert, operCert, operCertNum, operSched, operDomInt, operPaxCargo, typeFly, secondPilot, dprtPtSameEv, dprtAptId, dprtCity, dprtState, dprtCountry, dprtTime, dprtTimezn, destSameLocal, destAptId, destCity, destState, destCountry, phaseFltSpec, reportToIcao, Evacuation, lchgDate, lchgUserid, afmHrsSince, rwyNum, rwyLen, rwyWidth, siteSeeing, airMedical, medTypeFlight, acftYear, fuelOnBoard, commercialSpaceFlight, unmanned, ifrEquippedCert, eltMountedAircraft, eltConnectedAntenna, eltManufacturer, eltModel, eltReasonOther):
#         self.evID = evID
#         self.aircraftKey = aircraftKey
#         self.regisNo = regisNo
#         self.ntsbNo = ntsbNo
#         self.aircraftMissing = aircraftMissing
#         self.farPart = farPart
#         self.flightPlanFilled = flightPlanFilled
#         self.flightPlanActive = flightPlanActive
#         self.damage = damage
#         self.aircraftFire = aircraftFire
#         self.aircraftExpl = aircraftExpl
#         self.make = make
#         self.model = model
#         self.series = series
#         self.serialNo = serialNo
#         self.certMaxGrWt = certMaxGrWt
#         self.category = category
#         self.acftRegCls = acftRegCls
#         self.homebuilt = homebuilt
#         self.fcSeats = fcSeats
#         self.ccSeats = ccSeats
#         self.paxSeats = paxSeats
#         self.totalSeats = totalSeats
#         self.numEng = numEng
#         self.fixedRetractable = fixedRetractable
#         self.typeLastInsp = typeLastInsp
#         self.dateLastInsp = dateLastInsp
#         self.afmHrsLastInsp = afmHrsLastInsp
#         self.afmHrs = afmHrs
#         self.eltInstall = eltInstall
#         self.eltOper = eltOper
#         self.eltAidedLocEv = eltAidedLocEv
#         self.eltType = eltType
#         self.ownerAircraft = ownerAircraft
#         self.ownerStreet = ownerStreet
#         self.ownerCity = ownerCity
#         self.ownerState = ownerState
#         self.ownerCountry = ownerCountry
#         self.ownerZip = ownerZip
#         self.operIndividualName = operIndividualName
#         self.operName = operName
#         self.operSame = operSame
#         self.operDba = operDba
#         self.operAddrSame = operAddrSame
#         self.operStreet = operStreet
#         self.operCity = operCity
#         self.operState = operState
#         self.operCountry = operCountry
#         self.operZip = operZip
#         self.operCode = operCode
#         self.certsHeld = certsHeld
#         self.oprtngCert = oprtngCert
#         self.operCert = operCert
#         self.operCertNum = operCertNum
#         self.operSched = operSched
#         self.operDomInt = operDomInt
#         self.operPaxCargo = operPaxCargo
#         self.typeFly = typeFly
#         self.secondPilot = secondPilot
#         self.dprtPtSameEv = dprtPtSameEv
#         self.dprtAptId = dprtAptId
#         self.dprtCity = dprtCity
#         self.dprtState = dprtState
#         self.dprtCountry = dprtCountry
#         self.dprtTime = dprtTime
#         self.dprtTimezn = dprtTimezn
#         self.destSameLocal = destSameLocal
#         self.destAptId = destAptId
#         self.destCity = destCity
#         self.destState = destState
#         self.destCountry = destCountry
#         self.phaseFltSpec = phaseFltSpec
#         self.reportToIcao = reportToIcao
#         self.Evacuation = Evacuation
#         self.lchgDate = lchgDate
#         self.lchgUserid = lchgUserid
#         self.afmHrsSince = afmHrsSince
#         self.rwyNum = rwyNum
#         self.rwyLen = rwyLen
#         self.rwyWidth = rwyWidth
#         self.siteSeeing = siteSeeing
#         self.airMedical = airMedical
#         self.medTypeFlight = medTypeFlight
#         self.acftYear = acftYear
#         self.fuelOnBoard = fuelOnBoard
#         self.commercialSpaceFlight = commercialSpaceFlight
#         self.unmanned = unmanned
#         self.ifrEquippedCert = ifrEquippedCert
#         self.eltMountedAircraft = eltMountedAircraft
#         self.eltConnectedAntenna = eltConnectedAntenna
#         self.eltManufacturer = eltManufacturer
#         self.eltModel = eltModel
#         self.eltReasonOther = eltReasonOther
#     def getAsList(self):
#         return [self.evID, self.aircraftKey, self.regisNo, self.ntsbNo, self.aircraftMissing, self.farPart, self.flightPlanFilled, self.flightPlanActive, self.damage, self.aircraftFire, self.aircraftExpl, self.make, self.model, self.series, self.serialNo, self.certMaxGrWt, self.category, self.acftRegCls, self.homebuilt, self.fcSeats, self.ccSeats, self.paxSeats, self.totalSeats, self.numEng, self.fixedRetractable, self.typeLastInsp, self.dateLastInsp, self.afmHrsLastInsp, self.afmHrs, self.eltInstall, self.eltOper, self.eltAidedLocEv, self.eltType, self.ownerAircraft, self.ownerStreet, self.ownerCity, self.ownerState, self.ownerCountry, self.ownerZip, self.operIndividualName, self.operName, self.operSame, self.operDba, self.operAddrSame, self.operStreet, self.operCity, self.operState, self.operCountry, self.operZip, self.operCode, self.certsHeld, self.oprtngCert, self.operCert, self.operCertNum, self.operSched, self.operDomInt, self.operPaxCargo, self.typeFly, self.secondPilot, self.dprtPtSameEv, self.dprtAptId, self.dprtCity, self.dprtState, self.dprtCountry, self.dprtTime, self.dprtTimezn, self.destSameLocal, self.destAptId, self.destCity, self.destState, self.destCountry, self.phaseFltSpec, self.reportToIcao, self.Evacuation, self.lchgDate, self.lchgUserid, self.afmHrsSince, self.rwyNum, self.rwyLen, self.rwyWidth, self.siteSeeing, self.airMedical, self.medTypeFlight, self.acftYear, self.fuelOnBoard, self.commercialSpaceFlight, self.unmanned, self.ifrEquippedCert, self.eltMountedAircraft, self.eltConnectedAntenna, self.eltManufacturer, self.eltModel, self.eltReasonOther]

# def initializeDB():
#     global connection
#     global cursor 
#     connection = sql.connect(':memory:')
#     cursor = connection.cursor()
#     createDBTables()
    
# def createDBTables():
#     cursor.execute("""CREATE TABLE aircraft(
#             evID, 
#             aircraftKey, 
#             regisNo, 
#             ntsbNo, 
#             aircraftMissing, 
#             farPart, 
#             flightPlanFilled, 
#             flightPlanActive, 
#             damage, 
#             aircraftFire, 
#             aircraftExpl, 
#             make, 
#             model, 
#             series, 
#             serialNo, 
#             certMaxGrWt, 
#             category, 
#             acftRegCls, 
#             homebuilt, 
#             fcSeats, 
#             ccSeats, 
#             paxSeats, 
#             totalSeats, 
#             numEng, 
#             fixedRetractable, 
#             typeLastInsp, 
#             dateLastInsp, 
#             afmHrsLastInsp, 
#             afmHrs, 
#             eltInstall, 
#             eltOper, 
#             eltAidedLocEv, 
#             eltType, 
#             ownerAircraft, 
#             ownerStreet, 
#             ownerCity, 
#             ownerState, 
#             ownerCountry, 
#             ownerZip,
#             operIndividualName,
#             operName, 
#             operSame,
#             operDba,
#             operAddrSame,
#             operStreet,
#             operCity,
#             operState, 
#             operCountry, 
#             operZip,
#             operCode, 
#             certsHeld, 
#             oprtngCert, 
#             operCert, 
#             operCertNum, 
#             operSched,
#             operDomInt,
#             operPaxCargo,
#             typeFly, 
#             secondPilot, 
#             dprtPtSameEv, 
#             dprtAptId, 
#             dprtCity, 
#             dprtState, 
#             dprtCountry, 
#             dprtTime, 
#             dprtTimezn,
#             destSameLocal,
#             destAptId, 
#             destCity,
#             destState,
#             destCountry,
#             phaseFltSpec,
#             reportToIcao,
#             Evacuation,
#             lchgDate,
#             lchgUserid,
#             afmHrsSince, 
#             rwyNum,
#             rwyLen, 
#             rwyWidth, 
#             siteSeeing, 
#             airMedical,
#             medTypeFlight,
#             acftYear, 
#             fuelOnBoard, 
#             commercialSpaceFlight,
#             unmanned,
#             ifrEquippedCert,
#             eltMountedAircraft,
#             eltConnectedAntenna,
#             eltManufacturer,
#             eltModel, 
#             eltReasonOther
#             );""")

# def populateAircraftRow(row):
#     air = Aircraft(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49], row[50], row[51], row[52], row[53], row[54], row[55], row[56], row[57], row[58], row[59], row[60], row[61], row[62], row[63], row[64], row[65], row[66], row[67], row[68], row[69], row[70], row[71], row[72], row[73], row[74], row[75], row[76], row[77], row[78], row[79], row[80], row[81], row[82], row[83], row[84], row[85], row[86], row[87], row[88], row[89], row[90], row[91], row[92])
#     cursor.execute("INSERT INTO aircraft VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", air.getAsList())

# def populateDB():
#     with open('aircraft.csv', encoding='latin') as inFile:
#         reader = csv.reader(inFile)
#         next(reader)
#         for rec in reader:
#             populateAircraftRow(rec)

# def initializeDB():
#     global connection
#     global cursor 
#     connection = sql.connect('aircraftDB', check_same_thread=False)
#     cursor = connection.cursor()


# def callDatabase(state):
#     displayState(state)

def display(city, state):
    input = (city, state)
    cursor.execute("SELECT * FROM events WHERE ev_city = ? AND ev_state = ?;", input)
    result = cursor.fetchall()  
    
    print(result)
    return result
    # for names in result:
    #     print("\n    ", names[0])

#initializeDB()
#populateDB()
#displayState()
#connection.close()