import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0295, 0.0475).lineTo(0.0395, 0.0475).lineTo(0.0395, 0.035).lineTo(0.0295, 0.035).lineTo(0.0295, 0.0475).close()
solid=wp_sketch0.add(loop0).extrude(0.014434066375593677)
