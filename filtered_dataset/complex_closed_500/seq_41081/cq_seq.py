import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0207, 0.0).lineTo(0.0097, -0.0).lineTo(0.0097, 0.013).lineTo(0.0, 0.013).lineTo(0.0, 0.02).lineTo(0.0207, 0.02).lineTo(0.0207, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.04617139057011109)
