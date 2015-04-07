# -*- coding: cp936 -*-
import sys
import os
import glob


def RenameFiles(path, flag):
    time_file=[] 
    i = 1
    #path = "F:\\f"
    file_name_collection = os.listdir(path)
    capacity = len(file_name_collection)
    ws = 1
    while(capacity >= 10):
        capacity = capacity/10;
        ws = ws+1;
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file))==True:
            timeTemp = os.path.getmtime(file)
            time_file.append([timeTemp, file])
    if flag:
        time_file.sort()
    for file in time_file:
        filename = file[1]
        j = filename.rindex('.')#get the dot in order to parse the file type name
        length = len(filename)
        if filename[j+1:length]=='py':
            continue
        ii=i
        temp_ws = ws
        while(ii >= 10):
            ii = ii/10;
            temp_ws = temp_ws-1;#i进位后生成正确的前置0的个数
        newname = '0'*temp_ws + "%i"%i +'.' + filename[j+1:length]
        i = i+1
        try:
            os.chdir(path)
            os.rename(file[1], newname)
            print '重命名 ' + file[1] + ' to ' + newname + ' 成功'
        except:
            print '重命名 ' + file[1] + ' to ' + newname + ' 失败'


def main(argv):
    gc = raw_input("sort by time? y or n?")
    flag = False
    fpath = os.path.abspath(os.path.dirname(__file__))
    if gc == 'y':
        flag = True
    print fpath
    RenameFiles(fpath, flag)

if __name__ == '__main__':
    main(sys.argv)
    raw_input()
