import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-6.66478, 0.2).lineTo(6.66478, 0.2).lineTo(6.66478, 0.0).lineTo(-6.66478, 0.0).lineTo(-6.66478, 0.2).close()
solid=wp_sketch0.add(loop0).extrude(-6.905046992976679)
