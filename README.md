🤖 AI Code Reviewer
An intelligent code review assistant powered by Google's Gemini 1.5 Flash model. This Streamlit application helps developers get instant feedback on their code, identifying potential bugs and suggesting improvements.
🌟 Features

Real-time code analysis
Bug detection and reporting
Automated code improvement suggestions
User-friendly interface
Powered by Google's Gemini 1.5 Flash model
Instant feedback mechanism

🛠️ Installation

Clone the repository:

bashCopygit clone https://github.com/Arjun9271/AI_Code_Reviewer.git
cd AI_Code_Reviewer

Install the required dependencies:

bashCopypip install -r requirements.txt

Create a .env file in the root directory and add your Google API key:

envCopyGOOGLE_API_KEY=your_api_key_here
📦 Dependencies

streamlit
google-generativeai
python-dotenv
os

🚀 Usage

Run the Streamlit application:

bashCopystreamlit run app.py

Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
Enter your code in the text area
Click the "✨ Generate" button to get your code review

💡 How It Works

The application uses a custom system prompt that instructs the AI to act as a code reviewer
When code is submitted, it's analyzed by the Gemini 1.5 Flash model
The AI provides:

A code review heading
Bug reports (if any)
Fixed code suggestions (if needed)
Or confirmation that no changes are needed



🔒 Environment Variables
The application requires the following environment variable:

GOOGLE_API_KEY: Your Google API key for accessing the Gemini model

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
⚠️ Note
Make sure to keep your API key confidential and never commit it directly to the repository.
📝 License
This project is MIT licensed.
👨‍💻 Author

GitHub: @Arjun9271

✨ Acknowledgments

Google Gemini AI for providing the powerful language model
Streamlit for the excellent web application framework
