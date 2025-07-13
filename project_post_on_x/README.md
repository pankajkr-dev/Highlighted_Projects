# Post to X (Twitter) with Python

A simple Streamlit web application that allows you to post tweets directly to X (formerly Twitter) using the Twitter API v2.

## Features

- Clean and intuitive web interface built with Streamlit
- Direct posting to X/Twitter using Tweepy v2
- Character limit validation (280 characters)
- Real-time feedback on tweet posting status
- Clickable links to view posted tweets

## Screenshots

![App Interface](Screenshot%202025-07-13%20234307.png)
![Tweet Composition](Screenshot%202025-07-13%20234819.png)
![Success Message](Screenshot%202025-07-13%20234920.png)

## Prerequisites

Before running this application, you need:

1. **Python 3.7+** installed on your system
2. **X (Twitter) Developer Account** with API access
3. **Twitter API credentials** (Consumer Key, Consumer Secret, Access Token, Access Token Secret)

## Installation

1. Clone or download this repository
2. Install the required Python packages:

```bash
pip install streamlit tweepy
```

## Setup

### 1. Get Twitter API Credentials

1. Visit the [Twitter Developer Portal](https://developer.twitter.com/)
2. Create a new app or use an existing one
3. Generate your API credentials:
   - Consumer Key
   - Consumer Secret
   - Access Token
   - Access Token Secret

### 2. Configure API Credentials

⚠️ **Important Security Note**: The current implementation has API credentials directly embedded in the code. For production use, you should use environment variables or a secure configuration method.

**Option A: Environment Variables (Recommended)**

```python
import os
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
```

**Option B: Direct Replacement (Current Method)**
Replace the placeholder credentials in `x_post_app.py`:

```python
consumer_key = "your_consumer_key_here"
consumer_secret = "your_consumer_secret_here"
access_token = "your_access_token_here"
access_token_secret = "your_access_token_secret_here"
```

## Usage

1. Navigate to the project directory
2. Run the Streamlit application:

```bash
streamlit run x_post_app.py
```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`)
4. Write your tweet in the text area (max 280 characters)
5. Click "Post Tweet" to publish your tweet
6. View the success message with a link to your posted tweet

## File Structure

```
project_post_on_x/
├── README.md                          # This file
├── x_post_app.py                      # Main application file
├── Screenshot 2025-07-13 234307.png   # App interface screenshot
├── Screenshot 2025-07-13 234819.png   # Tweet composition screenshot
└── Screenshot 2025-07-13 234920.png   # Success message screenshot
```

## Dependencies

- **streamlit**: Web framework for creating the user interface
- **tweepy**: Python library for accessing the Twitter API

## Security Considerations

🔒 **Important**: Never commit your actual API credentials to version control. Consider:

1. Using environment variables
2. Using a `.env` file (and adding it to `.gitignore`)
3. Using cloud-based secret management services
4. Using Streamlit's secrets management for deployment

## Troubleshooting

### Common Issues

1. **"Failed to post tweet" error**:

   - Check your API credentials
   - Ensure your Twitter app has write permissions
   - Verify your account is in good standing

2. **"Module not found" error**:

   - Install required packages: `pip install streamlit tweepy`

3. **Empty tweet warning**:
   - Ensure you've entered text in the text area before clicking "Post Tweet"

## API Rate Limits

Be aware of Twitter's API rate limits:

- Tweet creation: 300 requests per 15-minute window (per user)
- Follow Twitter's developer guidelines and terms of service

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## Support

If you encounter any issues or have questions, please check the troubleshooting section above or refer to the official documentation:

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Tweepy Documentation](https://docs.tweepy.org/)
- [Twitter API Documentation](https://developer.twitter.com/en/docs)
