# 🛒 Grocery Database Project

## 📦 Running the Project with Docker

Follow these steps to run the application locally using Docker.

---

## ✅ Prerequisites

Make sure you have Docker installed:

* Install Docker Desktop: https://www.docker.com/products/docker-desktop

---

## 🚀 Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/FalconCharge/Grocer-DataBase
   cd grocery-database
   ```

2. **Run the application**

   ```bash
   docker compose up --build
   ```

   This will:

   * Build the containers
   * Start the database and web services
   * Automatically initialize the schema and synthetic data

   Open up http://localhost:5001/ on your choice of browser (tested on FireFox)

---

## 🔄 Resetting the Database

If you want to completely reset the database (clear all data and start fresh):

```bash
docker compose down -v
```

Then run again:

```bash
docker compose up --build
```

---

## 🧠 Notes

* The `-v` flag removes all volumes, including stored database data.
* Without `-v`, your data will persist between runs.
* Make sure Docker is running before executing commands.

---

## 🛠️ Troubleshooting

* If changes aren’t appearing, try rebuilding:

  ```bash
  docker compose down
  docker compose up --build
  ```
* If ports are already in use, stop other running containers.

---

## 📁 Project Structure

* `models/` – Shows different Tables used (orders, customers, inventory, products, order_items, tracking)
* `query/` – Used for some unqiue querys of the data
* `docker-compose.yml` – Container configuration
* `templates` – html files to view the database
* `app.py` – Main entry
* `db.py` – Used to connect to the database

