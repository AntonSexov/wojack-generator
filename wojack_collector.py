import requests
from lxml import html


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = "https://wojakparadise.net/wojak/"
ids = range(1, 5000)
count = 0
for pic_id in ids:
    pic_url = f"{url}{pic_id}/img"
    try:
        response = requests.get(pic_url, headers=headers)
        if response.status_code == 200:

            img = response.content

            response = requests.get(f"https://wojakparadise.net/wojak/{pic_id}", headers=headers)
            tree = html.fromstring(response.content)
            name_element = tree.xpath('body/div[@class="horizontal"]/div[@class="main-content"]/div[@class="content-1"]/div[@class="frame"]/div[@class="head_title"]/h1')
            name = "_".join(name_element[0].text.lower().split())
            
            with open(f"wojacks/image_{name}.jpg", "wb") as file:
                file.write(img)
            print(f"downloaded img {name}")
            count += 1

        else:
            print(f"downloading failed at {url}{pic_id}/img")

    except Exception as e:
        print(f"error: {e}")
print(f"images downloaded: {count}")