import fastjsonschema
import json
import requests
import zstandard as zstd
import tempfile


def validate_hif_json(filename: str) -> bool:
    """
    Validate a JSON file against the HIF (Hypergraph Interchange Format) schema.

    Args:
        filename: Path to the JSON file to validate.

    Returns:
        ``True`` if the file is valid HIF, ``False`` otherwise.
    """
    url = "https://raw.githubusercontent.com/HIF-org/HIF-standard/main/schemas/hif_schema.json"
    try:
        schema = requests.get(url, timeout=10).json()
    except (requests.RequestException, requests.Timeout):
        with open("../schema/hif_schema.json", "r") as f:
            schema = json.load(f)
    validator = fastjsonschema.compile(schema)
    hiftext = json.load(open(filename, "r"))
    try:
        validator(hiftext)
        return True
    except Exception:
        return False


def decompress_zst(zst_path: str) -> str:
    dctx = zstd.ZstdDecompressor()
    with (
        open(zst_path, "rb") as input_f,
        tempfile.NamedTemporaryFile(mode="wb", suffix=".json", delete=False) as tmp_file,
    ):
        dctx.copy_stream(input_f, tmp_file)
        output = tmp_file.name
    return output


def compress_to_zst(json_path: str) -> bytes:
    cctx = zstd.ZstdCompressor()
    with open(json_path, "rb") as input_f:
        compressed_content = cctx.compress(input_f.read())
    return compressed_content
