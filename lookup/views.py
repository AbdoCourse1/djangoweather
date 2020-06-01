from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode +"&distance=5&API_KEY=91421AF4-40E5-4F47-91E1-2E48E249AC51")

		try:
			api=json.loads(api_request.content)
		
			if api[0]['Category']['Name'] == 'Good':
				category_description = "(0 -50) Air quality is considered satisfactory, and air pollution poses little or no risk."
				category_color = "good"
			elif api['0']['Category']['Name']  == "Moderate":
				category_description = "(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people."
				category_color = "Moderate"
			elif api['0']['Category']['Name'] == "USG":
				category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at"
				category_color = "USG"
			elif api['0']['Category']['Name']  == "Unhealthy":
				category_description ="(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
				category_color = "Unhealthy"
			elif api['0']['Category']['Name']  == "Very Unhealthy":
				category_description = "(201 - 300) Health alert: everyone may experince more serious health effects."
				category_color = "Very"

			return render(request, 'home.html', {"api" : api, "category_description" : category_description, "category_color": category_color})
		except Exception as e:
				api= "Eror..."
				return render(request, 'home.html', {"api" : api})

	else:

		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=91421AF4-40E5-4F47-91E1-2E48E249AC51")

		try:
			api=json.loads(api_request.content)
		except Exception as e:
			api= "Eror..."

		if api[0]['Category']['Name'] == 'Good':
			category_description = "(0 -50) Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color = "good"
		elif api['0']['Category']['Name']  == "Moderate":
			category_description = "(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people."
			category_color = "Moderate"
		elif api['0']['Category']['Name'] == "USG":
			category_description = "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at"
			category_color = "USG"
		elif api['0']['Category']['Name']  == "Unhealthy":
			category_description ="(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "Unhealthy"
		elif api['0']['Category']['Name']  == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experince more serious health effects."
			category_color = "Very"

		return render(request, 'home.html', {"api" : api, "category_description" : category_description, "category_color": category_color})

def about(request):
	return render(request, 'about.html', {})