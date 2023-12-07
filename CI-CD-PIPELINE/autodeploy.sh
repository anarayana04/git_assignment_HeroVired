#!/bin/bash

# Set your Git repository URL and branch
REPO_URL="https://github.com/anarayana04/git_assignment_HeroVired.git"

# Clone the latest code
echo "Cloning the latest code from $REPO_URL..."
git clone $REPO_URL
cp /etc/nginx/sites-available/git_assignment_HeroVired/CI-CD-PIPELINE/index.html /var/www/html/
# Check if the clone was successful
if [ $? -eq 0 ]; then
    echo "Code cloned successfully."

    # Restart Nginx
    echo "Restarting Nginx..."
    sudo systemctl restart nginx

    # Check if Nginx restart was successful
    if [ $? -eq 0 ]; then
        echo "Nginx restarted successfully."
    else
        echo "Failed to restart Nginx. Please check Nginx configuration."
        exit 1
    fi
else
    echo "Failed to clone the latest code. Please check the Git repository URL and credentials."
    exit 1
fi

# Exit with success
rm -rf git_assignment_HeroVired
exit 0