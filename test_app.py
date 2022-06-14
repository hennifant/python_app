
from urllib import response
from app import app, get_post


import unittest

class TestWebApp(unittest.TestCase):

    def test_index(self):
       test=app.test_client(self)
       response=test.get('/')
       statuscode=response.status_code
       self.assertEqual(statuscode,200)

    def test_edit(self):
        tester=app.test_client(self)
        tester.post('/edit',data={'post': ''}, follow_redirects=True)
        try:
            id = get_post.query.first().id
        except:
            return print ('Nothing to edit')
        response=tester.get('/edit/{}'.format(id), follow_redirects=True)
        statuscode=response.status_code
        self.assertTrue(b'Editieren'in response.data)
        self.assertEqual(statuscode,200)

    def test_delete(self):
        tester=app.test_client(self)
        tester.post('/delete',data={'post': ''}, follow_redirects=True)
        try:
            id = get_post.query.first().id
        except:
            return print ('Nothing to delete')
        response=tester.get('/delete/{}'.format(id), follow_redirects=True)
        statuscode=response.status_code
        self.assertTrue(b'Eintrag loeschen'in response.data)
        self.assertEqual(statuscode,200)

#
if __name__ == '__main__':
   unittest.main() 