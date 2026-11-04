'use strict';
(() => {
  const navigation = document.querySelector('.section-nav');
  const wide = window.matchMedia('(min-width:1000px)');
  const setNavigation = () => { if (navigation) navigation.open = wide.matches; };
  setNavigation();
  wide.addEventListener('change', setNavigation);
  const revealTarget = () => {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    if (!id) return;
    const target = document.getElementById(id);
    if (!target) return;
    let parent = target;
    while (parent) { if (parent.tagName === 'DETAILS') parent.open = true; parent = parent.parentElement; }
    if (target.matches('[tabindex]')) target.focus({preventScroll:true});
    target.scrollIntoView({block:'start'});
  };
  window.addEventListener('hashchange', revealTarget);
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (link && link.hash === location.hash) revealTarget();
  });
  revealTarget();
})();
