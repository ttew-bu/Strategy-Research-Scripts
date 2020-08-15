#Tristan Tew
#GrodalReviewScraper
#This program will utilize various packages to scrape, aggregate, and export review data for wheelchairs from the United Spinal Website.
#Due to website connection issues/firewalls on frequent attempts to open the page, this program does need to run one page at a time and be manually reset

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

#I did not iterate through a loop to get the pages since there were just two URLs to work with

#store the url of the first page
url = 'https://unitedspinal.org/wheelchair-reviews-views/#home/?view_228_page=1&view_228_filters=%5B%7B%22field%22%3A%22field_210%22%2C%22operator%22%3A%22in%22%2C%22value%22%3A%5B%22Manual%20Wheelchair%20Alternate%20Propulsion%22%2C%22Manual%20Wheelchairs%20Carbon%20Frame%22%2C%22Manual%20Wheelchairs%20Folding%22%2C%22Manual%20Wheelchairs%20Heavy%20Duty%20%2F%20Bariatric%22%2C%22Manual%20Wheelchairs%20Magnesium%20Frame%22%2C%22Manual%20Wheelchairs%20Rigid%20Frame%22%2C%22Manual%20Wheelchairs%20Standing%22%2C%22Manual%20Wheelchairs%20Titanium%20Frame%22%2C%22Manual%20Wheelchairs%20Transit%22%2C%22Off%20Road%20Manual%20Wheelchairs%22%2C%22Off%20Road%20Power%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Manual%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Power%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Sports%20Wheelchairs%22%2C%22Power%20Wheelchairs%20Folding%20%26%20Transportable%22%2C%22Power%20Wheelchairs%20Front%20Drive%22%2C%22Power%20Wheelchairs%20Heavy%20Duty%20%2F%20Bariatric%22%2C%22Power%20Wheelchairs%20Mid%20Wheel%20Drive%22%2C%22Power%20Wheelchairs%20Other%22%2C%22Power%20Wheelchairs%20Rear%20Drive%22%2C%22Power%20Wheelchairs%20Standing%22%2C%22Self%20Balancing%20Wheelchairs%22%2C%22Sports%20Multi%20Purpose%20Wheelchair%22%2C%22Wheelchairs%20Stair%20Climbing%22%5D%7D%5D&view_228_per_page=500'

#store the url of the second page 
url_two = 'https://unitedspinal.org/wheelchair-reviews-views/#home/?view_228_page=2&view_228_filters=%5B%7B%22field%22%3A%22field_210%22%2C%22operator%22%3A%22in%22%2C%22value%22%3A%5B%22Manual%20Wheelchair%20Alternate%20Propulsion%22%2C%22Manual%20Wheelchairs%20Carbon%20Frame%22%2C%22Manual%20Wheelchairs%20Folding%22%2C%22Manual%20Wheelchairs%20Heavy%20Duty%20%2F%20Bariatric%22%2C%22Manual%20Wheelchairs%20Magnesium%20Frame%22%2C%22Manual%20Wheelchairs%20Rigid%20Frame%22%2C%22Manual%20Wheelchairs%20Standing%22%2C%22Manual%20Wheelchairs%20Titanium%20Frame%22%2C%22Manual%20Wheelchairs%20Transit%22%2C%22Off%20Road%20Manual%20Wheelchairs%22%2C%22Off%20Road%20Power%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Manual%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Power%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Sports%20Wheelchairs%22%2C%22Power%20Wheelchairs%20Folding%20%26%20Transportable%22%2C%22Power%20Wheelchairs%20Front%20Drive%22%2C%22Power%20Wheelchairs%20Heavy%20Duty%20%2F%20Bariatric%22%2C%22Power%20Wheelchairs%20Mid%20Wheel%20Drive%22%2C%22Power%20Wheelchairs%20Other%22%2C%22Power%20Wheelchairs%20Rear%20Drive%22%2C%22Power%20Wheelchairs%20Standing%22%2C%22Self%20Balancing%20Wheelchairs%22%2C%22Sports%20Multi%20Purpose%20Wheelchair%22%2C%22Wheelchairs%20Stair%20Climbing%22%5D%7D%5D&view_228_per_page=500'

#store a url for small batch testing 
test_url = 'https://unitedspinal.org/wheelchair-reviews-views/#home/?view_228_page=1&view_228_per_page=10'

#define the executable path on the webdriver using the file's destination 
driver = webdriver.Chrome(executable_path='C:/Users/trist/chromedriver/chromedriver.exe')

#get the url in the driver, use either URL or URL_two depending on which page you're trying to scrape
driver.get(url)

