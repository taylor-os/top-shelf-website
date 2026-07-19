# Top Shelf Website — Setup Notes

## Making the Audit Form Send Emails (Formspree)

The contact form on `contact.html` is wired to Formspree but needs a one-time setup. Takes about 5 minutes.

### Step 1 — Create a free Formspree account
Go to **formspree.io** and sign up with your email. Free, no credit card.

### Step 2 — Create a new form
1. In your Formspree dashboard, click **+ New Form**
2. Name it something like "Top Shelf Audit Requests"
3. Formspree will give you a **Form ID** — it looks like `xpwzabcd` (8 characters)

### Step 3 — Update contact.html
Open `contact.html` and find this line near the top:

```
action="https://formspree.io/f/FORMSPREE_ID"
```

Replace `FORMSPREE_ID` with your actual ID. Example:

```
action="https://formspree.io/f/xpwzabcd"
```

Save the file. That's it — the form will now email you every submission.

### Step 4 — Verify your email
Formspree will send a confirmation email to the address on your account the first time someone submits. Click the link to activate.

---

## Formspree Free Tier vs. Paid

| Plan | Submissions/month | Cost |
|------|------------------|------|
| Free | 50 | $0 |
| Basic | 1,000 | $10/mo |
| Gold | 10,000 | $40/mo |

For a small local business getting started, 50/month is plenty. Upgrade when you're getting close to the limit.

---

## Alternative: Netlify Forms (Free if hosting on Netlify)

If you host the site on Netlify (see below), you can use their built-in form handling instead — zero cost up to 100 submissions/month, no Formspree account needed.

To switch to Netlify Forms:
1. Remove the `action` and `method` attributes from the form tag in `contact.html`
2. Add the `netlify` attribute: `<form netlify name="audit-form">`
3. Deploy to Netlify — it auto-detects the form

Netlify will email you each submission and you can view them in the Netlify dashboard.

---

## Deploying the Website to Netlify (Free)

Netlify hosts static websites for free with a real HTTPS URL. No server needed.

### Drag-and-drop method (easiest)
1. Go to **netlify.com** and create a free account
2. In your dashboard, click **Add new site → Deploy manually**
3. Drag the entire `website/` folder onto the upload area
4. Netlify gives you a URL like `https://topshelf-abc123.netlify.app`
5. Optional: connect a custom domain (e.g. `topshelfbusinesssolutions.com`) in site settings

### When you update the site
Just drag the folder again — Netlify replaces the previous deployment.

### Custom domain
In Netlify site settings → Domain management → Add custom domain. Point your domain's DNS to Netlify (they walk you through it step by step).

---

## What the Form Sends

Each submission emails you:
- **Subject:** New Free Audit Request — Top Shelf Business Solutions
- **Fields:** Name, Business Name, Business Type, Phone, Email, Biggest Challenge
- After submit, visitor is redirected to `thank-you.html` automatically
