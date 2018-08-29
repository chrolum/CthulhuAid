def creatDict(iniPath):
    confDict = {}
    f = open(iniPath, 'r')
    confs = f.readlines()
    for conf in confs:
        data = conf.split(':')
        confDict[data[0]] = int(data[1].rstrip())
    return confDict
if __name__ == '__main__':
    conf = creatDict('config.ini')
    # print(conf.items())