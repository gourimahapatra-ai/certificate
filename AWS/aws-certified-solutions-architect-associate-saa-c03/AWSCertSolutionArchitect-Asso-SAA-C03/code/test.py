import argparse
import os
from openai import OpenAI

DEFAULT_OPENAI_BASE_URL = "https://bedrock-mantle.us-east-1.api.aws/v1"
OPENAI_API_KEY = "bedrock-api-key-YmVkcm9jay5hbWF6b25hd3MuY29tLz9BY3Rpb249Q2FsbFdpdGhCZWFyZXJUb2tlbiZYLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFTSUFSVTZVUU1IUDNTREpFSTZCJTJGMjAyNjA2MTglMkZ1cy1lYXN0LTElMkZiZWRyb2NrJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA2MThUMTQwOTIzWiZYLUFtei1FeHBpcmVzPTQzMjAwJlgtQW16LVNlY3VyaXR5LVRva2VuPUlRb0piM0pwWjJsdVgyVmpFTiUyRiUyRiUyRiUyRiUyRiUyRiUyRiUyRiUyRiUyRiUyRndFYUNYVnpMV1ZoYzNRdE1TSkhNRVVDSUglMkJ3czI3bG4zU0ZQNHpCaDhiVzlMN3dTOGJqeEtYdFl4VTRGV2FPQmxCcEFpRUFrNGh2OGljNEYydDhLd3BQTDVEa2lBSE5TOGZxV25IdnNzUXRCR2cydDdrcXp3TUlwJTJGJTJGJTJGJTJGJTJGJTJGJTJGJTJGJTJGJTJGJTJGQVJBQUdnd3hNVE0zTWpVME16SXlPRGNpREdoWEVWOCUyRnhvcCUyQmslMkZmJTJGJTJCU3FqQTc4SW04bHBZTVlnRmFQYXclMkZSSnREViUyQlNESHU2OTVla0ZwNEx2YjhPeXJVYkNvVVdRQ09uMHpLdmVJZnpUSVFWSWl6bWM0ZU5qckk0SjZSRTNWOG5teVI1JTJCdEZhNFlYNjdhZUpaSW9HZHB4U3p6R1NOUjRyRzc2TGZrYiUyRnVQVjR0WG1odTZhbUN5blN6V0VKMSUyRm9PNGhZQVhmJTJCdmtHVENxRFk1WExSQUhhbU56V2klMkI1SDVtcnQlMkZTVEVTSDc4VVRTMjF3WjJOTnVqZ213Qjg4cURoN1pPUk10ajZCRDFkJTJGdXpMYlN0bGdLZ0ElMkZHVnZjQVNReUdnSGZRcnJxYSUyRnFhcEhQMWM3QzRyUTRFeXJPRkZBWUhQempXVEdWUXZWY1dCOER0VzdIUFZ1akJCT1NVajhYWkk3ZWtaRVZRWUFLTm91NENTTDlicW1MT2tJUjNKdG9uaUNrNW9yRTF6V21iT0NNJTJGeElnUDJDRnpOYiUyRm5OWTRBN2hVemZHN0pES3Y3MHB1ZkxCNzRWVCUyQjBWZyUyQjBxYkN2bTkxaklKT0g3QnRJRWd5ZUw3R2JNZnZXT2hQWmhMVGxEak9ZcmttSTFHcW5VUG1aY2piMXNnSTloTFdJRjRWdnQ0bjhEMEZ1Zzk4bjQlMkZRSE9ONnBiUXlzdlQ5SW9hbGc5cDN1MCUyQjYlMkJPS1QwVk9DN2JpRkIxNmtRZDNVZ2t2aW1SJTJCZGxFZGVzVW9wbWNGVjRjQ29mSkcwODljaU1JWHF6OUVHT3Q0Q3lNVDNqbSUyQnBoaWQwclVQV1Y5MFRLWFBZJTJGTWdIeFN5M2U1RnJScTdVUUVxRk8xdG9oOW1LWCUyRm9wciUyRmhPZndrTml3QWFIUmV1ZzJmU3hJY3JzTEpqQ1U1bmdMMTl6cGRKJTJCSkk5cmswQnFvbWx5OWEyZmRFekNOd0lJSU9xSVU4R1REVGY0bHklMkZhNEZVVDl2c1dZOSUyRmNjQmhtSnZuSjNCZEZSNm1VRG02WkVTN2pEelBaMHJUcUw2UVBURThQYkgzRkdHSU9nWnR1MEN6UlB1NkNFendzUGJqV2MlMkYwbW12bktFVDZYNkRqdlFKSklDV3NlNSUyQkhPQmFVaEtGUm0wU1pWTFdSVFZVbWt6dmdWZm55VDFFdVVlUjFXNnR1MjhtQlRGSURwTWkxSlRGTEdzSFZlYlU5VzBsJTJCZyUyRkJRcHQxJTJCeXdybUxSVW5waUxkRUU0cm1abENaNDExd2NMU044WER1bFRFQnY5UjVGRXhjT21UWVZwM0hsck1UOGhic2Fvb0xGQTNIWHkyU09JaUxQd3lyVXNSVk1wS1Q4clp5UERKaGNJVEkxdThPdlZBbmJMMVlIY21XZlZGZ0J2emZwU1U5clJCazhMSmhaSFo5NzJGVWswJTNEJlgtQW16LVNpZ25hdHVyZT1jYmRmNWVhM2NjMmI4ZGYwYjAwYjE4NjBmNGUyMzRiYmRkNzhmMzE4MDBjNTU2MGM5NjE1OTI3ZTRjZTQ4YTZiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZWZXJzaW9uPTE="
OPENAI_BASE_URL = DEFAULT_OPENAI_BASE_URL


def get_openai_config(api_key: str | None = None, base_url: str | None = None):
    api_key = api_key or OPENAI_API_KEY
    base_url = base_url or OPENAI_BASE_URL

    if not api_key:
        raise RuntimeError(
            "Missing OpenAI credentials. Set OPENAI_API_KEY or OPENAI_ADMIN_KEY, or pass --api-key."
        )

    if not base_url:
        raise RuntimeError(
            "Missing OpenAI base URL. Set OPENAI_BASE_URL or pass --base-url."
        )

    return api_key, base_url


def create_client(api_key: str, base_url: str):
    return OpenAI(api_key=api_key, base_url=base_url)


def main():
    parser = argparse.ArgumentParser(description="Run a simple OpenAI/BEDROCK prompt.")
    parser.add_argument("--api-key", help="OpenAI or Bedrock API key")
    parser.add_argument("--base-url", help="OpenAI base URL")
    args = parser.parse_args()

    api_key, base_url = get_openai_config(args.api_key, args.base_url)
    client = create_client(api_key, base_url)

    response = client.responses.create(
        model="openai.gpt-oss-120b",
        input=[
            {"role": "user", "content": "What is the capital of France?"}   ],
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
