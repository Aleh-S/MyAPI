import requests
import json
from ConfigParser import SafeConfigParser
import os
import inspect
from random import randint
import base64


class Config:
    def __init__(self):
        self.parser = SafeConfigParser()
        if os.path.isfile('config.ini'):
            self.parser.read('config.ini')
        else:
            print('No config.ini found under the root folder.')
        self.domain = self.parser.get('Server', 'url')
        self.admin_login = self.parser.get('Server', 'user')
        self.password = self.parser.get('Server', 'passwd')
        self.puser = self.parser.get('Server', 'puser')
        self.testpath = self.parser.get('Server', 'testpath')



class Calls:
    def __init__(self):
        self.config = Config()
        self.no_json = 'NoJSON'


    def create_folder(self, folder_name, path=None, domain=None, method=None, content_type=None, accept=None,
                      username=None, password=None, print_call=True):

        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'POST'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password
        if path is None:
            path = self.config.testpath

        endpoint = '/public-api/v1/fs'
        url = '%s%s%s/%s' % (domain, endpoint, path, folder_name)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept
        data = dict()
        data['action'] = 'add_folder'
        data = json.dumps(data)

        headers['Authorization'] = 'Basic %s' % base64.b64decode('%s:%s' % (username, password))

        r = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=data
        )

        try:
            json_resp = json.loads(r.content)
        except ValueError:
            json_resp = self.no_json

        r.json = json_resp

        if print_call:

            self.nice_print_out(call_name='Create Folder', r=r, caller=inspect.stack()[1][3])

        return r




    def delete_folder(self, name, parent_path=None,domain=None, method=None, content_type=None, accept=None,
                      username=None, password=None, print_call=True, caller=None):

        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'DELETE'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password
        if caller is None:
            caller = inspect.stack()[1][3]

        endpoint = '/public-api/v1/fs'

        if parent_path is None:
            parent_path = self.config.testpath
        url = domain + endpoint + parent_path + '/' + name
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept

        headers['Authorization'] = 'Basic %s' % base64.b64decode('%s:%s' % (username, password))

        r = requests.request(
            method=method,
            url=url,
            headers=headers
            )

        try:
            json_resp = json.loads(r.content)
        except ValueError:
            json_resp = 'NoJSON'

        r.json = json_resp

        if print_call:
            self.nice_print_out(call_name='Delete Folder', r=r, caller=caller)

        return r



    def move_item(self, name, destination, parent_path=None, domain=None, method=None, content_type=None,
                  accept=None, username=None, password=None, print_call=True):

        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'POST'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password
        if parent_path is None:
            parent_path = self.config.testpath

        endpoint = '/public-api/v1/fs'
        url = '%s%s%s/%s' % (domain, endpoint, parent_path, name)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept
        data = dict()
        data['action'] = 'move'
        data['destination'] = destination + '/' + name
        data = json.dumps(data)

        headers['Authorization'] = 'Basic %s' % base64.b64encode('%s:%s' % (username, password))

        r = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=data
        )

        try:
            json_resp = json.loads(r.content)
        except ValueError:
            json_resp = self.no_json

        r.json = json_resp
        if print_call:
            self.nice_print_out(call_name='Move Item', r=r, caller=inspect.stack()[1][3])

        return r





    def set_perms(self, folder_path, users, permission, domain=None, method=None, content_type=None, accept=None,
                          username=None, password=None, print_call=True):

        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'POST'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password

        endpoint = '/public-api/v1/fs/perms/folder'
        url = '%s%s%s' % (domain, endpoint, folder_path)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept
        data = dict()
        data['users'] = []
        data['permission'] = permission
        if type(users) == list:
            for user in users:
                data['users'].append(user)
        else:
            data['users'].append(users)
        data = json.dumps(data)

        headers['Authorization'] = 'Basic %s' % base64.b64decode('%s:%s' % (username, password))

        r = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=data
            )

        try:
            json_resp = json.loads(r.content)
        except ValueError:
            json_resp = 'NoJSON'
        r.json = json_resp

        if print_call:
            self.nice_print_out(call_name='Set Permissions', r=r, caller=inspect.stack()[1][3])


        return r



    def list_perms(self, folder_path, users, domain=None, method=None, content_type=None, accept=None,
                              username=None, password=None, print_call=True):

        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'GET'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password

        endpoint = '/public-api/v1/fs/perms/folder'
        url = '%s%s%s' % (domain, endpoint, folder_path)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept

        url += '?users=%s' % users

        headers['Authorization'] = 'Basic %s' % base64.b64decode('%s:%s' % (username, password))

        r = requests.request(
            method=method,
            url=url,
            headers=headers
            )

        try:
            json_resp = json.loads(r.content)
        except ValueError:
            json_resp = 'NoJSON'
        r.json = json_resp

        if print_call:
            self.nice_print_out(call_name='List Permissions', r=r, caller=inspect.stack()[1][3])


        return r



    def list_folders(self, folder_path, domain=None, method=None, content_type=None, accept=None, username=None,
                     password=None, print_call=True, caller=None):
        if domain is None:
            domain = self.config.domain
        if method is None:
            method = 'GET'
        if content_type is None:
            content_type = 'application/json'
        if accept is None:
            accept = 'application/json'
        if username is None:
            username = self.config.admin_login
        if password is None:
            password = self.config.password
        if caller is None:
            caller = inspect.stack()[1][3]

        endpoint = '/public-api/v1/fs'
        url = '%s%s%s' % (domain, endpoint, folder_path)
        headers = dict()
        headers['Content-Type'] = content_type
        headers['Accept'] = accept

        headers['Authorization'] = 'Basic %s' % base64.b64decode('%s:%s' % (username, password))

        r = requests.request(
            method=method,
            url=url,
            headers=headers)


        try:
            json_resp = json.loads(r.content)
        except ValueError:
            json_resp = 'NoJSON'

        r.json = json_resp

        if print_call:
            self.nice_print_out(call_name='List Folders', r=r, caller=caller)

        return r

    @staticmethod
    def nice_print_out(call_name, r, caller):
        header_string = ''
        for key in r.request.headers:
            header_string += '-H "%s: %s" ' % (key, r.request.headers[key])
        print('\n*TestCase Name: %s, API Call: %s*' % (caller, call_name))
        if r.request.body:
            print('Curl is:\n curl %s "%s" -d \'%s\' -X %s' % (header_string, r.request.url, r.request.body,
                                                               r.request.method))
        else:
            print('Curl is:\n curl %s "%s" -X %s' % (header_string, r.request.url, r.request.method))
        print('\nResponse status code: %s' % r.status_code)
        if r.json != 'NoJSON':
            try:
                print('\nResponse body:\n %s' % json.dumps(r.json, indent=2))
            except TypeError:
                print('\nResponse body:\n %s' % r.json)
        else:
            print('\nNo body in the response.')



class Utils:
    def __init__(self):
        self.config = Config()
        self.calls = Calls()

    @staticmethod
    def random_name():
        return 'test_name%s' % randint(1000000, 9999999)

    def delete_all_except(self, l):
        resp = self.calls.list_folders(folder_path='/Shared', caller='Cleanup')
        l1 = resp.json
        for i in range(len(l1['folders'])):
            if l1['folders'][i]['name'] in l:
                l1['folders'][i] = None

        while l1['folders'].count(None) != len(l1['folders']):
            for elem in l1['folders']:
                if elem is not None:
                    self.calls.delete_folder(parent_path='/Shared', name=elem['name'], caller='Cleanup')
                    index = l1['folders'].index(elem)
                    del l1['folders'][index]

