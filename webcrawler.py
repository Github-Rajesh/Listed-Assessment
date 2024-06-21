import json
import csv
from googlesearch import search

def get_links(query, max_results):
    search_links = []
    try:
        # Perform Google search with the specified query
        search_query = f'site:youtube.com {query}'
        for url in search(search_query, num_results=max_results):
            if url.startswith('https://www.youtube.com'):
                search_links.append(url)
    except Exception as e:
        print(f"Error during search: {e}")
    return search_links

def save_to_file(data, output_file, file_format):
    try:
        if file_format == 'json':
            with open(output_file, 'w') as file:
                json.dump(data, file, indent=4)
        elif file_format == 'csv':
            with open(output_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Links'])
                writer.writerows([[link] for link in data])
        else:
            print(f"Unsupported file format: {file_format}")
    except Exception as e:
        print(f"Error saving to {file_format.upper()}: {e}")

# Set the search query and maximum number of results
query = 'openinapp.co'
max_results = 10000

# Get the YouTube links
search_links = get_links(query, max_results)

# Save the results to JSON
save_to_file(search_links, 'search_links.json', 'json')

# Save the results to CSV
save_to_file(search_links, 'search_links.csv', 'csv')
