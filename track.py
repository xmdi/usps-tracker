import requests
import sys
import ctypes
gn=0
if len(sys.argv)>1:
    url='https://tools.usps.com/go/TrackConfirmAction?tLabels='+sys.argv[1]
    s=requests.session()
    s.headers['User-Agent']='Mozilla/5.0'
    response=s.get(url)
    splat=response.text.split('\n')
    for line in splat:
        if '<span class="delivery-status-text">' in line:
            print('Package Status: %s'%line.strip().replace('<span class="delivery-status-text">','').replace('</span>',''))
        if '<strong>Expected Delivery Day:  </strong>' in line:
            print('Expected Delivery Day: %s'%line.strip().replace('<strong>Expected Delivery Day:  </strong>',''))
        if (gn==1):
            gn=0
            print(line.strip())
        if '<span class="callout">' in line:
            gn=1
else:
    print('no tracking number argument')
