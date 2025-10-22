import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(1.49555, 0.0).lineTo(1.49555, -0.0127).lineTo(0.0, -0.0127).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-4.230598242278881)
