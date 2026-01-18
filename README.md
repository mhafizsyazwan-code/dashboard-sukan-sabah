# Create and navigate to project directory
mkdir -p dashboard-sukan-sabah
cd dashboard-sukan-sabah

# Initialize Git repository
git init

# Create README file
echo "# dashboard-sukan-sabah" > README.md

# Add remote origin (replace with your actual URL)
# git remote add origin https://github.com/yourusername/dashboard-sukan-sabah.git

# Stage, commit, and push
git add README.md
git commit -m "chore: initialize repository"
git branch -M main  # Rename master to main if needed
git push -u origin main

# Create and switch to feature branch
git checkout -b feature/add-dashboard
