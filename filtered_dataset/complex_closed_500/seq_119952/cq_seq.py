import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.007, 0.0).lineTo(0.019, 0.0056).lineTo(0.019, 0.009).lineTo(0.007, 0.009).lineTo(0.007, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.001438781810444068)
