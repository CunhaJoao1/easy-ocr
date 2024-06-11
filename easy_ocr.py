import easyocr

def main(params):
    reader = easyocr.Reader(['pt'])
    reader = easyocr.Reader(['pt','pt'])
    result = reader.readtext(params, detail='False')
    text = ""

    for res in result:
        # print(res[1])
        text = text + " " + res[1]

    return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": text,
  }