# Automated Data Extraction Pipeline

This project was created to automate data scraping from a platform while integrating LangChain for turning the images gathered into CSV file.

## Script's Preliminary Requirements
1. Ollama Application (Gemini API Key as Alternative)
1. Facebook

## Code Process
1. With a project limitation where no API from the platform itself will be used, the script requires for an account on the platform to be logged in and for the screen to be unused.

1. The script then checks if a browser and Ollama application is running as a preliminary check.

1. The script uses the user's screen size and platform's layout to navigate and download the images needed from a post.

1. It then checks the directories of the individual location of interest to see if they already exist from previous usage of the script. If not, it creates a folder for each.

1. The cropped images are then passed to a reliable model to return a CSV response which is then turned into a CSV file.

1. The CSV file is manipulated through Pandas to fix the header and replace the files with proper separators.

1. Finally, the folder made will then be compressed on a zip file.
