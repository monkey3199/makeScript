import os, re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    constMap = {
        'HEADER': HEADER,
        'OKBLUE': OKBLUE,
        'OKGREEN': OKGREEN,
        'WARNING': WARNING,
        'FAIL': FAIL,
        'ENDC': ENDC,
        'BOLD': BOLD,
        'UNDERLINE': UNDERLINE
    }

    @classmethod
    def get(cls, name):
        return cls.constMap[name]
    
    @classmethod
    def colorText(cls, text, colorClass):
        if (cls.get(colorClass) == ''):
            return text
        return cls.get(colorClass) + text + cls.ENDC



def search(dirname):
    filenames = os.listdir(dirname)
    fullFilenames = []
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        fullFilenames.append(full_filename)

    return fullFilenames

def extractText(filename):
    print ('start extract text... ', end = '')
    
    try:
        subcriptFile = open(filename, 'r')
        text = ''
        rmRegex = [
            '^[0-9]\n$'
        ]
        
        while True:
            line = subcriptFile.readline()
            if not line: break

            newline = line
            for reg in rmRegex:
                p = re.compile(reg)
                # p.sub('')
                    

        text = filename

        print(bcolors.colorText('Success!', 'OKGREEN'))
        return text
    
    except:
        print(bcolors.colorText('Failed!', 'FAIL'))
        return False

def refineText(text):
    newText = filename
    return newText

def makeNewFile(text, filename):
    newFile = filename
    return newFile


# start main
print ("Start The Program To Make Script!!!!")
subscriptFolder = './subscript'

for index, filename in enumerate(search(subscriptFolder)):
    print ('[%d] Start making script from [%s] ===========================' % (index+1, bcolors.colorText(filename, 'OKBLUE')))
    extractText(filename)
    # extractText('test')