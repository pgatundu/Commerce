# 🛒 Commerce – Online Auction Site

A **Django-based e-commerce web application** that functions as an online auction site.  
Users can list items for sale, place bids, comment on listings, and manage their watchlists.  
Built as part of **CS50’s Web Programming with Python and JavaScript** course.  

---

## 🚀 Features
- 📦 **Create Listings** – Users can list items with title, description, image, and starting bid.  
- 💰 **Bidding System** – Place bids, with validation to ensure only higher bids are accepted.  
- 👀 **Watchlist** – Add and remove items from a personal watchlist.  
- 💬 **Comments** – Leave comments on active listings.  
- ✅ **Close Auctions** – Listing owners can close auctions, declaring the highest bidder as winner.  
- 🏷 **Categories** – Browse listings by category.  

---

## 🛠 Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (default)  

---

## 📦 Installation

Run the following commands:

```bash
# Clone the repository
git clone https://github.com/pgatundu/Commerce.git

# Navigate into the project
cd Commerce

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the development server
python manage.py runserver

