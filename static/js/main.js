// Minimal helper: reveal-on-scroll + smooth nav + hero text typing
(function(){
  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({behavior: 'smooth', block: 'start'});
      }
    });
  });

  // Sticky header shadow
  const header = document.querySelector('.site-header');
  const onScroll = () => {
    if (!header) return;
    if (window.scrollY > 10) header.classList.add('with-shadow');
    else header.classList.remove('with-shadow');
  };
  window.addEventListener('scroll', onScroll);
  onScroll();

  // Reveal on scroll
  const revealEls = document.querySelectorAll('[data-reveal]');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  revealEls.forEach(el => io.observe(el));

  // Simple slider (hero)
  const slides = document.querySelectorAll('.hero-slide');
  let idx = 0;
  function showSlide(i){
    slides.forEach((s, k) => s.classList.toggle('active', k === i));
  }
  if (slides.length) {
    showSlide(0);
    setInterval(() => {
      idx = (idx + 1) % slides.length;
      showSlide(idx);
    }, 4000);
  }

  // Typing effect for headline
  const typer = document.querySelector('[data-typer]');
  if (typer) {
    const text = typer.getAttribute('data-typer') || "";
    let i = 0;
    function typeNext() {
      typer.textContent = text.slice(0, i++);
      if (i <= text.length) requestAnimationFrame(typeNext);
    }
    typeNext();
  }
})();
