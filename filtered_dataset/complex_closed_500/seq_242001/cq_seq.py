import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1, 0.045).lineTo(0.09, 0.045).lineTo(0.09, 0.035).lineTo(0.1, 0.035).lineTo(0.1, 0.045).close()
solid=wp_sketch0.add(loop0).extrude(0.010930845996444631)
