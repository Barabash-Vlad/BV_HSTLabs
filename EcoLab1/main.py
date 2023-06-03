
import random
import time



n = 5
Timing = 2000
SensorPrior = [0, 5, 1, 2, 3]
SensorIntervals = [5, 3, 4, 2, 7]
ULimit = []
LLimit = []
buff = []
itemData = []
limitData = []
dataSet = []
timeData = []

lowerLimitArr = 45
upperLimitArr = 65

testByPriority = False
testByInterval = False

with open("maindata.txt", "w") as file:
    pass
with open("sensordata.txt", "w") as file:
    pass
with open("overvalue.txt", "w") as file:
    pass
main_data = []

class Sensor:
    def __init__(self, label, data, priority, interval, overLimitData, timeData):
        self.label = label
        self.data = data
        self.priority = priority
        self.interval = interval
        self.overLimitData = overLimitData
        self.timeData = timeData

    def testItem(self):

        itemIndex = int(self.label[7]) - 1
        itemValue = self.getRandNumb(LLimit[itemIndex] - buff[itemIndex], ULimit[itemIndex] + buff[itemIndex])
        #print(f"Тестування {itemIndex + 1}-го сенсора... Значення: {itemValue}")
        main_data.append(f"Тестування {itemIndex + 1}-го сенсора... Значення: {itemValue}")
        with open("maindata.txt", "a") as file:
            file.write(str(main_data) + "\n")
        main_data.clear()
        if itemValue < LLimit[itemIndex] or itemValue > ULimit[itemIndex]:
            #print(f"Значення Сенсора {itemIndex + 1} перевисило допустимий ліміт!")
            main_data.append(f"Значення Сенсора {itemIndex + 1} перевисило допустимий ліміт!")
            with open("maindata.txt", "a") as file:
                file.write(str(main_data) + "\n")
            main_data.clear()
            limitData[itemIndex].append(itemValue)
            timeData[itemIndex].append(self.getTime())
        itemData[itemIndex].append(itemValue)

    @staticmethod
    def getRandNumb(min, max):
        return random.uniform(min, max)

    @staticmethod
    def getTime():
        now = time.localtime()
        timeString = time.strftime("%H:%M:%S", now)
        return timeString


def InitializeOptions():
    for i in range(n):
        itemData.append([])
        limitData.append([])
        timeData.append([])
        label = f"Sensor {i + 1}"
        dataValues = itemData[i]
        priority = SensorPrior[i]
        interval = SensorIntervals[i]
        overLimitData = limitData[i]
        sensor = Sensor(label, dataValues, priority, interval, overLimitData, [])
        dataSet.append(sensor)
        ULimit.append(upperLimitArr)
        LLimit.append(lowerLimitArr)
        buff.append(0.5)


def testItemAllSensors():
    if testByPriority:
        sensorstestByPriority = sorted(dataSet, key=lambda x: x.priority)
        for sensor in sensorstestByPriority:
            sensor.testItem()
    elif testByInterval:
        for i, sensor in enumerate(dataSet):
            interval = sensor.interval * 1000
            while True:
                sensor.testItem()
                time.sleep(interval)
    else:
        for sensor in dataSet:
            sensor.testItem()


def printitemData():
    with open("sensordata.txt", "w") as file:
        pass
    for i in range(n):
        #print(f"Сенсор {i + 1} дані: {', '.join(str(x) for x in itemData[i])}")
        main_data.append(f"Сенсор {i + 1} дані: {', '.join(str(x) for x in itemData[i])}")
        with open("sensordata.txt", "a") as file:
            file.write(str(main_data) + "\n")
        main_data.clear()


def printOverLimitData():
    with open("overvalue.txt", "w") as file:
        pass
    for i in range(n):
        #print(f"Сенсор {i + 1} перевисив допустимі значення:")
        main_data.append(f"Сенсор {i + 1} перевисив допустимі значення:")
        with open("sensordata.txt", "a") as file:
            file.write(str(main_data) + "\n")
        main_data.clear()
        for j in range(len(limitData[i])):
            #print(f"Значення: {limitData[i][j]}  в: {timeData[i][j]}")
            main_data.append(f"Значення: {limitData[i][j]}  в: {timeData[i][j]}")
            with open("overvalue.txt", "a") as file:
                file.write(str(main_data) + "\n")
            main_data.clear()



def ChangePrior():
    global testByPriority
    testByPriority = not testByPriority
    #print("Пріорітет змінено")


InitializeOptions()

def strtobool(text):
    if text == "True":
        return True
    elif text == "False":
        return False


def OpenFile(file):
    flag = strtobool(file.read())
    file.close()
    return flag

def FlagnotFlag(file):
    file.write(str(False))
    file.close()

def Start_Pr():
    if testByInterval:
        testItemAllSensors()
    else:
        Flag1 = Flag2 = Flag3 = False
        while True:
            testItemAllSensors()
            Flag1 = OpenFile(open("flag1.txt", "r"))
            Flag2 = OpenFile(open("flag2.txt", "r"))
            Flag3 = OpenFile(open("flag3.txt", "r"))
            if Flag1:
                printitemData()
                FlagnotFlag(open("flag1.txt", "w"))
            elif Flag2:
                printOverLimitData()
                FlagnotFlag(open("flag2.txt", "w"))
            elif Flag3:
                ChangePrior()
                FlagnotFlag(open("flag3.txt", "w"))
            time.sleep(Timing / 2000)


if __name__ == '__main__':
    Start_Pr()




