#比较两个文件的不同
import filecmp

def compareFile(filea,fileb):
    if not filecmp.cmp(filea,fileb):
        readfilea = open(filea,'r')
        readfileb = open(fileb,'r')
        while True:
            linefilea = readfilea.readline().strip()
            linefileb = readfileb.readline().strip()
            if linefilea and linefileb:
                if linefilea != linefileb:
                    print('有不同! 前者内容为：', linefilea, '后者内容为：', linefileb)
            else:
                break
        readfilea.close()
        readfileb.close()
    else:
        print('服务返回字段都相同')

compareFile(r'.\MomentsAfter.txt', r'.\MomentsBefore.txt')

with open('.\Test.txt', 'r') as f:
    while True:
        lastitem = []
        firstitem = []
        fb = f.readline().strip().split()
        #print(fb[-1:-3:-1])
        if fb:
            lastitem.extend(fb[-1:-3:-1])
            firstitem.extend(fb[-3::-1])
            print(lastitem)
            print(firstitem)
        else:
            break
