from selenium import webdriver
from selenium.webdriver.chrome.options import Options

list_selector = [
  ["Bid(売値): ", "#root > main > div > div > div.XuqDlHPN > div._1IdtoV3i._2_d3RQf- > section._15smr45n._3D9KIUuT > div._2QdA_Jef > div > div._1vVJ9oXd._3ucBcVhW._2WmlQPbU > dl > dd"],
  ["Bid(買値): ", "#root > main > div > div > div.XuqDlHPN > div._1IdtoV3i._2_d3RQf- > section._15smr45n._3D9KIUuT > div._2QdA_Jef > div > div._1vVJ9oXd._3ucBcVhW._2t_FjeGH > dl > dd"],
  ["Change(始値比): ", "#root > main > div > div > div.XuqDlHPN > div._1IdtoV3i._2_d3RQf- > section._15smr45n._3D9KIUuT > div._2QdA_Jef > div > div._1vVJ9oXd._3ucBcVhW._4hyc0hX3 > dl > dd > span"],
  ["Open: ", "#root > main > div > div > div.XuqDlHPN > div._1IdtoV3i._2_d3RQf- > section._15smr45n._3D9KIUuT > div._2QdA_Jef > div > div._1vVJ9oXd._3ucBcVhW._1TcUUbuF > dl > dd"],
  ["High: ", "#root > main > div > div > div.XuqDlHPN > div._1IdtoV3i._2_d3RQf- > section._15smr45n._3D9KIUuT > div._2QdA_Jef > div > div._1vVJ9oXd._3ucBcVhW.l3zz7oWf > dl > dd"],
  ["Low: ", "#root > main > div > div > div.XuqDlHPN > div._1IdtoV3i._2_d3RQf- > section._15smr45n._3D9KIUuT > div._2QdA_Jef > div > div._1vVJ9oXd._3ucBcVhW._2zemqNZx > dl > dd"],
]



#print(list_selector[0][0])


import sys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

url = "https://finance.yahoo.co.jp/quote/USDJPY=FX"

driver.get(url)

#html = driver.page_source

for list in list_selector:
  #print("list[0] = :" + list[0])
  #print("list[1] = :" + list[1])

  mess = driver.find_element_by_css_selector(list[1])
  print(list[0] + str(mess.text).replace('\n',''))
  #exit()

driver.quit()
exit()
