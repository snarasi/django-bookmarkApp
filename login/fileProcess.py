#fileProcess.py
def process_uploaded_file(f):
	with open('temp.html','wb+') as temp_file_destination:
		for chunk in f.chunks():
			temp_file_destination.write(chunk)
