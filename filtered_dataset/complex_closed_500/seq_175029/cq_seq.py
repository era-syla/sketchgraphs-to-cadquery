import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.007, -0.007).lineTo(0.036, -0.007).lineTo(0.036, -0.036).lineTo(0.007, -0.036).lineTo(0.007, -0.007).close()
solid=wp_sketch0.add(loop0).extrude(0.08199319019286351)
