import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01111, -0.01098).lineTo(-0.01111, -0.01098).lineTo(-0.01111, 0.01098).lineTo(0.01111, 0.01098).lineTo(0.01111, -0.01098).close()
solid=wp_sketch0.add(loop0).extrude(0.048202868404776784)
