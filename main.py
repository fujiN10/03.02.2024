from geocoder import get_ll_span
from mapapi_PG import show_map

toponym_to_find = 'Тольятти'

if toponym_to_find:
    ll, spn = get_ll_span(toponym_to_find)
    add_params = f'pt={ll}'
    ll_spn = f'll={ll}&spn={spn}'
    show_map(ll_spn=ll_spn, spn=spn, map_type="map", add_params=add_params)
else:
    print('No toponym')
