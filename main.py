from os import listdir, path, makedirs, rename

#Directory to sort
directory = raw_input("Enter Folder : ")

#To make sure that the directory ends with a '/'
if not directory.endswith('/'):
    directory += '/'

#General File Type Extentions
exts = {
"Applications": ['.exe'],
"Code": ['.py','.java','.c','.cpp','.rb','.asm','.php','.html','.css','.js','.lua','.jar','.o','.obj'],
"Music": ['.mp3','.ogg','.wav'],
"Videos": ['.mp4','.3gp','.avi'],
"Pictures": ['.jpg','.jpeg','.png','.bmp','.gif'],
"Archives": ['.zip','.rar','.7zip','.tar','.iso'],
"Documents": ['.docx','.doc','.pdf','.txt','.ppt','.pptx','.ppsx','.pptm',
             '.docm','.dotx','.dotm','.docb','.xlsx','.xlsm','.xltx',
             '.xltm','.xlsb','.xla','.xlam','.xll','.xlw',
             '.ACCDB','.ACCDE','.ACCDT','.ACCDR','.pub',
             '.potx','.potm','.ppam','.ppsm','.sldx','.sldm']
}

#Check each file in the directory
for fil in listdir(directory):
    for typ,lis in exts.iteritems():
        for ex in lis:
            if fil.endswith(ex) or fil.endswith(ex.upper()):
                if not path.exists(directory+typ+'/'):
                    makedirs(directory+typ+'/')
                rename(directory+fil, directory+typ+'/'+fil)
                print fil + " : " + typ

print ""
print "How to Find What We Organised:"
print "Code Folder         - Contains Code, Object Files and jar Files."
print "Music Folder        - Contains Audio Files."
print "Videos Folder       - Contains Video Files."
print "Pictures Folder     - Contains Image Files."
print "Archives Folder     - Contains rar/zip Files and Other Archives."
print "Documents Folder    - Contains Powerpoint and Documents from MS Office."
print "Applications Folder - Contains applications and executable programs."
print "Other Folder        - Contains files that were not sorted into a folder."
