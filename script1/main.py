import requests

from services.text_extractor_service import (
    HTMLTextExtractor,
    PDFTextExtractor,
    TextComparisonService,
)


if __name__ == "__main__":
    html_source = requests.get(
        "https://sciencespectrumu.com/the-wild-life-of-isaac-newton-a2e356d1406a"
    ).text
    pdf_source = "./data/data-pdf.pdf"

    text_comparison_service = TextComparisonService(
        extractor1=HTMLTextExtractor(html_source),
        extractor2=PDFTextExtractor(pdf_source),
    )

    actual_compare_score = text_comparison_service.compare()

    assert actual_compare_score == 1.0, f"Cosine similarity is: {actual_compare_score}"
