import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.4318, 0.0).lineTo(0.4318, 0.1524).lineTo(0.0, 0.1524).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.8584763361556013)
