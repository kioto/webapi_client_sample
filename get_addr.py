"""郵便番号検索

以下のURLを発行
https://zipcloud.ibsnet.co.jp/api/search?zipcode=100-0001
"""

import sys
import httpx

URL = 'https://zipcloud.ibsnet.co.jp/api/search'


def main(zipcode):
    params = {'zipcode': zipcode}
    data = httpx.get(URL, params=params).json()

    if data.get('status') != 200:
        print(data.get('message'))
        return
    res = data.get('results')

    if res is None:
        print(f'ERROR: {zipcode}: Unknown zip code')
        return

    address = res[0]
    print(address['address1'], address['address2'], address['address3'])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <zipcode>')
        exit()

    main(sys.argv[1])
