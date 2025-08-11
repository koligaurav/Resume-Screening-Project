# Resume Category Predictor

A web-based application that uses machine learning to predict job categories from resume text. The application provides a beautiful, modern interface built with Streamlit where users can input their resume text and get instant category predictions.

## Features

- 🎯 **AI-Powered Prediction**: Uses trained machine learning models to predict resume categories
- 🌐 **Streamlit Interface**: Modern, responsive web interface built with Streamlit
- 📱 **Mobile Responsive**: Works perfectly on desktop, tablet, and mobile devices
- ⚡ **Real-time Analysis**: Instant predictions with loading animations
- 📝 **Sample Resume**: Built-in sample resume for testing
- 🎨 **Beautiful UI**: Modern gradient design with smooth animations
- 📊 **Category Display**: Shows all available categories in the sidebar
- 💡 **Helpful Tips**: Provides guidance for better predictions

## Supported Categories

The model can predict the following job categories:
- Data Science
- Python Developer
- Java Developer
- Web Designing
- DevOps Engineer
- Network Security Engineer
- Civil Engineer
- Mechanical Engineer
- Electrical Engineering
- Business Analyst
- HR
- Sales
- Arts
- Health and fitness
- And many more...

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download the project files** to your local machine

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the model files** in the project directory:
   - `tfidf.pkl` - TF-IDF vectorizer
   - `clf.pkl` - Trained classifier model
   - `encoder.pkl` - Label encoder

## Usage

1. **Start the Streamlit application**:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Open your web browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

3. **Use the application**:
   - Paste your resume text in the text area
   - Click "Predict Category" to get instant results
   - Try the sample resume feature to see how it works
   - View all available categories in the sidebar

## How It Works

1. **Text Preprocessing**: The resume text is cleaned by removing URLs, special characters, and unnecessary whitespace
2. **Feature Extraction**: The cleaned text is converted to numerical features using TF-IDF vectorization
3. **Prediction**: The trained machine learning model predicts the most likely job category
4. **Result Display**: The predicted category is displayed with a beautiful badge

## Project Structure

```
Resume Screening App/
├── streamlit_app.py        # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── tfidf.pkl             # TF-IDF vectorizer model
├── clf.pkl               # Trained classifier model
├── encoder.pkl           # Label encoder
├── corrected_screening.py # Original training script
├── screening.ipynb       # Jupyter notebook with analysis
└── UpdatedResumeDataSet.csv # Training dataset
```

## Model Information

The application uses:
- **TF-IDF Vectorization**: Converts text to numerical features
- **Support Vector Classifier (SVC)**: Multi-class classification model
- **Label Encoding**: Converts category names to numerical labels

The model was trained on a dataset of resumes from various job categories and achieves high accuracy in classification.

## Features of the Streamlit Interface

- **Responsive Design**: Works on all device sizes
- **Sidebar Information**: Shows model info and available categories
- **Sample Resume**: One-click sample resume loading
- **Character Counter**: Real-time character count
- **Beautiful Styling**: Custom CSS for modern appearance
- **Error Handling**: Graceful error messages
- **Loading Animations**: Visual feedback during prediction

## Troubleshooting

### Common Issues

1. **Model files not found**:
   - Ensure `tfidf.pkl`, `clf.pkl`, and `encoder.pkl` are in the project directory
   - These files should be generated from your training script

2. **Port already in use**:
   - Streamlit will automatically find an available port
   - Check the terminal output for the correct URL

3. **Dependencies not installed**:
   - Run `pip install -r requirements.txt` again
   - Check Python version compatibility

4. **Streamlit not found**:
   - Install Streamlit: `pip install streamlit`
   - Or use: `pip install -r requirements.txt`

### Error Messages

- **"Model files not found"**: Missing pickle files
- **"Please enter your resume text"**: Empty input validation
- **Streamlit connection errors**: Check if the server is running

## Running the Application

### Method 1: Direct Streamlit Run
```bash
streamlit run streamlit_app.py
```

### Method 2: Python Module Run
```bash
python -m streamlit run streamlit_app.py
```

### Method 3: With Custom Port
```bash
streamlit run streamlit_app.py --server.port 8502
```

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving the UI/UX
- Enhancing the machine learning model

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Review the Streamlit logs in the terminal
3. Ensure all dependencies are properly installed

---

**Happy Resume Screening! 🚀**
