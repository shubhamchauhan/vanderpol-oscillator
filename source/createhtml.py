import webbrowser

f = open('../output/130010021.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p>
<video width="800" height="600" autoplay>
  <source src="../output/130010021_animation.mp4" type="video/mp4">
</video
</body>
</html>"""

f.write(message)
f.close()

#Change path to reflect file location
#filename = '../output/130010021.html'
#webbrowser.open_new_tab(filename)