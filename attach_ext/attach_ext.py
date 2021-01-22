from typing import Optional, BinaryIO, cast, Generator
import email
import email.policy
import email.message
import email.utils
import time
import os


def _save_attach(att: email.message.EmailMessage, outdir: str = "output") -> None:
    filename = att.get_filename()
    if not filename:
        filename = f"{time.time()}"
    filename = filename.replace("\t", "")

    print(f"    Extracting {filename}")

    data: Optional[bytes] = att.get_payload(decode=True)
    if data is None:
        data = att.get_content().as_bytes()

    os.makedirs(outdir, exist_ok=True)

    with open(os.path.join(outdir, filename), "wb") as fw:
        fw.write(data)


def parse_email_from_fp(fp: BinaryIO, outdir: str = "output") -> None:
    em: email.message.EmailMessage = \
        cast(
            email.message.EmailMessage,
            email.message_from_binary_file(fp, policy=email.policy.default))

    for part in cast(Generator[email.message.EmailMessage, None, None], em.walk()):
        if part.is_attachment() or part.get_filename():
            _save_attach(part, outdir)


def parse_email_from_file(filepath: str):
    print(f"Parsing {filepath}")
    return parse_email_from_fp(
        open(filepath, "rb"),
        os.path.join("output", os.path.basename(filepath)))
