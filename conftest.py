import os
import shutil
import pytest
from utils import tmp


@pytest.fixture(scope="function")
def tmp_directory():
    if not os.path.exists(tmp):
        os.mkdir('tmp')

    yield

    shutil.rmtree(tmp)