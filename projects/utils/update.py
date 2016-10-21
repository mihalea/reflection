import requests
import json
import logging

from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.utils.dateparse import parse_datetime

API_URL = "https://api.github.com/"
log = logging.getLogger(__name__)
headers = {
    'User-Agent': 'Mihalea/Reflection',
    'Time-Zone': 'Europe/London'
}


# Update the project's metadata and commit it
def update(project, commit=True):
    try:
        log.debug("Updating project %s/%s" % (project.username, project.repository))
        metadata = get_metadata(project)
        download = get_download(project)

        project.updated_at = parse_datetime(metadata['updated_at'])
        project.language = metadata['language']
        project.description = metadata['description']

        """
        Update the readme if the sha stored in the database is different from the one requested now.
        Or if there is no sha it means there is no readme stored.
        """
        if download and (not project.sha or download['sha'] != project.sha):
            project.sha = download['sha']
            project.download_url = download['download_url']
            project.readme = get_readme(project)
            log.info("Updated the project's readme: " + project.username + "/" + project.repository)

        if commit:
            project.save()
        log.debug("Updated the project: " + project.username + "/" + project.repository)
    except ObjectDoesNotExist:
        log.warn("Project is not in the database and can't be updated " +
                 project.username + ":" + project.repository)
    except ValueError as err:
        log.warn(err)


def get_metadata(project):
    """ Get metadata from the API according to the values specified below """

    url = "{}repos/{}/{}".format(API_URL, project.username, project.repository)
    response = requests.get(url, headers)
    content = json.loads(response.text)

    fields = ['updated_at', 'language', 'description']
    results = {}
    for field in fields:
        if field not in content:
            raise ValueError("Could not find field '{}' for repository {}/{}".format(field,
                                                                                     project.username,
                                                                                     project.repository))

        results[field] = content[field]

    return results


def get_readme(project):
    """ Get the readme as a string if the url has been set, otherwise throw an error"""
    if not project.download_url:
        raise ValueError("The project {}/{} does not have a readme set".format(project.username, project.repository))

    readme = requests.get(project.download_url, headers).text
    return readme


def get_download(project):
    """ Get the readme's sha and download url """
    url = "{}repos/{}/{}/readme".format(API_URL, project.username, project.repository)
    response = requests.get(url, headers)
    content = json.loads(response.text)

    if 'sha' not in content or 'download_url' not in content:
        return None

    results = {
        'sha': content['sha'],
        'download_url': content['download_url'],
    }

    return results
