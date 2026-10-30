import dns.resolver
import dns.exception

resolver = dns.resolver.Resolver()
resolver.lifetime = 3   # give up after 3 seconds

def lookup(domain, record_type="A"):
    try:
        answers = resolver.resolve(domain, record_type)
        return [r.to_text() for r in answers]
    except dns.exception.DNSException:
        return []       # doesn't exist, no record, or timed out