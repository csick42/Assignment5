# AI Dev Notes

This file documents how I used AI (Cursor/Copilot-style assistance) while building my personal website. Each entry includes: 1) my prompt, 2) a concise summary of the AI output, and 3) whether I accepted, modified, or rejected the output.

## Prompts Log

### Prompt 1 — Base styles and layout
- Prompt: "Create a responsive styles.css with a dark gradient background, sticky header, grid utilities, cards, buttons, badges, tables, and accessible focus styles."
- AI Output: Variables for colors, container and grid utilities, sticky header/nav, hero section, cards, badges, table styling, form controls with focus rings, responsive breakpoints.
- Decision: Modified. I kept the system, tuned spacing/colors to match the brand feel.

### Prompt 2 — Homepage scaffold
- Prompt: "Generate index.html with semantic layout, hero copy, quick links, and shared navigation across pages."
- AI Output: Header/nav, hero with intro, quick links section, footer with dynamic year.
- Decision: Modified. I adjusted the intro text to reflect MSIS at Kelley and swapped the hero image path.

### Prompt 3 — About page with biography and image
- Prompt: "Build about.html using a detailed bio and an accessible image with alt and figcaption."
- AI Output: Semantic article, image tag with alt and caption, multi‑paragraph biography structure.
- Decision: Accepted with edits to biography wording to better reflect my voice.

### Prompt 4 — Resume page with HTML sections + PDF link
- Prompt: "Build a resume page with Education, Experience, Projects, Skills, and a button to open a PDF resume."
- AI Output: Structured sections with lists and a PDF call‑to‑action button.
- Decision: Modified. Rewrote all bullets to match my real resume and linked to `resources/Christian_Sickmeier_Resume.pdf`.

### Prompt 5 — Projects page: FinTime (I‑Core) + Social Media study
- Prompt: "Create projects.html featuring two projects with descriptions, images, and resource links. Include a citation link to the Kelley blog exactly as given."
- AI Output: Two project cards; FinTime section with placeholders; Social Media section with visuals grid; citation block with link.
- Decision: Modified. Rewired links to my exact filenames (`.xlsx`, `.docx`, `.pptx`, and website `.html` files in `resources/Website/Draft 2` and `Draft 3`), kept the blog link text verbatim.

### Prompt 6 — Fix broken images and use existing filenames
- Prompt: "Point images and download links to whatever exists in the resources directory without renaming."
- AI Output: Updated sources to existing paths and added generic fallbacks.
- Decision: Modified. I set explicit paths that match my repo (e.g., `images/cohort-photo.JPEG`, `images/team-photo.jpg`); I removed unused fallbacks.

### Prompt 7 — Contact form per assignment Step 4
- Prompt: "Enforce required fields, email type, minlength=8, confirm password match, patterns for first/last names, clear error messages, and redirect to thankyou.html."
- AI Output: Five inputs with labels/ids, type=email, name patterns, minlength, minimal JS that populates inline error messages and prevents submit on failure.
- Decision: Accepted with minor copy changes on error text.

### Prompt 8 — Accessibility and consistency pass
- Prompt: "Check semantics, headings, aria, alt text, and consistent navigation across pages; ensure responsiveness with the existing CSS utilities."
- AI Output: Recommendations to keep header/nav/main/footer, maintain alt text, and preserve focus states.
- Decision: Accepted. Verified labels and alt attributes; ensured year script is present in footers.

### Prompt 9 — AI log and reflection
- Prompt: "Draft a multi‑prompt dev_notes.md with prompts, output summaries, accept/modify/reject decisions, and a ~150‑word reflection."
- AI Output: Skeleton with sections and sample phrasing.
- Decision: Modified. Expanded to include 7+ prompts and tailored the reflection to my experience.

## Reflection (~180 words)
AI accelerated the scaffolding stages that usually slow me down: establishing a consistent design system, wiring semantic layouts, and generating repeatable elements like navigation and cards. It also saved time on the contact form by producing a solid baseline for validation (required, patterns, minlength) and a minimal script for clear error messages and redirect. Where AI made mistakes was mostly around assumptions—suggesting file names or paths that didn’t exist, over‑generalizing content, and occasionally omitting accessibility details. I corrected this by linking to the exact resources in my repository (including non‑PDF formats like .xlsx, .docx, .pptx, and .html), validating alt/label pairs, and tuning copy to reflect my authentic experience.

My balance strategy was: let AI handle boilerplate and structure, then I assumed ownership for accuracy, voice, accessibility, and repository realities. I continuously tested links and images, verified the form behavior, and ensured the Kelley blog citation remained exactly as required. The result is a site that feels like me—technically correct, accessible, and well organized—while demonstrating responsible AI use and critical oversight.
