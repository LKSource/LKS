import xlwings as xw
import math
from dateutil.relativedelta import relativedelta
import pandas as pd

onRolePer = {}
offRolePer = {}
infyRolePer = {}
onInfyRolePer = {}
offInfyRolePer = {}
dealStartDate = ''
dealMonths = 0
transitionMonths = 0
steadyState = ''
onStaff = 0
offStaff = 0
onSite = "Onsite"
offShore = "Offshore"
piPer = {}
onsitePer = {}


def config(sheet):
    print(sheet.range(1, 1).value)
    iRow = 1
    iCol = 5
    global dealStartDate, dealMonths, transitionMonths, steadyState, onStaff, offStaff, onSite, offShore, piPer
    dealStartDate = sheet.range(1, 2).value
    dealMonths = sheet.range(2, 2).value
    transitionMonths = sheet.range(3, 2).value
    steadyState = sheet.range(4, 2).value
    onStaff = sheet.range(5, 2).value
    offStaff = sheet.range(6, 2).value

    iRow = 1
    iCol = 5
    while sheet.range(iRow, iCol).value is not None:
        #print(sheet.range(iRow, iCol).value)
        if sheet.range(iRow, iCol + 2).value != 0:
            if sheet.range(iRow, iCol).value == onSite:
                onRolePer[sheet.range(iRow, iCol + 1).value] = sheet.range(iRow, iCol + 2).value
            else:
                offRolePer[sheet.range(iRow, iCol + 1).value] = sheet.range(iRow, iCol + 2).value
        iRow += 1

    iRow = 1
    iCol = 10
    while sheet.range(iRow, iCol).value is not None:
        #print(sheet.range(iRow, iCol).value)
        if (sheet.range(iRow, iCol).value + sheet.range(iRow,
                                                        iCol + 1).value) not in infyRolePer.keys():  #
            infyRolePer[sheet.range(iRow, iCol).value + sheet.range(iRow, iCol + 1).value] = []
            infyRolePer[sheet.range(iRow, iCol).value + sheet.range(iRow, iCol + 1).value].append(
                [sheet.range(iRow, iCol + 2).value, sheet.range(iRow, iCol + 3).value,
                 sheet.range(iRow, iCol + 4).value])
        else:
            infyRolePer[sheet.range(iRow, iCol).value + sheet.range(iRow, iCol + 1).value].append(
                [sheet.range(iRow, iCol + 2).value, sheet.range(iRow, iCol + 3).value,
                 sheet.range(iRow, iCol + 4).value])

        iRow += 1

    iRow = 12
    iCol = 1
    per = 0
    while sheet.range(iRow, iCol).value is not None:
        #print(sheet.range(iRow, iCol).value)
        per += float(sheet.range(iRow, iCol + 1).value)
        piPer[sheet.range(iRow, iCol).value] = round(per, 2)
        iRow += 1

    print(piPer)

    iRow = 21
    iCol = 1
    per = 0
    while sheet.range(iRow, iCol).value is not None:
        #print(sheet.range(iRow, iCol).value)
        #per += float(sheet.range(iRow, iCol + 1).value)
        onsitePer[sheet.range(iRow, iCol).value] = sheet.range(iRow, iCol + 1).value
        iRow += 1


def effSplit(scount, location):
    staffing = {}
    effCount = scount
    if location == onSite:
        for key in onRolePer.keys():
            staffing[key] = math.ceil(onRolePer[key] * effCount)
            if key == 'Subcon': effCount = scount - staffing[key]
    else:
        for key in offRolePer.keys():
            staffing[key] = math.ceil(offRolePer[key] * effCount)
            if key == 'Subcon': effCount = scount - staffing[key]

    if sum(staffing.values()) - staffing['Subcon'] != effCount:
        if location == onSite:
            iKey = min([(key) for key in onRolePer.keys() if onRolePer[key] != 0])
            staffing[iKey] = staffing[iKey] + effCount - (sum(staffing.values()) - staffing['Subcon'])
        else:
            iKey = min([(key) for key in offRolePer.keys() if offRolePer[key] != 0])
            staffing[iKey] = staffing[iKey] + effCount - (sum(staffing.values()) - staffing['Subcon'])
    #print(min([(key) for key in onRolePer.keys() if onRolePer[key] != 0]))
    #print(staffing)
    #print(sum(staffing.values()))
    return staffing


def getPI(mon):
    key = list(piPer.keys())
    key = key[::-1]
    for i in key:
        if mon >= i: return piPer[i]
    return 0


def getOnsitePer(mon):
    key = list(onsitePer.keys())
    key = key[::-1]
    for i in key:
        if mon >= i: return onsitePer[i]
    return 0


