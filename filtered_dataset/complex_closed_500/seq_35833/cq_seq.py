import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.1604, -0.00859).lineTo(-0.1604, -0.05105).lineTo(-0.174, -0.05105).lineTo(-0.174, -0.00859).lineTo(-0.1604, -0.00859).close()
solid=wp_sketch0.add(loop0).extrude(-0.07339287672609467)
