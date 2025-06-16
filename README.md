# 📬 Email Spam/Ham Classifier Web App

This is a simple web-based application that classifies email text as either **Spam** or **Ham (Not Spam)** using a trained machine learning model.  
It was built using **Django**, **scikit-learn**, and a clean frontend with **HTML, Tailwind CSS, and JavaScript**.

---

## 🔍 How It Works

1. The user enters a block of email text in a form.
2. That text is passed to a backend classifier built using `scikit-learn`.
3. The classifier outputs a label: `"Spam"` or `"Ham"`.
4. The result is displayed instantly with styling and feedback.

---

## ⚙️ Tech Stack

- **Backend**: Django (Python)
- **Machine Learning**: scikit-learn
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Deployment**: *https://mailai.pythonanywhere.com*

---

## 🤖 ML Model

- The model is trained on a standard labeled dataset (e.g., SMS Spam Collection or similar).
- Text is preprocessed using:
  - Lowercasing
  - Stopword removal
  - CountVectorizer or TfidfVectorizer
- Saved as a `.pkl` file and loaded in Django views

---

## 🖼️ UI

- Clean, responsive interface using **Tailwind CSS**
- JavaScript handles loading state and basic error checking
- Fast and minimal — no page reloads required for classification

---

## 🧪 Sample Workflow

1. User visits homepage
2. Enters sample email:  
   `"Congratulations! You've won a free iPhone. Click here."`
3. Clicks **"Classify"**
4. Server returns: **Spam**

---

## 🧑‍💻 Author

**Muhammad Kamkoriwala**  
📧 kamkoriwalamuhammad@gmail.com  
🔗 GitHub: [github.com/Dragoon812003](https://github.com/Dragoon812003)

---

## 📦 Notes

- This is a simple educational project built to explore ML deployment in web environments.
- No database is used for storage — the model runs stateless with every request.
- Can be extended to include:
  - Real email parsing
  - Email content preview
  - User login and email history
