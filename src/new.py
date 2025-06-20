import nltk

# Clear old cache (optional)
nltk.data.path.clear()

# Set a new path (optional if permissions are an issue)
nltk.data.path.append('C:/Users/Mirafra/nltk_data')

# Redownload resources
nltk.download('punkt', download_dir='C:/Users/Mirafra/nltk_data')
nltk.download('stopwords', download_dir='C:/Users/Mirafra/nltk_data')
