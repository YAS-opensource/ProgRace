class SVG_map:
    """
    This class generates the svg for the API response

    This class initializes itself with title, total range and progress.
    It calculates the necessary measurements from these info to generate
    the SVG.

    Attributes
    ----------
    __title__ : str
        title of the progress-bar
    __title_width__ : int
        width of title for svg
    __total_width__ : int
        total width of svg
    __progress__ : int
        percentage of progress
    __progressbar_width__ :
        width of the progress-bar
    __progress_color__ : str
        color of the progress-bar depending on the perentage of progress
        __green__ if progress > 66
        __yellow__ if 66 >= progress > 33
        __red__ if 33 >= progress > 0
    __progress_details_x__ : int
        position of progress details in X axis
    __red__ : str
        fill:rgb(240,113,120)
    __yellow__ : str
        fill:rgb(255,203,107)
    __green__ : str
        fill:rgb(195,232,141)"
    __keys__ : tuple of str
        keys for the svg_data_list dictionary

    Methods
    -------

    generate()
        generates and returns the SVG
    """

    def __init__(self, title="Prog", total=100, progress=30):
        """
        Parameters
        ----------

        title : str
            title of the progress-bar
        total : int
            total range of work
        progress : int
            progress of the work
        """

        self.__set_default__()
        self.__title__ = title
        self.__title_width__ = len(title) * 8.5 + 10
        self.__total_width__ = self.__title_width__ + 70
        self.__progress__ = int(progress / total * 100)
        self.__progress__ = self.__progress__ if self.__progress__ <= 100 else 100
        self.__progressbar_width__ = int(self.__progress__ / 100 * 70)
        self.__progress_color__ = self.__get_progress_color__(self.__progress__)
        self.__progress_details_x__ = self.__get_progress_details_x__(self.__progress__)

    def __set_default__(self):
        """
        sets default attributes
        """

        self.__green__ = "fill:rgb(195,232,141)"
        self.__red__ = "fill:rgb(240,113,120)"
        self.__yellow__ = "fill:rgb(255,203,107)"
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

    def __get_progress_details_x__(self, progress):
        """
        Parameters
        ----------

        progress : int
            percentage of progress

        Returns
        -------

        int
            position of progress details in X axis
        """

        if progress <= 9:
            return self.__title_width__ + 25
        elif progress <= 99:
            return self.__title_width__ + 20
        return self.__title_width__ + 15

    def __get_progress_color__(self, progress):
        """
        Parameters
        ----------

        progress: int
            percentage of progress

        Returns
        -------

        str
            returns __green__, __yellow__ or __red__
        """

        if progress <= 33:
            return self.__red__
        elif progress <= 66:
            return self.__yellow__
        return self.__green__

    def generate(self):
        """
        Returns
        -------

        str
            generates and returns SVG data as a str
        """

        svg_data = {
            "start": '<svg xmlns="http://www.w3.org/2000/svg" width="'
                     + str(self.__total_width__)
                     + '" height="20">',
            "style": "<style>"
                     + "    .bold { font: bold 13px Menlo, Monaco, Consolas, monospace;}"
                     + "    .txt { font: 13px sans-serif;}"
                     + "</style>",
            "title_rect": '<rect rx="3" width="'
                          + str(self.__title_width__)
                          + '" height="20" style="fill:rgb(15,17,26)" />',
            "title": '<text x="5" y="14" class="bold" style="fill:rgb(199,146,234)">'
                     + self.__title__
                     + "</text>",
            "progress_box": '<rect x="'
                            + str(self.__title_width__ - 5)
                            + '" rx="3" width="70" height="20" style="fill:rgb(70,75,93)" />',
            "progress_bar": '<rect x="'
                            + str(self.__title_width__ - 5)
                            + '" rx="3" width="'
                            + str(self.__progressbar_width__)
                            + '" height="20" style="'
                            + self.__progress_color__
                            + '" />',
            "progress_details": '<text x="'
                                + str(self.__progress_details_x__)
                                + '" y="14" class="txt" '
                                + 'style="fill:rgb(255,255,255); align:center">'
                                + str(self.__progress__)
                                + "%</text>",
            "error_text": "Sorry, your browser does not support inline SVG.",
            "end": "</svg>",
        }
        svg_data_list = [svg_data[key] for key in self.__keys__]
        return "\n".join(svg_data_list)
