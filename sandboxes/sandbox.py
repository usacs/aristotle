import docker
import rootpath

from os.path import abspath, join
from dataclasses import dataclass
from typing import Dict


@dataclass
class Sandbox:
    """ A data type to abstract the notion of a development "sandbox"

    This is an interface to test and run Dockerized software
    on an arbitrary container runtime (either local or remote).

    Args:
        client (docker.APIClient): Client for container runtime
        langauge (str): Desired programming language of the sandbox
        project_root (str): Global path to directory location in Docker build
            context (same server as the runtime itself)
    """
    SCHEMA: Dict[str, str] = {
        "python": "docker_files/Dockerfile.py",
        "golang": "docker_files/Dockerfile.go",
    }
    client: docker.APIClient
    language: str
    project_root: str

    def execute(self) -> docker.models.containers.Container:
        """ Builds and runs associated Dockerfile on :client:

        Returns:
            str: Output and error traces from the container at runtime

        Raises:
            docker.errors.APIError: If the server returns any other error
            docker.errors.BuildError: If there is an error in the build
            docker.errors.ImageNotFound: If the image is not found on the
                Docker server - this would generally indicate server-side
                corruption
        """
        dockerfile_path = abspath(
            join(rootpath.detect(), Sandbox.SCHEMA[self.language]))

        with open(dockerfile_path, "r") as df:
            image = self.client.images.build(
                fileobj=df,
                custom_context=True,
                buildargs={"PROJECT_ROOT": self.project_root})

        return self.client.containers.run(image, detach=True).attach()
