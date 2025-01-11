# S31_Whois.py
import whois

def whois_lookup(ip_address):
   #Perform a WHOIS lookup for the given IP address
    try:
        w = whois.whois(ip_address)  #LookUp process
        return w
    except Exception as e:
        return "WHOIS Lookup Failed: {}".format(e)

#End of code