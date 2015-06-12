import pubapiutils
import httplib

def test_create_delete_5_folders_positive():
    no_json = 'NoJSON'
    for i in range(5):
        folder_name = 'test_folder%s' % i
        resp = pubapiutils.create_folder(folder_name)
        assert resp.status_code == httplib.CREATED
        assert resp.json == no_json

        resp = pubapiutils.delete_folder(folder_name)
        assert resp.status_code == httplib.OK
        assert resp.json == no_json

