# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = True
    inc_serial          = True
    inc_i2c             = True


class Global_WS2812:

    numpix_1            = 96            # Anzahl LEDs im 1. Stripe
    numpix_2            = 96            # Anzahl LEDs im 2. Stripe
    numpix_3            = 96            # Anzahl LEDs im 3. Stripe
    numpix_4            = 96            # Anzahl LEDs im 4. Stripe
    numpix_5            = 96            # Anzahl LEDs im 5. Stripe
    numpix_6            = 96            # Anzahl LEDs im 6. Stripe

    # #########################################################################
    # === Start of Stripes ===
    # #########################################################################

    seg_01_strip        = 0             #  1. Ledsegment -> Stripe      # 1. Set -> 1. Segment -> 24 LEDs
    seg_01_start        = 0             #  1. Ledsegment -> Start
    seg_01_count        = 18            #  1. Ledsegment -> Anzahl

    seg_02_strip        = 0             #  2. Ledsegment -> Stripe      # 1. Set -> 2. Segment
    seg_02_start        = 18            #  2. Ledsegment -> Start
    seg_02_count        = 18            #  2. Ledsegment -> Anzahl

    seg_03_strip        = 0             #  3. Ledsegment -> Stripe      # 1. Set -> 3. Segment
    seg_03_start        = 36            #  3. Ledsegment -> Start
    seg_03_count        = 18            #  3. Ledsegment -> Anzahl
    
    seg_04_strip        = 1             #  4. Ledsegment -> Stripe      # 2. Set -> 1. Segment
    seg_04_start        = 0             #  4. Ledsegment -> Start
    seg_04_count        = 18            #  4. Ledsegment -> Anzahl

    seg_05_strip        = 1             #  5. Ledsegment -> Stripe      # 2. Set -> 2. Segment
    seg_05_start        = 18            #  5. Ledsegment -> Start
    seg_05_count        = 18            #  5. Ledsegment -> Anzahl
    
    seg_06_strip        = 1             #  6. Ledsegment -> Stripe      # 2. Set -> 3. Segment
    seg_06_start        = 36            #  6. Ledsegment -> Start
    seg_06_count        = 18            #  6. Ledsegment -> Anzahl
    
    seg_07_strip        = 2             #  7. Ledsegment -> Stripe      # 3. Set -> 1. Segment
    seg_07_start        = 0             #  7. Ledsegment -> Start
    seg_07_count        = 18            #  7. Ledsegment -> Anzahl

    seg_08_strip        = 2             #  8. Ledsegment -> Stripe      # 3. Set -> 2. Segment
    seg_08_start        = 18            #  8. Ledsegment -> Start
    seg_08_count        = 18            #  8. Ledsegment -> Anzahl
    
    seg_09_strip        = 2             #  9. Ledsegment -> Stripe      # 3. Set -> 3. Segment
    seg_09_start        = 36            #  9. Ledsegment -> Start
    seg_09_count        = 18            #  9. Ledsegment -> Anzahl

    seg_10_strip        = 3             # 10. Ledsegment -> Stripe      # 4. Set -> 1. Segment
    seg_10_start        = 0             # 10. Ledsegment -> Start
    seg_10_count        = 18            # 10. Ledsegment -> Anzahl
    
    seg_11_strip        = 3             # 11. Ledsegment -> Stripe      # 4. Set -> 2. Segment
    seg_11_start        = 18            # 11. Ledsegment -> Start
    seg_11_count        = 18            # 11. Ledsegment -> Anzahl

    seg_12_strip        = 3             # 12. Ledsegment -> Stripe      # 4. Set -> 3. Segment
    seg_12_start        = 36            # 12. Ledsegment -> Start
    seg_12_count        = 18            # 12. Ledsegment -> Anzahl

    # *************************************************************************

    seg_13_strip        = 4             # 13. Ledsegment -> Stripe      # Rumpf links
    seg_13_start        = 0             # 13. Ledsegment -> Start
    seg_13_count        = 96            # 13. Ledsegment -> Anzahl

    seg_14_strip        = 5             # 14. Ledsegment -> Stripe      # Rumpf rechts
    seg_14_start        = 0             # 14. Ledsegment -> Start
    seg_14_count        = 96            # 14. Ledsegment -> Anzahl
    
    # #########################################################################
    # === End of Stripes ===
    # #########################################################################

    seg_15_strip        = 1             # 15. Ledsegment -> Stripe      # 3. LED linker Teil
    seg_15_start        = 2             # 15. Ledsegment -> Start
    seg_15_count        = 1             # 15. Ledsegment -> Anzahl

    seg_16_strip        = 1             # 16. Ledsegment -> Stripe      # 4. LED linker Teil
    seg_16_start        = 3             # 16. Ledsegment -> Start
    seg_16_count        = 1             # 16. Ledsegment -> Anzahl
    
    seg_17_strip        = 1             # 17. Ledsegment -> Stripe      # 5. LED linker Teil
    seg_17_start        = 4             # 17. Ledsegment -> Start
    seg_17_count        = 1             # 17. Ledsegment -> Anzahl
    
    seg_18_strip        = 1             # 18. Ledsegment -> Stripe      # 6. LED linker Teil
    seg_18_start        = 5             # 18. Ledsegment -> Start
    seg_18_count        = 1             # 18. Ledsegment -> Anzahl

    seg_19_strip        = 1             # 19. Ledsegment -> Stripe      # 7. LED linker Teil
    seg_19_start        = 6             # 19. Ledsegment -> Start
    seg_19_count        = 1             # 19. Ledsegment -> Anzahl
    
    seg_20_strip        = 1             # 20. Ledsegment -> Stripe      # 8. LED linker Teil
    seg_20_start        = 7             # 20. Ledsegment -> Start
    seg_20_count        = 1             # 20. Ledsegment -> Anzahl

    # ************************************************************************
    
    seg_21_strip        = 2             # 21. Ledsegment -> Stripe      # 1. LED rechter Teil
    seg_21_start        = 0             # 21. Ledsegment -> Start
    seg_21_count        = 1             # 21. Ledsegment -> Anzahl
    
    seg_22_strip        = 2             # 22. Ledsegment -> Stripe      # 2. LED rechter Teil
    seg_22_start        = 1             # 22. Ledsegment -> Start
    seg_22_count        = 1             # 22. Ledsegment -> Anzahl

    seg_23_strip        = 2             # 23. Ledsegment -> Stripe      # 3. LED rechter Teil
    seg_23_start        = 2             # 23. Ledsegment -> Start
    seg_23_count        = 1             # 23. Ledsegment -> Anzahl
    
    seg_24_strip        = 2             # 24. Ledsegment -> Stripe      # 4. LED rechter Teil
    seg_24_start        = 3             # 24. Ledsegment -> Start
    seg_24_count        = 1             # 24. Ledsegment -> Anzahl

    seg_25_strip        = 2             # 25. Ledsegment -> Stripe      # 5. LED rechter Teil
    seg_25_start        = 4             # 25. Ledsegment -> Start
    seg_25_count        = 1             # 25. Ledsegment -> Anzahl

    seg_26_strip        = 2             # 26. Ledsegment -> Stripe      # 6. LED rechter Teil
    seg_26_start        = 5             # 26. Ledsegment -> Start
    seg_26_count        = 1             # 26. Ledsegment -> Anzahl
    
    seg_27_strip        = 2             # 27. Ledsegment -> Stripe      # 7. LED rechter Teil
    seg_27_start        = 6            # 27. Ledsegment -> Start
    seg_27_count        = 1             # 27. Ledsegment -> Anzahl

    seg_28_strip        = 2             # 28. Ledsegment -> Stripe      # 8. LED rechter Teil
    seg_28_start        = 7             # 28. Ledsegment -> Start
    seg_28_count        = 1             # 28. Ledsegment -> Anzahl

    # *************************************************************************
    
    seg_29_strip        = 3             # 29. Ledsegment -> Stripe      # 1. LED mittlerer Teil
    seg_29_start        = 0             # 29. Ledsegment -> Start
    seg_29_count        = 1             # 29. Ledsegment -> Anzahl
    
    seg_30_strip        = 3             # 30. Ledsegment -> Stripe      # 2. LED mittlerer Teil
    seg_30_start        = 1             # 30. Ledsegment -> Start
    seg_30_count        = 1             # 30. Ledsegment -> Anzahl

    seg_31_strip        = 3             # 31. Ledsegment -> Stripe      # 3. LED mittlerer Teil
    seg_31_start        = 2             # 31. Ledsegment -> Start
    seg_31_count        = 1             # 31. Ledsegment -> Anzahl
    
    # *************************************************************************

    seg_32_strip        = 4             # 32. Ledsegment -> Stripe		# 1. LED Startracker linke
    seg_32_start        = 0             # 32. Ledsegment -> Start
    seg_32_count        = 1             # 32. Ledsegment -> Anzahl

    # *************************************************************************

    seg_33_strip        = 5             # 33. Ledsegment -> Stripe		# 1. LED Startracker rechts
    seg_33_start        = 0             # 33. Ledsegment -> Start
    seg_33_count        = 1             # 33. Ledsegment -> Anzahl

    # *************************************************************************
    
    #seg_34_strip        = 2             # 34. Ledsegment -> Stripe
    #seg_34_start        = 9             # 34. Ledsegment -> Start
    #seg_34_count        = 1             # 34. Ledsegment -> Anzahl

    #seg_35_strip        = 2             # 35. Ledsegment -> Stripe
    #seg_35_start        = 10            # 35. Ledsegment -> Start
    #seg_35_count        = 1             # 35. Ledsegment -> Anzahl
    
    #seg_36_strip        = 2             # 36. Ledsegment -> Stripe
    #seg_36_start        = 11            # 36. Ledsegment -> Start
    #seg_36_count        = 1             # 36. Ledsegment -> Anzahl

# -----------------------------------------------------------------------------

    #seg_37_strip        = 3             # 37. Ledsegment -> Stripe
    #seg_37_start        = 0             # 37. Ledsegment -> Start
    #seg_37_count        = 16            # 37. Ledsegment -> Anzahl

# -----------------------------------------------------------------------------

# =============================================================================
# Color-Table             Red Green Blue
# =============================================================================
    color_def           = (  0,  0,  5)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (100,100,100)
    color_blink_off     = ( 50, 50, 50)


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