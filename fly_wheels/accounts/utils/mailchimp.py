import os, hashlib
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

API_KEY  = os.environ.get("MAILCHIMP_API_KEY")
SERVER   = os.environ.get("MAILCHIMP_SERVER_PREFIX")
LIST_ID  = os.environ.get("MAILCHIMP_AUDIENCE_ID")

_client = None
def client():
    global _client
    if _client is None:
        c = MailchimpMarketing.Client()
        c.set_config({"api_key": API_KEY, "server": SERVER})
        _client = c
    return _client

def subscribe(email: str, first_name: str = "", last_name: str = "",
              tags=None, double_opt_in: bool = True) -> bool:
    """Upsert a subscriber by email; returns True on success."""
    if not (API_KEY and SERVER and LIST_ID):
        return False
    email = (email or "").strip().lower()
    if not email:
        return False

    subscriber_hash = hashlib.md5(email.encode()).hexdigest()
    body = {
        "email_address": email,
        "status_if_new": "pending" if double_opt_in else "subscribed",
        "status": "subscribed",
        "merge_fields": {"FNAME": first_name or "", "LNAME": last_name or ""},
    }
    if tags:
        body["tags"] = list(tags)

    try:
        client().lists.set_list_member(LIST_ID, subscriber_hash, body)
        return True
    except ApiClientError as e:
        return False
