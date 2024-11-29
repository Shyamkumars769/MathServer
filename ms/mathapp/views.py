from django.shortcuts import render 
def EnergyCalc(request): 
    context = {
        'power': "0", 
        'intensity': "0", 
        'resistance': "0"
    }
    if request.method == 'POST': 
        print("POST method is used")
        intensity = request.POST.get('intensity', '0')
        resistance = request.POST.get('resistance', '0')
        print('request=', request) 
        print('intensity=', intensity) 
        print('resistance=', resistance) 
        power = (int(intensity) ** 2) * int(resistance)
        context['power'] = power
        context['intensity'] = intensity
        context['resistance'] = resistance 
        print('power=', power)  
    return render(request, 'mathapp/math.html', context)
