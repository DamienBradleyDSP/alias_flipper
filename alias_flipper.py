import scipy.signal as sci

def filter_highpass(input_signal):          # basic low and high pass filters
    h = sci.firwin(101,0.5,window='hamming',pass_zero=False)
    output = sci.lfilter(h,[1],input_signal) 

    return output

def filter_lowpass(input_signal):
    h = sci.firwin(101,0.5,window='hamming',pass_zero=True)
    output = sci.lfilter(h,[1],input_signal)

    return output

def decimate_then_zeropad(signal):

    downsampled_signal = []                         # decimates signal taking 1 in every 2 samples
    for n, sample in enumerate(signal):
        if n%2==0:
                downsampled_signal.append(sample)

    upsampled_signal = []                           # upsamples back to original rate - freqs are now mirrored in spectrum
    for n,sample in enumerate(downsampled_signal):
        upsampled_signal.append(sample)
        upsampled_signal.append(0)
    
    return upsampled_signal

def alias_flip(input_signal):   # flips a signal's frequency components, low frequencies are now high and vice versa

    # Low frequencies become high
    low_passed_original_sr = filter_lowpass(input_signal)

    alias_reflection = decimate_then_zeropad(low_passed_original_sr)

    output_signal = filter_highpass(alias_reflection)

    
    # High Frequencies become low
    high_passed_original_sr = filter_highpass(input_signal)

    alias_reflection = decimate_then_zeropad(high_passed_original_sr)

    output_signal2 = filter_lowpass(alias_reflection)

    
    # Return combination
    return output_signal + output_signal2


        
