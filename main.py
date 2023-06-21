import requests

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    print(f"File downloaded successfully: {save_path}")

# Example usage
file_url = input("Enter file location: ")
save_location = input("Enter download location: ")

download_file(file_url, save_location)
