# Automated Data Extraction Pipeline

This project was created to automate data scraping from a platform while integrating LangChain to turn the gathered images into CSV files.

Note: The computer **MUST NOT** be interacted with while the script is in the scraping process.

## Script's Preliminary Requirements

Installed Applications:

1. Browser (either Chrome or Firefox)
1. Ollama (with an account)

Conditions to be Satisfied:

1. A Facebook account must be logged in.
1. The Ollama application must be opened as a separate window.
1. Return to the browser within 8 seconds after running the script.


## Code Process
1. The script initially checks if a browser and the Ollama application are currently opened as required.

1. The script uses the user's keyboard shortcuts, screen size, and the platform's UI layout to navigate and download the images needed from a post.

1. It then checks the directories of the individual locations of interest to see if they already exist from previous usage of the script. If so, the files are then overwritten; otherwise, it creates a folder for each.

1. The cropped images are then passed to a reliable model in Ollama to return a CSV response, which is then turned into a CSV file.

1. The CSV file is manipulated through Pandas to fix the header and replace the files with proper separators.

1. Finally, the folder made will then be compressed into a ZIP file.
