#!/usr/bin/env python3

import atexit
import os
import pytest
import shutil
import subprocess


#
# Test entities
#

repo = {
    'files': ['ansible.cfg', 'hosts', 'infra.yaml', 'roles/init/tasks/main.yaml'],  # 1.6
}

lab = int(os.environ.get('LAB', 1))


#
# Helper functions
#

def cleanup():
    shutil.rmtree('.pytest_cache', ignore_errors=True)
    shutil.rmtree('__pycache__', ignore_errors=True)


#
# Local tests
#

def test_local_ansible_version():
    out = subprocess.check_output(['ansible', '--version'], text=True).partition('\n')[0]
    assert 'ansible [core 2.21.' in out, f'Wrong Ansible version: {out}'


@pytest.mark.parametrize('file', sorted(set(repo['files'])))
def test_local_repo_file_exists(file):
    assert os.path.exists(file), f'{file} is missing in the repository'


#
# Main
#

atexit.register(cleanup)
