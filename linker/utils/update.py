import requests
import json
import logging

from linker.models import Project
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

API_URL = "https://api.github.com/"
log = logging.getLogger(__name__)

def add(username, repository):
	try:
		project = Project.objects.get(username=username, repository=repository)
		#Project already exists therefore we don't proceed
		print("Project already exists!")
	except ObjectDoesNotExist:
		#Project does not exist already and it can be added
		try:
			sha, readme = get_metadata(username, repository)
			Project.objects.create(
				sha = sha,
				username = username,
				repository = repository,
				readme = readme)
		except ValueError as err:
			log.info("The provided username:repository could not be found")

	except MultipleObjectsReturned:
		#An error has ocurred and duplicates have been generated.
		#Further inspection needed
		print("THIS SHOULD NOT OCCUR")

def get_metadata(username, repository):
	url = "{}repos/{}/{}/readme".format(API_URL, username, repository)
	headers = {'User-Agent': 'Mihalea/Reflection'}
	response = requests.get(url, headers)
	content = json.loads(response.text)

	if not 'sha' in content:
		raise ValueError("The pair username:repository could not be found")

	sha = content['sha']
	readme = requests.get(content['download_url'], headers).text

	return sha, readme