def main():
    iExCol = 4
    iExRow = 2
    wk = xw.books.open(
        r'C:\Users\lingasamy_k\OneDrive - Infosys Limited\LINGAA\PythonProjects\pythonProject\DPSGen.xlsm')
    #wk = xw.books['DPSGen.xlsm']
    master_sheet = wk.sheets("Master")
    data_sheet = wk.sheets("Data")
    data_sheet.range((1, 1), (100, 100)).value = ""
    config(master_sheet)
#    for iRow in range(1, 10):
#        data_sheet.range(iRow, 1).value = iRow

    #Onsite
    for iCol in range(0, int (dealMonths - transitionMonths)):
        #print(dealStartDate + relativedelta(months=iCol - 1))
        iColn = iExCol + iCol + 1
        date_obj = pd.to_datetime((steadyState + relativedelta(months=iCol)))
        data_sheet.range(iExRow, iColn).value = date_obj.strftime('%b %Y')
        onOpt = (onStaff + offStaff) * getOnsitePer(iCol + 1)
        pi = getPI(iCol + 1)
        staffing = effSplit(math.ceil(onOpt * (1 - pi)), onSite)
        print(staffing)
        i = 1
        for key in staffing.keys():
            jl = onSite + key
            #print(onSite + key)
            #if jl in infyRolePer.keys() : print(infyRolePer[jl])
            if jl in infyRolePer.keys():
                if len(infyRolePer[jl]) == 1:
                    data_sheet.range(iExRow + i, iExCol - 2).value = jl
                    data_sheet.range(iExRow + i, iExCol - 1).value = infyRolePer[jl][0][0]
                    data_sheet.range(iExRow + i, iExCol).value = infyRolePer[jl][0][2]
                    data_sheet.range(iExRow + i, iColn).value = staffing[key]
                    i += 1
                else:
                    if len(infyRolePer[jl]) > 1:
                        sEffort = 0
                        for il in range(0, len(infyRolePer[jl])):
                            data_sheet.range(iExRow + i, iExCol - 2).value = jl
                            data_sheet.range(iExRow + i, iExCol - 1).value = infyRolePer[jl][il][0]
                            data_sheet.range(iExRow + i, iExCol).value = infyRolePer[jl][il][2]
                            sEffort += math.floor(infyRolePer[jl][il][1] * staffing[key])
                            if il == len(infyRolePer[jl]) - 1 and sEffort != staffing[key]:
                                data_sheet.range(iExRow + i, iColn).value = math.floor(
                                    infyRolePer[jl][il][1] * staffing[key]) + staffing[key] - sEffort
                            else:
                                data_sheet.range(iExRow + i, iColn).value = math.floor(
                                    infyRolePer[jl][il][1] * staffing[key])
                            i += 1
                #print(infyRolePer[jl])
                #print(jl + infyRolePer[jl][0][0])

    iExRow += i
    #Offshore
    for iCol in range(0, int (dealMonths - transitionMonths)):
        iColn = iExCol + iCol + 1
        offOpt = (onStaff + offStaff) * (1 - getOnsitePer(iCol + 1))
        pi = getPI(iCol + 1)
        staffing = effSplit(math.ceil(offOpt * (1 - pi)), offShore)
        i = 1
        for key in staffing.keys():
            jl = offShore + key
            #print(onSite + key)
            #if jl in infyRolePer.keys() : print(infyRolePer[jl])
            if jl in infyRolePer.keys():
                if len(infyRolePer[jl]) == 1:
                    data_sheet.range(iExRow + i, iExCol - 2).value = jl
                    data_sheet.range(iExRow + i, iExCol - 1).value = infyRolePer[jl][0][0]
                    data_sheet.range(iExRow + i, iExCol).value = infyRolePer[jl][0][2]
                    data_sheet.range(iExRow + i, iColn).value = staffing[key]
                    i += 1
                else:
                    if len(infyRolePer[jl]) > 1:
                        sEffort = 0
                        for il in range(0, len(infyRolePer[jl])):
                            data_sheet.range(iExRow + i, iExCol - 2).value = jl
                            data_sheet.range(iExRow + i, iExCol - 1).value = infyRolePer[jl][il][0]
                            data_sheet.range(iExRow + i, iExCol).value = infyRolePer[jl][il][2]
                            sEffort += math.floor(infyRolePer[jl][il][1] * staffing[key])
                            if il == len(infyRolePer[jl]) - 1 and sEffort != staffing[key]:
                                data_sheet.range(iExRow + i, iColn).value = math.floor(
                                    infyRolePer[jl][il][1] * staffing[key]) + staffing[key] - sEffort
                            else:
                                data_sheet.range(iExRow + i, iColn).value = math.floor(
                                    infyRolePer[jl][il][1] * staffing[key])
                            i += 1


if __name__ == '__main__':
    main()
