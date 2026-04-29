import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# ### Lowercasing
def ToLower(text):
    return text.lower()

# ### Punctuation & Special Characters
def RemoveChars(text):
    punctuation_pattern = r'[^\w\s]'

    return re.sub(punctuation_pattern, "", text)

# ### Stop-Words
# remove english stopwords function
def remove_stopwords(text, language):
    stop_words = set(stopwords.words(language))
    text = text.lower()
    word_tokens = text.split()
    filtered_text = [word for word in word_tokens if word not in stop_words]

    return filtered_text


# ### URLs
def remove_urls(text):
    url_pattern = re.compile(r"https://\S+|www\.\S+")
    return url_pattern.sub(r"", text)

# ### HTML tags
def remove_tags(text):
    html_tags_pattern = r"<.*?>"

    return re.sub(html_tags_pattern, "", text)