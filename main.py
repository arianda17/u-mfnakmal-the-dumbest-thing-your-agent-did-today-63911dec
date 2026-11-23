ENTRY = "My agent deleted the whole repository: the freshness file held 286 bytes instead of 287."


def main() -> None:
    assert isinstance(ENTRY, str), "entry must be a string"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1 to 200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
