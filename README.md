# 📝 Zenvi Followup Tool – Super Simple Setup Guide (For Complete Beginners)

Welcome to your **free followup automation tool**. This guide will show you how to set it up **even if you’ve never coded before**.

---

## ⚡ **What This Tool Does**

✅ Sends automatic follow-up emails to leads in your Google Sheet  
✅ Saves you time by emailing everyone in one click

---

## 🚀 **STEP 0. Install Required Apps**

### ✅ **1. Install Visual Studio Code (VSCode)**

- Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Click **Download for Windows** or **Download for Mac**
- Open the downloaded file and follow the install instructions

---

### ✅ **2. Install Python**

- Go to [https://python.org/downloads](https://python.org/downloads)
- Click **Download Python**
- Open the downloaded file
- IMPORTANT: **Check the box that says “Add Python to PATH”** before clicking Install

---

## 🚀 **STEP 1. Download the Followup Tool**

### ✅ **Option A. Easiest Way (Download ZIP)**

1. Go to the tool’s GitHub page (link will be provided)
2. Click the **green “Code” button**
3. Click **“Download ZIP”**
4. Find the downloaded file on your computer (usually in Downloads)
5. **Right-click → Extract All** (Windows) or **double-click to unzip** (Mac)
6. Open the unzipped folder

---

## 🚀 **STEP 2. Open the Tool in VSCode**

1. Open **Visual Studio Code**
2. Click **“File” > “Open Folder”**
3. Find and select the folder you just unzipped
4. Click **“Open”**

---

## 🚀 **STEP 3. Set Up Your Virtual Environment**

1. At the top menu in VSCode, click **“Terminal” > “New Terminal.”**

   - A black box will appear at the bottom.

2. Type (or copy and paste) this command:

### ✅ **For Mac:**

```bash
python3 -m venv venv
```

### ✅ **For Windows:**

```bash
python -m venv venv
```

3. Press **Enter**.
4. Then activate it:

### ✅ **For Mac:**

```bash
source venv/bin/activate
```

### ✅ **For Windows:**

```bash
venv\Scripts\activate
```

✅ If successful, you will see something like `(venv)` at the start of the line in your terminal.

---

## 🚀 **STEP 4. Install Required Packages**

In the same terminal, type:

```bash
pip install -r requirements.txt
```

Press **Enter**. Wait for it to finish installing.

---

## 🚀 **STEP 5. Set Up Your Google Credentials**

1. Go to the **`credentials`** folder in VSCode.
2. Open the file called **`google_creds.json`**.

3. Follow the **simple setup instructions** in `credentials_setup.md` to fill out your credentials.

✅ **Summary:**  
You will create a **Google Service Account**, download your credentials, and paste them here.

---

## 🚀 **STEP 6. Set Up Your Followup Config**

1. Go to **`client_configs/followup/`** folder.
2. Open **`welcome_followup.yaml`**.

3. Update:

- **client_name:** Your name or company
- **sheet_url:** The link to your Google Sheet with leads
- **email_template:** The message you want to send (e.g. “Hey {{name}}, just checking in!”)
- **subject_line:** The email subject (e.g. “Quick follow up, {{name}}”)
- **logo_url, cta_label, cta_link:** Optional for adding a button in your email

---

## 🚀 **STEP 7. Share Your Google Sheet**

1. Open your Google Sheet
2. Click **“Share”** (top right)
3. Copy the **client_email** from your `google_creds.json` file
4. Paste it into the Share box and give it **Editor access**

---

## 🚀 **STEP 8. Set Up Your Email Login**

1. In VSCode, find the file called **`.env.example`**
2. Rename it to **`.env`**

3. Open `.env` and replace with your info:

```
EMAIL_USERNAME=your_email_here@gmail.com
EMAIL_PASSWORD=your_app_password_here
```

✅ **Important:**  
If using Gmail, create an **App Password** (Google “Gmail App Password setup”) and paste it here instead of your normal password.

---

## 🚀 **STEP 9. Run the Followup Tool**

1. Make sure your virtual environment is still activated (see STEP 3).

2. In the terminal, type:

```bash
python3 -m zens_engine.products.followup.main --config welcome_followup
```

(If on Windows and python3 doesn’t work, use `python` instead.)

✅ **What will happen:**

- The tool will read your Google Sheet
- Send followup emails to each person with your template
- Mark them as emailed in your Sheet
- Save a log file of who was emailed

---

## 🎉 **ALL DONE!**

You have successfully set up your Zenvi Followup Automation Tool.

---

### ❓ **Need Extra Help?**

- Rewatch the setup video
- Double check every step slowly
- Contact Zenvi for paid setup support if needed

---

✅ **End of Dummy-Friendly Setup Guide**

You’re ready to automate your followups and save hours every week.
