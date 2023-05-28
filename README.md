# Movie Recommender

The Movie Recommender is a machine learning project that utilizes the Support Vector Machine (SVM) algorithm to recommend similar movies based on user searches. The frontend of the project is built using Streamlit, a Python library for creating interactive web applications.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the Movie Recommender locally, follow these steps:

1. Clone the repository: `git clone https://github.com/harshgupta1810/Movie_recommender.git`
2. Navigate to the project directory: `cd Movie_recommender`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Start the Streamlit server: `streamlit run app.py`
5. Access the web application in your browser at `http://localhost:8501`

Note: Ensure you have Python and pip installed on your system.

## Usage

1. Open the Movie Recommender web application in your preferred web browser.
2. Enter the name of a movie you're interested in the search bar.
3. Click the "Search" button or press Enter.
4. The application will utilize the SVM algorithm to analyze the input movie and recommend similar movies.
5. The recommended movies will be displayed on the screen along with their relevant details such as title, genre, and rating.

## Features

- Search for movies by title.
- Utilize the SVM algorithm to generate recommendations based on the input movie.
- Display recommended movies with relevant details.

## Contributing

Contributions to the Movie Recommender project are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## Credits

- The SVM algorithm used in this project is based on the scikit-learn library: [scikit-learn](https://scikit-learn.org/)
- The frontend of the project is built using Streamlit: [Streamlit](https://streamlit.io/)

## Acknowledgements

We would like to thank the open-source community for their valuable contributions and the developers behind the libraries used in this project.

## Roadmap

We have planned the following enhancements for future versions of the Movie Recommender project:

- Improve the accuracy and performance of the SVM algorithm.
- Implement user feedback functionality to refine the recommendations.
- Incorporate additional features such as movie ratings and user preferences.

## Known Issues

- Some movies may not have complete or accurate information in the recommendation results.
- The application may experience slower response times when searching for less popular or lesser-known movies.
