import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0217, 0.06683).lineTo(0.0291, 0.06683).lineTo(0.0291, -0.01826).lineTo(-0.0217, -0.01826).lineTo(-0.0217, 0.06683).close()
solid=wp_sketch0.add(loop0).extrude(-0.1589315278808244)
