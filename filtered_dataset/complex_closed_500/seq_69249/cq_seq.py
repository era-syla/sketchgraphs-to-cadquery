import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.145, 0.009).lineTo(0.145, 0.009).lineTo(0.145, -0.009).lineTo(-0.145, -0.009).lineTo(-0.145, 0.009).close()
solid=wp_sketch0.add(loop0).extrude(-0.47104255617154395)
