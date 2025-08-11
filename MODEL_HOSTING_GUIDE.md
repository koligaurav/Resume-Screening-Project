# 🚀 Model Hosting Guide for Deployment

## Problem
When deploying to Streamlit Cloud, the model files (`*.pkl`) are not included in the repository due to size limits, causing the "Model files not found" error.

## Solution Options

### Option 1: GitHub Releases (Recommended)

#### Step 1: Create a GitHub Release
1. Go to your GitHub repository: `https://github.com/koligaurav/Resume-Screening-Project`
2. Click on "Releases" in the right sidebar
3. Click "Create a new release"
4. Set:
   - **Tag version**: `v1.0`
   - **Release title**: `Model Files v1.0`
   - **Description**: `Model files for Resume Screening App`
5. **Drag and drop** your model files:
   - `clf.pkl` (224.68 MB)
   - `tfidf.pkl` (~1 MB)
   - `encoder.pkl` (~1 KB)
6. Click "Publish release"

#### Step 2: Update Download URLs
The URLs in `download_models_simple.py` will automatically work:
```python
model_urls = {
    'clf.pkl': 'https://github.com/koligaurav/Resume-Screening-Project/releases/download/v1.0/clf.pkl',
    'tfidf.pkl': 'https://github.com/koligaurav/Resume-Screening-Project/releases/download/v1.0/tfidf.pkl',
    'encoder.pkl': 'https://github.com/koligaurav/Resume-Screening-Project/releases/download/v1.0/encoder.pkl'
}
```

### Option 2: Google Drive

#### Step 1: Upload to Google Drive
1. Upload your model files to Google Drive
2. Right-click each file → "Get link" → "Copy link"
3. Extract the file ID from the URL

#### Step 2: Update File IDs
Replace the placeholders in `download_models.py`:
```python
model_files = {
    'clf.pkl': 'YOUR_ACTUAL_CLF_FILE_ID',
    'tfidf.pkl': 'YOUR_ACTUAL_TFIDF_FILE_ID', 
    'encoder.pkl': 'YOUR_ACTUAL_ENCODER_FILE_ID'
}
```

### Option 3: AWS S3

#### Step 1: Upload to S3
1. Create an S3 bucket
2. Upload model files
3. Make files public
4. Get the public URLs

#### Step 2: Update URLs
Replace URLs in `download_models_simple.py`:
```python
model_urls = {
    'clf.pkl': 'https://your-bucket.s3.amazonaws.com/clf.pkl',
    'tfidf.pkl': 'https://your-bucket.s3.amazonaws.com/tfidf.pkl',
    'encoder.pkl': 'https://your-bucket.s3.amazonaws.com/encoder.pkl'
}
```

### Option 4: Dropbox

#### Step 1: Upload to Dropbox
1. Upload files to Dropbox
2. Get share links
3. Convert to direct download links

#### Step 2: Update URLs
Replace URLs in `download_models_simple.py` with Dropbox direct links.

---

## 🎯 Recommended: GitHub Releases

**Why GitHub Releases is best:**
- ✅ Free hosting
- ✅ No file size limits
- ✅ Direct download URLs
- ✅ Version control
- ✅ Easy to update

---

## 📝 Steps to Deploy with Model Hosting

### 1. Host Your Model Files
Choose one of the options above (GitHub Releases recommended)

### 2. Update Download Script
- If using GitHub Releases: No changes needed
- If using other options: Update the URLs/file IDs

### 3. Push to GitHub
```bash
git add .
git commit -m "Add model download functionality"
git push origin main
```

### 4. Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your repository
3. Deploy

### 5. Test Deployment
- The app will automatically download model files on first run
- Subsequent runs will use cached models

---

## 🔧 Troubleshooting

### Model Download Fails
- Check internet connection
- Verify file URLs are correct
- Ensure files are publicly accessible

### Large File Downloads
- Consider compressing models
- Use smaller model variants
- Implement progress indicators

### Caching Issues
- Clear Streamlit cache if needed
- Check file permissions

---

## 📊 File Size Optimization

### Before Deployment
- Compress models using `joblib.dump()` with compression
- Use feature selection to reduce model size
- Consider lighter algorithms

### Example Compression
```python
import joblib

# Save with compression
joblib.dump(model, 'clf.pkl', compress=3)
```

---

## 🎉 Success!

Once you've hosted your model files and updated the download URLs, your Streamlit app will:
1. ✅ Automatically download missing models
2. ✅ Cache models for faster subsequent runs
3. ✅ Work seamlessly on any deployment platform
4. ✅ Handle errors gracefully

**Your app will be fully functional on Streamlit Cloud!** 🚀
