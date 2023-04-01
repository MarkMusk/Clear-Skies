import requests

def readMETAR(lat=False, lon=False, ICAO=False) -> False or dict:
    """
    Reads METAR data from METAR-TAF using a ICAO registered airport, if ICAO is a valid airport.
    Reads METAR data from METAR-TAF using nearest ICAO registered airport to (lat, lon), if (lat, lon) is a valid location.
    If error occurs -> False
    """
    TOKEN = 'BxqbOVGBtbgRohXpncK4CWhCmU18f1sQ'
    LANG = 'en-US'

    if not(lat and lon) or not(ICAO):
        return False
    elif lat and lon:
        response = requests.get(f"https://api.metar-taf.com/metar?api_key={TOKEN}&v=2.3&{LANG}=en-US&latitude={lat}&longitude={lon}")
        response_json = response.json()
        if not(response_json['status']):
            return False
    elif ICAO:
        response = requests.get(f"https://api.metar-taf.com/metar?api_key={TOKEN}&v=2.3&{LANG}=en-US&id={ICAO}")
        response_json = response.json()
        if not(response_json['status']):
            return False
    else:
        return False


print(readMETAR())

{'status': True, 'credits': -1, 'airport': {'id': 'CYYZ', 'iata': 'YYZ', 'name': 'Lester B. Pearson International Airport', 'name_translated': 'Lester B. Pearson International Airport', 'city_name': 'Eringate-Centennial-West Deane', 'admin1': 'Ontario', 'admin2': 'Toronto county', 'country_id': 'CA', 'country_name': 'Canada', 'lat': 43.6772, 'lng': -79.6306, 'metar': True, 'taf': True, 'timezone': -14400, 'fir': None, 'elevation': 569, 'type': 15, 'last_notam': 1678455766}, 'metar': {'cavok': False, 'ceiling': 2300, 'ceiling_color': '#0080f0', 'clouds': [{'id': 0, 'height': 2300, 'report': 'Overcast clouds', 'amount': 'OVC'}], 'code': 'MVFR', 'code_color': '#0080f0', 'colour_state': None, 'dewpoint': -6, 'dewpoint_exact': None, 'humidity': 69, 'is_day': True, 'observed': 1678647600, 'qnh': 1014.2, 'raw': 'METAR CYYZ 121900Z 11008KT 15SM OVC023 M01/M06 A2995 RMK SC8 SH DIST NW SLP152', 'recent_weather_report': None, 'remarks': ['SLP152: Sea level pressure is 1015.2 hPa (29.98 inHg)', 'SC8 SH DIST NW'], 'runway_condition': [], 'runway_visibility': [], 'snoclo': False, 'station_id': 'CYYZ', 'sunrise': 1678620953, 'sunset': 1678663238, 'temperature': -1, 'temperature_exact': None, 'trends': [], 'vertical_visibility': None, 'visibility': 24140.1, 'visibility_sign': None, 'visibility_color': '#28a745', 'visibility_min': None, 'visibility_min_direction': None, 'warnings': [], 'weather': 'Overcast', 'weather_image': 'overcast', 'weather_report': None, 'wind_color': '#28a745', 'wind_dir': 110, 'wind_dir_max': None, 'wind_dir_min': None, 'wind_gust': None, 'wind_speed': 8, 'ws_all': None, 'ws_runways': None, 'id': 399111108}, 'runways': [{'id_l': '6L', 'id_h': '24R', 'hdg_l': 57, 'hdg_h': 237, 'in_use': 57, 'xwnd': 6.4, 'hwnd': 4.8}, {'id_l': '6R', 'id_h': '24L', 'hdg_l': 57, 'hdg_h': 237, 'in_use': 57, 'xwnd': 6.4, 'hwnd': 4.8}, {'id_l': '5', 'id_h': '23', 'hdg_l': 57, 'hdg_h': 237, 'in_use': 57, 'xwnd': 6.4, 'hwnd': 4.8}, {'id_l': '15L', 'id_h': '33R', 'hdg_l': 147, 'hdg_h': 327, 'in_use': 147, 'xwnd': -4.8, 'hwnd': 6.4}, {'id_l': '15R', 'id_h': '33L', 'hdg_l': 147, 'hdg_h': 327, 'in_use': 147, 'xwnd': -4.8, 'hwnd': 6.4}, {'id_l': '15', 'id_h': '33', 'hdg_l': 147, 'hdg_h': 327, 'in_use': 147, 'xwnd': -4.8, 'hwnd': 6.4}], 'stations': [{'id': 'CYYZ', 'name': 'Lester B. Pearson International Airport', 'taf': True}, {'id': 'CXTO', 'name': 'Toronto City', 'taf': False}, {'id': 'CYTZ', 'name': 'Billy Bishop Toronto City Centre Airport', 'taf': True}, {'id': 'CWWB', 'name': 'Burlington Piers', 'taf': False}, {'id': 'CXHM', 'name': 'Hamilton Rbg Cs', 'taf': False}, {'id': 'CXVN', 'name': 'Vineland (au8)', 'taf': False}]}