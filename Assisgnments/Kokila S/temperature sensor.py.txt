def adc_raw_value(v):
    if(v >= MIN_VOLT and v <= MAX_VOLT):
        ADC = (v*(ADC_RESOLUTION/SYSVOLT))
        return round(ADC)
    else:
        return None