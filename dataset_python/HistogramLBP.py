from copy import deepcopy
from lbp_codes import LBP_Codes


class HistogramLBP:
    def __init__(self, image, image_length=28):
        self._image_length = image_length
        self._section_length = 3
        self.power_by_position = {
            '0:0': 0,
            '0:1': 1,
            '0:2': 2,
            '1:2': 3,
            '2:2': 4,
            '2:1': 5,
            '2:0': 6,
            '1:0': 7,
        }
        self.image = image
        self.__set_coded_image(image)
        self.__set_histogram()

    def __set_histogram(self):
        self.histogram = [0 for _ in range(59)]
        for i in range(self._image_length):
            for j in range(self._image_length):
                self.histogram[LBP_Codes[self._coded_image[i][j]]] += 1

    def __set_coded_image(self, image):
        self._coded_image = deepcopy(image)
        for i, line in enumerate(image):
            for j in range(len(line)):
                self._coded_image[i][j] = self.__get_coded_image(i, j)

    def __get_coded_image(self, x_pixel, y_pixel):
        binary_image = [[0 for i in range(self._section_length)] for j in range(self._section_length)]
        center_value = self.__get_value_by_index(self.image, x_pixel, y_pixel)

        for x_absolute_position, x_relative_position in zip(range(x_pixel - 1, 2 + x_pixel), range(3)):
            for y_absolute_position, y_relative_position in zip(range(y_pixel - 1, 2 + y_pixel), range(3)):
                if x_absolute_position == x_pixel and y_absolute_position == y_pixel:
                    continue

                if self.__get_value_by_index(self.image, x_absolute_position, y_absolute_position) >= center_value:
                    binary_result = 1
                else:
                    binary_result = 0
                if binary_result:
                    try:
                        binary_image[x_relative_position][y_relative_position] = binary_result
                    except IndexError:
                        pass
        return self.__get_code(binary_image)

    def __get_code(self, image_section):
        result = 0
        for i in range(self._section_length):
            for j in range(self._section_length):
                if i == 1 and j == 1:
                    continue
                result += pow(2, self.power_by_position.get(f'{i}:{j}', 0)) * image_section[i][j]

        return result

    def __get_value_by_index(self, array, i, j) -> int:
        try:
            return array[i][j]
        except IndexError:
            return 0
