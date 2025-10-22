import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.065, -0.00665).lineTo(0.06, -0.00665).lineTo(0.06, -0.00165).lineTo(0.065, -0.00165).lineTo(0.065, -0.00665).close()
solid=wp_sketch0.add(loop0).extrude(0.00452404113383476)
