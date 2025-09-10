# Bias-Detector – Smashing Hidden Bias in Text

## Overview

Political content can be persuasive without being outright false. Words shape perception subtly, and I wanted to build a tool that lets **people see through propaganda** and make informed judgments.
**BiasBreaker** is a browser extension that helps users uncover subtle bias, loaded language, and propaganda in political speeches, articles, and social media posts. It highlights emotionally charged words, scores text for neutrality, and empowers users to critically analyze content in real time.

---

## Features

- Highlights **loaded or emotionally charged words**
- Detects **bias and propaganda**
- Provides a **neutrality score** for text
- Works seamlessly on **Chrome and Brave**

---

## How It Works

1. The extension extracts the page text and sends it to the backend AI server.
2. The AI analyzes the text for loaded words, emotional language, and context-based bias.
3. The extension highlights key words and displays a **summary neutrality score** in real time.

---

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/soham-rath/Propaganda-Lens.git
cd Bias-Detector
```

### 2. Set up the backend:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3. Start the backend server:

```bash
uvicorn server:app --reload
```

### 4. Load the extension in Chrome/Brave:

- Go to the extensions page (chrome://extensions/)

- Enable **Developer mode**

- Click **Load unpacked** and select the **frontend** folder

---

## What's Next

- Add support for **more languages and text formats**
- Improve the **bias detection model** with community feedback
- Include **visualizations and historical tracking** of bias trends

---

## Contributing

Contributions are welcome! You can help by:

1. Adding new spreadsheet features (formulas, formatting, copy-paste, etc.)

2. Improving performance & UI

3. Writing documentation or tutorials

Opening issues or pull requests for bug fixes and ideas
