import os, re
from docx import Document
from docx.shared import Inches

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
    fileInfos = []
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        fileInfo = {
            'name': filename,
            'fullPath': full_filename
        }
        fileInfos.append(fileInfo)

    return fileInfos

def extractText(filename):
    print ('start extract text... ', end = '')
    
    try:
        subcriptFile = open(filename, 'r')
        text = filename + '\n\n'
        rmRegex = { 
            '^\d\n$': '',
            '^\d{2}:\d{2}:\d{2},\d+ --> \d{2}:\d{2}:\d{2},\d+$': '',
            '<.*?>': '',
            '^\n$': ''
        }
        
        while True:
            line = subcriptFile.readline()
            if not line: break

            newLine = line
            for reg in list(rmRegex.keys()):
                p = re.compile(reg)
                newLine = p.sub(rmRegex[reg], newLine)

            if newLine: newLine += '\n'
            text += newLine

        print(bcolors.colorText('Success!', 'OKGREEN'))
        return text
    
    except:
        print(bcolors.colorText('Failed!', 'FAIL'))
        return False

# def refineText(text):
#     newText = filename
#     return newText

def makeNewFile(text, filename):
    print ('start make word file... ', end = '')

    try:
        document = Document()
        document.add_paragraph(text)
        document.add_page_break()
        document.save(filename+'.docx')
        
        print(bcolors.colorText('Success!', 'OKGREEN'))
        return document
    except:
        print(bcolors.colorText('Failed!', 'FAIL'))
        return False


# start main
print ("Start The Program To Make Script!!!!")
subscriptFolder = './subscript'

for index, fileinfo in enumerate(search(subscriptFolder)):
    print ('[%d] Start making script from [%s] ===========================' % (index+1, bcolors.colorText(fileinfo['fullPath'], 'OKBLUE')))
    
    makeNewFile(extractText(fileinfo['fullPath']), 'script/'+fileinfo['name'])
