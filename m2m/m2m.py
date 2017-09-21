#!/usr/bin/env python

# functions
__all__ = ['get_latest']
import requests
import json
import time
import datetime
from .instrument_dict import instrument_dict

def get_latest(instrument):
    # define instrument parameters
    base_url = 'https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv'
    site = instrument_dict[instrument]['site']
    platform = instrument_dict[instrument]['platform']
    code = instrument_dict[instrument]['code']
    stream = instrument_dict[instrument]['stream']

    # get timing parameters
    response = requests.get('%s/%s/%s/%s/metadata/times' % (base_url, site, platform, code))
    for item in response.json():
        if item['stream'] == 'tmpsf_sample':
            end_time = item['endTime']
            end_time = datetime.datetime.strptime(end_time[:-1] + '000', '%Y-%m-%dT%H:%M:%S.%f')
    start_time = end_time - datetime.timedelta(milliseconds=1)
    start_time = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    # get last recording 
    response = requests.get('%s/%s/%s/%s/streamed/%s?beginDT=%s&limit=1000' % 
        (base_url, site, platform, code, stream, start_time))

    # output filters
    if instrument == 'ashes_temp_array_01':
        output = [response.json()[-1]['time']]
        for j in range(1, 25):
            probe = ('temperature%02.0f' % j)
            output.append(response.json()[-1][probe])
        return output
    else:
        raise SystemError('No output filter for the requested instrument stream.')

#def main():
#    output = get_latest('ashes_temp_array_01')
#    print(output)

# main sentinel
#if __name__ == "__main__":
#    main()
