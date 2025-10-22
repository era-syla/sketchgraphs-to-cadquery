import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0075, 0.02).lineTo(0.0195, 0.02).lineTo(0.0195, -0.02).lineTo(0.0075, -0.02).lineTo(0.0075, 0.02).close()
solid=wp_sketch0.add(loop0).extrude(0.09924222181786803)
