import base64
import os
import requests
from dotenv import load_dotenv


def extract_tag_content(html_string, tag):
    start_index = html_string.find(tag)
    if start_index != -1:
        content_begin = html_string[start_index:]
        end_index = content_begin.find(">") - 1
        tag_content = content_begin[:end_index]
        tag_content = tag_content[tag_content.find("content=") + 9:]
        return tag_content
    else:
        return "Not found"


def get_html_tags(urls):
    # Code to connect to Netprism API
    print('starting netprism connection')
    netprism_api_url = 'https://canary.netprism.dev/v1/task'
    load_dotenv()
    api_key = os.getenv('API_KEY')
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    productObjs = []

    for url in urls:
        request_body = {
            'url': url,
            'type': 'webpage',
            'options': {
                'jsRender': True,
            }
        }
        response = requests.post(netprism_api_url, headers=headers, json=request_body)
        response_json = response.json()
        # Retrieve the task ID from the response
        data = response_json['data']
        decoded_html = base64.b64decode(data)
        decoded_html = decoded_html.decode('utf-8')
        index = decoded_html.find("<meta")

        decoded_html = decoded_html[index:]

        # Extract title tag
        title_tag = extract_tag_content(decoded_html, "<meta property=\"og:title\"")
        print("Title Tag:", title_tag)

        # Extract image tag
        image_tag = extract_tag_content(decoded_html, "<meta property=\"og:image\"")
        print("Image Tag:", image_tag)

        # Extract price tag
        price_tag = extract_tag_content(decoded_html, "<meta property=\"og:price:amount\"")
        print("Price Tag:", price_tag)

        productObjs.append({'url': url,
            'title': title_tag,
            'image': image_tag,
            'price': price_tag})

    print('finished netprism connection')
    with open("output.txt", "w") as f:
        # Write some text to the file
        f.write(decoded_html)

    return productObjs



# # Code to test file with a single url

# import base64
# import os
# import requests
# from dotenv import load_dotenv


# # CODE TO SET UP NETPRISM ENDPOINT
# print('starting netprism connection')
# netprism_api_url = 'https://canary.netprism.dev/v1/task'
# load_dotenv()
# api_key = os.getenv('API_KEY')
# headers = {
#     'Authorization': f'Bearer {api_key}',
#     'Content-Type': 'application/json'
# }
# request_body = {
#     'url': 'https://www.walmart.com/ip/Sony-PlayStation-PS5-Video-Game-Console-Digital-Edition-PlayStation-5/497243975?wmlspartner=wlpa&selectedSellerId=101067841',
#     'type': 'webpage',
#     'options': {
#         'jsRender': True
#     }
# }

# response2 = requests.post(netprism_api_url, headers=headers, json=request_body)
# response_json = response2.json()
# # Retrieve the task ID from the response
# data = response_json['data']
# decoded_html = base64.b64decode(data)
# decoded_html = decoded_html.decode('utf-8')
# index = decoded_html.find("<meta")

# decoded_html = decoded_html[index: ]


# def extract_tag_content(html_string, tag):
#     start_index = html_string.find(tag)
#     print("start: ", start_index)
#     if start_index != -1:
#         content_begin = html_string[start_index:]

#         end_index = content_begin.find(">") - 1

#         tag_content = content_begin[:end_index]
#         tag_content = tag_content[tag_content.find("content=") + 9: ]
#         return tag_content
#     else:
#         return None

# # Extract title tag
# title_tag = extract_tag_content(decoded_html, "<meta property=\"og:title\"")
# print("Title Tag:", title_tag)

# # Extract image tag
# image_tag = extract_tag_content(decoded_html, "<meta property=\"og:image\"")
# print("Image Tag:", image_tag)

# # Extract price tag
# price_tag = extract_tag_content(decoded_html, "<meta property=\"og:price:amount\"")
# print("Price Tag:", price_tag)


# print('finished netprism connection')
# with open("output2.txt", "w") as f:
#     # Write some text to the file
#     f.write(decoded_html)