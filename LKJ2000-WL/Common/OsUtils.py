# -*- coding: utf-8 -*-
import os
import binascii
import datetime
import re
import serial

def dict_entry_inc(dict, key):
    if key in dict.keys():
        dict[key] += 1
    else:
        dict[key] = 1

# "\0x12x34\0x56\0x78\0x9A\0xBC" => "12 34 56 78 9A BC"
def binstr_to_hexstr(arg):
    result = ''
    hLen = len(arg)
    for i in range(hLen):
        hvol = ord(arg[i])
        hhex = '%02X'%hvol
        result += hhex+' '
    return result

# "\0x12x34\0x56\0x78\0x9A\0xBC" => [0x12, 0x34, 0x56, 0x78]
def binstr_to_int_list(arg):
    result = []
    hLen = len(arg)
    for i in range(hLen):
        val = ord(arg[i])
        result.append(val)
    return result

# [0x12, 0x34, 0x56, 0x78] => "\0x1200x34\0x56\0x78\0x9A\0xBC"
def int_list_to_binstr(int_list):
    result = bytearray(int_list)
    return result

# "12 34 56 78 9A BC" => [0x12, 0x34]
def hexstr_to_int_list(arg):
    result = []
    arg = arg.replace(' ','')
    hLen = len(arg)
    for i in range(hLen//2):
        val = int(arg[i*2:i*2+2], 16)
        result.append(val)
    return result

# "12 34 56 78 9A BC" => "\0x1200x34\0x56\0x78\0x9A\0xBC"
def hexstr_to_binstr(hex_list):
    int_list = hexstr_to_int_list(hex_list)
    result = bytearray(int_list)
    return result

# [0x68, 0xF1, 0x16, 0x25] => "68 F1 16 25"
def int_list_to_hexstr(int_list):
    result = ""
    for int in int_list:
        result += "%02X " % (int)
    return result.strip()

# [0x68, 0xF1, 0x16, 0x25] => "68F11625"
def int_list_to_hexstr_without_space(int_list):
    result = ""
    for int in int_list:
        result += "%02X" % (int)
    return result.strip()

# "68F11625" => [0x68, 0xF1, 0x16, 0x25]
def hexstr_to_int_list_2(arg):
    result = []
    hLen = len(arg)
    for i in range(hLen//2):
        val = int(arg[i*2:i*2+2], 16)
        result.append(val)
    return result

# [00,00,00,17,18,32] => "00,00,00,11,12,20"
def int_to_hex_list(val):
    result = []
    for i in range(len(val)):
        hexval = hex(val[i])
        hexval = hexval[2:]
        result.append(hexval)
    return result

def toHexList(val, len):
    result = []
    for i in range(0, len):
        result.append(val & 0xFF)
        val = val >> 8
    return result

def fromHexList(int_list, offset, len):
    result = 0
    ilist = range(offset, offset + len)
    ilist.reverse()
    #print int_list
    for i in ilist:
        result = (result << 8) + int_list[i]
    return result

def isascii(str):
    _isascii = lambda s: len(s) == len(s.encode())
    return _isascii(str)

def to_asciistr(h):
    list_s = []
    for i in range(0, len(h), 2):
        list_s.append(chr(int(h[i:i+2], 16)))
    return ''.join(list_s)


def ascii_to_hexstr(s):
    list_h = []
    for c in s:
        list_h.append(str(hex(ord(c))[2:]))
    # return list_h
    return ''.join(list_h)


def ascii_to_intlist(s):
    list_h = []
    for c in s:
        list_h.append(ord(c))
    return list_h

def get_file_line_cnt(filepath):
    line_cnt = 0
    file = open(filepath)
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        line_cnt += len(lines)
    file.close()
    return line_cnt

def check_file_type(filename, file_type_list):
    for type in file_type_list:
        if filename.endswith(type):
            return True
    return False

#file_ext is like: "*.c;*.h"
def get_files(folder_path, file_ext, recursive = False):
    result_list = []
    if os.path.isfile(folder_path):
        return [folder_path]
    if not folder_path.endswith("\\"):
        folder_path += "\\"
    file_type_list = file_ext.replace("*","").split(";")
    for filename in os.listdir(folder_path):
        if os.path.isdir(folder_path + filename) and recursive:
            result_list.extend(get_files(folder_path + filename, file_ext, recursive))
        elif os.path.isfile(folder_path + filename) and check_file_type(filename,file_type_list):
            result_list.append(folder_path + filename)
    return result_list

def get_mac_from_str(line):
    mac_pattern = re.compile("..:..:..:..:..:..")
    mac_match = re.search(mac_pattern, line)
    if mac_match != None:
        return mac_match.group(0)
    return ""

# 112233445566 -> 11:22:33:44:55:66
# 11 22 33 44 55 66 -> 11:22:33:44:55:66
# 11:22:33:44:55:66 -> 11:22:33:44:55:66
# 11-22-33-44-55-66 -> 11:22:33:44:55:66
#def mac_addr_refine(mac):
#    return mac_addr_refine(mac, ":")

def mac_addr_refine(mac, spliter=":"):
    mac = mac.replace(' ', "")
    mac = mac.replace(':', "")
    mac = mac.replace('-', "")

    if len(mac) == len("112233445566"):
        result = ""
        for i in range(0,6):
            if result != "":
                result += spliter
            result += mac[i*2:i*2+2]
        return result
    return ""

def mac_addr_reverse(mac):
    return ":".join(mac.split(':')[::-1])

# print bin_str like 'hV\x00\x00\x01\x16'
def print_binstr(tag, data):
    print(tag)
    for i in data:
        print("%02X" % (ord(i))),
    print("")

# print int list like [0x68, 0x16, 0xF1, 0x00]
def print_int_list(tag, data):
    print(tag)
    for i in data:
        print("%02X" % i)
    print("")

def log_time(newline = "\n"):
    print("\n%s%s" % (str(datetime.datetime.now())[:-3], newline))


def str_2char_revert(org_str):
    org_str = org_str.replace(' ','').replace(':',"")
    if len(org_str) % 2 == 1:
        org_str = '0' + org_str
    result = re.findall(r'.{2}', org_str)
    result.reverse()
    return ''.join(result)

def get_lines(file_path, cnt):
    file = open(file_path)
    line_cnt = 0
    read_meter_cmds = []
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            read_meter_cmds.append(line.strip())
            line_cnt = line_cnt + 1
            if line_cnt >= cnt:
                break

        if line_cnt >= cnt:
            break
    file.close()
    return read_meter_cmds

def open_uart(port, baudrate, timeout):
    try:
        ser = serial.Serial(
          port=port,
          baudrate=baudrate,
          parity=serial.PARITY_EVEN,
          stopbits=serial.STOPBITS_ONE,
          #bytesize=serial.SEVENBITS
          bytesize=serial.EIGHTBITS,
          timeout=timeout
        )
        return ser
    except Exception:
        print("failed to open UART %s.\n%s" % (port, str(e)))
        return None

def create_file(file_path):
    try:
        file = open(file_path, "w")
        file.close()
        return True
    except:
        return False

class clog:
    _log_path = ""
    _print_flag = True
    _log_file_flag = True
    @classmethod
    def set_path(cls, log_path):
        if create_file(log_path):
            cls._log_path = log_path
        else:
            cls._log_path = clog.generate_filepath() + ".txt"
            create_file(cls._log_path)

    @classmethod
    def generate_filepath(cls):
        file_name = "cctt_%s_log.txt" % (str(datetime.datetime.now())[:-3])
        file_name = file_name.replace(":", "-").replace(" ", "_")
        return file_name

    @classmethod
    def write_line(cls, line, ts = ""):
        if cls._log_path== "":
            clog.set_path(clog.generate_filepath())
        if ts == None:
            ts = str(datetime.datetime.now())[:-3]
        if cls._print_flag:
            print("%s %s" % (ts, line.strip()))
        if cls._log_file_flag:
            file = open(cls._log_path, "ab+")
            file.write("%s %s\n" % (ts, line))
            file.close()


def get_latest_file(path, ext):
    latest_time = 0
    latest_file = ""
    file_list = get_files(path, ext)
    for file_path in file_list:
        data_time = float(os.path.getmtime(file_path))
        if data_time > latest_time:
            latest_file = file_path
    return latest_file

def get_out_file_path(file_path):
    dot_index = file_path.rfind('.')
    out_file_path = file_path[0:dot_index]
    out_file_path += ".out"
    out_file_path += file_path[dot_index:]

def get_out_ex_file_path(file_path):
    dot_index = file_path.rfind('.')
    out_file_path = file_path[0:dot_index]
    out_file_path += ".out_ex"
    out_file_path += file_path[dot_index:]

