import json
import csv
from googlesearch import search

def get_links(query, max_results):
    search_links = ['youtube.com openinapp.co']

    # Perform Google search with the specified query
    search_query = f'site:youtube.com {query}'
    try:
        for url in search(search_query, num_results=max_results):
            if url.startswith('https://www.youtube.com'):
                search_links.append(url)
    except Exception as e:
        print(f"Error during search: {e}")

    return search_links

def save_to_json(search_links, output_file):
    try:
        with open(output_file, 'w') as file:
            json.dump(search_links, file, indent=4)
    except Exception as e:
        print(f"Error saving to JSON: {e}")

def save_to_csv(search_links, output_file):
    try:
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Links'])
            writer.writerows([[link] for link in search_links]) 
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# Set the search query and maximum number of results
query = 'openinapp.co'
max_results = 10000

# Get the YouTube links
search_links = get_links(query, max_results)

# Save the results to JSON
save_to_json(search_links, 'search_links.json')

# Save the results to CSV
save_to_csv(search_links, 'search_links.csv')
