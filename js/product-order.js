/**
 * ImpactMojo — email-first product order gate  (v1.0)
 *
 * Runs on every product page that carries the `product-order` Netlify form.
 * Enforces: the buyer CANNOT see the UPI QR / payment details until they have
 * given us a valid email. The moment they proceed to pay we capture that email
 * as a lead (a `product-order` submission with an empty upi_ref), so even a
 * pay-and-ghost buyer leaves us a way to reach them.
 *
 * Flow:
 *   1. Page loads → payment card (QR + UPI id + WhatsApp) and the UPI-reference
 *      field + submit button are hidden. Only Name + Email + a "Show payment
 *      details →" button are shown.
 *   2. Valid email entered → click "Show payment details" → we POST a lead
 *      (name/email/product, no upi_ref) and reveal the payment card + the
 *      reference field + the submit button.
 *   3. Buyer pays, enters the UPI reference, submits → the existing per-page
 *      submitOrder() fires the normal "I've paid" submission (with upi_ref),
 *      which is what triggers the Confirm-&-deliver pipeline.
 *
 * Pure progressive enhancement: if the expected structure isn't found, the page
 * is left exactly as it was. Depends on nothing.
 */
(function () {
  "use strict";
  function init() {
    var form = document.querySelector('form[name="product-order"]');
    if (!form || form.dataset.emailGated) return;

    var pay = form.closest(".pay") || document.querySelector(".pay");
    var nameI = form.querySelector('[name="name"]');
    var emailI = form.querySelector('[name="email"]');
    var refI = form.querySelector('[name="upi_ref"]');
    var submitBtn = form.querySelector('[type="submit"], button:not([type])');
    if (!pay || !emailI || !refI || !submitBtn) return; // unexpected shape → leave as-is

    // The payment card is the .card inside .pay that does NOT contain the form
    // (it holds the QR, UPI id and the "Order on WhatsApp" button).
    var payCard = null;
    var cards = pay.querySelectorAll(".card");
    for (var i = 0; i < cards.length; i++) {
      if (!cards[i].contains(form)) { payCard = cards[i]; break; }
    }
    if (!payCard) return;

    form.dataset.emailGated = "1";

    var refField = refI.closest(".field") || refI;
    var emailField = emailI.closest(".field") || emailI;

    // Hide payment + the reference field + submit until an email is given.
    payCard.style.display = "none";
    refField.style.display = "none";
    submitBtn.style.display = "none";

    var hint = document.createElement("p");
    hint.className = "note";
    hint.style.margin = ".2rem 0 .6rem";
    hint.textContent = "Enter your email first — that’s where we send your file after payment.";

    var gate = document.createElement("button");
    gate.type = "button";
    gate.className = submitBtn.className || "btn buy";
    gate.style.width = "100%";
    gate.style.justifyContent = "center";
    gate.textContent = "Show payment details →";

    emailField.insertAdjacentElement("afterend", gate);
    emailField.insertAdjacentElement("afterend", hint);

    function validEmail(v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); }

    var captured = false;
    function captureLead() {
      if (captured) return;
      captured = true;
      try {
        var product = (form.querySelector('[name="product"]') || {}).value || "";
        var body = new URLSearchParams({
          "form-name": "product-order",
          name: (nameI && nameI.value || "").trim(),
          email: (emailI.value || "").trim(),
          product: product,
          upi_ref: "" // empty ⇒ pre-payment lead; submission-created skips the confirm email
        }).toString();
        fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: body })
          .catch(function () {});
      } catch (e) { /* non-blocking */ }
    }

    var revealed = false;
    function reveal() {
      if (revealed) return;
      revealed = true;
      payCard.style.display = "";
      refField.style.display = "";
      submitBtn.style.display = "";
      gate.style.display = "none";
      hint.style.display = "none";
      if (payCard.scrollIntoView) payCard.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }

    gate.addEventListener("click", function () {
      var em = (emailI.value || "").trim();
      if (!validEmail(em)) {
        emailI.focus();
        if (emailI.reportValidity) emailI.reportValidity();
        hint.style.color = "#B45309";
        hint.textContent = "Please enter a valid email so we can send your file.";
        return;
      }
      captureLead();
      reveal();
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
