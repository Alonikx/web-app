from .models import BronTable, Places
from django.shortcuts import render


def home(request):
    # Переменная в которую записываются все объекты из модели brontable
    bron = BronTable.objects.all()
    # Переменная, в которую записываются объекты, у которых place_id=0
    place_id = Places.objects.filter(place_id=0)
    # Переменная, в которую записываются объекты, у которых time_id=1
    place_id_1 = BronTable.objects.filter(time_id=1)
    # Переменная, в которую записываются объекты, у которых time_id=2
    place_id_2 = BronTable.objects.filter(time_id=2)
    place_num = Places.objects.all()
    return render(request, 'main/index.html', {'bron': bron, 'place': place_id, 'place_num': place_num,
                                               'place_id_1': place_id_1, 'place_id_2': place_id_2})
