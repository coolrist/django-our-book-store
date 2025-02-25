# Create your classes here.

# Create your methods here.
def metadata(title, **kwargs):
    """
    This function return the metadata (title...) of a page to the view.
    """
    meta = {"title": title}
    meta.update(kwargs)
    return meta
