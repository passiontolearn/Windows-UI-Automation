from splinter import Browser
import datetime
import time

browser = Browser('chrome')

minutes_to_run=3
counter=0
finish_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes_to_run)
while datetime.datetime.now() < finish_time:
	browser.visit('http://google.com?hl=en')
	browser.fill('q', 'ebay\n')
	'''
	if browser.is_text_present('ebay'):
		print("Yes, the official website was found!")
	else:
		print("No, it wasn't found... We need to improve our SEO techniques")
	'''	
	browser.click_link_by_partial_text('eBay:')
	counter +=1
	print("Finished ",counter, " time(s)")
	time.sleep(0.01)
	
#browser.quit()