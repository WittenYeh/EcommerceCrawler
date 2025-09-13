import requests
import random
import time

class WebCrawler:
    def __init__(self):
        self.session = requests.Session()
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
        ]
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
    def fetch_html(self, offer_id: str) -> str | None:
        """
        Fetches the HTML content for a given 1688 offer ID using enhanced techniques.

        Args:
            offer_id (str): The product's offer ID.

        Returns:
            str: The HTML content of the page, or None if an error occurs or if blocked.
        """
        url = f"https://detail.1688.com/offer/{offer_id}.html"
        
        # --- Enhancements ---
        # 1. Rotate User-Agent for each request
        self.session.headers['User-Agent'] = random.choice(self.user_agents)
        # 2. Set a Referer to simulate navigation from the site's homepage
        self.session.headers['Referer'] = 'https://www.1688.com/'

        print(f"Fetching data from: {url}")
        try:
            # 3. Use the session object to make the request (handles cookies automatically)
            response = self.session.get(url, timeout=15)
            response.raise_for_status()

            # 4. Check for blocking page content even if status code is 200
            if "unusual traffic" in response.text or "detected unusual traffic" in response.text:
                print(f"Failed to fetch product {offer_id}: Blocked by anti-scraping mechanism.")
                # Save the blocking page for debugging
                with open(f"blocked_{offer_id}.html", "w", encoding="utf-8") as f:
                    f.write(response.text)
                return None

            print(f"Fetched product {offer_id} successfully.")
            
            # 5. Add a random delay to mimic human behavior
            time.sleep(random.uniform(2, 5)) 
            
            return response.text

        except requests.RequestException as e:
            print(f"Error fetching product {offer_id}: {e}")
            return None