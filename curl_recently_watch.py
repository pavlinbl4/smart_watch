import requests

cookies = {
    '_tuid': '763f154e6f7a5688b620e45110e0b176ee11e427',
    '_space': 'spb_cl',
    'ab_test': '90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A10',
    'ab_test_analytics': '90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A10',
    'ab_test_segment': '46',
    'old_design': '0',
    'is_show_welcome_mechanics': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': '*/*',
    'Accept-Language': 'en,en-US;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.citilink.ru/catalog/smart-chasy/?sorting=price_asc&pf=available.all%2Cdiscount.any%2Crating.any%2Camazfit%2C23525_835chernyy%2C9315_835&f=available.all%2Cdiscount.any%2Crating.any%2Camazfit%2C23525_835chernyy',
    'content-type': 'application/json',
    'Origin': 'https://www.citilink.ru',
    'DNT': '1',
    'Connection': 'keep-alive',
    # 'Cookie': '_tuid=763f154e6f7a5688b620e45110e0b176ee11e427; _space=spb_cl; ab_test=90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_analytics=90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A2%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_segment=46; old_design=0; is_show_welcome_mechanics=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=4',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

json_data = {
    'query': 'query GetRecentlyViewed($input:Catalog_RecentlyViewedInput!){recommendations{recentlyViewedProducts(input:$input){...ProductSnippetBase}}}fragment ProductSnippetBase on Catalog_Product{id,name,shortName,slug,isAvailable,images{citilink{...Image}},price{...ProductPrice},category{id,name},brand{name},multiplicity,quantityInPackageFromSupplier}fragment Image on Image{sources{url,size}}fragment ProductPrice on Catalog_ProductPrice{current,old,club,clubPriceViewType}',
    'variables': {
        'input': {
            'limit': 16,
        },
    },
}

response = requests.post('https://www.citilink.ru/graphql/', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"query":"query GetRecentlyViewed($input:Catalog_RecentlyViewedInput!){recommendations{recentlyViewedProducts(input:$input){...ProductSnippetBase}}}fragment ProductSnippetBase on Catalog_Product{id,name,shortName,slug,isAvailable,images{citilink{...Image}},price{...ProductPrice},category{id,name},brand{name},multiplicity,quantityInPackageFromSupplier}fragment Image on Image{sources{url,size}}fragment ProductPrice on Catalog_ProductPrice{current,old,club,clubPriceViewType}","variables":{"input":{"limit":16}}}'
#response = requests.post('https://www.citilink.ru/graphql/', cookies=cookies, headers=headers, data=data)

print(response.json())