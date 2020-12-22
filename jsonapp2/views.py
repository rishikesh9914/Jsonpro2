import json

from django.shortcuts import render

# Create your views here.
from jsonapp2.utils import search_train


def showIndex(request):
    if request.method == 'POST':
        train_name=request.POST.get("t1")
        data=search_train(train_name)

        json_data = json.loads(data)
        if data:
             return render(request,"index.html",{"data": json_data})
        else:
            return render(request, "index.html", {"error":"Sorry...Train not available"})

    else:
       return render(request,"index.html")

