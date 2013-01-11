from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.db.models import Count, Max, Min
from house.models import *


def index_page(request):
    map_border = House.objects.aggregate(Max('coord_lon'), Min('coord_lon'), Max('coord_lat'), Min('coord_lat'))
    if map_border['coord_lat__max'] != None:
        map_center = {
            'lat': (map_border['coord_lat__max'] + map_border['coord_lat__min']) / 2,
            'lon': (map_border['coord_lon__max'] + map_border['coord_lon__min']) / 2,
        }
    else:
        map_center = False

    return render_to_response('house/index.html', {
        'cluster_list': Cluster.objects.all(),
        'street_list': Street.objects.order_by('name').annotate(house_count=Count('house')),
        'house_list': House.objects.all(),
        'map_center': map_center,
        }, context_instance=RequestContext(request))


def street(request, id):
    map_border = House.objects.filter(street=id).aggregate(Max('coord_lon'), Min('coord_lon'), Max('coord_lat'), Min('coord_lat'))
    if map_border['coord_lat__max'] != None:
        map_center = {
            'lat': (map_border['coord_lat__max'] + map_border['coord_lat__min']) / 2,
            'lon': (map_border['coord_lon__max'] + map_border['coord_lon__min']) / 2,
        }
    else:
        map_center = False

    return render_to_response('house/street.html', {
        'street': Street.objects.get(pk=id),
        'cluster_list': Cluster.objects.all(),
        'street_list': Street.objects.order_by('name').annotate(house_count=Count('house')),
        'house_list': House.objects.filter(street=id).extra(select={'number_int': 'LPAD(IF(number REGEXP "[0-9]$", CONCAT(number, " "), number), 6, " ")'}).order_by('number_int'),
        'map_center': map_center,
        }, context_instance=RequestContext(request))


def house(request, id):
    h = House.objects.get(pk=id)

    return render_to_response('house/house.html', {
        'house': h,
        'cluster_list': Cluster.objects.all(),
        'street_list': Street.objects.order_by('name').annotate(house_count=Count('house')),
        'photo': HousePhoto.objects.filter(house=h),
        'passport': HousePassport.objects.filter(house=h),
        'is_admin': True,
        }, context_instance=RequestContext(request))

