#!/bin/bash

# Set MySQL root user and password
MYSQL_USER="root"
MYSQL_PASSWORD="your_root_password"

# Function to check if a user exists
check_user_exists() {
  local user="$1"
  local host="$2"
  local result=$(mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -se "SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = '$user' AND host = '$host');")
  echo $result
}

# Function to create a user if it doesn't exist
create_user_if_not_exists() {
  local user="$1"
  local host="$2"
  if [ $(check_user_exists $user $host) -eq 0 ]; then
    echo "Creating user '$user'@'$host'..."
    mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "CREATE USER '$user'@'$host';"
  else
    echo "User '$user'@'$host' already exists."
  fi
}

# Function to grant privileges to a user
grant_privileges() {
  local user="$1"
  local host="$2"
  echo "Granting privileges to '$user'@'$host'..."
  mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "GRANT ALL PRIVILEGES ON *.* TO '$user'@'$host';"
}

# Function to show grants for a user
show_grants() {
  local user="$1"
  local host="$2"
  echo "Privileges for '$user'@'$host':"
  mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "SHOW GRANTS FOR '$user'@'$host';"
}

# Main script execution
echo "Checking and managing MySQL users..."

# User and host details
USER_1="user_0d_1"
USER_2="user_0d_2"
HOST="localhost"

# Create users if they do not exist
create_user_if_not_exists $USER_1 $HOST
create_user_if_not_exists $USER_2 $HOST

# Grant privileges to users
grant_privileges $USER_1 $HOST
grant_privileges $USER_2 $HOST

# Show grants for users
show_grants $USER_1 $HOST
show_grants $USER_2 $HOST

echo "Script execution completed."
