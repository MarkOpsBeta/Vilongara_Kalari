"""Builds the static Vylongara Kalari website into ./site (shared header/footer, home + legal pages)."""
import os, datetime

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root

# ---- business details (placeholders are listed in README "Before you publish") ----
C = dict(
    name="Vylongara Kalari",
    domain="vailongarakalari.in",
    address="Vylongara Kalari, near Chumanna Mannu, Thrissur, Kerala – 680XXX",
    phones=["+91 77363 34581", "+91 80896 14581"],
    email="vailongarakalari2025@gmail.com",
    wa="916282126602",          # WhatsApp booking number, country code, no +
    office="9 AM – 5 PM",
    instagram="https://www.instagram.com/vailongara_kalari?obrf=MXBwdWF6NXVwMXA2dg==",
    facebook="https://www.facebook.com/share/1HTxwyCHn2/",
    updated="7 November 2026",
    map_q="Vailongara Kalari, Chumanna Mannu, Thrissur, Kerala",  # spelling as listed on Google Maps
)
WA = f"https://wa.me/{C['wa']}?text=Namaskaram"
TEL = lambda n: "tel:" + n.replace(" ", "")
WA_SHOW = "+" + C["wa"][:2] + " " + C["wa"][2:7] + " " + C["wa"][7:]
YEAR = datetime.date.today().year

