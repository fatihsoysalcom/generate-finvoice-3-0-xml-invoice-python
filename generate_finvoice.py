import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

def generate_finvoice_xml():
    """
    Generates a sample Finvoice 3.0 XML e-invoice.
    """
    # Define Finvoice namespace, crucial for valid Finvoice XML.
    ns = "http://www.finvoice.fi/Finvoice"
    ET.register_namespace('', ns) # Register default namespace for cleaner output

    # Create the root element <Finvoice> with the specified version and namespace.
    # This element signifies adherence to the Finvoice 3.0 standard.
    finvoice_root = ET.Element(f"{{{ns}}}Finvoice", Version="3.0")

    # Create the main <Invoice> element which encapsulates all invoice details.
    invoice_elem = ET.SubElement(finvoice_root, f"{{{ns}}}Invoice")

    # Invoice Details section: Contains general information about the invoice.
    invoice_details = ET.SubElement(invoice_elem, f"{{{ns}}}InvoiceDetails")
    ET.SubElement(invoice_details, f"{{{ns}}}InvoiceNumber").text = "INV-2023-001"
    ET.SubElement(invoice_details, f"{{{ns}}}InvoiceDate").text = datetime.now().strftime("%Y%m%d")
    ET.SubElement(invoice_details, f"{{{ns}}}InvoiceTypeCode").text = "SALESINVOICE"

    # Seller Party Information: Details of the company issuing the invoice.
    seller_party = ET.SubElement(invoice_elem, f"{{{ns}}}SellerParty")
    ET.SubElement(seller_party, f"{{{ns}}}PartyIdentifier").text = "FI1234567-8" # Finnish Business ID (Y-tunnus)
    ET.SubElement(seller_party, f"{{{ns}}}PartyName").text = "My Company Oy"
    ET.SubElement(seller_party, f"{{{ns}}}PartyStreetAddress").text = "Example Street 1"
    ET.SubElement(seller_party, f"{{{ns}}}PartyPostCode").text = "00100"
    ET.SubElement(seller_party, f"{{{ns}}}PartyCity").text = "Helsinki"
    ET.SubElement(seller_party, f"{{{ns}}}CountryCode").text = "FI"

    # Buyer Party Information: Details of the recipient of the invoice.
    buyer_party = ET.SubElement(invoice_elem, f"{{{ns}}}BuyerParty")
    ET.SubElement(buyer_party, f"{{{ns}}}PartyIdentifier").text = "FI9876543-2"
    ET.SubElement(buyer_party, f"{{{ns}}}PartyName").text = "Customer Ltd"
    ET.SubElement(buyer_party, f"{{{ns}}}PartyStreetAddress").text = "Customer Road 5"
    ET.SubElement(buyer_party, f"{{{ns}}}PartyPostCode").text = "00500"
    ET.SubElement(buyer_party, f"{{{ns}}}PartyCity").text = "Espoo"
    ET.SubElement(buyer_party, f"{{{ns}}}CountryCode").text = "FI"

    # Invoice Row: Represents a single line item for a product or service.
    invoice_row1 = ET.SubElement(invoice_elem, f"{{{ns}}}InvoiceRow")
    ET.SubElement(invoice_row1, f"{{{ns}}}ArticleName").text = "Consulting Service"
    ET.SubElement(invoice_row1, f"{{{ns}}}ArticleQuantity").text = "10.0"
    ET.SubElement(invoice_row1, f"{{{ns}}}UnitOfMeasure").text = "h"
    ET.SubElement(invoice_row1, f"{{{ns}}}UnitPriceAmount").text = "50.00"
    ET.SubElement(invoice_row1, f"{{{ns}}}RowTotalAmount").text = "500.00"
    ET.SubElement(invoice_row1, f"{{{ns}}}VATPercentage").text = "24.00"
    ET.SubElement(invoice_row1, f"{{{ns}}}VATAmount").text = "120.00" # Calculated: 500 * 0.24

    # Invoice Total: Summarizes the financial amounts for the entire invoice.
    invoice_total = ET.SubElement(invoice_elem, f"{{{ns}}}InvoiceTotal")
    ET.SubElement(invoice_total, f"{{{ns}}}TotalVatExcludedAmount").text = "500.00"
    ET.SubElement(invoice_total, f"{{{ns}}}TotalVatAmount").text = "120.00"
    ET.SubElement(invoice_total, f"{{{ns}}}TotalVatIncludedAmount").text = "620.00"

    # Pretty print the XML for readability.
    rough_string = ET.tostring(finvoice_root, 'utf-8')
    reparsed_xml = minidom.parseString(rough_string)
    pretty_xml_as_string = reparsed_xml.toprettyxml(indent="  ")

    return pretty_xml_as_string

if __name__ == "__main__":
    xml_content = generate_finvoice_xml()
    output_filename = "finvoice_sample.xml"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"Finvoice 3.0 XML sample generated successfully to {output_filename}")
