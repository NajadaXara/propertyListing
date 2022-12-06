# Write a SQL script that can create a simple SQL table for listings
# (listing table -> static/listing_table.jpg)
import sqlite3 as sql

# Create connection to properties SQLite DB
connection = sql.connect('properties.db')
cursor = connection.cursor()

# Drop listing table if already exists and create a new one
# Populate with mock data
cursor.executescript(""" 
        DROP TABLE IF EXISTS property_listing;
        CREATE TABLE "property_listing"(
            "id" INTEGER PRIMARY KEY AUTOINCREMENT, 
            "property_address" TEXT, 
            "listing_price" INTEGER
        );
        INSERT INTO "property_listing"(id, property_address, listing_price)
        VALUES 
            (2343424, '125 Parkway Dr.', 255000),
            (3343234, '1222 Jones Rd.', 135000),
            (22344324, '33 Main Street', 245000);
    """
)
print("Table 'property_listing' created")

# commit and close connection
connection.commit()
connection.close()
