document.addEventListener("DOMContentLoaded", () => {
	document.querySelectorAll(".headroom").forEach((element) => {
		new Headroom(element, {
			tolerance: 20,
			offset: 50,
			classes: {
				initial: "animated",
				pinned: "slideDown",
				unpinned: "slideUp"
			}
		}).init();
	});
});
