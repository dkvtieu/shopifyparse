import json
import urllib2

# Requests the page and returns the JSON file
def get_page(url, index):
	current_page_url = url 	+ str(index)
	request = urllib2.Request(current_page_url)
	response = urllib2.urlopen(request)
	json_file = json.loads(response.read())
	return json_file

# Returns the item prices within the given JSON file
def get_item_prices(json_file):
	product_list = json_file["products"]
	total_page_price = 0

	# Checks if page is placeholder/empty
	if not product_list:
		return 0
	
	for item in product_list:
		variant_list = item["variants"]
		for variant in variant_list:
			total_page_price += float(variant["price"])

	return total_page_price


def main():
	page_index = 1
	total_price = 0
	page_url = "http://shopicruit.myshopify.com/products.json?page="

	while True:
		current_page_price = get_item_prices(get_page(page_url, page_index))

		if current_page_price == 0:
		 	break
		
		total_price += current_page_price
		page_index += 1


	print "The total cost to buy all clocks and watches would be " + str(total_price)

if __name__ == '__main__':
	main()