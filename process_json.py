#Simple code that takes a given bussiness ID and finds all 
#similar bussiness in the same city
# We can start here and build upon this.

import json
import ijson
import time
from pprint import pprint


target_business_id = "0DI8Dt2PJp07XkVvIElIcQ"
yelp_file_business = "/Users/AswinAk/Downloads/yelp_dataset_challenge_round9/yelp_academic_dataset_business.json"

yelp_similar_businesses = []
target_business_object = None

#This will read the json file line by line and find the bussiness with the corresponding ID
with open(yelp_file_business) as f:
  for line in f:
    temp_business = json.loads(line)
    if temp_business["business_id"] == target_business_id:
      target_business_object = temp_business
      break


print 'Found business', target_business_object["name"]

#Category, zip and city of the target business
business_category = target_business_object["categories"]   #each business is assigned several categories, check the data
business_city = target_business_object["city"]
business_zip = target_business_object["postal_code"]

print 'categories: ',business_category

#This will again go through the entire file line by line and look for businesses with similar categories and in the same city
with open(yelp_file_business) as f:
  for line in f:
    temp_business = json.loads(line)
    temp_categories = temp_business["categories"]
    if not temp_categories is None:
      #print set(temp_categories).intersection(set(business_category))
      if len(set(temp_categories).intersection(set(business_category))) > 2:   #looking for businesses that have atleas 3 categories in common
      	if temp_business["city"] == business_city:
          yelp_similar_businesses.append(temp_business)

# the list yelp_similar_businesses will now contain all similar bussiness in the same city
print 'No of similar businesses: ',len(yelp_similar_businesses)




