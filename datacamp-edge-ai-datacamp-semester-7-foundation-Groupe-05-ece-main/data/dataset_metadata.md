# Dataset Metadata (The Librarian)

Do **not** commit raw datasets or model weights to this repository. Keep them on the shared MinIO server and document how to fetch them here.

## How to fetch data from MinIO

1. Obtain MinIO endpoint, bucket name, and credentials from the course staff (never commit secrets).
2. Store credentials in a local `.env` (gitignored) or your environment:
   - `MINIO_ENDPOINT`
   - `MINIO_ACCESS_KEY`
   - `MINIO_SECRET_KEY`
   - `MINIO_BUCKET`
3. Download objects into a local path under `data/` (ignored by `.gitignore` for `*.csv`, etc.).
4. Record below: object keys, schema, license, and last-updated date.

## Dataset inventory

| Object key (MinIO) | Local path | Description | Schema / notes | Updated |
| :--- | :--- | :--- | :--- | :--- |
| _(example)_ `s7/raw/sample.parquet` | `data/sample.parquet` | _(describe)_ | _(columns)_ | YYYY-MM-DD |

## Fetch script notes

Document the script or CLI command your group uses (e.g. `mc cp`, `boto3`, `minio` Python client). Keep fetch logic in `src/` or a small script—not in notebooks committed with embedded credentials.
