# #############################################################################
# ### Init WS2812
# #############################################################################


class WS2812_Objects:

    def __init__(self, io_port, count, color):
        self.io_port    = io_port
        self.count      = count
        self.color      = color


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

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.numpix_2)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()