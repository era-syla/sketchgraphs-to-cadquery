import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00476, 0.001).lineTo(-0.00476, 0.001).lineTo(-0.00476, 0.00222).lineTo(0.00476, 0.00222).lineTo(0.00476, 0.001).close()
solid=wp_sketch0.add(loop0).extrude(0.015159760392187258)
