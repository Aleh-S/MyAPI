import pubapiutils
import httplib

def test_delete_5_folders_positive():
    no_json = 'NoJSON'

    # folder_name = 'test_folder'
    # resp = pubapiutils.delete_folder(folder_name)
    # assert resp.status_code == httplib.OK
    # assert resp.json == no_json


    for i in range(1, 5):
        folder_name = 'testAPI%s' % i
        resp = pubapiutils.delete_folder(folder_name)
        assert resp.status_code == httplib.OK
        assert resp.json == no_json




    #
    #     folder_path = '/Shared/test_folder'
    # l = []
    # for i in range(5):
    #     folder_name = 'test_folder%s' % i
    #     resp = pubapiutils.create_folder(folder_name)
    #     assert resp.status_code == httplib.CREATED
    #     assert resp.json == no_json
    #     l.append(folder_name)
    # for item in l:
    #     resp = pubapiutils.delete_folder(folder_path=folder_path + item)
    #     assert resp.status_code == httplib.OK