#!/usr/bin/python

# BBBC021 dataset
links = [
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week1_22123.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week1_22141.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week1_22161.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week1_22361.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week1_22381.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week1_22401.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week2_24121.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week2_24141.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week2_24161.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week2_24361.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week2_24381.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week2_24401.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week3_25421.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week3_25441.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week3_25461.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week3_25681.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week3_25701.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week3_25721.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week4_27481.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week4_27521.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week4_27542.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week4_27801.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week4_27821.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week4_27861.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week5_28901.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week5_28921.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week5_28961.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week5_29301.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week5_29321.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week5_29341.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week6_31641.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week6_31661.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week6_31681.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week6_32061.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week6_32121.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week6_32161.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week7_34341.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week7_34381.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week7_34641.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week7_34661.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week7_34681.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week8_38203.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week8_38221.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week8_38241.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week8_38341.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week8_38342.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week9_39206.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week9_39221.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week9_39222.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week9_39282.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week9_39283.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week9_39301.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week10_40111.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week10_40115.zip",
  "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_images_Week10_40119.zip"
]

import urllib2
import sys

# Input url
def download(url):

	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,

	f.close()

def main(argv):
	if len(argv) == 0:
		filtered_links = links		
	else:

		def filterForWeek(url):
			if url.find(argv[0]) != -1 and url[url.find(argv[0]) + len(argv[0])] == '_':
				return True
			else:
				return False

		filtered_links = filter(filterForWeek, links)

	print "Script is going to download these files:"
	print filtered_links
	raw_input("Press Enter to continue ...")

	for url in filtered_links:
		download(url)

if __name__ == "__main__":
	main(sys.argv[1:])




