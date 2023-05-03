import json

# THIS FILE IS FOR MESSING WITH THE PRODUCT_JSON FORMAT 
# (so that we don't have ugly commented code in our main app)
def main():
    with open('product_data.json', 'r') as f:
        URLs = json.load(f)
    for entry in URLs['products']:
        print("********************************")
        print(entry['product_name'])
        print(entry)
        print()

if __name__ == '__main__':
    main()
