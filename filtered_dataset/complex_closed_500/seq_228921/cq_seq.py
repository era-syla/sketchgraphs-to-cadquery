import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.01299).lineTo(0.0075, -0.0).lineTo(-0.0075, -0.0).lineTo(-0.0, 0.01299).close()
solid=wp_sketch0.add(loop0).extrude(-0.013539217650268576)
