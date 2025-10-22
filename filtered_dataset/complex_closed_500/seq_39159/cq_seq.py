import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00526, 0.024).lineTo(0.00394, 0.024).lineTo(0.00394, 0.01975).lineTo(-0.00526, 0.01975).lineTo(-0.00526, 0.024).close()
solid=wp_sketch0.add(loop0).extrude(0.014530349469545942)