I = {  # inline icons (stroke = currentColor)
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-2-1.2 7.5 7.5 0 0 1-1.4-1.7c-.1-.2 0-.4.1-.5l.4-.4.2-.4v-.4l-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.4-.3Z"/></svg>',
 "lamp": '<svg viewBox="0 0 40 40" fill="currentColor" aria-hidden="true"><path d="M20 4c2.2 3 3 5 3 6.6A3 3 0 0 1 17 10.6C17 9 17.8 7 20 4z" opacity=".85"/><path d="M8 17h24c-1 4-5.5 6-12 6S9 21 8 17z"/><rect x="18.5" y="23" width="3" height="8"/><path d="M12 35c0-2.5 3.6-4 8-4s8 1.5 8 4z"/></svg>',
 "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3.2"/></svg>',
 "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="m12 3 2.6 5.5 6 .8-4.4 4.2 1.1 6L12 16.6 6.7 19.5l1.1-6L3.4 9.3l6-.8L12 3Z"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "lotus": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 20c-4 0-8-2-9-6 3 0 6 1 9 4 3-3 6-4 9-4-1 4-5 6-9 6Z"/><path d="M12 18c-2-2-3-5-3-8 1.5 1 2.5 2 3 3.5.5-1.5 1.5-2.5 3-3.5 0 3-1 6-3 8Z"/><path d="M12 13.5C11 11 11 7 12 4c1 3 1 7 0 9.5Z"/></svg>',
 "insta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4a21 21 0 0 0-2.3-.1c-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21h3Z"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600&family=Marcellus&family=Noto+Serif+Malayalam:wght@600;700&display=swap" rel="stylesheet">')

def head(title, desc, path="", extra=""):
    url = f"https://{C['domain']}/{path}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://{C['domain']}/assets/img/og-image.jpg">
<meta name="theme-color" content="#6E1414">
<!-- Meta (Facebook) domain verification: paste the meta tag Meta gives you on the next line -->

<link rel="icon" type="image/png" href="/assets/img/favicon.png"><link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="/assets/css/style.css">
{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(home=True):
    p = "" if home else "/"
    return f"""<header class="site-header">
  <nav class="container nav" aria-label="Main">
    <a class="brand" href="/">
      <img src="/assets/img/logo.png" alt="" width="48" height="48">
      <span><span class="brand-name">{C['name']}</span><span class="brand-sub">Mashinottam · Jyothisham</span></span>
    </a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu">{I['menu']}</button>
    <ul class="menu" id="menu">
      <li><a href="{p}#heritage">Heritage</a></li>
      <li><a href="{p}#acharya">Acharya</a></li>
      <li><a href="{p}#services">Services</a></li>
      <li><a href="{p}#poojas">Poojas</a></li>
      <li><a href="{p}#kshetram">Kshetram</a></li>
      <li><a href="{p}#visit">Visit</a></li>
      <li><a class="btn btn-maroon" href="{WA}" target="_blank" rel="noopener">{I['wa']} Book on WhatsApp</a></li>
    </ul>
  </nav>
</header>
"""

def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand"><img src="/assets/img/logo.png" alt=""><strong>{C['name']}</strong></div>
        <p class="ml" style="color:#E3BE72">6 തലമുറകളായി 300+ വർഷങ്ങളുടെ പാരമ്പര്യം</p>
        <p>{C['address']}</p>
        {social()}
      </div>
      <div>
        <h4>Visit &amp; contact</h4>
        <ul>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp: {WA_SHOW}</a></li>
          {"".join(f'<li><a href="{TEL(n)}">{n}</a></li>' for n in C["phones"])}
          <li><a href="mailto:{C['email']}">{C['email']}</a></li>
          <li>Office: {C['office']}</li>
          <li><a href="/contact.html">Contact us</a></li>
        </ul>
      </div>
      <div>
        <h4>Policies</h4>
        <ul>
          <li><a href="/privacy-policy.html">Privacy Policy</a></li>
          <li><a href="/terms.html">Terms &amp; Conditions</a></li>
          <li><a href="/refund-policy.html">Cancellation &amp; Refund Policy</a></li>
          <li><a href="/service-delivery-policy.html">Service Delivery Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {YEAR} {C['name']}. All rights reserved.</span>
      <span>Payments are processed securely by Razorpay.</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Book on WhatsApp">{I['wa']}</a>
<script src="/assets/js/config.js"></script>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""

def social(cls="social"):
    return (f'<div class="{cls}">'
            f'<a href="{C["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram">{I["insta"]}</a>'
            f'<a href="{C["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook">{I["fb"]}</a></div>')

def phone_items(style=""):
    return "".join(f'<li>{I["phone"]}<a{style} href="{TEL(n)}">{n}</a></li>' for n in C["phones"])

def divider():
    return f'<div class="divider">{I["lamp"]}</div>'

# ======================= HOME =======================
gens = [
    ("First generation", "Founding Acharya"),
    ("Second generation", "Acharya"),
    ("Third generation", "Acharya"),
    ("Fourth generation", "Acharya"),
    ("Fifth generation", "Acharya"),
    ("Sixth generation", "Present Acharya"),
]
lineage = "\n".join(
    f"""      <div class="gen{' current' if i == 6 else ''} reveal">
        <div class="arch"><img src="/assets/img/lineage/generation-{i}.jpg" alt="{t} Acharya of {C['name']}" loading="lazy"></div>
        <span class="num">{g}</span>
        <h4><!-- EDIT: Acharya's name -->{t}</h4>
      </div>""" for i, (g, t) in enumerate(gens, start=1))

gallery_items = [("g1", 1, "The Kshetram"), ("g2", 2, "Sreekovil"), ("g3", 3, "Evening deeparadhana"),
                 ("g4", 4, "Kalari"), ("g5", 5, "Amavasi Kalasha Pooja"), ("g6", 6, "Kshetram grounds")]
gallery = "\n".join(
    f'      <figure class="{c}" style="margin:0"><button type="button" data-full="/assets/img/kshetram/kshetram-{n}.jpg" aria-label="Open photo: {cap}"><img src="/assets/img/kshetram/kshetram-{n}.jpg" alt="{cap}, {C["name"]}" loading="lazy"><figcaption>{cap}</figcaption></button></figure>'
    for c, n, cap in gallery_items)

faqs = [
    ("What is Mashinottam?", "Mashinottam is a traditional Kerala practice of seeking guidance through observation of mashi (sacred ink). At Vylongara Kalari it has been practised by the same family for six generations."),
    ("Do I need to book before visiting?", "Yes. Please book on WhatsApp at least 2 days ahead. On your booked date you may come any time between 10 AM and 4 PM; devotees are seen in order of arrival."),
    ("How much does a consultation cost?", "There is no fixed fee for a direct consultation. A ₹101 booking token confirms your visit, and you may offer any dakshina you wish on the day. Online phone consultations are ₹1,001."),
    ("Can I consult from abroad or another city?", "Yes. Choose an online consultation on WhatsApp. The Acharya calls you on a normal phone call between 7 PM and 10 PM in the time slot you book."),
    ("Which details are needed for a booking?", "Name, age, house name, star (nakshatra) and place of the person for whom the consultation or pooja is booked."),
    ("Are payments refundable?", "Booking tokens, consultation fees and pooja payments are non-refundable. Please see our Cancellation & Refund Policy for the exceptions."),
]
faq = "\n".join(f"      <details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)

home = head(f"{C['name']} | Mashinottam & Jyothisham, Thrissur",
            "Vylongara Kalari near Chumanna Mannu, Thrissur: six generations and 300+ years of Mashinottam and Jyothisham tradition. Book consultations and poojas on WhatsApp.") + header() + f"""
<main id="main">
  <!-- HERO: replace /assets/img/kshetram/hero.jpg with a large photo of the Kshetram (2000×1200 or larger) -->
  <section class="hero" style="padding:0">
    <div class="hero-media"><img src="/assets/img/kshetram/hero.jpg" alt="{C['name']} Kshetram" fetchpriority="high"></div>
    <div class="hero-frame"></div>
    <div class="container hero-content">
      <span class="eyebrow">Near Chumanna Mannu · Thrissur · Kerala</span>
      <h1 class="hero-ml">6 തലമുറകളായി 300+ വർഷങ്ങളുടെ പാരമ്പര്യം.<br>മഷി നോട്ടത്തിലൂടെ പ്രശ്നങ്ങൾ പരിഹരിക്കുന്നു.</h1>
      <p class="hero-en">Six generations and more than three centuries of Mashinottam and Jyothisham, carried forward with devotion at Vylongara Kalari.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{I['wa']} Book a consultation</a>
        <a class="btn btn-ghost" href="#heritage">Our heritage</a>
      </div>
    </div>
  </section>

  <div class="stats">
    <div class="container">
      <div class="stat"><strong>6</strong><span>Generations of Acharyas</span></div>
      <div class="stat"><strong>300+</strong><span>Years of tradition</span></div>
      <div class="stat"><strong>Daily</strong><span>Consultations, no holidays</span></div>
      <div class="stat"><strong>Online</strong><span>Phone consultations, 7–10 PM</span></div>
    </div>
  </div>

  <!-- HERITAGE -->
  <section id="heritage" class="pattern">
    <div class="container">
      <div class="split">
        <div class="heritage-text reveal">
          <span class="eyebrow">Our heritage</span>
          <h2>A living tradition, passed from Acharya to Acharya</h2>
          <!-- EDIT: replace with the Kalari's own history when received -->
          <p>For more than three hundred years, the family at Vylongara Kalari has preserved the knowledge of Mashinottam and Jyothisham, handing it down through six generations of Acharyas.</p>
          <p>What began as a family practice beside the Kshetram near Chumanna Mannu has become a place where devotees from across Kerala and beyond come for guidance, prayer and peace of mind.</p>
          <p class="quote">“Every generation receives the tradition as it was given, and keeps it as it was kept.”</p>
        </div>
        <div class="wide-img reveal"><img src="/assets/img/kshetram/kshetram-2.jpg" alt="Inside the Kshetram at {C['name']}" loading="lazy"></div>
      </div>
      <div class="center" style="margin-top:80px">
        <span class="eyebrow">The lineage</span>
        <h2>Six generations of Acharyas</h2>
        {divider()}
      </div>
      <div class="lineage">
{lineage}
      </div>
    </div>
  </section>

  <!-- MAIN ACHARYA -->
  <section id="acharya" class="bg-maroon">
    <div class="container acharya">
      <div class="acharya-frame reveal">
        <!-- Replace /assets/img/acharya-main.jpg with a portrait of the present Acharya (1000×1300, portrait) -->
        <div class="arch"><img src="/assets/img/acharya-main.jpg" alt="The present Acharya of {C['name']}" loading="lazy"></div>
      </div>
      <div class="reveal">
        <span class="eyebrow" style="color:var(--gold-soft)">The present Acharya</span>
        <h2><!-- EDIT: name -->Acharya of Vylongara Kalari</h2>
        <p class="role">Sixth generation · Mashinottam &amp; Jyothisham</p>
        <!-- EDIT: replace with the Acharya's own introduction -->
        <p class="lead">The present Acharya carries forward the family's practice as the sixth generation, guiding devotees through Mashinottam and Jyothisham every day at the Kalari.</p>
        <p>Devotees are received with patience and care. Each consultation is unhurried: some take a few minutes, others much longer, as each person's situation requires.</p>
        <a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener" style="margin-top:12px">{I['wa']} Book a consultation</a>
      </div>
    </div>
  </section>

  <!-- SERVICES -->
  <section id="services">
    <div class="container">
      <div class="center">
        <span class="eyebrow">Consultations</span>
        <h2>How we can guide you</h2>
        {divider()}
        <p class="lead">Both consultations are with the same Acharya. Choose one when you book; anything further is discussed on the day.</p>
      </div>
      <div class="cards">
        <article class="card reveal">
          <div class="icon">{I['eye']}</div>
          <h3>Mashinottam</h3>
          <p>The traditional practice of seeking guidance through mashi, at the Kalari. Devotees are seen every day from 10 AM to 4 PM in order of arrival on their booked date.</p>
          <div class="meta"><span>Booking token, then dakshina as you wish</span><span class="price">₹101</span></div>
        </article>
        <article class="card reveal">
          <div class="icon">{I['star']}</div>
          <h3>Jyothisham</h3>
          <p>Traditional astrological consultation with the Acharya at the Kalari, 10 AM to 4 PM every day. Pay the token online or in cash at the office.</p>
          <div class="meta"><span>Booking token, then dakshina as you wish</span><span class="price">₹101</span></div>
        </article>
        <article class="card reveal">
          <div class="icon">{I['phone']}</div>
          <h3>Online consultation</h3>
          <p>For devotees who cannot travel: a normal phone call from the Acharya between 7 PM and 10 PM, in a 30-minute slot you choose. Limited to six each evening.</p>
          <div class="meta"><span>Paid online when booking</span><span class="price">₹1,001</span></div>
        </article>
      </div>
    </div>
  </section>

  <!-- POOJAS -->
  <section id="poojas" class="bg-sand">
    <div class="container">
      <div class="center">
        <span class="eyebrow">Poojas at the Kshetram</span>
        <h2>Poojas and offerings</h2>
        {divider()}
      </div>
      <div class="pooja-grid">
        <article class="pooja-feature reveal">
          <img src="/assets/img/kshetram/kshetram-5.jpg" alt="Amavasi Kalasha Pooja at {C['name']}" loading="lazy">
          <div class="inner">
            <span class="eyebrow" style="color:var(--gold-soft)">Every Amavasi</span>
            <h3>Amavasi Kalasha Pooja</h3>
            <p>11 AM – 1:30 PM. Devotees take part in the sitting pooja; for those unable to attend, a kalasham is done in their name at the end.</p>
            <span class="price">₹3,001</span>
          </div>
        </article>
        <div class="pooja-list reveal">
          <h3>Vishesha Kshetra Poojas</h3>
          <p style="color:var(--muted)">Performed on pooja days from 10 AM to 2 PM, usually as advised by the Acharya during consultation.</p>
          <ul>
            <li>{I['lotus']}<div><strong>Navakam</strong><span>Kshetra pooja</span></div></li>
            <li>{I['lotus']}<div><strong>Panchagavyam</strong><span>Kshetra pooja</span></div></li>
            <li>{I['lotus']}<div><strong>Ganapathy Homam</strong><span>Kshetra pooja</span></div></li>
          </ul>
          <div class="days"><span>Tuesday</span><span>Friday</span><span>Sunday</span><span>Amavasi</span></div>
          <p style="margin:18px 0 0;font-size:.92rem;color:var(--muted)">Rates and available dates are shared on WhatsApp.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- KSHETRAM GALLERY: replace kshetram-1.jpg … kshetram-6.jpg -->
  <section id="kshetram">
    <div class="container">
      <div class="center">
        <span class="eyebrow">The Kshetram</span>
        <h2>A place of prayer and stillness</h2>
        {divider()}
      </div>
      <div class="gallery">
{gallery}
      </div>
    </div>
  </section>

  <!-- HOW TO BOOK -->
  <section class="bg-maroon">
    <div class="container">
      <div class="center">
        <span class="eyebrow" style="color:var(--gold-soft)">Booking</span>
        <h2>Book in four simple steps on WhatsApp</h2>
        <p class="lead">Available day and night. No app or account needed.</p>
      </div>
      <div class="steps">
        <div class="step"><h3>Message us</h3><p>Send “Namaskaram” to our WhatsApp number.</p></div>
        <div class="step"><h3>Choose</h3><p>Pick a consultation or pooja, and give the person's name, age, house name, star and place.</p></div>
        <div class="step"><h3>Pick a date</h3><p>Choose from the dates that are open. Online consultations also choose a call time.</p></div>
        <div class="step"><h3>Confirm</h3><p>Pay securely by UPI or card (or cash at the office for direct visits) and receive your confirmation.</p></div>
      </div>
      <div class="center" style="margin-top:40px"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{I['wa']} Start booking</a></div>
    </div>
  </section>

  <!-- VISIT -->
  <section id="visit">
    <div class="container">
      <div class="center">
        <span class="eyebrow">Plan your visit</span>
        <h2>Timings and location</h2>
        {divider()}
      </div>
      <div class="visit">
        <div class="timings reveal">
          <h3>Timings</h3>
          <table>
            <tr><td>Temple nada (morning)</td><td>5:00 – 9:30 AM</td></tr>
            <tr><td>Temple nada (evening)</td><td>5:30 – 8:00 PM</td></tr>
            <tr><td>Consultations at the Kalari</td><td>10 AM – 4 PM, every day</td></tr>
            <tr><td>Online consultations</td><td>7 – 10 PM</td></tr>
            <tr><td>Poojas</td><td>Tue, Fri, Sun · 10 AM – 2 PM</td></tr>
            <tr><td>Amavasi Kalasha Pooja</td><td>11 AM – 1:30 PM</td></tr>
          </table>
          <ul class="contact-list" style="color:var(--ink)">
            <li>{I['pin']}<span>{C['address']}</span></li>
            {phone_items()}
          </ul>
        </div>
        <div class="map reveal">
          <iframe title="Map to {C['name']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
            src="https://www.google.com/maps?q={C['map_q'].replace(' ', '+')}&amp;output=embed"></iframe>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="bg-sand">
    <div class="container">
      <div class="center">
        <span class="eyebrow">Questions</span>
        <h2>Frequently asked</h2>
      </div>
      <div class="faq">
{faq}
      </div>
    </div>
  </section>

  <!-- CONTACT + ENQUIRY -->
  <section id="contact" class="bg-maroon">
    <div class="container contact">
      <div>
        <span class="eyebrow" style="color:var(--gold-soft)">Contact</span>
        <h2>We are here to help</h2>
        <p class="lead">For bookings, WhatsApp is the quickest. For anything else, send us a message and our office will reply.</p>
        <ul class="contact-list">
          <li>{I['wa']}<a style="color:#fff" href="{WA}" target="_blank" rel="noopener">WhatsApp: {WA_SHOW}</a></li>
          {phone_items(' style="color:#fff"')}
          <li>{I['mail']}<a style="color:#fff" href="mailto:{C['email']}">{C['email']}</a></li>
          <li>{I['clock']}<span>Office: {C['office']}</span></li>
        </ul>
        {social("social social-lg")}
      </div>
      <form class="form" id="enquiry" novalidate style="position:relative">
        <h3>Send an enquiry</h3>
        <div class="row">
          <div><label for="f-name">Name</label><input id="f-name" name="name" required autocomplete="name"></div>
          <div><label for="f-phone">Phone / WhatsApp</label><input id="f-phone" name="phone" required inputmode="tel" autocomplete="tel"></div>
        </div>
        <label for="f-topic">About</label>
        <select id="f-topic" name="topic">
          <option>Consultation</option><option>Online consultation</option><option>Amavasi Kalasha Pooja</option><option>Vishesha poojas</option><option>Other</option>
        </select>
        <label for="f-msg">Message</label>
        <textarea id="f-msg" name="message" rows="4" required></textarea>
        <input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px">
        <button class="btn btn-maroon" type="submit">Send enquiry</button>
        <small>By sending, you agree to our <a href="/privacy-policy.html">Privacy Policy</a>.</small>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </section>
</main>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo"><button type="button" aria-label="Close">×</button><img alt=""></div>
""" + footer()

# ======================= LEGAL PAGES =======================
def legal_page(fname, title, subtitle, body, desc):
    html = head(f"{title} | {C['name']}", desc, fname) + header(home=False) + f"""
<main id="main">
  <div class="page-hero"><div class="container"><h1>{title}</h1><p>{subtitle}</p></div></div>
  <article class="container legal">
{body}
  </article>
</main>
""" + footer()
    open(os.path.join(OUT, fname), "w").write(html)

who = f"""<div class="box"><strong>{C['name']}</strong><br>{C['address']}<br>Phone: {" / ".join(C['phones'])} · WhatsApp: {WA_SHOW}<br>Email: <a href="mailto:{C['email']}">{C['email']}</a></div>"""

privacy = f"""    <p><em>Last updated: {C['updated']}</em></p>
    <p>This Privacy Policy explains how {C['name']} (“we”, “us”) collects, uses and protects personal information when you visit this website, contact us, or book a consultation or pooja through WhatsApp.</p>
    {who}
    <h2>1. Information we collect</h2>
    <ul>
      <li><strong>Booking details</strong> you give us: name, age, house name, star (nakshatra), place, and the date and service you choose.</li>
      <li><strong>Contact details</strong>: your WhatsApp number and WhatsApp profile name, and your phone number or email if you send an enquiry.</li>
      <li><strong>Messages</strong> you send to our WhatsApp number, including questions to our automated assistant.</li>
      <li><strong>Payment information</strong>: payments are processed by Razorpay. We receive the payment status, amount and a payment reference. We never see or store your card, UPI PIN or bank login details.</li>
      <li><strong>Advertising source</strong>: if you reach us from a Facebook or Instagram advertisement, Meta may share which advertisement you clicked.</li>
    </ul>
    <h2>2. How we use it</h2>
    <ul>
      <li>To book, confirm and manage your consultation or pooja, and to send confirmations and reminders on WhatsApp.</li>
      <li>To prepare for your consultation or pooja (for example, the sankalpam requires name and star).</li>
      <li>To answer your questions and enquiries.</li>
      <li>To keep accounting and payment records as required by law.</li>
    </ul>
    <p>We do <strong>not</strong> sell, rent or trade your personal information, and we do not send promotional messages without your consent.</p>
    <h2>3. Automated assistant</h2>
    <p>Our WhatsApp number uses an automated assistant to handle bookings and answer common questions. When you type a question, its text may be processed by an artificial-intelligence service (OpenAI) only to produce a reply. The assistant does not give readings or predictions; those are given only by the Acharya. You can ask to speak to a person at any time.</p>
    <h2>4. Service providers we use</h2>
    <table>
      <tr><th>Provider</th><th>Purpose</th></tr>
      <tr><td>Meta Platforms (WhatsApp Business Platform)</td><td>Sending and receiving WhatsApp messages</td></tr>
      <tr><td>Razorpay Software Pvt. Ltd.</td><td>Processing online payments</td></tr>
      <tr><td>Google (Workspace / Sheets)</td><td>Storing booking records</td></tr>
      <tr><td>OpenAI</td><td>Generating replies to typed questions</td></tr>
      <tr><td>Supabase</td><td>Storing website enquiry form submissions</td></tr>
      <tr><td>Hosting provider</td><td>Running our booking automation and this website</td></tr>
    </table>
    <p>These providers process information only to provide their service to us and under their own privacy and security terms.</p>
    <h2>5. How long we keep it</h2>
    <p>Booking and payment records are kept for as long as needed for our services and for accounting and legal requirements (generally up to 8 years for payment records). Chat messages and enquiries are kept for up to 24 months and then deleted, unless needed to resolve a dispute.</p>
    <h2>6. Your choices and rights</h2>
    <ul>
      <li>Send <strong>STOP</strong> on WhatsApp at any time to stop all messages; send <strong>START</strong> to resume.</li>
      <li>You may ask us to access, correct or delete your personal information, or withdraw consent, by writing to <a href="mailto:{C['email']}">{C['email']}</a>. We will respond within 30 days. Some payment records must be kept by law.</li>
      <li>These rights are provided in line with India's Digital Personal Data Protection Act, 2023.</li>
    </ul>
    <h2>7. Security</h2>
    <p>We use secure (HTTPS) connections and access-controlled accounts, and limit access to booking information to our office staff and the Acharya.</p>
    <h2>8. Children</h2>
    <p>Bookings for minors must be made by a parent or guardian, who provides the minor's details on their behalf.</p>
    <h2>9. Website</h2>
    <p>This website does not use advertising or tracking cookies. Embedded Google Maps and Google Fonts may set their own cookies under Google's policies.</p>
    <h2>10. Changes and contact</h2>
    <p>We may update this policy; the date above shows the latest version. Questions or complaints (grievance contact): <a href="mailto:{C['email']}">{C['email']}</a>, {" / ".join(C['phones'])}.</p>"""

terms = f"""    <p><em>Last updated: {C['updated']}</em></p>
    <p>These Terms apply to bookings and services of {C['name']}, whether made on WhatsApp, by phone, through this website or in person. By booking, you agree to them.</p>
    {who}
    <h2>1. Our services</h2>
    <p>{C['name']} offers traditional Mashinottam and Jyothisham consultations (in person and by phone) and poojas at the Kshetram, including Amavasi Kalasha Pooja and Vishesha Kshetra Poojas.</p>
    <div class="box"><strong>Please note:</strong> our services are traditional spiritual and religious guidance. They are not a substitute for medical, psychological, legal or financial advice, and no specific outcome or result is promised or guaranteed. Please consult a qualified professional for such matters. In an emergency, call 112.</div>
    <h2>2. Bookings</h2>
    <ul>
      <li>Direct consultations are booked for a <strong>date</strong>; on that date devotees are seen between 10 AM and 4 PM in order of arrival. Bookings must be made at least 2 days ahead.</li>
      <li>Online consultations are booked for a date and a 30-minute window between 7 PM and 10 PM. The Acharya calls the number given at booking.</li>
      <li>Poojas are booked for the date shown at booking. Amavasi Kalasha Pooja bookings close one day before the Amavasi.</li>
      <li>A booking is confirmed only when you receive a confirmation message from us with a booking ID.</li>
      <li>Please give correct details (name, age, house name, star, place). You may book for a family member with their consent.</li>
    </ul>
    <h2>3. Fees and payment</h2>
    <table>
      <tr><th>Service</th><th>Amount</th><th>When</th></tr>
      <tr><td>Direct consultation – booking token</td><td>₹101</td><td>Online when booking, or in cash at the office on the day</td></tr>
      <tr><td>Dakshina for direct consultation</td><td>As you wish</td><td>Offered in person on the day</td></tr>
      <tr><td>Online consultation</td><td>₹1,001</td><td>Online when booking</td></tr>
      <tr><td>Amavasi Kalasha Pooja</td><td>₹3,001</td><td>Online when booking</td></tr>
      <tr><td>Vishesha Kshetra Poojas</td><td>As advised / shown at booking</td><td>Online when booking</td></tr>
    </table>
    <p>Online payments are processed by Razorpay. Prices are in Indian Rupees and may change; the price shown when you book applies to that booking.</p>
    <h2>4. Cancellations and refunds</h2>
    <p>See our <a href="/refund-policy.html">Cancellation &amp; Refund Policy</a>.</p>
    <h2>5. Conduct at the Kalari and Kshetram</h2>
    <p>Devotees are asked to follow the customs of the Kshetram and the instructions of the staff. We may decline or reschedule a consultation if these are not followed.</p>
    <h2>6. Communication</h2>
    <p>By booking, you agree to receive booking confirmations and reminders on WhatsApp. You can stop messages at any time by sending STOP.</p>
    <h2>7. Liability</h2>
    <p>To the extent permitted by law, our liability for any booking is limited to the amount you paid for it. We are not responsible for delays or failures caused by events outside our control, including network, payment-gateway or WhatsApp outages.</p>
    <h2>8. Governing law</h2>
    <p>These Terms are governed by the laws of India. Courts at Thrissur, Kerala have jurisdiction.</p>
    <h2>9. Contact</h2>
    <p><a href="mailto:{C['email']}">{C['email']}</a> · {" / ".join(C['phones'])}</p>"""

refund = f"""    <p><em>Last updated: {C['updated']}</em></p>
    {who}
    <h2>1. Summary</h2>
    <table>
      <tr><th>Payment</th><th>Refundable?</th></tr>
      <tr><td>₹101 booking token (direct consultation)</td><td>No – it reserves your visit</td></tr>
      <tr><td>₹1,001 online consultation</td><td>No – but rescheduled once if the call could not take place</td></tr>
      <tr><td>Amavasi Kalasha Pooja (₹3,001)</td><td>No – if you cannot attend, a kalasham is done in your name</td></tr>
      <tr><td>Vishesha Kshetra Poojas</td><td>No</td></tr>
      <tr><td>Dakshina</td><td>Not applicable – offered voluntarily in person</td></tr>
    </table>
    <h2>2. Changing your date</h2>
    <ul>
      <li><strong>Direct consultation:</strong> you may change the date once, up to 1 day before, by messaging us on WhatsApp.</li>
      <li><strong>Online consultation:</strong> you may move to another available slot once, up to 1 day before. If the Acharya calls during your slot and cannot reach you after two attempts, our office will offer one new slot.</li>
      <li><strong>Poojas:</strong> date changes are at the discretion of the Kalari and must be requested at least 2 days before.</li>
    </ul>
    <h2>3. When we refund in full</h2>
    <ul>
      <li>If <strong>we</strong> cancel a consultation or pooja and you do not accept a new date.</li>
      <li>If you were <strong>charged twice</strong> for the same booking, or charged but no booking was created.</li>
      <li>If you paid after your booking link had expired and no slot was available.</li>
    </ul>
    <h2>4. How refunds are made</h2>
    <p>Approved refunds are initiated within <strong>3 working days</strong> to the original payment method through Razorpay. Banks and UPI apps usually credit the amount within <strong>5–7 working days</strong> after that. Cash payments are refunded in cash at the office or by bank transfer.</p>
    <h2>5. How to ask</h2>
    <p>Message us on WhatsApp or write to <a href="mailto:{C['email']}">{C['email']}</a> with your booking ID and payment reference.</p>"""

delivery = f"""    <p><em>Last updated: {C['updated']}</em></p>
    {who}
    <h2>No physical goods</h2>
    <p>{C['name']} provides services only. We do not sell or ship physical products, and prasadam is not sent by post.</p>
    <h2>How services are delivered</h2>
    <ul>
      <li><strong>Booking confirmation</strong> is sent on WhatsApp immediately after successful payment (or immediately, for cash-at-office bookings).</li>
      <li><strong>Direct consultations</strong> take place at the Kalari on the booked date, between 10 AM and 4 PM, in order of arrival.</li>
      <li><strong>Online consultations</strong> are delivered as a phone call from the Acharya to the number given at booking, during the booked 30-minute window between 7 PM and 10 PM.</li>
      <li><strong>Poojas</strong> are performed at the Kshetram on the booked date (Vishesha poojas 10 AM – 2 PM; Amavasi Kalasha Pooja 11 AM – 1:30 PM).</li>
    </ul>
    <h2>Questions</h2>
    <p>WhatsApp us or write to <a href="mailto:{C['email']}">{C['email']}</a>.</p>"""

contact = f"""    {who}
    <h2>Book or ask a question</h2>
    <p>The quickest way is WhatsApp. Our booking assistant is available day and night; our office replies between {C['office']}.</p>
    <p><a class="btn btn-maroon" href="{WA}" target="_blank" rel="noopener">{I['wa']} Message us on WhatsApp</a></p>
    <h2>Visit</h2>
    <p>{C['address']}</p>
    <p>Consultations: every day, 10 AM – 4 PM (please book at least 2 days ahead).<br>Temple nada: 5:00 – 9:30 AM and 5:30 – 8:00 PM.</p>
    <h2>Phone and email</h2>
    <p>{"<br>".join(f'Phone: <a href="{TEL(n)}">{n}</a>' for n in C["phones"])}<br>WhatsApp: <a href="{WA}" target="_blank" rel="noopener">{WA_SHOW}</a><br>Email: <a href="mailto:{C['email']}">{C['email']}</a></p>
    <p>Office: {C['office']}</p>
    <h2>Follow us</h2>
    {social("social social-dark")}
    <p><a href="/#contact">Send an enquiry from our home page</a></p>"""

notfound = head(f"Page not found | {C['name']}", "Page not found") + header(home=False) + f"""
<main id="main"><div class="page-hero" style="padding:120px 0"><div class="container"><h1>Page not found</h1><p>The page you were looking for is not here.</p>
<p style="margin-top:24px"><a class="btn btn-gold" href="/">Go to home page</a></p></div></div></main>
""" + footer()

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "index.html"), "w").write(home)
open(os.path.join(OUT, "404.html"), "w").write(notfound)
legal_page("privacy-policy.html", "Privacy Policy", "How we collect, use and protect your information", privacy, f"Privacy Policy of {C['name']}.")
legal_page("terms.html", "Terms &amp; Conditions", "Terms for consultations, poojas and payments", terms, f"Terms and Conditions of {C['name']}.")
legal_page("refund-policy.html", "Cancellation &amp; Refund Policy", "Changes, cancellations and refunds", refund, f"Cancellation and Refund Policy of {C['name']}.")
legal_page("service-delivery-policy.html", "Service Delivery Policy", "How and when our services are delivered", delivery, f"Service Delivery Policy of {C['name']}.")
legal_page("contact.html", "Contact Us", "We are here to help", contact, f"Contact {C['name']}, near Chumanna Mannu, Thrissur.")

# robots + sitemap + CNAME
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: https://{C['domain']}/sitemap.xml\n")
pages = ["", "contact.html", "privacy-policy.html", "terms.html", "refund-policy.html", "service-delivery-policy.html"]
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>https://{C['domain']}/{p}</loc></url>\n" for p in pages) + "</urlset>\n")
open(os.path.join(OUT, "CNAME"), "w").write(C["domain"] + "\n")
print("built", sorted(f for f in os.listdir(OUT) if f.endswith(('.html', '.txt', '.xml')) or f == 'CNAME'))
