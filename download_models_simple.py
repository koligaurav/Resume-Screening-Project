import os
import requests
import pickle

def download_models():
    """Download model files from direct URLs"""
    
    # You can host these files on GitHub Releases, AWS S3, or any file hosting service
    model_urls = {
        'clf.pkl': 'https://github.com/koligaurav/Resume-Screening-Project/releases/download/v1.0/clf.pkl',
        'tfidf.pkl': 'https://github.com/koligaurav/Resume-Screening-Project/releases/download/v1.0/tfidf.pkl',
        'encoder.pkl': 'https://github.com/koligaurav/Resume-Screening-Project/releases/download/v1.0/encoder.pkl'
    }
    
    print("🔍 Checking for model files...")
    
    # Check if models already exist
    missing_files = []
    for filename in model_urls.keys():
        if not os.path.exists(filename):
            missing_files.append(filename)
    
    if not missing_files:
        print("✅ All model files already exist!")
        return True
    
    print(f"📥 Missing files: {missing_files}")
    print("🔄 Downloading missing model files...")
    
    # Download missing files
    success_count = 0
    for filename, url in model_urls.items():
        if filename in missing_files:
            try:
                print(f"Downloading {filename}...")
                response = requests.get(url, stream=True)
                
                if response.status_code == 200:
                    with open(filename, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"✅ Successfully downloaded {filename}")
                    success_count += 1
                else:
                    print(f"❌ Failed to download {filename} (Status: {response.status_code})")
            except Exception as e:
                print(f"❌ Error downloading {filename}: {str(e)}")
    
    if success_count == len(missing_files):
        print("🎉 All model files downloaded successfully!")
        return True
    else:
        print(f"⚠️ Only {success_count}/{len(missing_files)} files downloaded successfully")
        return False

if __name__ == "__main__":
    download_models()
