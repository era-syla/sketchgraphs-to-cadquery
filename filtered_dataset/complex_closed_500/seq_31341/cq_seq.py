import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04344, 0.1161).lineTo(0.04344, 0.0).lineTo(0.02696, 0.0).lineTo(0.04344, 0.1161).close()
solid=wp_sketch0.add(loop0).extrude(0.32138452445924814)
