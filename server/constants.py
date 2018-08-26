import os

TEST_CONSTANT = 'hello world'
SERVER_DEFAULTS = {
    "HOST": os.getenv("HOST", "127.0.0.1"),
    "PORT": int(os.getenv("PORT", 5000)),
}


# valid types of information for items
VALID_CONDITIONS = ['new', 'like new', 'used']
VALID_WEBSITES = ['eBay', 'Amazon', 'B&H Photo and Video']