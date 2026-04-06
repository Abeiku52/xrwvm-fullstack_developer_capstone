# Screenshot Guide for Tasks 19-21

The Django application is now ready for taking the required screenshots. Here are the URLs and instructions:

## Task 19: Dealers filtered by State (dealersbystate.png/jpeg)

**URL to visit:** `http://127.0.0.1:8000/dealers/state/?state=KS`

**Steps:**
1. Open your browser and go to: `http://127.0.0.1:8000/dealers/state/`
2. Select "Kansas" from the state dropdown
3. Click "Filter Dealers" button
4. The URL will update to show `?state=KS` parameter
5. Take screenshot showing:
   - Dealers filtered by Kansas state
   - The endpoint visible in browser address bar
   - Save as `dealersbystate.png` or `dealersbystate.jpeg`

## Task 20: Dealer Details with Reviews (dealer_id_reviews.png/jpeg)

**URL to visit:** `http://127.0.0.1:8000/dealer/1/`

**Steps:**
1. Open your browser and go to: `http://127.0.0.1:8000/dealer/1/`
2. The page will show dealer details and reviews
3. Take screenshot showing:
   - Dealer information (Elite Motors Wichita)
   - Customer reviews section with existing reviews
   - The endpoint `/dealer/1/` visible in browser address bar
   - Save as `dealer_id_reviews.png` or `dealer_id_reviews.jpeg`

## Task 21: Post Review Page (dealership_review_submission.png/jpeg)

**URL to visit:** `http://127.0.0.1:8000/dealer/1/review/`

**Steps:**
1. Open your browser and go to: `http://127.0.0.1:8000/dealer/1/review/`
2. Fill out the review form with sample data:
   - Select a star rating (e.g., 5 stars)
   - Enter review text (e.g., "Excellent service and great selection of cars!")
   - Select car make (e.g., "Toyota")
   - Enter car model (e.g., "Camry")
   - Select year (e.g., "2023")
   - Select purchase type (e.g., "Purchase")
   - Enter your name (optional)
3. **DO NOT SUBMIT** - just fill out the form
4. Take screenshot showing:
   - The filled-out review form BEFORE submission
   - The endpoint `/dealer/1/review/` visible in browser address bar
   - Save as `dealership_review_submission.png` or `dealership_review_submission.jpeg`

## Available Dealers in Database:
- Dealer ID 1: Elite Motors Wichita (Kansas)
- Dealer ID 2: Metro Car Center Detroit (Michigan)
- Dealer ID 3: Premium Auto Kansas City (Kansas)
- Dealer ID 4: Sunshine Auto Florida (Florida)

## API Endpoints Available:
- `/api/dealers/` - All dealers
- `/api/dealers/state/KS/` - Dealers in Kansas
- `/api/dealers/1/` - Specific dealer details
- `/api/reviews/1/` - Reviews for dealer ID 1

## Notes:
- The Django server is running on `http://127.0.0.1:8000/`
- All pages are responsive and styled with Bootstrap
- The pages will load dealer data dynamically via JavaScript
- Make sure the browser address bar is visible in all screenshots