from google.cloud import storage
import os
import sys

def upload_file_to_gcs(file_path, bucket_name):
    """Uploads a file to Google Cloud Storage and returns the URL."""
    # Initialize a GCS client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Define the blob name (filename)
    blob_name = os.path.basename(file_path)

    # Create a blob object
    blob = bucket.blob(blob_name)

    # Upload the file to GCS
    with open(file_path, "rb") as f:
        blob.upload_from_file(f)

    # Generate the public URL for the uploaded file
    url = f"https://storage.googleapis.com/{bucket_name}/{blob_name}"

    return url

if __name__ == "__main__":
    # Set your file path and bucket name

    file_path = sys.argv[0]
    bucket_name = "my-bucket3722"
    print("Number of arguments:", len(sys.argv))
    print("Arguments:", str(sys.argv))

    # Upload the file and get the URL
    file_url = upload_file_to_gcs(file_path, bucket_name)
    print("Uploaded file URL:", file_url)
