from ctypes import cdll, c_char, c_ubyte, c_short, c_ushort, c_int, c_uint, c_ulong, c_long, pointer, byref, Structure

LIBRARY_FILENAME = 'libApiTSM64.so'
api_lib = cdll.LoadLibrary(LIBRARY_FILENAME)

dsInt8_t = c_char
dsUint8_t = c_ubyte
dsInt16_t = c_short
dsUint16_t = c_ushort
dsInt32_t = c_int
dsUint32_t = c_uint
dsULong_t = c_ulong
dsLong_t = c_long
dsInt64_t = c_long
dsUint64_t = c_long

class dsmApiVersionEx(Structure):
    _fields_ = [
        ('stVersion', dsUint16_t),
        ('stVersion', dsUint16_t),
        ('version', dsUint16_t),
        ('release', dsUint16_t),
        ('level', dsUint16_t),
        ('subLevel', dsUint16_t),
    ]

dsmBeginGetData = api_lib.dsmBeginGetData
dsmBeginGetData.argtypes = ()
dsmBeginGetData.restype = None

dsmQueryApiVersionEx = api_lib.dsmQueryApiVersionEx
dsmQueryApiVersionEx.argtypes = (pointer(dsmApiVersionEx))
dsmQueryApiVersionEx.restype = None