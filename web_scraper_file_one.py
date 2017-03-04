import urllib
import lxml.html
import final_second

first_url = 'http://www.thelearningpoint.net/system/app/pages/search?scope=search-site&q=school&offset=10'

# scrapping off first ten pages of URL by incrementing the offset value from 10 to 100
for k in range(10, 101):
    next_url = first_url + str(k)
    connection = urllib.urlopen(first_url)
    dom = lxml.html.fromstring(connection.read())

print "Please find the school details in schools_details.csv file"

# creating the required CSV file to store the data
filename = "schools_details.csv"
f = open(filename, "a")

headers = "School_Name, Email_id\n"

f.write(headers)
f.close()

url1 = "http://www.thelearningpoint.net"

l = list()
i = 0

for link in dom.xpath('//div/h3/a/@href'):  # select the url in href for all a tags(links)
    new_url = url1 + link
    l.insert(i, new_url)
    final_second.school_fun(l[i])
    i += 1
