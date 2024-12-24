# Movie Recommender

## Website
[Movie Recommender Web App](https://movierecommender-pof22t3ecfsgaqpxs458tn.streamlit.app)

## Overview
This project is a movie recommender system based on content-based recommendation using vectorization. It utilizes Jupyter Notebook for preprocessing and creating `.pkl` files, and Python with Streamlit for launching a web application.

## Requirements
- Python 3.x
- Pandas
- Streamlit
- Scikit-learn

## Usage
1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```
2. **Navigate to the project directory:**
    ```bash
    cd movie-recommender
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Launch the web application:**
    ```bash
    streamlit run app.py
    ```
5. **Visit the following link in your web browser:**
    [Movie Recommender Web App](https://movierecommender-pof22t3ecfsgaqpxs458tn.streamlit.app)

## How it works
- The project preprocesses movie data and uses vectorization techniques for content-based recommendation.
- Jupyter Notebook files (`preprocessing.ipynb`, `vectorization.ipynb`) are used to create `.pkl` files for the model.
- The web application is launched using Streamlit, where users can input their GitHub link to access the movie recommender.

## Inspiration
This project is inspired by [this YouTube video](https://www.youtube.com/watch?v=1xtrIEwY_zY&t=3877s).

## License
[MIT License](LICENSE)
