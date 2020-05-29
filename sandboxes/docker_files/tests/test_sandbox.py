import docker
import pytest

from os.path import abspath, dirname, join

from sandbox import Sandbox


class TestSandbox:
    @pytest.fixture(scope="module")
    def client(self) -> docker.APIClient:
        return docker.DockerClient(base_url="unix:///var/run/docker.sock")

    def test_go_sample(self, client):
        d_name = dirname(__file__)
        box = Sandbox(client=client,
                      language="golang",
                      project_root=abspath(join(d_name, "test_go_sample")))

        assert box.parse() == "Hello World!\n"
