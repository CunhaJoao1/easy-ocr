import easyocr

def main(params):
    # reader = easyocr.Reader(['es'], gpu=True)
    reader = easyocr.Reader(['es','es'], gpu=True)
    result = reader.readtext(params, detail='False')
    text = ""

    for res in result:
        # print(res[1])
        text = text + " " + res[1]

    print(text)
    return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": text,
  }