######################################################
### Main-Program                                   ###
### Projekt: H2Electra                             ###
### Version: 0.99                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from libs.module_init import Global_Module as MyModule
import time

pix_array_01 = [11]
pix_array_02 = [10]
pix_array_03 = [ 6]
pix_array_06 = [ 3, 4]
pix_array_04 = [ 2 ,5]
pix_array_05 = [ 0, 1]
pix_array_07 = [ 7, 8]
pix_array_08 = [ 9]
pix_array_09 = [16, 24]
pix_array_10 = [19]
pix_array_11 = [17, 25]
pix_array_12 = [29, 30]
pix_array_13 = [28]
pix_array_14 = [14, 22]
pix_array_15 = [12, 13, 20, 21]
pix_array_16 = [31, 32]

obj_offset = 0          # Offset bei Zählung ab 1 = -1

def blink_func():
    MyWS2812.do_blink()


# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    blink_couter = 0
    
    while(1):
        blink_couter = blink_couter + 1
        # Loop-Delay !!!
        time.sleep(0.01)        # 10ms
        
    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### ____ Main ____                                                          ###
# ###############################################################################

if __name__ == "__main__":

    print("___Start_Program___")

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        #print("WS2812 -> Run self test")
        MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        import module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        #print("Serial-COM -> Load-Module")
        import module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End_of_Programm___!!!")

# ##############################################################################
