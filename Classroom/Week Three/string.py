"""String Analysis Tutorial - analyse URLs and asset IDs"""


def analyse_url(url: str) -> None:
    """Analyse information contained in a URL>"""
    
    print("|n--- URL Analysis ---")
    print(f"URL: {url}")

    # Check the start of the URL.
    if url.startswith("https://"):
        print("HTTPS detected - connection is encrypted.")
    elif url[0:4] == "http":
        print("HTTP detected - connection is not encrypted.")
    else:
        print("URL protocol not recognised.")

    # Check for text anywhere within the URL.
    if "admin" in url:
        print("Admin access detected.")
    if "docs" in url:
        print("Documentation detected.")


def main() -> None:
    """Run the program."""

def analyse_asset(asset_id: str) -> tuple[str, str, str]:
    """Analyse an asset ID and return its components."""

    print("\n--- Asset ID Analysis ---")
    print(f"Asset ID: {asset_id}")

    # Split the asset ID into seperate parts.
    parts = asset_id.split("-")

    asset_type = parts[0]

def main() -> None:
    """Run the program."""

    url = "https://portal.example.net/admin/docs"
    asset_id = "RTR-2048-gla"

    analyse_url(url)


if __name__ == "__main__":
    main()