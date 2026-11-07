// Vailongara Kalari website: menu, scroll reveal, photo lightbox, enquiry form.
(function () {
  const cfg = window.VK_CONFIG || {};

  // Mobile menu
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.getElementById('menu');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }));
  }

  // Reveal sections as they scroll into view
  const items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { threshold: 0.12 });
    items.forEach(el => io.observe(el));
  } else {
    items.forEach(el => el.classList.add('in'));
  }

  // Gallery lightbox
  const lb = document.getElementById('lightbox');
  if (lb) {
    const img = lb.querySelector('img');
    const close = () => { lb.classList.remove('open'); img.src = ''; };
    document.querySelectorAll('.gallery button').forEach(b => b.addEventListener('click', () => {
      img.src = b.dataset.full; img.alt = b.querySelector('img').alt; lb.classList.add('open');
    }));
    lb.addEventListener('click', e => { if (e.target !== img) close(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  // Enquiry form -> Supabase (or WhatsApp if Supabase is not configured)
  const form = document.getElementById('enquiry');
  if (form) {
    const status = form.querySelector('.form-status');
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const data = Object.fromEntries(new FormData(form).entries());
      if (data.website) return;                          // spam trap
      if (!data.name || !data.phone || !data.message) {
        status.className = 'form-status err'; status.textContent = 'Please fill in your name, phone and message.'; return;
      }
      const row = { name: data.name.trim(), phone: data.phone.trim(), topic: data.topic, message: data.message.trim() };
      if (!cfg.SUPABASE_URL || !cfg.SUPABASE_ANON_KEY) {
        const text = `Namaskaram. ${row.topic} enquiry from ${row.name} (${row.phone}): ${row.message}`;
        window.open(`https://wa.me/${cfg.WHATSAPP_NUMBER}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
        return;
      }
      const btn = form.querySelector('button[type=submit]');
      btn.disabled = true; status.className = 'form-status'; status.textContent = 'Sending…';
      try {
        const res = await fetch(`${cfg.SUPABASE_URL}/rest/v1/enquiries`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', apikey: cfg.SUPABASE_ANON_KEY,
            Authorization: `Bearer ${cfg.SUPABASE_ANON_KEY}`, Prefer: 'return=minimal' },
          body: JSON.stringify(row),
        });
        if (!res.ok) throw new Error(res.status);
        form.reset();
        status.className = 'form-status ok'; status.textContent = 'Thank you. Our office will contact you soon. 🙏';
      } catch (err) {
        status.className = 'form-status err'; status.textContent = 'Sorry, that did not send. Please message us on WhatsApp.';
      } finally { btn.disabled = false; }
    });
  }
})();
