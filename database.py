class Ard:
    def __init__(self):
        self.ard=None   # arduino serial port
        self.wb =Workbook()
        self.ws = self.wb.active
    def serial_ports(self):
        global flag
        ports = list(serial.tools.list_ports.comports())
        result=[]
        for port in ports:
            if "COM" in port[1]:
                result.append(port[0])
        if result==[]:
            tkinter.messagebox.showerror('연결오류', '연결 상태 확인')
        else:
            self.ard=serial.Serial(result[0],57600)
            while 1:
                signal=bytes.decode(self.ard.readline(self.ard.inWaiting())[:-2])
                if signal=='A':
                    self.ard.write('A'.encode())
                    break
            print("연결 확인")
            flag=1
        
    def start(self):
        global t1, t2
        print("start")
        self.ard.write([1])   # start signal
        t1=time.time()
        
    def end(self):
        global title, cnt, t1, t2
        print("end")
        self.ard.write([0])   # stop signal
        t2=time.time()
        t=t2-t1
        origin=[]
        while 1:
            line=int(bytes.decode(self.ard.readline()[:-2]))
            if line==-1:  # end of data
                break
            origin.append(line)
        origin.append(t)
        print(origin)
        writexlsx(self.wb, self.ws, origin, title)
        cnt+=1
               
    def exit(self):
        if self.ard!=[] and self.ard!=None:
            self.ard.close()