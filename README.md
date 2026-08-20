# 🎬 Movie Recommendation System

A **content-based movie recommendation system** built using Python and Machine Learning.
The system recommends movies that are similar to a movie selected by the user based on features such as **genres, keywords, cast, and crew**.

> This project was built as part of my learning journey in Machine Learning and Recommendation Systems.

---

## 📌 Project Overview

With thousands of movies available across different platforms, finding something interesting to watch can be difficult.

This project solves that problem by recommending movies similar to a movie selected by the user.

For example, if a user selects **"The Dark Knight"**, the system analyzes its characteristics and recommends other movies with similar content.

The project uses a **Content-Based Filtering** approach rather than relying on ratings from other users.

---

## 🚀 Features

* 🔍 Search/select a movie from the available dataset
* 🎥 Recommend movies similar to the selected movie
* 🧠 Content-based recommendation using movie metadata
* 📊 Text feature extraction and preprocessing
* 🔢 Vectorization using **Bag of Words**
* 📐 Similarity calculation using **Cosine Similarity**
* 🌐 Interactive web interface using **Streamlit**
* ⚡ Fast recommendations using precomputed similarity data

---

## 🧠 How It Works

The recommendation pipeline can be summarized as:

```text
Movie Dataset
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Feature Engineering
      ↓
Combine Movie Metadata
      ↓
Text Preprocessing
      ↓
Bag of Words Vectorization
      ↓
Cosine Similarity
      ↓
Find Similar Movies
      ↓
Display Recommendations
```

### 1. Data Collection

The project uses movie metadata containing information such as:

* Movie title
* Genres
* Keywords
* Cast
* Crew
* Overview

---

### 2. Feature Engineering

Relevant information from different columns is combined into a single textual feature.

For example:

```text
Action Adventure
Batman Gotham City
Christian Bale Michael Caine
Christopher Nolan
```

This combined representation allows the model to compare movies based on their content.

---

### 3. Text Preprocessing

The textual data is cleaned and transformed before vectorization.

Typical preprocessing steps include:

* Converting text to lowercase
* Removing unnecessary spaces
* Removing irrelevant information
* Converting lists/dictionaries into usable text
* Stemming words

---

### 4. Bag of Words

The combined movie tags are converted into numerical vectors using **CountVectorizer / Bag of Words**.

Each movie is represented as a vector in a high-dimensional feature space.

---

### 5. Cosine Similarity

The similarity between movies is calculated using **Cosine Similarity**.

Conceptually:

```text
Movie A → Vector A
Movie B → Vector B

              ↓

      Cosine Similarity

              ↓

       Similarity Score
```

Movies with higher similarity scores are considered more similar.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* NumPy
* Pandas
* Scikit-learn
* NLTK
* Streamlit
* Requests

### Concepts Used

* Machine Learning
* Natural Language Processing
* Feature Engineering
* Text Vectorization
* Content-Based Filtering
* Cosine Similarity

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
│
├── movie.pkl
│
├── movies_recommender_system.ipynb
│
├── similarity.pkl
│
└── README.md
```

### File Description

| File                      | Description                              |
| ------------------------- | ---------------------------------------- |
| `app.py`                  | Streamlit application                    |
| `movie_recommender_system.ipynb` | Data preprocessing and model development |
| `movie.pkl`          | Processed movie information              |
| `similarity.pkl`          | Precomputed movie similarity matrix      |       
| `README.md`               | Project documentation                    |

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Movie-Recommendation-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Movie-Recommendation-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🎯 Example

Suppose the user selects:

```text
The Dark Knight
```

The system calculates the similarity between this movie and all other movies in the dataset.

It then returns the movies with the highest similarity scores.

Example:

```text
Recommended Movies:

1. The Dark Knight Rises
2. Batman Begins
3. Man of Steel
4. Watchmen
5. Iron Man
```

*The exact recommendations depend on the dataset and preprocessing used.*

---

## 📊 Recommendation Method

This project uses **Content-Based Filtering**.

Unlike collaborative filtering, the system does not need information about other users.

Instead, recommendations are generated based on the similarity between movie features.

### Content-Based Filtering

```text
Selected Movie
      ↓
Movie Features
      ↓
Feature Vector
      ↓
Compare with Other Movies
      ↓
Cosine Similarity
      ↓
Top-N Similar Movies
```

---

## 🔑 Key Concepts Learned

Through this project, I worked with:

* Data preprocessing
* Feature engineering
* NLP-based text preprocessing
* Bag of Words
* Vectorization
* Cosine similarity
* Recommendation systems
* Model serialization using Pickle
* Streamlit application development
* Connecting a Machine Learning model with a web interface

---

## 📄 License

This project is intended for **educational and learning purposes**.

[1]: https://github.com/campusx-official/ML-Roadmap-for-2022?utm_source=chatgpt.com "GitHub - campusx-official/ML-Roadmap-for-2022: A curated list of Machine learning videos, links, projects and datasets to help you conquer the ML landscape in 6 months · GitHub"
