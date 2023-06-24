#!/bin/bash

# MySQL server credentials
MYSQL_ROOT_USER="root"
MYSQL_ROOT_PASSWORD=""

# Database and user details
DB_NAME="hbnb_test_db"
DB_USER="hbnb_test"
DB_PASSWORD="hbnb_test_pwd"

# Create the database if it doesn't exist
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

# Create the user if it doesn't exist
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"

# Grant privileges on the hbnb_test_db database to hbnb_test user
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"

# Grant SELECT privilege on the performance_schema database to hbnb_test user
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "GRANT SELECT ON performance_schema.* TO '$DB_USER'@'localhost';"

echo "MySQL server setup completed."


echo "Setting server 2"
# Database and user details
DB_NAME="hbnb_dev_db"
DB_USER="hbnb_dev"
DB_PASSWORD="hbnb_dev_pwd"

# Create the database if it doesn't exist
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

# Create the user if it doesn't exist
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"

# Grant privileges on the hbnb_test_db database to hbnb_test user
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';"

# Grant SELECT privilege on the performance_schema database to hbnb_test user
mysql -u $MYSQL_ROOT_USER -p$MYSQL_ROOT_PASSWORD -e "GRANT SELECT ON performance_schema.* TO '$DB_USER'@'localhost';"

echo "MySQL server setup completed."
