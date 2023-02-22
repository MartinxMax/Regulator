# @Мартин.
import serial,argparse,textwrap,sys,os,datetime
Version = "@Мартин. Regulator V2.0.0"
Title='''
************************************************************************************
<注释>:本工具提供自动锁屏服务功能
<notes>:This tool provides automatic lock screen service function
************************************************************************************'''

Logo = f'''
 _______                                 __              __                         
/       \                               /  |            /  |                        
$$$$$$$  |  ______    ______   __    __ $$ |  ______   _$$ |_     ______    ______  
$$ |__$$ | /      \  /      \ /  |  /  |$$ | /      \ / $$   |   /      \  /      \ 
$$    $$< /$$$$$$  |/$$$$$$  |$$ |  $$ |$$ | $$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |
$$$$$$$  |$$    $$ |$$ |  $$ |$$ |  $$ |$$ | /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ 
$$ |  $$ |$$$$$$$$/ $$ \__$$ |$$ \__$$ |$$ |/$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |      
$$ |  $$ |$$       |$$    $$ |$$    $$/ $$ |$$    $$ |  $$  $$/ $$    $$/ $$ |      
$$/   $$/  $$$$$$$/  $$$$$$$ | $$$$$$/  $$/  $$$$$$$/    $$$$/   $$$$$$/  $$/       
                    /  \__$$ |                                                      
                    $$    $$/                                                       
                     $$$$$$/                                                          
                                        Github ==> https://github.com/MartinxMax
                                        {Version}
'''

CONF = '''
[+] ---------------------------------------
| COM:{}\tBaudrate:{}\tBytesize:{}
| Parity:{}\tStopbits:{}\tTimeout:{}
| Rtscts:{}\tDsrdtr:{}\tXonxoff:{}
| WriteTimeout:{}\tInterCharTimeout:{}
 -------------------------------------------
'''

class Main():
    def __init__(self,args):
        self.COM = args.COM
        self.Baud = args.Baud
        self.CMD = args.CMD

    def Server(self):
        try:
            ser = serial.Serial(self.COM, self.Baud, timeout=0.5)
        except:
            print("[!]COM Interface exception")
            return False
        else:
            print(CONF.format(ser.name,ser.baudrate,ser.bytesize,ser.parity,ser.stopbits,ser.timeout,ser.writeTimeout,\
                ser.xonxoff,ser.rtscts,ser.dsrdtr,ser.interCharTimeout))
            print("[+]Equipment monitoring")
            while True:
                try:
                    if '~' in ser.readline().decode():
                        Status = os.popen(self.CMD)
                        if Status:
                            print(f"[+]Command execute @{self.CMD}@ Success!-----[{datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')}]")
                        else:
                            print(f"[!]Command execute @{self.CMD}@ Fail!")
                except:
                    print("[-]Exit")
                    break


    def run(self):
        if self.COM:
            self.Server()
        else:
            print("[!]You must select a valid COM port!")


def main():
    print(Logo, "\n", Title)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
        Example:
            author-Github==>https://github.com/MartinxMax
        Basic usage:
            python3 {C51} -c (COM13) -b (Baud rate) #You must fill in the COM port, and then you can not fill in the baud rate, which is 9600 by default
            '''.format(C51=sys.argv[0]
                       )))
    parser.add_argument('-c', '--COM', default=None, help='COM Port')
    parser.add_argument('-b', '--Baud', type=int, default=9600, help='Baud rate')
    parser.add_argument('-cmd', '--CMD', default="RunDll32.exe user32.dll,LockWorkStation", help='CMD')
    Main(parser.parse_args()).run()


if __name__ == '__main__':
    main()
