# Vylongara Kalari — website

Static website for **vailongarakalari.in**: home page with large Kshetram photos, the six-generation lineage (five Acharya portraits plus a lamp for the sixth generation, who is still learning) and the present Acharya, plus the policy pages that Meta, Razorpay and Google ask for.

- Hosting: **GitHub Pages** (free, HTTPS)
- Domain: **GoDaddy**
- Enquiry form: **Supabase** (optional; without it the form opens WhatsApp)

```
index.html                     Home page
contact.html                   Contact Us
privacy-policy.html            Privacy Policy
terms.html                     Terms & Conditions
refund-policy.html             Cancellation & Refund Policy
service-delivery-policy.html   Service Delivery Policy (Razorpay asks for this)
404.html                       Not-found page
CNAME                          Tells GitHub Pages the domain
assets/css/style.css           All styling
assets/js/config.js            Supabase + WhatsApp settings
assets/js/main.js              Menu, gallery, enquiry form
assets/img/...                 Logo and photos (replace the placeholders)
supabase/schema.sql            Enquiries table for Supabase
tools/build.py                 Optional generator (see "Editing")
```

---

## 1. Before you publish — replace the placeholders

Already filled in: name (Vylongara Kalari), WhatsApp +91 62821 26602, phones +91 77363 34581 / +91 80896 14581, email vailongarakalari2025@gmail.com, office hours 9 AM – 5 PM, Instagram and Facebook links. To change any of them later, edit the `C = dict(...)` block in `tools/build.py` and run it (see "Editing").

Still to fill: the **PIN code** — search for `680XXX` and replace it with the real PIN (the address should match the Udyam certificate).

In `index.html`, lines marked `<!-- EDIT -->` are where the Kalari's own words go: history, the Acharyas' names, the present Acharya's introduction.

### Photos

Replace these files **keeping the same names** (JPG, under ~400 KB each; compress at squoosh.app):

| File | What | Shape / size |
| --- | --- | --- |
| `assets/img/kshetram/hero.jpg` | Main Kshetram photo (top of page) | Landscape, 2000×1200 or larger |
| `assets/img/kshetram/kshetram-1.jpg` | Kshetram front | Landscape 1600×1100 |
| `assets/img/kshetram/kshetram-2.jpg` | Sreekovil / inside (also used in Heritage) | Landscape 1600×1100 |
| `assets/img/kshetram/kshetram-3.jpg` | Evening deeparadhana | 1600×1600 |
| `assets/img/kshetram/kshetram-4.jpg` | Kalari | 1600×1100 |
| `assets/img/kshetram/kshetram-5.jpg` | Amavasi Kalasha Pooja | 1600×1100 |
| `assets/img/kshetram/kshetram-6.jpg` | Kshetram grounds | 1600×1600 |
| `assets/img/acharya-main.jpg` | Present Acharya (5th generation), large portrait | Portrait 1000×1300 |
| `assets/img/lineage/generation-1.jpg` … `generation-4.jpg` | Portraits of the four earlier Acharyas, 1st to 4th generation (old photos or paintings are fine) | Portrait 600×760 |
| `assets/img/lineage/generation-5.jpg` | Present Acharya (5th generation); can be a crop of the same photo as `acharya-main.jpg` | Portrait 600×760 |
| `assets/img/og-image.jpg` | Picture shown when the link is shared on WhatsApp/Facebook | 1200×630 |

Captions under the gallery photos are in `index.html` (search `figcaption`).

---

## 2. Put the code on GitHub

1. github.com → **New repository** → name `vailongara-kalari-website` → Public → Create.
2. **Add file → Upload files** → drag in *everything inside this folder* (so `index.html` is at the top level, not inside another folder) → **Commit changes**.

## 3. Turn on GitHub Pages

1. Repository → **Settings → Pages**.
2. Source: **Deploy from a branch** → Branch **main**, folder **/ (root)** → Save.
3. Custom domain: `vailongarakalari.in` → Save (the `CNAME` file already contains it).
4. After step 4 finishes, tick **Enforce HTTPS**.

## 4. Point the GoDaddy domain to GitHub

GoDaddy → **My Products → vailongarakalari.in → DNS** (Manage DNS):

1. Delete the existing **A** record for `@` ("Parked") and any **CNAME** for `www`.
2. Add four **A** records, Name `@`:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
3. Add a **CNAME**: Name `www` → Value `<your-github-username>.github.io`
4. Wait 15 minutes to a few hours. GitHub Pages shows "DNS check successful" → tick **Enforce HTTPS**.

✅ `https://vailongarakalari.in` opens the site with a padlock.

## 5. Email on the domain (optional, helps Meta verification)

The site currently shows the Kalari Gmail. If Meta asks for a domain email, create `info@vailongarakalari.in` with **Zoho Mail** (free plan) or GoDaddy email, or forward it to the Kalari Gmail with **ImprovMX** (free). Each gives you MX/TXT records to add in GoDaddy DNS — add them *without* touching the GitHub records above.

## 6. Supabase enquiry form (optional)

1. supabase.com → **New project** → name `vailongara-kalari`, region **Mumbai (ap-south-1)**.
2. **SQL Editor → New query** → paste `supabase/schema.sql` → **Run**.
3. **Project Settings → API**: copy **Project URL** and the **anon public** key into `assets/js/config.js` → commit.
4. Test: send an enquiry on the site → it appears in **Table Editor → enquiries**. Office staff can mark `status` as CONTACTED / CLOSED.

The anon key is safe in a public website: the database rules only allow adding enquiries, never reading them.

## 7. Use the site for verification

| Where | What to enter |
| --- | --- |
| **Meta Business verification** | Website `https://vailongarakalari.in`; confirm contact by **domain** or **info@** email |
| **Meta domain verification** | Business Settings → Brand safety → Domains → Add → *Meta-tag*: paste the tag on the marked line in `index.html` `<head>` → commit → Verify (or use the DNS TXT option in GoDaddy) |
| **Meta app (Live mode)** | Privacy policy URL `https://vailongarakalari.in/privacy-policy.html`, Terms URL `https://vailongarakalari.in/terms.html` |
| **Razorpay activation** | Website + Contact `/contact.html`, Privacy `/privacy-policy.html`, Terms `/terms.html`, Refunds `/refund-policy.html`, Shipping/Delivery `/service-delivery-policy.html` |
| **Google OAuth branding** | Home page `https://vailongarakalari.in`, Privacy `/privacy-policy.html`, authorised domain `vailongarakalari.in` |

The policy pages are a practical starting point, not legal advice; have them reviewed if the Kalari wants certainty.

---

## Editing

- **Small changes:** edit the HTML files directly on GitHub (pencil icon) → Commit. The live site updates in about a minute.
- **Many changes to details** (phone, address, prices) across all pages: edit the `C = dict(...)` block at the top of `tools/build.py` and run `python tools/build.py` — it regenerates all pages. Don't mix the two methods: running the generator overwrites direct HTML edits.
- Colours and fonts are at the top of `assets/css/style.css` (`:root`).
