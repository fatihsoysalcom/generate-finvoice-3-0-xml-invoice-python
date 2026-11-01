# Generate Finvoice 3.0 XML Invoice Python

This Python script demonstrates how to programmatically generate a basic Finvoice 3.0 e-invoice in XML format. It uses standard library features (`xml.etree.ElementTree` and `xml.dom.minidom`) to construct a minimal invoice structure, including seller/buyer details, invoice rows, and totals, saving it to a file. This illustrates creating e-invoices without specialized software, adhering to the Finvoice 3.0 standard.

## Language

`python`

## How to Run

1. Save the code as `generate_finvoice.py`.
2. Run `python generate_finvoice.py` in your terminal.
3. A `finvoice_sample.xml` file will be created in the same directory.

## Original Article

This example accompanies the Turkish article: [Fatura Yazılımına İhtiyaç Duymadan Finvoice 3.0 E-Fatura Nasıl Oluşturulur ve Gönderilir?](https://fatihsoysal.com/blog/fatura-yazilimina-ihtiyac-duymadan-finvoice-3-0-e-fatura-nasil-olusturulur-ve-gonderilir/).

## License

MIT — see [LICENSE](LICENSE).
