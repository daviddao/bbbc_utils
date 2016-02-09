csv_url = "https://www.broadinstitute.org/bbbc/BBBC021/BBBC021_v1_image.csv"

import urllib2
import sys
import pandas as pd

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

	# First download the CSV
	download(csv_url)

	# Create a pandas dataframe
	df = pd.read_csv("./BBBC021_v1_image.csv")

	string = argv[0] + "_"
	df_filtered = df[df.Image_PathName_Actin.str.contains(string)] 
	df_filtered.to_csv(index=False)

if __name__ == "__main__":
	main(sys.argv[1:])
