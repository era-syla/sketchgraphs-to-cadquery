import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0015, -0.0015).lineTo(0.0015, -0.0415).lineTo(0.0415, -0.0415).lineTo(0.0415, -0.0315).lineTo(0.0115, -0.0315).lineTo(0.0115, -0.0015).lineTo(0.0015, -0.0015).close()
solid=wp_sketch0.add(loop0).extrude(-0.07053227087541872)
