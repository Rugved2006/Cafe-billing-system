# Cafe Billing System (Python)

A simple and interactive **Café Billing System** made using Python.  
This program allows customers to browse menus by cuisine, place orders, and receive a fully itemized bill including:

- Subtotal  
- Discount (for large orders)  
- Service Charge  
- GST  
- Final Grand Total  

---

##  Features

-  **Menu categorized** into *Indian*, *Chinese*, and *Italian*.
-  **Interactive order selection** with item quantities.
-  **Automatic billing** with:
  - 10% Service Charge  
  - 18% GST  
  - 10% Bulk Discount for orders above ₹3500  
-  **Final receipt** showing:
  - Item-wise details  
  - Subtotal  
  - Discounts  
  - GST & service charge  
  - Grand total  

---

##  How to Use

1. Run the Python script:
   ```bash
   python cafe_billing.py
   ```
2. Browse through menu categories.
3. Add items and choose quantities.
4. Complete your order.
5. Receive a detailed bill.

---

## 📁 Project Structure

```
├── cafe_billing.py
├── README.md
```

---

##  Code Overview

The main components of the project:

- `display_menu()` – Shows the full menu  
- `take_order()` – Handles user order input  
- `calculate_bill()` – Computes cost, discount, GST, service charge  
- `print_bill()` – Prints the final detailed receipt  

---

##  Billing Formula

```
Subtotal = sum(price × quantity)
Discount = 10% (if subtotal > 3500)
Service Charge = 10% of (subtotal – discount)
GST = 18% of (subtotal – discount + service charge)
Grand Total = subtotal – discount + service charge + GST
```

---

##  Requirements

- Python 3.7+
- No external libraries required

---
