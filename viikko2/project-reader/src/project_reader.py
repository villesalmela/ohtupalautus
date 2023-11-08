from urllib import request
from project import Project
import tomllib # standard library since python 3.11


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono
        data = tomllib.loads(content)
        poetry_data = data["tool"]["poetry"]

        # ja muodosta Project-olio sen tietojen perusteella
        return Project(name=poetry_data["name"], license=poetry_data["license"], authors=poetry_data["authors"], description=poetry_data["description"], dependencies=poetry_data["dependencies"], dev_dependencies=poetry_data["group"]["dev"]["dependencies"])
