import docker
import rootpath

from os.path import abspath, join


class Sandbox:
    SCHEMA = {
        "python": "docker_files/Dockerfile.py",
        "golang": "docker_files/Dockerfile.go",
    }

    def __init__(self, client: docker.APIClient, language: str,
                 project_root: str):
        self.client = client
        self.language = language
        self.project_root = project_root

    def parse(self) -> str:
        df_path = abspath(
            join(rootpath.detect(), Sandbox.SCHEMA[self.language]))

        with open(df_path, "r") as df:
            image = self.client.images.build(
                fileobj=df,
                custom_context=True,
                buildargs={"PROJECT_ROOT": self.project_root})

        return self.client.containers.run(image).attach()