try:

    #wait for the page to load using an arbitrary asset that is created via Javascript on the destination page
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'kn-detail-body'))
    )

    #Create an empty dictionary 
    chairs = []

    #Create a counter for product IDs in the database
    num = 0

    #Iterate over the elements on the website within the class that contains all of the Javascript-enabled elements
    for item in driver.find_elements_by_class_name("kn-list-item-container"):

        #Iterate to create unique ID for dataset
        num += 1 

        #idd stores the "id" for every chair that gets loaded on the website
        idd = item.get_attribute("id")

        #Checks to see if the asset exists
        if item.find_elements_by_xpath('//*[@id="%s"]/section/div[1]/div[2]/div/div/div/div/span/h2/strong/span' % idd):

            #store the text of the element that follows this path, which remains the same across all IDs
            name = item.find_element_by_xpath('//*[@id="%s"]/section/div[1]/div[2]/div/div/div/div/span/h2/strong/span' % idd).text

        else: 
            #give a null condition and store it in the dictionary 
            name = "N/A"

        #Same as above but for a different field
        if item.find_elements_by_xpath('//*[@id="%s"]/section/div[1]/div[3]/div[1]/div/div/div/span/strong/em/span' % idd):
            producer = item.find_element_by_xpath('//*[@id="%s"]/section/div[1]/div[3]/div[1]/div/div/div/span/strong/em/span' % idd).text

        else:
            producer = "N/A"

        #Same as above but for a different field
        if item.find_elements_by_xpath('//*[@id="%s"]/section/div[1]/div[3]/div[2]/div/div/div/span/strong/span' % idd):
            producer_country = item.find_element_by_xpath('//*[@id="%s"]/section/div[1]/div[3]/div[2]/div/div/div/span/strong/span' % idd).text

        else:
            producer_country = "N/A"

        #Same as above but for a different field
        if item.find_elements_by_xpath('//*[@id="%s"]/section/div[1]/div[4]/div/div/div/div/span/h2/strong/span' % idd):
            production_status = item.find_element_by_xpath('//*[@id="%s"]/section/div[1]/div[4]/div/div/div/div/span/h2/strong/span' % idd).text

        else:
            production_status = "N/A"

        #Same as above but for a different field
        if item.find_elements_by_xpath('//*[@id="%s"]/section/div[1]/div[5]/div/div/div/div/span/span/p' % idd):
            product_description = item.find_element_by_xpath('//*[@id="%s"]/section/div[1]/div[5]/div/div/div/div/span/span/p[1]' % idd).text
            #print(product_description)

        else: 
            product_description: product_description ="None"

        if item.find_elements_by_xpath('//*[@id="%s"]/section/div[1]/div[5]/div/div/div/div/span/span/p/img' % idd):
            image = item.find_element_by_xpath('//*[@id="%s"]/section/div[1]/div[5]/div/div/div/div/span/span/p/img' % idd).get_attribute("src")
        
        else:
            image = "N/A"
        print(idd)

        #all products have a score or a null value, so it does not require IF/ELSE logic to prevent the program from crashing 
        durability_score = item.find_element_by_xpath('//*[@id="view_228-field_223-%s-value"]' % idd).get_attribute('value')

        #Same as above but for a different field
        user_friendliness_score = item.find_element_by_xpath('//*[@id="view_228-field_222-%s-value"]' % idd).get_attribute('value')

        #Same as above but for a different field
        expectation_score = item.find_element_by_xpath('//*[@id="view_228-field_224-%s-value"]' % idd).get_attribute('value')

        #create a blank accumulator variable that will be used for each chair
        n=0

        #If a product has an undefined score, that is because there are no reviews, so reflect that in the code 
        if durability_score == 'undefined':
            n = 0 

        #Alternatively, for all products that have at least one review
        else:

            #each time this occurs, use the webdriver to open up a new tab
            driver.find_element_by_class_name('kn-link-page').send_keys(Keys.COMMAND + "t")

            #the review url framework to be opened in the new tab and scraped- 
            #luckily, I can just substitute in the ID number for the product to access the reviews over the iterations
            ur = ('https://unitedspinal.org/wheelchair-reviews-views/#home/wheelchair-review-details2/%s/' % idd)

            #Open the new window 
            driver.execute_script("window.open('');")

            #Switch to the new tab 
            driver.switch_to.window(driver.window_handles[1])

            #open the url in the new tab
            driver.get(ur)

            #Delay the scraping until all assets are loaded with a 15 second limit to find the review field loaded in. 
            element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'field_190'))
            )

            #create a loop that counts each review on each chair's page
            for item in driver.find_elements_by_class_name("field_190"):

                n += 1 

            #print(idd)

            #Once the driver has finished scraping the review page close it
            driver.close()

            #Once the driver has closed, switch back to the original window, which is the main list page. 
            driver.switch_to.window(driver.window_handles[0])

        #Add all of the new chairs to the chairs dictionary 
        chairs.append({'Unique ID': num, 'Name': name, 'Producer': producer, 'Producer Country' : producer_country, 'Production Status': production_status, 'Expectation Score': expectation_score, 
        'Durability Score': durability_score, 'Ease of Use Score': user_friendliness_score, 'Product Description': product_description, 'Number of Reviews': n, "Image URL":image})

    #Create an alert for when the scraper has completed the page 
    print('done!')

    #print(chairs)


    #Columns for the CSV should only be active when creating the form, or it will begin appending the original document with an extra set of column names 
    csv_columns = ['Name', 'Producer', 'Producer Country', 'Production Status', "Expectation Score", "Durability Score", 
    "Ease of Use Score", "Product Description", "Number of Reviews", "Image URL"]

    #below are the two command sets for exporting to a CSV. I could not automate the system as it crashed the program, so for the first page I ran the first set and
    #the second one for the second set. 

# only use when initially creating the CSV, not adding on the second page of results
    with open('TEST2.csv', 'w', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for item in chairs:
            writer.writerow(item)

#only use when adding to the the csv, not writing the first set of results
# with open('TEST2.csv', 'a+', encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=csv_columns)
#     writer.writeheader()
#     for item in chairs:
#         writer.writerow(item)

finally:
    driver.quit()

