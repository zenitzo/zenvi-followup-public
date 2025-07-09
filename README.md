# Zenvi Automation Engine ⚙️📬

This is a production-grade, modular automation system built with Python. Each product (like `followup`, `onboarding`, or `proposal_generator`) reads inputs from sources like Google Sheets or webhooks, processes them using YAML configs, and sends outputs like branded emails or PDF proposals — with full logging and deduplication.

---

## 🧠 What It Does

- ✅ Modular plug-and-play products (followup, onboarding, proposal generator, etc.)
- ✅ Reads lead data from Google Sheets (via gspread)
- ✅ Filters leads by trigger column/value (e.g. `Stage: onboard`)
- ✅ Sends **branded HTML emails with personalization**
- ✅ Logs activity per campaign (e.g. `lead_welcome_emails.csv`)
- ✅ Dedupes based on both sheet status + log history
- ✅ Updates a status column in the Sheet after each send

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/zenvi-automation.git
cd zenvi-automation
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your `.env` File

Create a `.env` file in the project root:

```
EMAIL_USERNAME=youremail@example.com
EMAIL_PASSWORD=yourpassword
```

> ⚠️ For Gmail, use an App Password instead of your login.

---

## 📝 Configure a Campaign

YAML configs live under:

```
client_configs/{product_slug}/{your_config}.yaml
```

Example for `onboarding`:

```yaml
client_name: "Your Brand"
sheet_url: "https://docs.google.com/..."
email_template: "Hey {{name}}, this is Akira from Zen Automations!"
subject_line: "Hey {{name}}, welcome aboard!"
trigger_column: "Stage"
trigger_value: "onboard"
email_field: "Email"
name_field: "Name"
campaign: "onboarding_welcome"
source_type: "gspread"
status_column: "Automation Status"
logo_url: "https://yourdomain.com/logo.png"
cta_label: "Start Now"
cta_link: "https://yourlink.com"
```

---

## 🚀 How to Run Each Product

From the root folder, run a product using:

```bash
python3 -m zens_engine.products.followup.main --config welcome_followup
```

```bash
python3 -m zens_engine.products.onboarding.main --config onboarding_welcome
```

```bash
python3 -m zens_engine.products.proposal_generator.main --config test_proposal
```

> `--config` refers to the YAML name (without `.yaml` extension)

---

## 📦 Output and Logging

- Emails sent via SMTP
- Logged to: `zens_engine/logs/{product}/{campaign}_emails.csv`
- Sheet status column updated (e.g. `Automation Status` = "Emailed")

---

## 🧪 Optional Features (Coming Soon)

- `--dry_run` mode to simulate sends
- Multi-source input support (Supabase, APIs)
- PDF proposal attachments
- CRM and webhook integrations

---

## 🔒 Version

This is the **v1.8 stable release** of the Zenvi Automation Engine — powering real campaigns across multiple businesses.

More plug-and-play products (proposals, payment flows, deadline reminders) are live or coming soon.