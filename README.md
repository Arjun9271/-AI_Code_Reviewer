# 🤖 AI Code Reviewer

An intelligent code review assistant powered by Google's Gemini 1.5 Flash model. This Streamlit application helps developers get instant feedback on their code, identifying potential bugs and suggesting improvements.

## 🌟 Features

- Real-time code analysis
- Bug detection and reporting
- Automated code improvement suggestions
- User-friendly interface
- Powered by Google's Gemini 1.5 Flash model
- Instant feedback mechanism

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Arjun9271/AI_Code_Reviewer.git
cd AI_Code_Reviewer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

## 📦 Dependencies

- streamlit
- google-generativeai
- python-dotenv
- os

## 🚀 Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter your code in the text area

4. Click the "✨ Generate" button to get your code review

## 💡 How It Works

1. The application uses a custom system prompt that instructs the AI to act as a code reviewer
2. When code is submitted, it's analyzed by the Gemini 1.5 Flash model
3. The AI provides:
   - A code review heading
   - Bug reports (if any)
   - Fixed code suggestions (if needed)
   - Or confirmation that no changes are needed

## 🔒 Environment Variables

The application requires the following environment variable:
- `GOOGLE_API_KEY`: Your Google API key for accessing the Gemini model

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Arjun9271/AI_Code_Reviewer/issues).

## ⚠️ Note

Make sure to keep your API key confidential and never commit it directly to the repository.

## 📝 License

This project is [MIT](LICENSE) licensed.

## 👨‍💻 Author

- GitHub: [@Arjun9271](https://github.com/Arjun9271)

## ✨ Acknowledgments

- Google Gemini AI for providing the powerful language model
- Streamlit for the excellent web application framework
