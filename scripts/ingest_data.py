from advanced_rag.ingestion.loader import ingest_pdf


def main():
    count = ingest_pdf(
        "/home/gaurav/Documents/advanced_rag/data/EthanolBlendingInIndia_compressed.pdf"
    )
    print(f"Ingested {count} chunks")


if __name__ == "__main__":
    main()
