class SVG_map:
    def __init__(self, title="Prog", total=100, progress=30):
        self.__set_default__()
        self.__title__ = title
        self.__title_width__ = len(title) * 9 + 10
        self.__total_width__ = self.__title_width__ + 70
        self.__progress__ = int(progress / total * 100)
        self.__progress__ = self.__progress__ if self.__progress__ <= 100 else 100
        self.__progressbar_width__ = int(self.__progress__ / 100 * 70)
        self.__progress_color__ = self.__get_progress_color__(self.__progress__)
        self.__progress_details_x__ = self.__get_progress_details_X__(self.__progress__)

    def __set_default__(self):
        self.__green__ = "fill:rgb(100,255,100)"
        self.__red__ = "fill:rgb(255,100,100)"
        self.__yellow__ = "fill:rgb(255,250,100)"
        self.__keys__ = (
            "start",
            "style",
            "title_rect",
            "title",
            "progress_box",
            "progress_bar",
            "progress_details",
            "error_text",
            "end",
        )
    
    def __get_progress_details_X__(self, progress):
        if progress <= 9:
            return self.__title_width__ + 25
        elif progress <= 99:
            return self.__title_width__ + 20
        return self.__title_width__ + 15

    def __get_progress_color__(self, progress):
        if progress <= 33:
            return self.__red__
        elif progress <= 66:
            return self.__yellow__
        return self.__green__

    def generate(self):
        svg_data = {
            "start": '<svg xmlns="http://www.w3.org/2000/svg" width="'
            + str(self.__total_width__)
            + '" height="20">',
            "style": "<style>"
            + "    .bold { font: bold 13px sans-serif;}"
            + "    .txt { font: 13px sans-serif;}"
            + "</style>",
            "title_rect": '<rect rx="3" width="'
            + str(self.__title_width__)
            + '" height="20" style="fill:rgb(100,100,255)" />',
            "title": '<text x="5" y="14" class="bold" style="fill:rgb(250,250,250)">'
            + self.__title__
            + "</text>",
            "progress_box": '<rect x="'
            + str(self.__title_width__ - 5)
            + '" rx="3" width="70" height="20" style="fill:rgb(200,200,200)" />',
            "progress_bar": '<rect x="'
            + str(self.__title_width__ - 5)
            + '" rx="3" width="'
            + str(self.__progressbar_width__)
            + '" height="20" style="'
            + self.__progress_color__
            + '" />',
            "progress_details": '<text x="'
            + str(self.__progress_details_x__)
            + '" y="14" class="txt" style="fill:rgb(5,5,5); align:center">'
            + str(self.__progress__)
            + "%</text>",
            "error_text": "Sorry, your browser does not support inline SVG.",
            "end": "</svg>",
        }
        svg_data_list = [svg_data[key] for key in self.__keys__]
        return "\n".join(svg_data_list)
