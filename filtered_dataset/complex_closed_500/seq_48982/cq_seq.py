import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.05012, -0.00041).lineTo(0.05012, -0.0).lineTo(0.07, 0.0).lineTo(0.07078, -0.00318).lineTo(0.05475, -0.00318).lineTo(0.05233, -0.001).lineTo(0.05012, -0.00041).close()
solid=wp_sketch0.add(loop0).extrude(0.009130299937899626)
