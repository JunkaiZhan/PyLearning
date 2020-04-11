#!/usr/bin/python3

# Author : zhanjunkai
# Date   : 2019/09/08

from klib import ktp
import re
import openpyxl
import smtplib
import os
import shutil

from email.mime.text import MIMEText

# =============================================================
# Function    : replace_in_file(file_name, pattern, new_string)
# Description : Replace the string which are matched by the
#               pattern with the new string in file
# =============================================================
def replace_in_file(file_name, pattern, new_string):
    ktp.check_file(file_name)
    file_in     = open(file_name, 'r')
    content     = file_in.read()
    content     = re.sub(pattern, new_string, content)
    file_out    = open(file_name, 'w')
    file_out.write(content)
    file_in.close()
    file_out.close()

# =============================================================
# Function    : delete_in_file(file_name, pattern)
# Description : Delete the string which are matched by the
#               pattern with the new string in file
# =============================================================
def delete_in_file(file_name, pattern):
    replace_in_file(file_name, pattern, '')

# =================================================================================
# Function    : send_email(text, dst_mailbox, mailserver, port, src_mailbox, passwd)
# Description : sent text from src_mailbox on mailserver.port to 
#               dst_mailbox
# =================================================================================
def send_email(subject, ext, dst_mailbox, src_mailbox, passwd, mailserver='smtp.163.com', port=25):
    smtpobj = smtplib.SMTP(mailserver, port)
    smtpobj.login(src_mailbox, passwd)
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = src_mailbox
    msg['To'] = dst_mailbox
    msg['Subject'] =  subject
    status = smtpobj.sendmail(src_mailbox, [dst_mailbox], msg.as_string())
    if status != {}:
        print('Error occured: From %s to %s, Status is %s' % (src_mailbox, dst_mailbox, status))
    else:
        print('The email is sent successfully from %s to %s' % (src_mailbox, dst_mailbox))
    smtpobj.quit()

# ========================================================
# Function    : organize_file_into_folder(file_type, path)
# Description : organize the file in file_type in path
#               into the folder or subfolder with the 
#               same name
# ======================================================== 
def organize_file_into_folder(file_type, path):
    os.chdir(path)
    files = []
    for obj in os.listdir():
        if obj.endswith(file_type):
            files.append(obj.split('.')[0])
    print("The files organized in %s are: " % path)
    print(files)
    for folder_name, subfolders, filenames in os.walk(path):
        current_folder = folder_name.split(os.path.sep)[-1]
        if current_folder in files:
            file_name = current_folder + "." + file_type
            shutil.move(file_name, folder_name)
            print("I have moved the file: %s into folder: %s" % (file_name, folder_name))

# =======================================================================
# Function    : cp_dir(src_dir, dst_dir)
# Description : copy the whole srouce directory to destination directory
# ========================================================================
def cp_dir(src_dir, dst_dir):
    # check if need create the dst_dir
    shutil.copytree(src_dir, dst_dir)

# =====================================================
# Function    : rm_file(file_path)
# Description : delete the file_path
# ===================================================== 
def rm_file(file_path):
    os.unlink(file_path)

# =====================================================
# Function    : rm_file_in_path(path, type)
# Description : delete the files of type in path 
# ===================================================== 
def rm_file_in_path(path, type):
    current_dir = os.getcwd()
    os.chdir(path)
    for file_name in os.listdir():
        if file_name.endswith("." + type):
            os.unlink(file_name)
            print(">>> Delete the file: " + path + file_name)
    os.chdir(current_dir)

# =====================================================
# Function    : rm_dir(path)
# Description : delete the whole path
# ===================================================== 
def rm_dir(path):
    # check if the path exists
    shutil.rmtree(path)

