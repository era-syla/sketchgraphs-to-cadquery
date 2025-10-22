import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.013, 0.013).lineTo(0.013, 0.013).lineTo(0.013, -0.013).lineTo(-0.013, -0.013).lineTo(-0.013, 0.013).close()
solid=wp_sketch0.add(loop0).extrude(0.015601649912676678)
