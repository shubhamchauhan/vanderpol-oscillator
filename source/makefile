all: ../output/130010021_animation.mp4 ../output/position_velocity.png ../output/phase_plot.png ../output/130010021.pdf ../output/130010021.html 

../output/position_velocity.png: graphic.py vanderpol.py ../input.txt
	python graphic.py

../output/phase_plot.png: graphic.py vanderpol.py ../input.txt
	python graphic.py

../output/130010021_animation.mp4: graphic.py vanderpol.py ../input.txt
	python graphic.py

../output/130010021.pdf: ../output/phase_plot.png 130010021.tex
	pdflatex --output-directory=../output 130010021.tex

../output/130010021.html: ../output/130010021_animation.mp4 createhtml.py
	python createhtml.py