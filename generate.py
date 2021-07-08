# AUTHOR/DEVELOPER: JISHAN SHAIKH

# How input.txt is generated?
# Bash script (in /svg/)
# $ ls --format=single-column > input.txt

# How to execute this file?
# python3 generate.py > output.txt
# python3 generate.py > previews.html
# FOR INDEX.HTML FILE (Comment line 20, Uncomment line 21)
# python3 generate.py > docs/index.html 

all_files = open('input.txt', 'r')
Lines = all_files.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
	count += 1
	print("<img src=\"svg/{}\" />\n".format(line.strip()))
	#print("<img src=\"../svg/{}\" />\n".format(line.strip()))
	
print("Total lines printed: {}".format(count))
