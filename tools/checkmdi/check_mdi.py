#!/usr/bin/env python3

import dns.resolver
import xml.etree.ElementTree as ET
from urllib.request import urlopen, Request
import pandas as pd
from utils.excel_writer import write_to_excel
from utils.color_logger import log_info, log_success, log_error, log_warning

# Get domains
def get_domains(domain):
    body = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:exm="http://schemas.microsoft.com/exchange/services/2006/messages"
        xmlns:ext="http://schemas.microsoft.com/exchange/services/2006/types"
        xmlns:a="http://www.w3.org/2005/08/addressing"
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Header>
        <a:RequestedServerVersion>Exchange2010</a:RequestedServerVersion>
        <a:MessageID>urn:uuid:6389558d-9e05-465e-ade9-aae14c4bcd10</a:MessageID>
        <a:Action soap:mustUnderstand="1">http://schemas.microsoft.com/exchange/2010/Autodiscover/Autodiscover/GetFederationInformation</a:Action>
        <a:To soap:mustUnderstand="1">https://autodiscover.byfcxu-dom.extest.microsoft.com/autodiscover/autodiscover.svc</a:To>
        <a:ReplyTo>
        <a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address>
        </a:ReplyTo>
    </soap:Header>
    <soap:Body>
        <GetFederationInformationRequestMessage xmlns="http://schemas.microsoft.com/exchange/2010/Autodiscover">
        <Request>
            <Domain>{domain}</Domain>
        </Request>
        </GetFederationInformationRequestMessage>
    </soap:Body>
    </soap:Envelope>"""

    headers = {
        "Content-type": "text/xml; charset=utf-8",
        "User-agent": "AutodiscoverClient"
    }

    try:
        httprequest = Request(
            "https://autodiscover-s.outlook.com/autodiscover/autodiscover.svc", headers=headers, data=body.encode())

        with urlopen(httprequest) as response:
            response = response.read().decode()
    except Exception:
        log_error("[-] Unable to execute request. Wrong domain?")
        return

    domains = []
    tree = ET.fromstring(response)
    for elem in tree.iter():
        if elem.tag == "{http://schemas.microsoft.com/exchange/2010/Autodiscover}Domain":
            domains.append(elem.text)


    # Write domains to Excel
    if domains:
        df_domains = pd.DataFrame(domains, columns=["Domains"])
        write_to_excel(df_domains, sheet_name="Domains")

    # Extract tenant name and write to Excel
    tenant = ""
    for domain in domains:
        if "onmicrosoft.com" in domain:
            tenant = domain.split(".")[0]

    log_success(f"[+] Tenant found: {tenant}")

    if tenant:
        df_tenant = pd.DataFrame([tenant], columns=["Tenant"])
        write_to_excel(df_tenant, sheet_name="Tenants")

    # Check MDI instance
    check_mdi(tenant)


# Identify MDI usage
def check_mdi(tenant):
    tenant += "sensorapi.atp.azure.com"
    mdi_result = []

    try:
        dns.resolver.resolve(tenant)
        log_success(f"[+]An MDI instance was found for {tenant}!")
        mdi_result.append({"Tenant": tenant, "Status": "MDI instance found"})
    except Exception:
        log_warning(f"[-] No MDI instance was found for {tenant}")
        

    # Write MDI results to Excel
    if mdi_result:
        df_mdi = pd.DataFrame(mdi_result)
        write_to_excel(df_mdi, sheet_name="MDI Instances")
