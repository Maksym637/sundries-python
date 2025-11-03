from services.text_extractor_service import (
    HTMLTextExtractor,
    PDFTextExtractor,
    TextComparisonService,
)


if __name__ == "__main__":
    text_comparison_service = TextComparisonService(
        extractor1=HTMLTextExtractor(),
        extractor2=PDFTextExtractor(),
    )

    actual_compare_score = text_comparison_service.compare()

    assert actual_compare_score == 1.0, f"Cosine similarity is: {actual_compare_score}"
