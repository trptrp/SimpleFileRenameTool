# -*- coding: cp936 -*-
import sys
import os
import glob


def RenameFiles(path):
    i = 1
    #path = "F:\\f"
    file_name_collection = os.listdir(path)
    capacity = len(file_name_collection)
    ws = 1
    while(capacity >= 10):
        capacity = capacity/10;
        ws = ws+1;
    print ws
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file))==True:
            j = file.rindex('.')#get the dot in order to parse the file type name
            length = len(file)
            if file[j+1:length]=='py':
                continue
            ii=i
            while(ii >= 10):
                ii = ii/10;
                ws = ws-1;#i进位后生成正确的前置0的个数
            newname = '0'*ws + "%i"%i +'.' + file[j+1:length]
            i = i+1
            try:
                os.chdir(path)
                os.rename(file, newname)
                print '重命名 ' + file + ' to ' + newname + ' 成功'
            except:
                print '重命名 ' + file + ' to ' + newname + ' 失败'

def main(argv):
    fpath = os.path.abspath(os.path.dirname(__file__))
    #RenameFiles(path)
    print fpath
    RenameFiles(fpath)

if __name__ == '__main__':
    main(sys.argv)
    raw_input()



