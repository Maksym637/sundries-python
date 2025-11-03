from abc import ABC, abstractmethod


class TextExtractor(ABC):
    @abstractmethod
    def extract_text(self):
        pass


class HTMLTextExtractor(TextExtractor):
    def __init__(self, inner_html_source):
        pass

    def extract_text(self):
        pass


class PDFTextExtractor(TextExtractor):
    def __init__(self, file_name_source):
        pass

    def extract_text(self):
        pass


class TextComparisonService:
    def __init__(self, extractor1: TextExtractor, extractor2: TextExtractor):
        self.extractor1 = extractor1
        self.extractor2 = extractor2

    def compare(self):
        pass
