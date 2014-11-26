from ctypes import c_char, c_ubyte, c_short, c_ushort, c_int, c_uint, c_ulong, c_long, pointer, Structure

dsInt8_t = c_char
dsUint8_t = c_ubyte
dsInt16_t = c_short
dsUint16_t = c_ushort
dsInt32_t = c_int
dsUint32_t = c_uint
dsULong_t = c_ulong
dsLong_t = c_long
dsChar_t = c_char

def dsTEXT(x):
    return x

dsString_t = pointer(dsChar_t)

class dsUint160_t(Structure):
    _fields_ = [
        ('top', dsUint32_t),
        ('hi_hi', dsUint32_t),
        ('hi_lo', dsUint32_t)
        ('lo_hi', dsUint32_t),
        ('lo_lo', dsUint32_t)
    ]

class dsmBool_t(Structure):
    _fields_ = [
        ('dsmFalse', c_int),
        ('dsmTrue', c_int)
    ]
    
dsmFalse = 0
dsmTrue = 1

uint8 = dsUint8_t
int8 = dsInt8_t
uint16 = dsUint16_t
int16 = dsInt16_t
uint32 = dsUint32_t
int32 = dsInt32_t

class dsStruct64_t(Structure):
    _fields_ = [
        ('hi', dsUint32_t),
        ('lo', dsUint32_t)
    ]

uint64 = dsStruct64_t
dsBool_t  = dsmBool_t
bool_t = dsBool_t
bTrue = dsmTrue
bFalse = dsmFalse

dsInt64_t = c_long
dsUint64_t = c_ulong
