# These are some research notes for information collection

## Start-from-Scratch Approach

- We make our own DB like camelcamelcamel and take pricing data from Amazon, Newegg, etc API

## Douche Approach

- We take our pricing data from existing DB such as camelcamelcamel

### Amazon:

- Camelcamelcamel if we feel like flooding their already overworked servers.

### Ebay:

- The website can display 'sold' items for up to 60 or 90 days depending on what the item is
- Can purchase Terapeak for additional pricing history
- Maybe we can collect pricing data straight fromt the website make our own database for eBay pricing history?

### Grailed:

- Grailed uses React so scrolling is only activated locally. Scrapers already exist for Grailed.
- Grailed offers a ["sold section"](https://www.grailed.com/feed/-pjlWV8wqQ)

### Forums:

- Forums will be more tricky to scrape but it's still somewhat doable.
- Bad thing is a lot of forums delete sold listings.
