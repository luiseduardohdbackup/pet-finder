#!/usr/bin/python2.5
# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup and teardown fixtures for all the tests in the tests/ directory."""

import os
import sys
import unittest

from google.appengine.api import apiproxy_stub_map
from google.appengine.api import datastore_file_stub

import remote_api

def setup():
    # Create a new apiproxy and temp datastore to use for this test suite
    apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()
    temp_db = datastore_file_stub.DatastoreFileStub(
        'PersonFinderUnittestDataStore', None, None, trusted=True)
    apiproxy_stub_map.apiproxy.RegisterStub('datastore', temp_db)

    # An application id is required to access the datastore, so let's create one
    os.environ['APPLICATION_ID'] = 'person-finder-test'
