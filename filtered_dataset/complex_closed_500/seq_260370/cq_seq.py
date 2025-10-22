import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0035, 0.004).lineTo(0.00404, 0.00346).lineTo(0.00404, 0.00054).lineTo(0.0035, -0.0).lineTo(0.00504, 0.0).lineTo(0.00504, 0.004).lineTo(0.0035, 0.004).close()
solid=wp_sketch0.add(loop0).extrude(-0.0024172576835838964)
