# YouTube Comment Extractor

## YouTube API Setup Guide

1. **Create a Google Cloud Project**  
   - Go to [Google Cloud Console](https://console.developers.google.com/).
   - Click on `Select a project` and then `New Project`.
   - Enter a project name and click `Create`.

2. **Enable YouTube Data API v3**  
   - In the project dashboard, click on `Library` in the left hand menu.
   - Search for `YouTube Data API v3` and select it.
   - Click on the `Enable` button.

3. **Create Credentials**  
   - Go to `Credentials` in the left menu.
   - Click on `Create Credentials` and select `API Key`.
   - Copy your API Key and store it securely.

4. **Set Up OAuth Consent Screen**  
   - Under the `APIs & Services` menu, go to `OAuth consent screen`.
   - Choose `External` and fill out the required information.
   - Save and proceed.

## Usage Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Catherine42963/youtube-comment-extractor.git
   ```

2. **Install dependencies**  
   Navigate to the project directory and run:
   ```bash
   npm install
   ```

3. **Set your API key**  
   - In the project, locate the `config.js` file.
   - Replace `YOUR_API_KEY` with the API key you created earlier.

4. **Run the application**  
   ```bash
   node index.js
   ```  
   - Follow the prompts to extract comments from YouTube videos.

## Notes  
- Ensure you have Node.js installed on your system.  
- For detailed documentation, refer to the [YouTube Data API Documentation](https://developers.google.com/youtube/v3/docs)