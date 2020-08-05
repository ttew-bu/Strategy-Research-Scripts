#Tristan Tew
#IndividualReviewScraper

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


#store the url of the first page
url = 'https://unitedspinal.org/wheelchair-reviews-views/#home/?view_228_page=1&view_228_filters=%5B%7B%22field%22%3A%22field_210%22%2C%22operator%22%3A%22in%22%2C%22value%22%3A%5B%22Manual%20Wheelchair%20Alternate%20Propulsion%22%2C%22Manual%20Wheelchairs%20Carbon%20Frame%22%2C%22Manual%20Wheelchairs%20Folding%22%2C%22Manual%20Wheelchairs%20Heavy%20Duty%20%2F%20Bariatric%22%2C%22Manual%20Wheelchairs%20Magnesium%20Frame%22%2C%22Manual%20Wheelchairs%20Rigid%20Frame%22%2C%22Manual%20Wheelchairs%20Standing%22%2C%22Manual%20Wheelchairs%20Titanium%20Frame%22%2C%22Manual%20Wheelchairs%20Transit%22%2C%22Off%20Road%20Manual%20Wheelchairs%22%2C%22Off%20Road%20Power%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Manual%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Power%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Sports%20Wheelchairs%22%2C%22Power%20Wheelchairs%20Folding%20%26%20Transportable%22%2C%22Power%20Wheelchairs%20Front%20Drive%22%2C%22Power%20Wheelchairs%20Heavy%20Duty%20%2F%20Bariatric%22%2C%22Power%20Wheelchairs%20Mid%20Wheel%20Drive%22%2C%22Power%20Wheelchairs%20Other%22%2C%22Power%20Wheelchairs%20Rear%20Drive%22%2C%22Power%20Wheelchairs%20Standing%22%2C%22Self%20Balancing%20Wheelchairs%22%2C%22Sports%20Multi%20Purpose%20Wheelchair%22%2C%22Wheelchairs%20Stair%20Climbing%22%5D%7D%5D&view_228_per_page=500'

#store the url of the second page 
url_two = 'https://unitedspinal.org/wheelchair-reviews-views/#home/?view_228_page=2&view_228_filters=%5B%7B%22field%22%3A%22field_210%22%2C%22operator%22%3A%22in%22%2C%22value%22%3A%5B%22Manual%20Wheelchair%20Alternate%20Propulsion%22%2C%22Manual%20Wheelchairs%20Carbon%20Frame%22%2C%22Manual%20Wheelchairs%20Folding%22%2C%22Manual%20Wheelchairs%20Heavy%20Duty%20%2F%20Bariatric%22%2C%22Manual%20Wheelchairs%20Magnesium%20Frame%22%2C%22Manual%20Wheelchairs%20Rigid%20Frame%22%2C%22Manual%20Wheelchairs%20Standing%22%2C%22Manual%20Wheelchairs%20Titanium%20Frame%22%2C%22Manual%20Wheelchairs%20Transit%22%2C%22Off%20Road%20Manual%20Wheelchairs%22%2C%22Off%20Road%20Power%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Manual%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Power%20Wheelchairs%22%2C%22Pediatric%2FYouth%20Sports%20Wheelchairs%22%2C%22Power%20Wheelchairs%20Folding%20%26%20Transportable%22%2C%22Power%20Wheelchairs%20Front%20Drive%22%2C%22Power%20Wheelchairs%20Heavy%20Duty%20%2F%20Bariatric%22%2C%22Power%20Wheelchairs%20Mid%20Wheel%20Drive%22%2C%22Power%20Wheelchairs%20Other%22%2C%22Power%20Wheelchairs%20Rear%20Drive%22%2C%22Power%20Wheelchairs%20Standing%22%2C%22Self%20Balancing%20Wheelchairs%22%2C%22Sports%20Multi%20Purpose%20Wheelchair%22%2C%22Wheelchairs%20Stair%20Climbing%22%5D%7D%5D&view_228_per_page=500'

#store a url for small batch testing 
test_url = 'https://unitedspinal.org/wheelchair-reviews-views/#home/?view_228_page=1&view_228_per_page=10'

#define the executable path on the webdriver using the file's destination 
driver = webdriver.Chrome(executable_path='C:/Users/trist/chromedriver/chromedriver.exe')

#get the url in the driver, use either URL or URL_two depending on which page you're trying to scrape
driver.get(url_two)

#Create an empty dictionary 
chairs = []

