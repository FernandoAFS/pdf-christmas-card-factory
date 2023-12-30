#!/bin/env python3

import argparse
import jinja2
import base64
import textwrap
import sys
import unoserver.client

# THERE IS ONLY ONE TEMPLATE FILE IN THIS EXAMPLE.
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("./")
)

def photo_b64(src):
    with open(src, "rb") as f:
        photo_bytes = f.read()

    photo_base64 = base64.b64encode(photo_bytes).decode()
    return textwrap.fill(photo_base64, 73)


def main():
    parser = argparse.ArgumentParser(
        prog="Christmas card generator",
        description="Use this to turn the fodp template to a pdf file!",
    )
    parser.add_argument("name", help="Name to be used in the template")
    parser.add_argument("photo", help="Path of the photo to be used as a portrait")
    parser.add_argument("--action", help="Filetype to be outputed (fodp or pdf), default pdf", default="pdf")
    parser.add_argument("--unoserver-host", default="localhost")
    parser.add_argument("--unoserver-port", default="2003")

    args = parser.parse_args()

    name = args.name
    photo_path = args.photo
    action = args.action
    unoserver_host = args.unoserver_host
    unoserver_port = args.unoserver_port

    if action not in ["fodp", "pdf"]:
        raise ValueError(f"Action argument can either be fodp or pdf but not {action}")

    # template.xml is the same as the document linked above with the two arguments.
    # check the github repository for more details.
    template = env.get_template("template.xml")
    photo_base64 = b64image=photo_b64(photo_path)
    fodp_document = template.render(name=name, b64image=photo_base64)

    if action == "fodp":
        print(fodp_document)
        return

    client = unoserver.client.UnoClient(server=unoserver_host, port=unoserver_port)
    pdf_bin = client.convert(indata=fodp_document.encode(), convert_to="pdf")
    sys.stdout.buffer.write(pdf_bin)


if __name__ == "__main__":
    main()
