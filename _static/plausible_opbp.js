var script = document.createElement("script");
script.defer = true;
script.src = "https://plausible.io/js/script.js";
script.dataset.domain = "opbphysics";

// optional if using proxy
// script.dataset.api = 'https://yourproxy.com/api/event';

document.getElementsByTagName("head")[0].appendChild(script);