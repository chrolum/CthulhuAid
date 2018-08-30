import re

class cocLog:
    def __init__(self, inputFilePath):
        self.inputFilePath = inputFilePath
        self.log = self.readLog()
        self.regex = {'nameRegex': r'\:[0-9][0-9] (.*?)\(', 'majorRoleRegex': r'\:(*?)\n'}

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

    def resPrinter(self, msgArr, outPutPath): # a aMsg object array
        file = open(outPutPath, 'w')
        for msg in msgArr:
            file.write('<'+ msg.name + '>' + msg.msg)
        file.close()

    def process_filter(self, msgArr, filter_name = True, filter_keyword = True, filter_command = True):
        if filter_name:
            pass
        if filter_command:
            pass
        if filter_keyword:
            pass
        for msg in msgArr:
            if (msg.name in Name):
                pass
            else:
                tmp.append(msg)
        return tmp

    def filter_name(self, msg_name):
        '''
        judge a name whether has been include in the filter name list
        :return: bool
        '''

    def filter_keyword(self, str):
        '''
        try to match the keyword in str, if the str only has the keyword
        :return: filtered str
        '''

    def filter_command(self, str):
        '''

        :param str:
        :return:
        '''

    def unitTest(self):
        pass

class aMsg:
    def __init__(self, name = 'NA', msg = 'NA'):
        self.name = name
        self.msg = msg

if __name__ == '__main__':
    res = cocLog('inputFile.txt')
    raw = res.process_RawLog()
    filterName = ['系统消息', '跑团用小号']
    name_filter = res.process_filter(raw, filterName)
    res.resPrinter(name_filter, 'raw.txt')
