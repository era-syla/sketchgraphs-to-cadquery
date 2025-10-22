import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01403, 0.01385).lineTo(0.00739, 0.01385).lineTo(0.00739, 0.01503).lineTo(0.01403, 0.01503).lineTo(0.01403, 0.01385).close()
solid=wp_sketch0.add(loop0).extrude(0.01647249720688011)
