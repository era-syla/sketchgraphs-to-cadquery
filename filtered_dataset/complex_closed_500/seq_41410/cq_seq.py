import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.009, 0.051).lineTo(0.009, 0.051).lineTo(0.006, 0.048).lineTo(-0.006, 0.048).lineTo(-0.009, 0.051).close()
solid=wp_sketch0.add(loop0).extrude(0.007859392364163886)
