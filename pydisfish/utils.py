

def get_domain(url: str) -> str:
    """Return the domain from the url"""
    return url.split('?')[0].split('#')[0].replace('http://', '').replace('https://', '').split('/')[0]