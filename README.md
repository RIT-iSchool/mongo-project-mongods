[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10443004&assignment_repo_type=AssignmentRepo)

## Technology Stack

- **Python**: Most of the code is written in Python, because of simplicity and familiarity.

- **Flask**: Flask is a web framework for Python, used to build the web application and handle HTTP requests.

- **Pandas**: Pandas is a library in Python that is used for reading and processing data.

- **MongoDB**: The project is based on MongoDB.

- **GridFS**: GridFS is used to store images, as chunks in the database.

- **HTML/CSS**: HTML is used for creating web pages, while CSS is used for styling web pages and defining their layout and appearance.

- **JavaScript**: JavaScript is used for creating geospatial indices.

- **Jinja2**: Jinja2 is used to allow embedding Python code within HTML templates to generate dynamic content.

We used the `Instagram - 42M Posts 1.2M Locations 4.5M Profiles | Kaggle` dataset.
We originally had 1.4k posts and images extracted. More data was required for the project, but the original dataset was seemingly deleted and we only had access to our previous versions of the extracted data. We were able to extract around 9k posts and their corresponding images for the project.

Our project is a Python Flask web application that interacts with a MongoDB database. The application allows users to search and view Instagram posts, as well as add comments to posts. The application uses the pandas library to read data from a CSV file and insert it into a MongoDB collection. It also uses the gridfs module to store and retrieve image files from the database.

The application has the following routes:

- `'/'`: Renders the `search.html` template, which is the home page of the application.
- `'/search_posts'`: Handles a form submission with search query and field information. Depending on the field selected, it performs a text or geospatial search and renders the `results.html` template with the search results.
- `'/show_post/<post_id>'`: Retrieves a post based on the post ID in the URL and renders the `post.html` template with the post details, image, and comments.
- `'/download_image/<image_id>'`: Retrieves an image file from the GridFS by its ID and sends it as a file download to the client.
- `'/add_comment/<post_id>'`: Handles a form submission with a comment for a post. It inserts the comment into the comments collection and redirects back to the `'/show_post'` route for the corresponding post.

The application also includes JavaScript code for creating a geospatial index on the postLoc field. Additionally, the application includes an HTML template that defines the layout and rendering logic for displaying post details, images, and comments.
