# Vendor Management System with Performance Metrics
- This project is a Vendor Management System developed using Django and Django REST Framework. The system handles vendor profiles, purchase order tracking, and calculates vendor performance metrics.
## Getting Started

### Prerequisites

- Python 
- Django
- Django REST Framework

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Vendor_manage.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Vendor_Manage
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

# Running the Server
 ### 1. Apply database migrations:
  ```bash
  python manage.py migrate
  ```
 ### 2. Create a superuser (for accessing the Django admin):
 ```bash
 python manage.py createsuperuser
 ```
 ### Run the development server:
 ```bash
 python manage.py runserver
 ```
 ### 4. Access the API at http://127.0.0.1:8000/api/

# API Endpoints :
### Vendor Management
 - Create Vendor:
   - **POST /api/vendors/**: Create a new vendor.
 - List Vendors:
   - **GET /api/vendors/**: List all vendors.
 - Retrieve Vendor:
   - **GET /api/vendors/{vendor_id}**/: Retrieve details of a specific vendor.
 - Update Vendor:
   - **PUT /api/vendors/{vendor_id}**/: Update a vendor's details.
 - Delete Vendor:
   - **DELETE /api/vendors/{vendor_id}**/: Delete a vendor.
 - Get all orders of a specific vendor
   - **GET /api/vendors/{vendor_id}**/orders
### Purchase Order Tracking
- Create Purchase Order:
   - **POST /api/purchase_orders/:** Create a purchase order.
- List Purchase Orders:
   - **GET /api/purchase_orders/**: List all purchase orders.
- Retrieve Purchase Order:
  - **GET /api/purchase_orders/{po_id}/**: Retrieve details of a specific purchase order.
- Update Purchase Order:
  - **PUT /api/purchase_orders/{po_id}/**: Update a purchase order.
- Delete Purchase Order:
  - **DELETE /api/purchase_orders/{po_id}/**: Delete a purchase order.
### Vendor Performance Metrics
- Retrieve Vendor Performance:
  - **GET /api/vendors/{vendor_id}/performance/**: Retrieve performance metrics for a specific vendor.
### Acknowledge Purchase Order
- Acknowledge Purchase Order:
  - **POST /api/purchase_orders/{po_id}/acknowledge/**: Acknowledge a purchase order, updating acknowledgment date and triggering metric recalculation.
 ## Authentication
- API endpoints are secured using token-based authentication. Users must include a valid token in the Authorization header of their requests.
   
