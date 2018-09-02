import re
import configparser
'''
1. sperate the filter fuction from cocLog class and make a new class filter
'''

class cocLog(object, MessageFilter):
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
                    msg.append(f.readline())#msg = [name, msg noValue]
                log.append(msg)
        return log

    def process_RawLog(self):
        rawLog = []
        for nameLine, msgLine, noValueLine in self.log:
            name = re.findall(re.compile(self.regex['nameRegex']), nameLine)
            rawLog.append(aMsg(name[0], msgLine))
        return rawLog

    def resPrinter(self, msgArr, outPutPath='output.txt'): # a aMsg object array
        file = open(outPutPath, 'w')
        for msg in msgArr:
            file.write('<'+ msg.name + '>' + msg.msg)
        file.close()

    def process_filter(self, msgArr): #filter_name = False, filter_keyword = False, filter_command = False
        tmp = []
        for msg in msgArr:
            if self.filter_name(msg.name) or self.filter_command(msg.msg):
                pass
            else:
                msg.msg = self.filter_keyword(msg.msg)
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
        command_flag = ['.', '/']
        if str[0] in command_flag:
            return True
        else:
            return False

    def unitTest(self):

class aMsg:
    def __init__(self, name = 'NA', msg = 'NA'):
        self.name = name
        self.msg = msg

class MessageFilter:
    def __init__(self):
        self.regex = {'nameRegex': r'\:[0-9][0-9] (.*?)\('}
        self.config = configparser.ConfigParser().read('config.ini')

    def process(self, msgList):# msgList is a message object list



if __name__ == '__main__':
    log = cocLog('inputFile.txt')
    raw = log.process_RawLog()
    res = log.process_filter(raw)
    log.resPrinter(res, 'raw.txt')
