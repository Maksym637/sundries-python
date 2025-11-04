from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from pypdf import PdfReader

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TextExtractor(ABC):
    @abstractmethod
    def extract_text(self):
        pass


class HTMLTextExtractor(TextExtractor):
    def __init__(self, html_source):
        self.beautiful_soup = BeautifulSoup(html_source, "html.parser")

    def extract_text(self):
        paragraph = self.beautiful_soup.find("p", id="a742")

        return paragraph.get_text(strip=True)


class PDFTextExtractor(TextExtractor):
    def __init__(self, pdf_source):
        self.file_path = pdf_source

    def extract_text(self):
        text_buffer = ""

        with open(self.file_path, "rb") as file:
            reader = PdfReader(file)

            for page in reader.pages:
                text_buffer += page.extract_text()

        return text_buffer


class TextComparisonService:
    def __init__(self, extractor1: TextExtractor, extractor2: TextExtractor):
        self.extractor1 = extractor1
        self.extractor2 = extractor2

    def __get_cosine_similarity(self, text1, text2):
        vectorizer = TfidfVectorizer().fit_transform([text1, text2])
        similarity = cosine_similarity(vectorizer[0], vectorizer[1])

        return similarity[0][0]

    def compare(self):
        html_text = self.extractor1.extract_text()
        pdf_text = self.extractor2.extract_text()

        compare_score = self.__get_cosine_similarity(html_text, pdf_text)

        return compare_score
