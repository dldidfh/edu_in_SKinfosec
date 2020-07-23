from selenium import webdriver
import os

driver = webdriver.Chrome("C:/Users/USER/Desktop/workspace/test_git/python_workspace/homework/chromedriver.exe")

bugNum = 68392
os.getcwd()

for X in range(2):
     driver.get("https://bugs.eclipse.org/bugs/show_bug.cgi?id=" + bugNum.__str__())
     print("https://bugs.eclipse.org/bugs/show_bug.cgi?id="+bugNum.__str__())
     dir_elems = driver.find_elements_by_xpath('//*[@id="c0"]/pre')
     dir_elems_importance = driver.find_elements_by_xpath('[<td>(.*?)[span id ="votes_container">]')
     dir_elems_result = dir_elems + "|" + dir_elems_importance
     bugNum = bugNum + 1
     bugName = bugNum.__str__()
     print(bugNum)
     for str in dir_elems_result:
          print(str.text)
          name = bugName +".txt"
          f = open(name , 'w')
          f.write(str.text)
          f.close()