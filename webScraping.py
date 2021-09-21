import csv
import requests
from bs4 import BeautifulSoup

class WebScraping():

    def test(self):

        page = requests.get("https://en.wikipedia.org/wiki/Bangalore")
        soup1 = BeautifulSoup(page.content, 'html.parser')

        all_text = []
        #Getting the heading
        heading = soup1.find_all('h1',id="firstHeading")[0]
        headingtext=heading.get_text()
        print(headingtext)

        #Getting the first paragraph text
        para1 = soup1.find('div',class_ = 'mw-parser-output')
        para1_tag = para1.find_all('p')[1]
        para1_text = para1_tag.get_text()
        print(para1_text)
        print("***************************")
        print(type(para1_text))

        #Getting the second paragraph text
        para2 = soup1.find('div', class_='mw-parser-output')
        para2_tag = para2.find_all('p')[2]
        para2_text = para2_tag.get_text()
        print(para2_text)

        #Getting the First Image
        image_1 =soup1.find('a',class_='image')
        image_2 = image_1.findAll('img')
        image_3 = image_2[0]['src']
        print("The image 1 is : ")
        print(image_3)

        #Getting the Map Image
        image2_1 = soup1.find('a', class_='mw-kartographer-map')
        image2_2 = image2_1.findAll('img')[0]['src']
        # example = images2[0]
        #example['src']
        print("The image 2 is : ")
        print(image2_2)
#
#
#
        text_list =[headingtext,para1_text,para2_text,image_2,image2_2]
        all_text.append(text_list)

#
        my_file = open('textfile.csv', "w", newline='',encoding='utf-8')
        writer = csv.writer(my_file)
        # for row in all_text:
        #     writer.writerow(row)
        writer.writerows(all_text)
#
#
cc = WebScraping()
cc.test()
#
#
# #     def _download_images(self, image_info):
# #         response = requests.get(image_info[0], stream=True)
# #         realname = ''.join(e for e in image_info[1] if e.isalnum())
# #
# #         file = open(self.folder.format(realname), 'wb')
# #
# #         response.raw.decode_content = True
# #         shutil.copyfileobj(response.raw, file)
# #         del response
# #
# #
# #     def scrape_images(self):
# #         image_info = self._get_info()
# #
# #         for i in range(0, len(image_info)):
# #             self.download_image(image_info[i])
# #
# # def scrape_images(self):
# #     image_info = self._get_info()
# #
# #     for i in range(0, len(image_info)):
# #         self.download_image(image_info[i])