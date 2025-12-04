Merged. Summary of fixes:
- Restored sqlite fallback and moved model definitions above routes.
- Fixed instantiation (use Recipe instead of undefined lowercase), corrected __repr__ placement, standardized redirects to url_for(), and normalized indentation.
- Added minimal templates and Procfile for quick Render demo.
Recommend: attach Render managed Postgres and set SQLALCHEMY_DATABASE_URI env var; add Flask-Migrate for schema changes in future.