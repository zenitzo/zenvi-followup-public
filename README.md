# 📝 Zenvi Followup Tool – Super Simple Setup Guide (For Complete Beginners)

Welcome to your **free followup automation tool**. This guide will show you how to set it up **even if you’ve never coded before**.

---

## ⚡ **What This Tool Does**

✅ Sends automatic follow-up emails to leads in your Google Sheet  
✅ Saves you time by emailing everyone in one click

---

## 🚀 **STEP 0. Install Required Apps**

### ✅ **1. Install Visual Studio Code (VSCode)**

- [Download VSCode](https://code.visualstudio.com/)  
- Click **Download for Windows** or **Download for Mac**  
- Open the downloaded file and follow the install instructions

---

### ✅ **2. Install Python**

- [Download Python](https://python.org/downloads)  
- Click **Download Python**  
- Open the downloaded file  
- **IMPORTANT:** Check the box that says **“Add Python to PATH”** before clicking Install

---

## 🚀 **STEP 1. Download the Followup Tool**

### ✅ **Download ZIP**

1. Download the tool ZIP file from the link you received (e.g. Gumroad)
2. Find the downloaded file on your computer (usually in Downloads)
3. **Right-click → Extract All** (Windows) or **double-click to unzip** (Mac)
4. Open the unzipped folder

---

## 🚀 **STEP 2. Open the Tool in VSCode**

1. Open **Visual Studio Code**  
2. Click **“File” > “Open Folder”**  
3. Find and select the folder you just unzipped  
4. Click **“Open”**

---

## 🚀 **STEP 3. Install Required Packages**

1. In VSCode, click **“Terminal > New Terminal.”**
2. A black box (terminal) will appear at the bottom.  
3. Type the following command: pip install -r requirements.txt
4. Press **Enter**. Wait for it to finish installing.

✅ **What this does:** Installs everything needed to run the tool.

---

## 🚀 **STEP 4. Set Up Google Service Account & API Credentials**

### ✅ **1. Go to Google Cloud Console**

- [Google Cloud Console](https://console.cloud.google.com/)

### ✅ **2. Create a new project**

- Click the dropdown at the top → **New Project**

### ✅ **3. Enable Google Sheets API**

- In left sidebar, go to **APIs & Services > Library**  
- Search **“Google Sheets API”**, click it, then click **Enable**

### ✅ **4. Create Service Account**

- In left sidebar, go to **APIs & Services > Credentials**  
- Click **“Create Credentials” > “Service account”**  
- Name it (e.g. `zenvi-followup`) and click **Done**

### ✅ **5. Generate Service Account Key**

- Click into the **service account you just created**  
- Go to **“Keys” tab**  
- Click **“Add Key” > “Create new key”**  
- Choose **JSON**, then click **Create**

✅ A JSON file will download automatically.

---

## 🚀 **STEP 5. Add Google Credentials to the Tool**

1. In VSCode, if there is no credential folder simply create a new folder and call it credentials
2. now drag that JSON file you just downloaded into that folder. ( rename it to google_creds.json )

✅ Save the file.

---

## 🚀 **STEP 6. Share Your Google Sheet**

1. Copy **client_email** from your `google_creds.json`
2. Open your Google Sheet
3. Click **Share** (top right)
4. Paste the service account email and give it **Editor access**

✅ **Why:** This lets the tool read and update your sheet automatically.

---

## 🚀 **STEP 7. Configure Your Followup Settings**

1. Go to **`client_configs/followup/welcome_followup.yaml`**
2. Edit these fields:

- **client_name:** Your name or company
- **sheet_url:** Link to your Google Sheet with leads
- **email_template:** Your message (e.g. “Hey {{name}}, just checking in!”)
- **subject_line:** Email subject (e.g. “Quick follow up, {{name}}”)
- **trigger_column / trigger_value:** Filters leads to email (e.g. Status: New Lead)
- **email_field / name_field:** Columns with recipient email and name
- **campaign:** Unique name for this email batch
- **status_column:** Column to update after emailing
- **logo_url / cta_label / cta_link:** (Optional) for adding a button in emails

✅ Save the file.

---

## 🚀 **STEP 8. Set Up Your Email Login**

1. In VSCode, find **`.env.example`**
2. Rename it to **`.env`**
3. Open `.env` and replace with your info:

```
EMAIL_USERNAME=your_email_here@gmail.com
EMAIL_PASSWORD=your_app_password_here
```

✅ **How to create a Gmail App Password:**

- [Google App Passwords Setup](https://myaccount.google.com/apppasswords)
- Choose **Mail > Other (Custom name)** → name it “Zenvi Tool” → Generate
- Copy the 16-digit password and paste it here

---

## 🚀 **STEP 9. Run the Followup Tool**

In VSCode terminal, type:

```bash
python3 -m zens_engine.products.followup.main --config welcome_followup
```
hit enter

✅ **What happens:**

- Reads your Google Sheet  
- Sends followup emails to leads with your template  
- Updates their status in the sheet  
- Saves a log of all sent emails

---

## 🎉 **ALL DONE!**

You’ve successfully set up your Zenvi Followup Tool.

---

### ❓ **Need Extra Help?**

- Rewatch the setup video provided  
- Double-check every step slowly  
- Contact Zenvi for done-for-you setup if needed
- Paste your errors into Chat GPT

---

✅ **End of Beginner Setup Guide**

You’re ready to automate your followups and save hours every week.