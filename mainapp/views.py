from django.shortcuts import render
from main import process_data2
# Create your views here.


def index(request):
    if request.FILES:
        import pandas as pd
        csv = request.FILES['file']
        data = pd.read_csv(csv)
        output = process_data2(data)
        return render(request, 'results.html', {
            'output': output
        })
    return render(request, 'index.html')
