# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_debug_led       = True
    inc_ws2812_init     = True
    inc_decoder         = True
    inc_serial          = True

class Global_Colors:
# -----------------------------------------------------------------------------

    color_def           = (  5,  0,  0)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (  0,200,  0)
    color_blink_off     = (  0, 10,  0)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Init Global")
    mg = Global_Colors
    print(mg.color_def)
    print(mg.color_off)
    if Global_Module.inc_debug_led:
        import init.debug_led as board_led


 
#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()