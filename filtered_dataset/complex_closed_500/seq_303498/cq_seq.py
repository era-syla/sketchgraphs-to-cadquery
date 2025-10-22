import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.015, 0.0).lineTo(-0.005, 0.0).lineTo(-0.005, 0.012).lineTo(-0.015, 0.012).lineTo(-0.015, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.020729161115161522)
