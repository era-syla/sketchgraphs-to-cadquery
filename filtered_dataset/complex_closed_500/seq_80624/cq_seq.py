import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04458, 0.0).lineTo(0.06208, 0.0).lineTo(0.06208, -0.003).lineTo(0.04458, -0.003).lineTo(0.04458, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.01545900785580463)
