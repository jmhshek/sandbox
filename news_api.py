import requests
import json
import pandas
from io import StringIO 

# The headers remain the same for all the requests
headers = {'Authorization': 'b7de039e294740bb84d8dff8c2bbf97d'}

# All the endpoints in this section

# To fetch the top headlines
top_headlines_url = 'https://newsapi.org/v2/top-headlines'
# To fetch news articles
everything_news_url = 'https://newsapi.org/v2/everything'
# To retrieve the sources
sources_url = 'https://newsapi.org/v2/sources'

# Add parameters to request URL based on what type of headlines news you want

# All the payloads in this section
headlines_payload = {'category': 'business', 'country': 'us'}
everything_payload = {'q': 'finance', 'language': 'en', 'sortBy': 'popularity'}
sources_payload = {'category': 'general', 'language': 'en', 'country': 'us'}

# Fire a request based on the requirement, just change the url and the params field

# Request to fetch the top headlines
response = requests.get(url=top_headlines_url, headers=headers, params=headlines_payload)

# Request to fetch every news article
#response = requests.get(url=everything_news_url, headers=headers, params=everything_payload)

# Request to fetch the sources
# response = requests.get(url=sources_url, headers=headers, params=sources_payload)

# If you just want to print
pretty_json_output = json.dumps(response.json(), indent=4)
print(pretty_json_output)
# print(response.json())

# To store the relevant json data to a csv

# Convert response to a pure json string
response_json_string = json.dumps(response.json())

# A json object is equivalent to a dictionary in Python
# retrieve json objects to a python dict
response_dict = json.loads(response_json_string)
print(response_dict)

# Info about articles is represented as an array in the json response
# A json array is equivalent to a list in python
# We want info only about articles
articles_list = response_dict['articles']

# We want info only about sources
# sources_list = response_dict['sources']
# And then you can specify one of these sources explicitly if you like while fetching the news

# Convert articles list to json string , convert json string to dataframe , write df to csv!
df = pandas.read_json(StringIO(json.dumps((articles_list))))

# Convert sources list to json string , convert json string to dataframe , write df to csv!
# df = pandas.read_json(json.dumps(sources_list))
