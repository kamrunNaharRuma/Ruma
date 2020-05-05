from bokeh.plotting import figure,output_file,show

x = [1,2,3,4,5]
y = [1,2,3,4,5]

output_file('index.html')

p = figure(
    title='Bonton Installation',
    x_axis_label='X Axis',
    y_axis_label='Y Axis'
)


p.line(x,y,legend='Test',line_width=5)

show(p)
