
# Get all a and convert them into an array
var list = document.getElementsByTagName('a')
var array = [].splice.call(list)

# Get the links
var array = array.map(function(x){return x.href})

# Filter for links with BBBC in it
function get_zips(x) {
	if (x.split(".").pop() === "zip") {
		return true
	} else {
		return false
	}
}

# All the links of the zipped files
array = array.filter(get_zips)
