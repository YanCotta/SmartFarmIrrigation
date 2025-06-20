#!/usr/bin/env python3
"""
SmartFarmIrrigation - Setup Script
Automatiza a configuração inicial do projeto
"""

import os
import sys
import subprocess
import sqlite3
from pathlib import Path

def print_step(step_num, description):
    """Print a formatted step description"""
    print(f"\n🔧 Step {step_num}: {description}")
    print("-" * 50)

def check_python_version():
    """Check if Python version is adequate"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_requirements():
    """Install Python requirements"""
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, cwd="scripts")
        print("✅ Python dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install Python dependencies")
        return False

def setup_environment_file():
    """Create .env file if it doesn't exist"""
    env_file = Path(".env")
    if not env_file.exists():
        env_content = """# OpenWeather API Configuration
OPENWEATHER_API_KEY=YOUR_ACTUAL_API_KEY_HERE
CITY=Sao Paulo,BR

# Database Configuration
DB_PATH=irrigation.db

# Model Configuration
MODEL_VERSION=v1.0
"""
        with open(env_file, "w") as f:
            f.write(env_content)
        print("✅ .env file created")
        print("⚠️  Please edit .env and add your OpenWeather API key!")
    else:
        print("✅ .env file already exists")

def initialize_database():
    """Initialize the SQLite database"""
    try:
        # Import and run database initialization
        sys.path.append('scripts')
        from database import initialize_database
        initialize_database()
        print("✅ Database initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to initialize database: {e}")
        return False

def train_initial_model():
    """Train the initial ML model"""
    try:
        subprocess.run([sys.executable, "train_model.py"], 
                      check=True, cwd="scripts")
        print("✅ Initial ML model trained successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to train initial model")
        return False

def verify_setup():
    """Verify that setup was successful"""
    checks = []
    
    # Check if model file exists
    if Path("irrigation_model.joblib").exists():
        checks.append("✅ ML Model file found")
    else:
        checks.append("❌ ML Model file missing")
    
    # Check if database exists
    if Path("irrigation.db").exists():
        checks.append("✅ Database file found")
    else:
        checks.append("❌ Database file missing")
    
    # Check if .env exists
    if Path(".env").exists():
        checks.append("✅ Environment file found")
    else:
        checks.append("❌ Environment file missing")
    
    return checks

def main():
    """Main setup function"""
    print("🌱 SmartFarmIrrigation Setup Script")
    print("=" * 50)
    
    # Step 1: Check Python version
    print_step(1, "Checking Python version")
    if not check_python_version():
        sys.exit(1)
    
    # Step 2: Install requirements
    print_step(2, "Installing Python dependencies")
    if not install_requirements():
        print("⚠️  You may need to install dependencies manually:")
        print("cd scripts && pip install -r requirements.txt")
    
    # Step 3: Setup environment file
    print_step(3, "Setting up environment configuration")
    setup_environment_file()
    
    # Step 4: Initialize database
    print_step(4, "Initializing database")
    if not initialize_database():
        print("⚠️  You may need to initialize the database manually:")
        print("cd scripts && python database.py")
    
    # Step 5: Train initial model
    print_step(5, "Training initial ML model")
    if not train_initial_model():
        print("⚠️  You may need to train the model manually:")
        print("cd scripts && python train_model.py")
    
    # Step 6: Verify setup
    print_step(6, "Verifying setup")
    checks = verify_setup()
    for check in checks:
        print(check)
    
    # Final instructions
    print("\n🎉 Setup completed!")
    print("\n📝 Next steps:")
    print("1. Edit .env file and add your OpenWeather API key")
    print("2. Run the dashboard: cd scripts && streamlit run dashboard.py")
    print("3. Check the INSTALL.md for detailed instructions")
    print("\n🆘 If you encounter issues, check the troubleshooting section in INSTALL.md")

if __name__ == "__main__":
    main()
