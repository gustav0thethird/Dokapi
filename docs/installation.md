# Installation

## Prerequisites

Before installing Dokapi, ensure you have the following:

- Python 3.6 or higher
- pip (Python package installer)

## Installation Steps

1. **Clone the Repository**

   Open your terminal and clone the Dokapi repository:

   ```bash
   git clone https://github.com/gustav0thethird/Dokapi.git
   cd Dokapi
   ```

2. **Install Dependencies**

   Install the required Python packages using pip. Run the following command in the terminal:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all necessary dependencies listed in the `requirements.txt` file.

3. **Verify Installation**

   To verify that Dokapi is installed correctly, you can run the following command:

   ```bash
   python dokapi.py
   ```

   If the installation was successful, you should see a prompt asking for a target URL or IP.

## Additional Configuration

- Ensure that you have access to the Tor network if you plan to use the Tor proxy feature. You may need to install the Tor service and configure it accordingly.

- If you want to enable CSV output for reports, ensure that the `Reports` directory exists or is created automatically by the application.

## Running Dokapi

To run Dokapi, execute the following command in your terminal:

```bash
python dokapi.py
```

You will be prompted to enter a target URL or IP and whether to use the Tor proxy.

## Troubleshooting

If you encounter issues during installation or while running Dokapi, check the following:

- Ensure that all dependencies are installed correctly.
- Verify that your Python version is compatible.
- Check your internet connection and Tor service status if using the Tor proxy.

For further assistance, refer to the [README.md](README.md) file or open an issue in the GitHub repository.
