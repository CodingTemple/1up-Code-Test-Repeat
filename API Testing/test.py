import unittest
from app import app, db, Entry

class EntryAPITestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.context = app.app_context()
        self.context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def test_create_entry(self):
        response = self.app.post('/entries', json={'content': 'Test Entry'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertTrue(data['id'] > 0)

    def test_get_entry(self):
        entry = Entry(content='Test Entry')
        db.session.add(entry)
        db.session.commit()
        response = self.app.get(f'/entries/{entry.id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['content'], 'Test Entry')

    def test_update_entry(self):
        entry = Entry(content='Initial Content')
        db.session.add(entry)
        db.session.commit()
        response = self.app.put(f'/entries/{entry.id}', json={'content': 'Updated Content'})
        self.assertEqual(response.status_code, 200)
        # Use session.get() to retrieve the updated entry
        updated_entry = db.session.get(Entry, entry.id)
        self.assertEqual(updated_entry.content, 'Updated Content')

    def test_delete_entry(self):
        entry = Entry(content='Test Entry')
        db.session.add(entry)
        db.session.commit()
        response = self.app.delete(f'/entries/{entry.id}')
        self.assertEqual(response.status_code, 204)
        # Use session.get() to check if the entry has been deleted
        deleted_entry = db.session.get(Entry, entry.id)
        self.assertIsNone(deleted_entry)

if __name__ == '__main__':
    unittest.main()
