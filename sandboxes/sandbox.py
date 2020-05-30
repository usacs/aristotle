import docker
import rootpath

from os.path import abspath, join
from dataclasses import dataclass
from typing import Dict


@dataclass
class Sandbox:
    SCHEMA: Dict[str, str] = {
        "python": "docker_files/Dockerfile.py",
        "golang": "docker_files/Dockerfile.go",
    }
    client: docker.APIClient
    language: str
    project_root: str

    def execute(self) -> docker.models.containers.Container:
        dockerfile_path = abspath(
            join(rootpath.detect(), Sandbox.SCHEMA[self.language]))

        with open(dockerfile_path, "r") as df:
            image = self.client.images.build(
                fileobj=df,
                custom_context=True,
                buildargs={"PROJECT_ROOT": self.project_root})

        return self.client.containers.run(image, detach=True).attach()
