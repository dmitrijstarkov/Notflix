import os, subprocess

for dirname,dirnames,filenames in os.walk('/todo_dashify'):
	for subdirname in dirnames:
		for i,j,filenames in os.walk('todo_dashify/'+str(subdirname)):
			for filename in filenames:
				if filename == 'metadata.txt' or filename == '.DS_Store':
					continue
				else:
					video_dash_file=subdirname+'/'+filename
					video_dash_script='/usr/bin/dashify.sh'
					space = ' '
					print(video_dash_file)
					subprocess.call([video_dash_script+space+video_dash_file],shell=True)

