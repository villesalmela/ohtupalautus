class Project:
    def __init__(self, name, license, authors, description, dependencies, dev_dependencies):
        self.name = name
        self.license = license
        self.authors = authors
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n- " + "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: {self._stringify_dependencies(self.authors)}"
            f"\n\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
