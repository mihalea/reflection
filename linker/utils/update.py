import requests
import json
import logging

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

API_URL = "https://api.github.com/"
log = logging.getLogger(__name__)


def update(project):
    try:
        sha, readme = get_metadata(project.username, project.repository)

        if not project.sha or sha != project.sha:
            project.sha = sha
            project.readme = readme
            project.save()
            log.info("Updated the project " + project.username + "/" + project.repository)

        log.debug("Project has not changed: " + project.username + "/" + project.repository)
    except ObjectDoesNotExist:
        log.warn("Project is not in the database and can't be updated " +
                 project.username + ":" + project.repository)


def get_metadata(username, repository):
    url = "{}repos/{}/{}/readme".format(API_URL, username, repository)
    headers = {'User-Agent': 'Mihalea/Reflection'}
    response = requests.get(url, headers)
    content = json.loads(response.text)

    if 'sha' not in content:
        raise ValueError("The project " + username + "/" + repository +
                         " could not be found on github or it doesn't have a readme")

    sha = content['sha']

    readme = requests.get(content['download_url'], headers).text
    return sha, readme
