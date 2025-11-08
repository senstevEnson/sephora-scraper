thonclass ProductParser:
    def parse_product(self, product):
        parsed_product = {
            "source": product.get("source", {}),
            "brand": product.get("brand", ""),
            "title": product.get("title", ""),
            "description": product.get("description", ""),
            "categories": product.get("categories", []),
            "options": product.get("options", []),
            "variants": product.get("variants", []),
            "medias": product.get("medias", []),
            "stats": product.get("stats", {})
        }
        return parsed_product