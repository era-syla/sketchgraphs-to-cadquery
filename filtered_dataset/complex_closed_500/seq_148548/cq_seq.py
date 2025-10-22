import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01, 0.008).lineTo(0.012, 0.008).lineTo(0.012, 0.026).lineTo(0.01, 0.026).lineTo(0.01, 0.008).close()
solid=wp_sketch0.add(loop0).extrude(0.049994966654892455)