try:

    #wait for the page to load using an arbitrary asset that is created via Javascript on the destination page
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'view_228-field_223-5d13e3553ce161255b4bdaae-value'))
        #5d13e3483ce161255b4bd2cc - used in the line above when waiting for the first page to load 
        #5d13e3553ce161255b4bdaae - used in the line above when waiting for the second page to load 
        #5d13e34a3ce161255b4bd3cd - used for small batch tests to make sure the program works
    )

    #Iterate over the elements on the website within the class that contains all of the Javascript-enabled elements
    for item in driver.find_elements_by_class_name("kn-list-item-container"):

        #idd stores the "id" for every chair that gets loaded on the website
        idd = item.get_attribute("id")
        #print(idd)

        #Checks to see if the asset exists
        if item.find_elements_by_xpath('//*[@id="%s"]/section/div[1]/div[2]/div/div/div/div/span/h2/strong/span' % idd):

            #store the text of the element that follows this path, which remains the same across all IDs
            name = item.find_element_by_xpath('//*[@id="%s"]/section/div[1]/div[2]/div/div/div/div/span/h2/strong/span' % idd).text
        else:
            #give a null condition and store it in the dictionary 
            name = "N/A"

        #all products have a score or a null value, so it does not require IF/ELSE logic to prevent the program from crashing 
        durability_score = item.find_element_by_xpath('//*[@id="view_228-field_223-%s-value"]' % idd).get_attribute('value')
        #print(durability_score)

        #create a blank accumulator variable that will be used for each chair
        n = 0

        #If a product has an undefined score, that is because there are no reviews, so reflect that in the code 
        if durability_score == 'undefined':
            n = 0 

            #Skip the rest of the loop if there are no scores to review 
            continue

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
            for item in driver.find_elements_by_class_name("kn-list-item-container"):
                
                review_name = name
                #print(review_name)

                n +=1 
                # print (n)

                review_id = item.get_attribute("id")
                #print(review_id)

                review_num = n 

                if item.find_elements_by_xpath('//*[@id="%s"]/section/div/div[1]/div/div/div' % review_id):
                    author = item.find_element_by_xpath('//*[@id="%s"]/section/div/div[1]/div/div/div' % review_id).text 
                else: 
                    author = "N/A"

                rev_dur_score = item.find_element_by_xpath('//*[@id="view_233-field_197-%s-value"]' % review_id).get_attribute('value')
                #print(rev_dur_score)

                rev_ease_score = item.find_element_by_xpath('//*[@id="view_233-field_198-%s-value"]' % review_id).get_attribute('value')

                rev_expectations_score = item.find_element_by_xpath('//*[@id="view_233-field_199-%s-value"]' % review_id).get_attribute('value')

                if item.find_elements_by_xpath('//*[@id="%s"]/section/div/div[4]/div/div/div[2]' % review_id):
                    strengths = item.find_element_by_xpath('//*[@id="%s"]/section/div/div[4]/div/div/div[2]' % review_id).text 
                else: 
                    strengths = "N/A"

                if item.find_elements_by_xpath('//*[@id="%s"]/section/div/div[4]/div/div/div[4]' % review_id):
                    weaknesses = item.find_element_by_xpath('//*[@id="%s"]/section/div/div[4]/div/div/div[4]' % review_id).text 
                else: 
                    weakenesses = "N/A"

                if item.find_elements_by_xpath('//*[@id="%s"]/section/div/div[4]/div/div/div[6]' % review_id):
                    other_comments = item.find_element_by_xpath('//*[@id="%s"]/section/div/div[4]/div/div/div[6]' % review_id).text 
                else: 
                    other_comments = "N/A" 

                #Add all of the new chairs to the chairs dictionary 
                chairs.append({'review name': review_name, 'review id': review_id, 'review number': review_num, 'review author': author, 'review duration score':rev_dur_score, 
                'review ease score': rev_ease_score, 'review expectation score': rev_expectations_score, 
                'strengths': strengths, 'weaknesses': weaknesses, 'other comments': other_comments})

        #Once the driver has finished scraping the review page close it
        driver.close()

        #Once the driver has closed, switch back to the original window, which is the main list page. 
        driver.switch_to.window(driver.window_handles[0])

    #Create an alert for when the scraper has completed the page 
    print('done!')


    csv_columns = ['review name', 'review number', 'review author', 'review duration score', 'review ease score', 
    'review expectation score', 'strengths', 'weaknesses', 'other comments', 'review id']

    #only use when initially creating the CSV, not adding on the second page of results
    # with open('TEST2.csv', 'w', encoding="utf-8") as f:
    #     writer = csv.DictWriter(f, fieldnames=csv_columns)
    #     writer.writeheader()
    #     for item in chairs:
    #         writer.writerow(item)
    #only use when adding to the the csv, not writing the first set of results
    with open('TEST2.csv', 'a+', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for item in chairs:
            writer.writerow(item)

finally:
    driver.quit()