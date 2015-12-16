import requests
import json
import logging

from linker.models import Project
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.contrib.auth.decorators import user_passes_test

API_URL = "https://api.github.com/"
log = logging.getLogger(__name__)

@user_passes_test(is_staff)
def add(username, repository):
	try:
		project = Project.objects.get(username=username, repository=repository)
		#Project already exists therefore we don't proceed
		msg = "Project already exists: " + username + "/" + repository
		log.debug(msg)
		return msg
	except ObjectDoesNotExist:
		#Project does not exist already and it can be added
		try:
			sha, readme = get_metadata(username, repository)
			Project.objects.create(
				sha = sha,
				username = username,
				repository = repository,
				readme = readme)
			log.info("Added a new project! " + username + "/" + repository)
		except ValueError as err:
			log.info(err)

	except MultipleObjectsReturned:
		#An error has ocurred and duplicates have been generated.
		#Further inspection needed
		log.error("Multiple projects with the same pair returned. This should" +
			"not happen")

@user_passes_test(is_staff)
def update(username, repository):
	try:
		project = Project.objects.get(username=username, repository=repository)
		sha, readme = get_metadata(username, repository)

		if sha != project.sha:
			project.sha = sha
			project.readme = readme
			project.save()
			log.info("Updated the project " + username + "/" + repository)

		log.debug("Project has not changed: " + username + "/" + repository)
	except ObjectDoesNotExist:
		log.warn("Project is not in the database and can't be updated " +
			username + ":" + repository)

@user_passes_test(is_staff)
def get_metadata(username, repository):
	url = "{}repos/{}/{}/readme".format(API_URL, username, repository)
	headers = {'User-Agent': 'Mihalea/Reflection'}
	response = requests.get(url, headers)
	content = json.loads(response.text)

	if not 'sha' in content:
		raise ValueError("The project " + username + "/" + repository +
		  "could not be found on github")

	sha = content['sha']

	readme = requests.get(content['download_url'], headers).text
	return sha, readme

def is_staff(user):
	return user.is_staff
