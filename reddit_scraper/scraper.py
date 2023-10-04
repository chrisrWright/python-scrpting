from selenium import webdriver

# Define the URL
url = "https://www.reddit.com/r/all/"

# Get user input for the subreddit
subreddit = input("Enter the subreddit you want to search for (e.g., 'nba'): ")

# Initialize the webdriver (make sure to replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable)
driver = webdriver.Chrome(r'C:\Users\chris\Documents\drivers\chromedriver.exe')

# Open the URL
driver.get(url)

# Find all the posts
posts = driver.find_elements_by_css_selector('div.Post')

# Loop through the posts
for post in posts:
    # Check if the post is from the user-specified subreddit
    if post.find_element_by_css_selector('a[data-click-id="subreddit"]').text.lower() == f"r/{subreddit}":
        title = post.find_element_by_css_selector('h3').text
        print(title)

# Close the webdriver
driver.quit()
