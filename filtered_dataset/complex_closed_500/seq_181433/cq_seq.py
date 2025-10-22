import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.09001, -0.00019).lineTo(0.02143, -0.00019).lineTo(0.02143, 0.00019).lineTo(0.09001, 0.00019).lineTo(0.09001, -0.00019).close()
solid=wp_sketch0.add(loop0).extrude(-0.1633523718972856)
