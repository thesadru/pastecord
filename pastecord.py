"""Api wrapper for pastecord.com

Create a new pastecord document:
>>> document = create_document('print("Hello World!")')
>>> document
Document('wivewoniki')
>>> document.url
'https://pastecord.com/wivewoniki'
>>> print(document.read())
print("Hello World!")

Save a pastecord document:
>>> d = Document('https://pastecord.com/wivewoniki')
>>> d.save()
"""
import re
from typing import Optional, Union

import requests


def _parse_url(url: str) -> Optional[str]:
    """Parse a pastecord url"""
    match = re.search(r"pastecord.com(?:/raw|/documents)?/(\w+)(?:\.\w+)?", url)
    if match is None:
        return None
    return match.group(1)

class Document:
    """A pastecord document object"""
    key: str
    
    def __init__(self, key: str) -> None:
        """Initialize a new document with either a key or a url
        
        >>> Document('yjiqonigoj')
        Document('yjiqonigoj')
        >>> Document('https://pastecord.com/rowelysaki.py')
        Document('rowelysaki')
        """
        self.key = _parse_url(key) or key
    
    def __repr__(self) -> str:
        return f"{type(self).__qualname__}({self.key!r})"
    
    @property
    def url(self) -> str:
        """Direct url to the document"""
        return self.url_as()
    
    @property
    def raw_url(self) -> str:
        """Url to the raw document data"""
        return self.url_as(raw=True)
    
    def url_as(self, extension: str = None, raw: bool = False, document: bool = False) -> str:
        """Create a url to the document
        
        >>> document = Document('cicegavyca')
        >>> document.url_as('py')
        'https://pastecord.com/cicegavyca.py'
        >>> document.url_as(raw=True)
        'https://pastecord.com/raw/cicegavyca'
        >>> document.url_as(document=True)
        'https://pastecord.com/documents/cicegavyca'
        """
        if raw and document:
            raise TypeError("url cannot be raw and a document at the same time")
        if extension and (raw or document):
            raise TypeError("cannot have an extension with a raw or document url")

        filename = self.key
        if raw:
            filename = 'raw/' + filename
        if document:
            filename = 'documents/' + filename
        if extension:
            filename += '.' + extension.strip('.')
        
        return "https://pastecord.com/" + filename
    
    def read_raw(self) -> bytes:
        """Read the raw data of the document"""
        r = requests.get(self.raw_url)
        if r.status_code == 404:
            raise Exception(f"Document {self.key} does not exist")
        r.raise_for_status()
        return r.content

    def read(self, encoding: str = 'utf-8', errors: str = 'strict') -> str:
        """Read the data of the document"""
        return self.read_raw().decode(encoding, errors)
    
    def save(self, filename: str):
        """Save the document as a file"""
        r = requests.get(self.raw_url, stream=True)
        if r.status_code == 404:
            raise Exception(f"Document {self.key} does not exist")
        r.raise_for_status()
        
        with open(filename, 'wb') as file:
            for chunk in r.iter_content(10 * 1024):
                file.write(chunk)

def create_document(content: Union[str, bytes]) -> Document:
    """Create a new pastecord document
    
    Takes in the content of the new document and returns the created document.
    """
    r = requests.post("https://pastecord.com/documents", data=content)
    r.raise_for_status()
    
    return Document(r.json()['key'])

def upload_file(filename: str) -> Document:
    """Upload a file to pastecord
    
    Takes in the filename of the uploaded file and returns the created document.
    """
    with open(filename) as file:
        return create_document(file.read())

def document(url: str) -> Document:
    """An alias for creating a document from a url."""
    return Document(url)

