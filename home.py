from dataclasses import dataclass

import streamlit as st
import numpy as np


@dataclass
class Thumbnail:
    image_source: str | np.ndarray

    def render(self, col):
        col.image(self.image_source)


@dataclass
class Item:
    name: str
    price: int
    thumbnail: Thumbnail
    

    def render(self, col):
        self.thumbnail.render(col)
        col.write(f"{self.name}: ¥ {self.price}")


@dataclass
class Carousel:
    title: str
    items: list[Item]

    def render(self):
        with st.container():
            st.header(self.title)
            with st.container():
                for item, col in zip(
                    self.items,
                    st.columns(len(self.items))
                ):
                    item.render(col)


@dataclass
class Home:
    carousels: list[Carousel]

    def render(self):
        for carousel in self.carousels:
            carousel.render()


def main():
    Home([
        Carousel(
            "Carousel 1",
            [
                Item(
                    "Apple",
                    100,
                    Thumbnail("https://t4.ftcdn.net/jpg/02/52/93/81/360_F_252938192_JQQL8VoqyQVwVB98oRnZl83epseTVaHe.jpg")
                ),
                Item(
                    "Orange",
                    200,
                    Thumbnail("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Oranges_-_whole-halved-segment.jpg/640px-Oranges_-_whole-halved-segment.jpg")
                ),
                Item(
                    "Banana",
                    300,
                    Thumbnail("https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Bananas_white_background_DS.jpg/640px-Bananas_white_background_DS.jpg")
                ),
            ]
        ),
        Carousel(
            "Carousel 2",
            [
                Item(
                    "Orange",
                    200,
                    Thumbnail("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Oranges_-_whole-halved-segment.jpg/640px-Oranges_-_whole-halved-segment.jpg")
                ),
                Item(
                    "Apple",
                    100,
                    Thumbnail("https://t4.ftcdn.net/jpg/02/52/93/81/360_F_252938192_JQQL8VoqyQVwVB98oRnZl83epseTVaHe.jpg")
                ),
                Item(
                    "Banana",
                    300,
                    Thumbnail("https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Bananas_white_background_DS.jpg/640px-Bananas_white_background_DS.jpg")
                ),
            ]
        )
    ]).render()

if __name__ == "__main__":
    main()
