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

The application has the following routes:

- `'/'`: Renders the `search.html` template, which is the home page of the application.
- `'/search_posts'`: Handles a form submission with search query and field information. Depending on the field selected, it performs a text or geospatial search and renders the `results.html` template with the search results.
- `'/show_post/<post_id>'`: Retrieves a post based on the post ID in the URL and renders the `post.html` template with the post details, image, and comments.
- `'/download_image/<image_id>'`: Retrieves an image file from the GridFS by its ID and sends it as a file download to the client.
- `'/add_comment/<post_id>'`: Handles a form submission with a comment for a post. It inserts the comment into the comments collection and redirects back to the `'/show_post'` route for the corresponding post.
