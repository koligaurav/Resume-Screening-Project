import os
import requests
import pickle
from pathlib import Path

def download_file_from_drive(file_id, filename):
    """Download file from Google Drive"""
    try:
        # Google Drive direct download URL
        url = f"https://drive.google.com/uc?id={file_id}&export=download"
        
        print(f"Downloading {filename}...")
        response = requests.get(url, stream=True)
        
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"✅ Successfully downloaded {filename}")
            return True
        else:
            print(f"❌ Failed to download {filename}")
            return False
    except Exception as e:
        print(f"❌ Error downloading {filename}: {str(e)}")
        return False

def download_models():
    """Download all required model files"""
    # Google Drive file IDs (you'll need to replace these with your actual file IDs)
    model_files = {
        'clf.pkl': 'YOUR_CLF_FILE_ID_HERE',
        'tfidf.pkl': 'YOUR_TFIDF_FILE_ID_HERE', 
        'encoder.pkl': 'YOUR_ENCODER_FILE_ID_HERE'
    }
    
    print("🔍 Checking for model files...")
    
    # Check if models already exist
    missing_files = []
    for filename in model_files.keys():
        if not os.path.exists(filename):
            missing_files.append(filename)
    
    if not missing_files:
        print("✅ All model files already exist!")
        return True
    
    print(f"📥 Missing files: {missing_files}")
    print("🔄 Downloading missing model files...")
    
    # Download missing files
    success_count = 0
    for filename, file_id in model_files.items():
        if filename in missing_files:
            if download_file_from_drive(file_id, filename):
                success_count += 1
    
    if success_count == len(missing_files):
        print("🎉 All model files downloaded successfully!")
        return True
    else:
        print(f"⚠️ Only {success_count}/{len(missing_files)} files downloaded successfully")
        return False

if __name__ == "__main__":
    download_models()
