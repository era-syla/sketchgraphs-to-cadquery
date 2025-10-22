import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-10.87824, 3.088).lineTo(16.2651, 3.088).lineTo(16.2651, -15.44723).lineTo(-10.87824, -15.44723).lineTo(-10.87824, 3.088).close()
solid=wp_sketch0.add(loop0).extrude(21.764374287170835)
