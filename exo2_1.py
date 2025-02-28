from gpiozero import LED, Button
from time import sleep

#A=8,B=9,C=10,D=11,E=12,F=13,G=17
sega = LED(8)
segb = LED(9)
segc = LED(10)
segd = LED(11)
sege = LED(12)
segf = LED(13)
segg = LED(17)
led_alarm = LED(26)
#btn_activate

btn = Button(27)
btn_reset = Button(21)
#Alarm zones
zone1 = Button(22)
zone2 = Button(5)
zone3 = Button(6)
zone4 = Button(19)

#False= unarmed, True= armed
systemStatus = 0

def show0():
    #0
    sega.off()
    segb.off()
    segc.off()
    segd.off()
    sege.off()
    segf.off()
    segg.on()

def show1():
    #1
    sega.on()
    segb.off()
    segc.off()
    segd.on()
    sege.on()
    segf.on()
    segg.on()

def show2():
    #2
    sega.off()
    segb.off()
    segc.on()
    segd.off()
    sege.off()
    segf.on()
    segg.off()  
    
def show3():
    #3
    sega.off()
    segb.off()
    segc.off()
    segd.off()
    sege.on()
    segf.on()
    segg.off() 

def show4():
    #4
    sega.on()
    segb.off()
    segc.off()
    segd.on()
    sege.on()
    segf.off()
    segg.off() 

def show5():
    #5
    sega.off()
    segb.on()
    segc.off()
    segd.off()
    sege.on()
    segf.off()
    segg.off()  

def show6():
    #6
    sega.off()
    segb.on()
    segc.off()
    segd.off()
    sege.off()
    segf.off()
    segg.off() 

def show7():
    #7
    sega.off()
    segb.off()
    segc.off()
    segd.on()
    sege.on()
    segf.on()
    segg.on()     

def show8():
    #8
    sega.off()
    segb.off()
    segc.off()
    segd.off()
    sege.off()
    segf.off()
    segg.off()  

def show9():
    #9
    sega.off()
    segb.off()
    segc.off()
    segd.on()
    sege.on()
    segf.off()
    segg.off()    

def showA():
    #A
    sega.off()
    segb.off()
    segc.off()
    segd.on()
    sege.off()
    segf.off()
    segg.off()

def cout_up():
    #0
    show0()
    sleep(1)
    #1
    show1()    
    sleep(1)
    #2
    show2() 
    sleep(1)
    #3
    show3()  
    sleep(1)
    #4
    show4()
    sleep(1)
    #5
    show5()
    sleep(1)
    #6
    show6() 
    sleep(1)
    #7
    show7() 
    sleep(1)
    #8
    show8()  
    sleep(1)
    #9
    show9()
    sleep(1)
    #A
    showA()

def cout_down():
    #9
    show9()    
    sleep(1)
    #8
    show8()  
    sleep(1)
    #7
    show7()   
    sleep(1)
    #6
    show6()  
    sleep(1)
    #5
    show5() 
    sleep(1)
    #4
    show4()  
    sleep(1)
    #3
    show3()    
    sleep(1)
    #2
    show2()  
    sleep(1)
    #1
    show1()    
    sleep(1)
    #0
    show0()
    sleep(1)

def LedTurnOn():
    led_alarm.on()
       
def LedTurnOff():
    led_alarm.off()

def BlinkZoneBtn():
    zones = {
        zone1: show1,
        zone2: show2,
        zone3: show3,
        zone4: show4
    }
    
    for key, val in zones.items():
        if key:
            val()
            led_alarm.blink()
            break  


    
def UpdateSysStatus():
    if systemStatus == 0:
        cout_up()     
        LedTurnOn()
        systemStatus = 1
    elif systemStatus == 1:
        cout_down()
        LedTurnOff()
        systemStatus = 0
    if systemStatus == 1:
        BlinkZoneBtn()

def btnPressed(btnSelected,Defs):
    btnSelected.when_Pressed = Defs
    

btnPressed(btn,UpdateSysStatus)    


    
                