
# 🔴Youtube_Channel_Comments_Scraper

This Python script uses the YouTube Data API v3 to extract top-level comments from all videos on a specific YouTube channel and export them into an Excel file for analysis, research, or reporting.📈🔍


## 🔍Overview
This tool automates:
- ✅ Retrieving **all video IDs** from a target YouTube channel  
- ✅ Extracting **top-level comments** from each video  
- ✅ Handling **errors**, such as videos with disabled comments  
- ✅ Exporting the extracted comments into a **structured Excel spreadsheet**

---
## 🧰Prerequisites

Ensure the following Python packages are installed:

```bash
  pip install google-api-python-client pandas openpyxl
```
You will also need a valid YouTube Data API v3 Key (see below).
## 🔑 How to Get a YouTube API Key

Follow these steps to obtain your API key:

- Go to the [Google Cloud Console](https://console.cloud.google.com/welcome?_gl=1*1w9bddn*_up*MQ..&gclid=CjwKCAjwk43ABhBIEiwAvvMEB1gqEhMdWtocaqjwTSqRT9dl1wPbxVQ1KtGI9a-g9K2eMP4IC-jKhBoCagkQAvD_BwE&gclsrc=aw.ds&project=magnetic-quasar-457317-f3).
- Sign in using your Google account.
- Click **"Create a Project"** or select an existing one.
- In the top search bar, type **"YouTube Data API v3"**.
- Select it from the results, then click **"Enable"**.
- In the left sidebar, go to **"Credentials"**.
- Click **"Create Credentials"** → **"API key"**.
- Copy the generated key and paste it into the script:

```python
    API_KEY = "YOUR_API_KEY_HERE"
```

## 🎯 How to Get a Channel ID

To find the **Channel ID** of a target YouTube channel:

- Open the YouTube channel in your web browser.
- Click the **"About"** tab (or **"More"**, depending on your platform).
- Scroll down and click **"Share Channel"** or look for the **Channel ID** section.
- Copy the **Channel ID** shown and paste it into the script where required:

```python
channel_id = "YOUR_CHANNEL_ID"
```


## 🚀 Getting Started

- **Clone or download** this repository to your local machine.

- **Open the Python script** in your preferred editor.

- **Replace the placeholder values**:
   - `DEVELOPER_KEY` with your **YouTube API key**
   - `channel_id` with the **Channel ID** of the target channel

- **Run the script** using the command:

    ```bash
    python your_script_name.py
    ```

- The comments will be saved to an Excel file named:

    ```
    comments.xlsx
    ```


## 📁 Output Format

The resulting Excel file includes:

| Column         | Description                          |
|----------------|--------------------------------------|
| `author`       | Commenter’s display name             |
| `published_at` | Timestamp of original comment        |
| `updated_at`   | Last updated timestamp               |
| `like_count`   | Number of likes                      |
| `text`         | Comment content                      |


## ⚠️ Notes

- Only **top-level comments** are collected (replies are excluded).
- The script automatically handles **pagination** for channels with many videos.
- Videos with **disabled comments** are gracefully skipped.
- **API quota limits** may restrict usage — use your key responsibly.


## 🤝 Contributions

Contributions are welcome!  
Feel free to submit a **pull request** or open an **issue** to suggest improvements, report bugs, or request new features.
