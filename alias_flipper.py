import scipy.signal as sci

def half_nyquist_filter(input_signal,filt_type):
    if filt_type=='lowpass':
        h = sci.firwin(101,0.5,window='hamming',pass_zero=True)
        output = sci.lfilter(h,[1],input_signal)
    else:
        h = sci.firwin(101,0.5,window='hamming',pass_zero=False)
        output = sci.lfilter(h,[1],input_signal) 
    
    return output

def decimate_then_zeropad(signal):
    downsampled_signal = []
    for n, sample in enumerate(signal):
        if n%2==0:
                downsampled_signal.append(sample)

    upsampled_signal = []
    for n,sample in enumerate(downsampled_signal):
        upsampled_signal.append(sample)
        upsampled_signal.append(0)
    
    return upsampled_signal

def alias_flip(input_signal):   # flips a signal's frequency components, low frequencies are now high and vice versa


    low_passed_original_sr = half_nyquist_filter(input_signal,'lowpass')

    alias_reflection = decimate_then_zeropad(low_passed_original_sr)

    output_signal = half_nyquist_filter(alias_reflection,'highpass')

    

    high_passed_original_sr = half_nyquist_filter(input_signal,'highpass')

    alias_reflection = decimate_then_zeropad(high_passed_original_sr)

    output_signal2 = half_nyquist_filter(alias_reflection,'lowpass')

    

    return output_signal2


        
