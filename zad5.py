def main():
    slownik = {}
    def make_car(firma, model, **kwargs):
        slownik['firma'] = firma
        slownik['model'] = model
        for key, value in kwargs.items():
            slownik[key] = value
    make_car("fiat", "125p", kolor = "bialy")
    print(slownik)

if __name__ == "__main__":
    main()
