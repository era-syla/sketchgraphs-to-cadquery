import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.007, 0.00165).lineTo(0.007, 0.00165).lineTo(0.007, -0.00165).lineTo(-0.007, -0.00165).lineTo(-0.007, 0.00165).close()
solid=wp_sketch0.add(loop0).extrude(-0.011441689221331987)
