import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.003, -0.0).lineTo(0.00797, 0.012).lineTo(0.15, 0.012).lineTo(0.15, 0.0).lineTo(0.003, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.1023256520038055)
