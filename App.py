from flask import Flask, request, jsonify
from Scraper import scraperFn
from OpenApi import get_css_selectors  # Import get_css_selectors

app = Flask(__name__)

@app.route("/api/reviews")
def apiHandler():
    # Retrieve the 'page' query parameter
    query = request.args.get('page')

    # Print the query parameter to the console
    print(f"Received query parameter: {query}")
    
    if not query:
        return jsonify({"error": "No page parameter provided."}), 400
    
    try:
        # Call the scraper function with the provided URL
        html_content = scraperFn(query)

        # Pass the scraped HTML to OpenAI for CSS selector identification
        res = get_css_selectors(html_content)

        # If OpenAI didn't return valid JSON
        if res is None:
            return jsonify({"error": "Failed to extract CSS selectors from OpenAI response."}), 500

        # Return the CSS selectors as JSON
        return jsonify(res)

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while processing the request."}), 500

if __name__ == "__main__":
    app.run(port=3000, debug=True) 
