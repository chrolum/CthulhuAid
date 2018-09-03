# -*- coding: utf-8 -*-
import re
import configparser

"""
To-do-list:
1.Configuration: base on a configuration file to control the status of filter function(include name, keyword, command and plot)

2.optimize the process_filter(), make it more fixable ,which should add or delet the filter function more simply

3.compete the unit test(learn how to write a unit test and when should i use it)
"""

class cocLog:
    def __init__(self, inputFilePath):
        self.inputFilePath = inputFilePath
        self.log = self.readLog()
        self.regex = {'nameRegex': r'\:[0-9][0-9] (.*?)\(', 'majorRoleRegex': r'\:(*?)\n'}
        self.filterGameRole = ['跑团用小号', '系统消息','神北小毯']
        self.command_flag = ['.', '/']
        self.keyWord = ['[表情]', '[图片]']

    def readLog(self):
        log = []
        with open(self.inputFilePath, 'rU', encoding='utf-8', newline='\r\n') as f:
            while True:
                msg = []
                line = f.readline()
                if not line:
                    break
                msg.append(line)
                for i in range(0,2):
                    msg.append(f.readline())#msg = [name, msg, noValue]
                log.append(msg)
        return log

    def process_RawLog(self):
        rawLog = []
        for nameLine, msgLine, noValueLine in self.log:
            name = re.findall(re.compile(self.regex['nameRegex']), nameLine)
            rawLog.append(aMsg(name[0], msgLine))#rawLog is a aMsg object list
        return rawLog

    def resPrinter(self, msgArr, outPutPath='output.txt'): # a aMsg object list
        file = open(outPutPath, 'w')
        for msg in msgArr:
            file.write('<'+ msg.name + '>' + msg.msg)
        file.close()

    def process_filter(self, msgSaveJudage, msgFilter): #two para are the list of func
        '''
        this function have two base fuction :
        1.bool return value to judage the msg weather save
        2.filter the str with special condition
        :param msgSaveJudage:
        :param msgFilter:
        :return:
        '''
        tmp = []
        for msg in msgArr:
            if msgSaveJudage[0](msg) or msgSaveJudage[1](msg) or msgSaveJudage[2](msg):
                pass
            else:
                for func in msgFilter:
                    msg.msg = func(msg.msg)
                tmp.append(msg)
        return tmp

    def filter_name(self, msg_name):
        if msg_name in self.filterGameRole:
            return True
        else:
            return False

    def filter_keyword(self, rawStr):
        str = rawStr
        for keyword in self.keyWord:
            str = str.replace(keyword, '')
        return str

    def filter_command(self, str):
        if str[0] in self.command_flag:# a command is a string that begins with '.' or '/'
            return True
        else:
            return False

    def filter_plot(self, str): #save the msg with flag ':'
        if str[0] == ':':
            return True
        else:
            return False

    def unitTest(self):
        pass

    # def process_conf_filter(self, conf):

    # def readConfiguration(self):


class aMsg:
    def __init__(self, name = 'NA', msg = 'NA'):
        self.name = name
        self.msg = msg

class MsgFilter:
    def __init__(self):
        self.configuration = self.readConfiguration()
    def readConfiguration(self):
        confPath = 'conf.ini'
        config = configparser.ConfigParser()
        config.read(confPath)
    def process_filter(self):


if __name__ == '__main__':
    log = cocLog('inputFile.txt')
    raw = log.process_RawLog()
    res = log.process_filter(raw)
    log.resPrinter(res, 'raw.txt')
