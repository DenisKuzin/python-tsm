from ctypes import cdll

LIBRARY_FILENAME = 'libApiTSM64.so'

if __name__ == '__main__':
    api_lib = cdll.LoadLibrary(LIBRARY_FILENAME)