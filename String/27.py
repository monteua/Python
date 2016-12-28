'''
Write a Python program to remove existing indentation from all of the lines in a given text.
'''

import textwrap

text = '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce euismod dignissim augue, non hendrerit nisl scelerisque a.
            Phasellus pharetra volutpat est ut finibus.
            Morbi facilisis nec leo at tempus. Etiam dapibus metus ac ligula sollicitudin, eget maximus eros semper.
            Phasellus elementum elementum est sed consectetur. Ut magna eros, sagittis eget ligula non, aliquet pellentesque nunc.
            Ut imperdiet nibh eget fringilla congue. Fusce quis ultrices velit, ac sollicitudin enim. Ut iaculis posuere velit.
            Duis justo nunc, ornare vel eros sed, euismod dignissim ligula. Pellentesque molestie, augue a vehicula malesuada, urna
            erat sodales ex, at molestie nisi sapien in nisl. Maecenas condimentum lectus nec laoreet placerat.
            Cras faucibus efficitur vulputate. Aliquam ut massa volutpat, hendrerit diam sed, condimentum eros.
            Nullam egestas nunc vehicula faucibus tristique.
'''

print textwrap.dedent(text)