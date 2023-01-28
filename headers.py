import requests

headers = {
    'authority': 'drm3.mp.lura.live',
    'accept': '*/*',
    'accept-language': 'en,es-ES;q=0.9,es;q=0.8',
    'origin': 'https://vix.com',
    'referer': 'https://vix.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
}

data = '\b\x04'

response = requests.post(
    'https://drm3.mp.lura.live/cenc?eqp=k_4c7HFfiFBsnGuD62K-w9TxNJPcks71WM2EE9BLCnoDnsB0valcjBgc4Hv-Ptff0qKmEjxAfJ3ppc5bekx8zLEcOPpj7PTpRI6crrS5QhhvMV2g0NxRanErCrf7jAoX3j2XAx32CCXfRzIkgROqIZ1N4A_RUjVOXYRJZ3r9Ejej397GpUonfuqvBsImo5U7CBS_XwEvOsjlKqKfnSVR8HxE-TtmHeAa65lUVTP-89RvhAN58mm2nXU-EYNRhVBzU0bhv76Ze_O44mzc1mWhaWWDOt_HSTlQyQ16Q50Yi-FjYtPwBe6mxrqeXAk97gjE&anvauth=tb=0~te=1674089318~sgn=ab5813ab467b9fadb701515fe5394f0dca2527d0ea113fbf94dabd286b50d6b2&t=1674078518',
    headers=headers,
    data=data,
)
