from sqlalchemy.orm import Session
from unittest import TestCase
from unittest.mock import create_autospec, patch

from repositories.AuthorRepository import AuthorRepository


class TestAuthorRepository(TestCase):
    session: Session
    authorRepository: AuthorRepository

    def setUp(self):
        super().setUp()
        self.session = create_autospec(Session)
        self.authorRepository = AuthorRepository(
            self.session
        )

    @patch("models.AuthorModel.Author", autospec=True)
    def test_create(self, Author):
        author = Author(name="JK Rowling")
        self.authorRepository.create(author)

        # Should call add method on Session
        self.session.add.assert_called_once_with(author)

    @patch("models.AuthorModel.Author", autospec=True)
    def test_delete(self, Author):
        author = Author(id=1)
        self.authorRepository.delete(author)

        # Should call delete method on Session
        self.session.delete.assert_called_once_with(author)

    @patch("models.AuthorModel.Author", autospec=True)
    def test_get(self, Author):
        author = Author(id=1)
        self.authorRepository.get(author)

        # Should call get method on Session
        self.session.get.assert_called_once()

    @patch("models.AuthorModel.Author", autospec=True)
    def test_list(self, Author):
        self.authorRepository.list(None, 100, 0)

        # Should call query method on Session
        self.session.query.assert_called_once()

        self.authorRepository.list("Stephen Knight", 100, 0)

        # Should call filter_by method on QueryResponse
        self.session.query(
            Author
        ).filter_by.assert_called_once_with(
            name="Stephen Knight"
        )

    @patch("models.AuthorModel.Author", autospec=True)
    def test_update(self, Author):
        author = Author(name="Ray Dalio")
        self.authorRepository.update(id=1, author=author)

        # Should call merge method on Session
        self.session.merge.assert_called_once_with(author)
